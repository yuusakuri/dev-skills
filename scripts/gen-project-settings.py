#!/usr/bin/env python3
"""Generate the `.claude/settings.json` a project needs to use this curation.

Committing that file registers every upstream marketplace for everyone who
trusts the repository folder, and records which plugins the project expects.

Usage:
    python3 scripts/gen-project-settings.py              # print to stdout
    python3 scripts/gen-project-settings.py --write DIR  # merge into DIR/.claude/settings.json
    python3 scripts/gen-project-settings.py --commands   # print the install commands instead

Note: registering a marketplace is not the same as installing its plugins.
Claude Code (v2.1.195+) does not auto-install plugins that come from an external
source, so each developer still runs the `claude plugin install` commands once.
`--commands` prints exactly those.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

# This repository's own marketplace, which carries the router skill.
SELF = {
    "marketplace": "dev-skills",
    "repo": "yuusakuri/dev-skills",
    "plugins": ["dev-lifecycle"],
}

# Marketplaces that Claude Code registers on its own; adding them would be noise.
PREREGISTERED = {"claude-plugins-official"}


def marketplace_name(install_line: str) -> str | None:
    """Extract `marketplace` from a `/plugin install plugin@marketplace` line."""
    m = re.search(r"@([A-Za-z0-9._-]+)", install_line)
    return m.group(1) if m else None


def plugin_names(install_line: str) -> list[str]:
    """Every plugin named on an install line, including any listed in its comment."""
    head, _, comment = install_line.partition("#")
    names = re.findall(r"install\s+([A-Za-z0-9._-]+)@", head)
    names += re.findall(r"\b([a-z0-9]+(?:-[a-z0-9]+)+)\b", comment)
    seen, out = set(), []
    for n in names:
        if n not in seen and n != "plus":
            seen.add(n)
            out.append(n)
    return out


def build() -> tuple[dict, list[str]]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    marketplaces: dict[str, dict] = {}
    enabled: list[str] = []
    commands: list[str] = []

    marketplaces[SELF["marketplace"]] = {
        "source": {"source": "github", "repo": SELF["repo"]}
    }
    for p in SELF["plugins"]:
        enabled.append(f"{p}@{SELF['marketplace']}")
        commands.append(
            f"claude plugin install {p}@{SELF['marketplace']} --scope project"
        )

    for src in catalog["sources"].values():
        mkt = marketplace_name(src["install"])
        if not mkt:
            continue
        if mkt not in PREREGISTERED:
            marketplaces[mkt] = {
                "source": {"source": "github", "repo": src["repo"]}
            }
        for p in plugin_names(src["install"]):
            ref = f"{p}@{mkt}"
            if ref not in enabled:
                enabled.append(ref)
                commands.append(f"claude plugin install {ref} --scope project")

    return {"extraKnownMarketplaces": marketplaces, "enabledPlugins": enabled}, commands


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", metavar="DIR", help="merge into DIR/.claude/settings.json")
    ap.add_argument("--commands", action="store_true", help="print install commands instead")
    args = ap.parse_args()

    settings, commands = build()

    if args.commands:
        print("\n".join(commands))
        return 0

    if not args.write:
        print(json.dumps(settings, indent=2))
        return 0

    target = Path(args.write).expanduser().resolve() / ".claude" / "settings.json"
    target.parent.mkdir(parents=True, exist_ok=True)

    existing = {}
    if target.is_file():
        try:
            existing = json.loads(target.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"error: {target} is not valid JSON — {e}", file=sys.stderr)
            return 1

    # Merge rather than overwrite: a project's own settings must survive.
    merged = dict(existing)
    merged["extraKnownMarketplaces"] = {
        **existing.get("extraKnownMarketplaces", {}),
        **settings["extraKnownMarketplaces"],
    }
    merged["enabledPlugins"] = sorted(
        set(existing.get("enabledPlugins", [])) | set(settings["enabledPlugins"])
    )

    target.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target}")
    print(f"  marketplaces: {len(merged['extraKnownMarketplaces'])}")
    print(f"  plugins:      {len(merged['enabledPlugins'])}")
    print("\nNext, each developer runs once (registering a marketplace does not install):")
    print("\n".join("  " + c for c in commands))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Output was piped into something that closed early, such as `head`.
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
