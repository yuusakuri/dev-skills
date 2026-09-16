#!/usr/bin/env python3
"""Validate every SKILL.md in this repository against the Agent Skills spec.

Spec: https://agentskills.io/specification

Checks frontmatter validity, the name/directory match, length limits, and the
repository's own conventions (a `metadata.phase` that the lifecycle router knows
about, and a description long enough to route on).

Exit code 0 when every skill passes, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "plugins" / "dev-lifecycle" / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESC_MAX = 1024
DESC_MIN = 40          # repo convention: a description short enough to be useless
COMPAT_MAX = 500
BODY_MAX_LINES = 500   # spec recommendation

KNOWN_PHASES = {
    "meta",
    "0-orientation",
    "1-requirements",
    "2-design",
    "3-planning",
    "4-implementation",
    "5-quality",
    "6-verification",
    "7-review",
    "8-release",
    "9-operations",
}

ALLOWED_KEYS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
}


def parse_frontmatter(text: str):
    """Return (mapping, body, error). Deliberately minimal: no YAML dependency.

    Supports the flat `key: value` and one level of nested mapping that these
    skills use, which is all the spec's frontmatter needs.
    """
    if not text.startswith("---\n"):
        return None, None, "file does not start with a '---' frontmatter fence"
    end = text.find("\n---\n", 3)
    if end == -1:
        return None, None, "frontmatter is not closed by a '---' line"

    raw, body = text[4:end], text[end + 5:]
    data: dict[str, object] = {}
    current_parent: str | None = None

    for lineno, line in enumerate(raw.split("\n"), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indented = line[0] in " \t"
        if ":" not in line:
            return None, None, f"line {lineno}: expected 'key: value', got {line!r}"
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()

        if indented:
            if current_parent is None:
                return None, None, f"line {lineno}: indented key with no parent"
            data.setdefault(current_parent, {})
            if not isinstance(data[current_parent], dict):
                return None, None, f"line {lineno}: '{current_parent}' has both a value and children"
            data[current_parent][key] = value.strip("\"'")
            continue

        if value == "":
            current_parent = key
            data[key] = {}
        else:
            current_parent = None
            data[key] = value.strip("\"'")

    return data, body, None


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        return [f"{skill_dir.name}: no SKILL.md"]

    data, body, err = parse_frontmatter(path.read_text(encoding="utf-8"))
    if err:
        return [f"{skill_dir.name}: {err}"]

    def fail(msg: str) -> None:
        errors.append(f"{skill_dir.name}: {msg}")

    for key in data:
        if key not in ALLOWED_KEYS:
            fail(f"unknown frontmatter key {key!r} (spec allows {sorted(ALLOWED_KEYS)})")

    name = data.get("name")
    if not isinstance(name, str) or not name:
        fail("missing required field 'name'")
    else:
        if len(name) > NAME_MAX:
            fail(f"name is {len(name)} chars, max {NAME_MAX}")
        if not NAME_RE.match(name):
            fail(f"name {name!r} must be lowercase alphanumeric with single internal hyphens")
        if name != skill_dir.name:
            fail(f"name {name!r} does not match directory {skill_dir.name!r}")

    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip():
        fail("missing required field 'description'")
    else:
        if len(desc) > DESC_MAX:
            fail(f"description is {len(desc)} chars, max {DESC_MAX}")
        if len(desc) < DESC_MIN:
            fail(f"description is {len(desc)} chars; too short to route on (min {DESC_MIN})")
        # description が起動条件を述べているかは判定しない。以前は "use when" などの
        # 英語表現を含むかで見ていたが、それは英語の説明文しか通さない検査だった。
        # 文章が要件を満たしているかは、文字列の照合で決められる種類のものではない。

    compat = data.get("compatibility")
    if isinstance(compat, str) and len(compat) > COMPAT_MAX:
        fail(f"compatibility is {len(compat)} chars, max {COMPAT_MAX}")

    meta = data.get("metadata")
    if not isinstance(meta, dict):
        fail("missing 'metadata' mapping (repo convention)")
    else:
        phase = meta.get("phase")
        if phase is None:
            fail("metadata.phase is required by repo convention")
        elif phase not in KNOWN_PHASES:
            fail(f"metadata.phase {phase!r} is not one of {sorted(KNOWN_PHASES)}")

    if body is not None:
        lines = body.count("\n")
        if lines > BODY_MAX_LINES:
            fail(f"body is {lines} lines; spec recommends under {BODY_MAX_LINES} — move detail to references/")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: {SKILLS_DIR} not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        print(f"error: no skills under {SKILLS_DIR}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for d in skill_dirs:
        all_errors.extend(validate(d))

    # The router must name every curated skill, or the curation silently loses one.
    router = SKILLS_DIR / "development-lifecycle" / "SKILL.md"
    catalog_path = ROOT / "catalog.json"
    if router.is_file() and catalog_path.is_file():
        router_text = router.read_text(encoding="utf-8")
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        for phase in catalog["phases"]:
            for entry in phase["entries"]:
                name = entry["skill"]
                # Accept the bare name or any plugin-qualified form of it.
                if f"`{name}`" not in router_text and f":{name}`" not in router_text:
                    all_errors.append(
                        f"development-lifecycle: does not route to curated skill "
                        f"'{name}' ({entry['source']}) — add it to the phase map"
                    )

    # Manifests must be parseable, and the marketplace must point at the plugin.
    for manifest in (
        ROOT / ".claude-plugin" / "marketplace.json",
        ROOT / "plugins" / "dev-lifecycle" / ".claude-plugin" / "plugin.json",
    ):
        try:
            json.loads(manifest.read_text(encoding="utf-8"))
        except FileNotFoundError:
            all_errors.append(f"{manifest.relative_to(ROOT)}: missing")
        except json.JSONDecodeError as exc:
            all_errors.append(f"{manifest.relative_to(ROOT)}: invalid JSON — {exc}")

    if all_errors:
        print(f"FAIL — {len(all_errors)} problem(s):\n", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"OK — {len(skill_dirs)} skills valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
