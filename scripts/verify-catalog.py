#!/usr/bin/env python3
"""Verify every curated skill in catalog.json exists at its pinned upstream ref.

This repository curates rather than copies, so a broken upstream reference is the
only way it can rot: a renamed or deleted upstream skill silently breaks routing.
This script fetches each referenced SKILL.md from raw.githubusercontent.com at the
pinned commit and checks that the file exists and that its frontmatter `name`
matches the name this catalog routes to.

Usage:  python3 scripts/verify-catalog.py [--quiet]
Exit:   0 if every reference resolves, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
RAW = "https://raw.githubusercontent.com/{repo}/{ref}/{path}/SKILL.md"
MARKET = "https://raw.githubusercontent.com/{repo}/{ref}/.claude-plugin/marketplace.json"
TIMEOUT = 30


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "dev-skills-verify"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # network/DNS/TLS
        return 0, str(e)


def frontmatter_name(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    m = re.search(r"^name:\s*(.+)$", text[:end], re.M)
    return m.group(1).strip().strip("\"'") if m else None


def verify_installability(sources: dict) -> list[str]:
    """Check each source's install command against its own marketplace manifest.

    `catalog.json` documents how to install every source. Upstream can rename a
    marketplace or a plugin, which silently turns those commands into
    instructions that fail for anyone following the README.
    """
    problems: list[str] = []
    print("[install] documented commands resolve to real plugins")

    for key, src in sources.items():
        install = src.get("install", "")
        ref_match = re.search(r"install\s+([A-Za-z0-9._-]+)@([A-Za-z0-9._-]+)", install)
        if not ref_match:
            continue
        plugin, marketplace = ref_match.group(1), ref_match.group(2)

        # Anthropic registers this one itself; it has no manifest to read here.
        if marketplace == "claude-plugins-official":
            print(f"  skip {plugin}@{marketplace} (Anthropic official marketplace)")
            continue

        status, body = fetch(MARKET.format(repo=src["repo"], ref=src["ref"]))
        if status != 200:
            problems.append(
                f"{key} — no .claude-plugin/marketplace.json at {src['repo']}@{src['ref'][:8]}"
            )
            print(f"  FAIL {plugin}@{marketplace} (no marketplace manifest)")
            continue

        try:
            manifest = json.loads(body)
        except json.JSONDecodeError as exc:
            problems.append(f"{key} — marketplace.json is not valid JSON ({exc})")
            continue

        actual = manifest.get("name")
        if actual != marketplace:
            problems.append(
                f"{key} — install says '@{marketplace}' but the marketplace is named "
                f"'{actual}'; the documented command would fail"
            )
            print(f"  FAIL {plugin}@{marketplace} (marketplace is '{actual}')")
            continue

        names = {p.get("name") for p in manifest.get("plugins", [])}
        missing = [n for n in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b", install)
                   if n in names or n == plugin]
        if plugin not in names:
            problems.append(
                f"{key} — plugin '{plugin}' is not in marketplace '{marketplace}'"
            )
            print(f"  FAIL {plugin}@{marketplace} (plugin not listed)")
            continue

        extra = len(missing) - 1
        suffix = f" (+{extra} more named in the comment)" if extra > 0 else ""
        print(f"  ok   {plugin}@{marketplace}{suffix}")

    return problems


def main() -> int:
    quiet = "--quiet" in sys.argv
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    sources = catalog["sources"]

    jobs = []
    for phase in catalog["phases"]:
        for e in phase["entries"]:
            src = sources[e["source"]]
            jobs.append((phase["id"], e, src,
                         RAW.format(repo=src["repo"], ref=src["ref"], path=e["path"])))

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda j: fetch(j[3]), jobs))

    failures: list[str] = []
    by_phase: dict[str, list[str]] = {}

    for (phase_id, entry, src, url), (status, body) in zip(jobs, results):
        label = f"{entry['source']}:{entry['skill']}"
        if status != 200:
            failures.append(
                f"{label} — HTTP {status} at {src['repo']}@{src['ref'][:8]}/{entry['path']}"
            )
            by_phase.setdefault(phase_id, []).append(f"  FAIL {label}")
            continue

        declared = frontmatter_name(body)
        if declared is None:
            failures.append(f"{label} — no frontmatter `name` in upstream SKILL.md")
            by_phase.setdefault(phase_id, []).append(f"  WARN {label} (no name field)")
            continue
        if declared != entry["skill"]:
            failures.append(
                f"{label} — upstream frontmatter name is {declared!r}, catalog routes to "
                f"{entry['skill']!r}; upstream may have renamed it"
            )
            by_phase.setdefault(phase_id, []).append(f"  FAIL {label} (name mismatch)")
            continue

        by_phase.setdefault(phase_id, []).append(
            f"  ok   {label:<52} {len(body):>6} bytes"
        )

    if not quiet:
        for phase in catalog["phases"]:
            print(f"[{phase['id']}] {phase['title']}")
            for line in by_phase.get(phase["id"], []):
                print(line)

    # A reference that resolves is not the same as a skill anyone can install.
    # Prove the documented install commands name a real marketplace and plugin.
    install_failures = verify_installability(sources)
    failures.extend(install_failures)

    total = len(jobs)
    print()
    if failures:
        print(f"FAIL — {len(failures)} of {total} curated references broken:\n", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        print(
            "\nFix: update the path or ref in catalog.json, or drop the entry and "
            "re-route that phase in the development-lifecycle skill.",
            file=sys.stderr,
        )
        return 1

    print(f"OK — all {total} curated references resolve at their pinned refs")
    print(f"     across {len(sources)} upstream repositories, 0 files copied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
