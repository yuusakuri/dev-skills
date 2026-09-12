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
