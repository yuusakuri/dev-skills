# Notices and attribution

## This repository

MIT ([LICENSE](LICENSE)), (c) 2026 yuusakuri.
That covers only this repository's own content: the `development-lifecycle` router skill, `catalog.json`, the scripts, and the docs.

## Curated upstream skills

**This repository redistributes no upstream content.** `catalog.json` references each upstream repository at a pinned commit; `/plugin marketplace add` fetches them from their own repositories at install time.
Upstream licences, attribution, and updates therefore apply directly and unmodified, and each author remains the distributor of their own work.

Verify at any time with `python3 scripts/verify-catalog.py`, which fetches every referenced `SKILL.md` from its pinned commit and checks that every documented install command names a marketplace and plugin that really exist.

### obra/superpowers

- Repository: <https://github.com/obra/superpowers>
- Author: Jesse Vincent
- Licence: MIT
- Pinned commit: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (tag `v6.3.0`)
- Skills curated from it: 12

### anthropics/skills

- Repository: <https://github.com/anthropics/skills>
- Author: Anthropic
- Licence: Apache-2.0
- Pinned commit: `34040c9c568585f6929bedeaad110ad08f079624`
- Skills curated from it: 4

### addyosmani/agent-skills

- Repository: <https://github.com/addyosmani/agent-skills>
- Author: Addy Osmani
- Licence: MIT
- Pinned commit: `be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39`
- Skills curated from it: 9
- Note: Production-grade engineering skills.
  Referenced at upstream HEAD rather than through any mirror, because vendored copies of it in the wild are already several revisions behind.

### alirezarezvani/claude-skills

- Repository: <https://github.com/alirezarezvani/claude-skills>
- Author: Alireza Rezvani
- Licence: MIT
- Pinned commit: `19392f7a08264ed00486a251f5b2098321771f94`
- Skills curated from it: 26

### mohitagw15856/pm-claude-skills

- Repository: <https://github.com/mohitagw15856/pm-claude-skills>
- Author: mohitagw15856
- Licence: MIT
- Pinned commit: `f67821d42c8c6db20752030e12ded030a623bee3`
- Skills curated from it: 5
- Note: Listed in Anthropic's official plugin directory

## Why origins, not mirrors

Skills are referenced from the repository that authors them, never through a catalog that has vendored a copy.
Vendored copies drift: at the time of writing, one widely used mirror of `addyosmani/agent-skills` is pinned several revisions behind upstream, and its copy of `security-and-hardening` is missing roughly 57 lines that exist upstream.

Vendoring is a legitimate approach — it works offline and pins exactly — but it makes the vendoring catalog responsible for staying current.
This repository chose the other trade-off.

## Plugin names are preserved deliberately

Superpowers skills cross-reference each other as `superpowers:<skill-name>`, so they are installed under the plugin name `superpowers` and those references resolve.

## Deliberate exclusions

- **Anthropic's document skills** (`docx`, `pdf`, `pptx`, `xlsx`) are *source-available, not open source* — "(c) 2025 Anthropic, PBC.
  All rights reserved." Install them from Anthropic's own marketplace and accept their terms if you want them.
- **`doc-coauthoring`** (`anthropics/skills`) ships without a licence file.
- **`rohitg00/awesome-claude-code-toolkit`** (2.6k stars, Apache-2.0) was curated and then removed: its marketplace exposes only command-based plugins, and the repository's own `skills/` directory is not an installable plugin, so the one entry taken from it could never be installed by the documented method.
- **`phuryn/pm-skills`** (26.3k stars, MIT): `pre-mortem` (4.1 KB) and `retro` (2.8 KB) add little over `ship-gate` and `launch-readiness`.
- Smaller specialist collections reviewed and left out on scale grounds, not quality: [`arozumenko/sdlc-skills`](https://github.com/arozumenko/sdlc-skills) and [`Security-Phoenix-demo/security-skills-claude-code`](https://github.com/Security-Phoenix-demo/security-skills-claude-code).

## Updating a pin

Edit the `ref` in `catalog.json`, then run:

```bash
python3 scripts/verify-catalog.py
python3 scripts/validate-skills.py
```

Upstream skill *names* and plugin names are part of this repository's routing and install instructions, so a rename upstream fails verification by design.
