# Notices and attribution

## This repository

MIT ([LICENSE](LICENSE)), (c) 2026 yuusakuri. That covers only this repository's own
content: the `development-lifecycle` router skill, `catalog.json`, the scripts, and the
docs.

## Curated upstream skills

**This repository redistributes no upstream content.** `catalog.json` references each
upstream repository at a pinned commit; `/plugin marketplace add` fetches them from
their own repositories at install time. Upstream licences, attribution, and updates
therefore apply directly and unmodified, and each author remains the distributor of
their own work.

Verify at any time with `python3 scripts/verify-catalog.py`, which fetches every
referenced `SKILL.md` from its pinned commit.

### obra/superpowers

- Repository: <https://github.com/obra/superpowers>
- Author: Jesse Vincent
- Licence: MIT
- Pinned commit: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (tag `v6.3.0`)
- Format: Agent Skills
- Skills curated from it: 12

### anthropics/skills

- Repository: <https://github.com/anthropics/skills>
- Author: Anthropic
- Licence: Apache-2.0
- Pinned commit: `34040c9c568585f6929bedeaad110ad08f079624`
- Format: Agent Skills
- Skills curated from it: 4

### alirezarezvani/claude-skills

- Repository: <https://github.com/alirezarezvani/claude-skills>
- Author: Alireza Rezvani
- Licence: MIT
- Pinned commit: `19392f7a08264ed00486a251f5b2098321771f94`
- Format: Agent Skills
- Skills curated from it: 24

### mohitagw15856/pm-claude-skills

- Repository: <https://github.com/mohitagw15856/pm-claude-skills>
- Author: mohitagw15856
- Licence: MIT
- Pinned commit: `f67821d42c8c6db20752030e12ded030a623bee3`
- Format: Agent Skills
- Skills curated from it: 5
- Note: Listed in Anthropic's official plugin directory

### rohitg00/awesome-claude-code-toolkit

- Repository: <https://github.com/rohitg00/awesome-claude-code-toolkit>
- Author: Rohit Ghumare
- Licence: Apache-2.0
- Pinned commit: `ebdf1d596d2cde5c5cceb32177e8d1cf4829e7d9`
- Format: slash commands + agents (NOT Agent Skills)
- Skills curated from it: 1
- Note: Its marketplace exposes command-based plugins; the repo's own skills/ directory is not listed as an installable plugin. Referenced only as an optional supplement.

## Plugin names are preserved deliberately

Superpowers skills cross-reference each other as `superpowers:<skill-name>`. They are
installed from Superpowers' own marketplace under the plugin name `superpowers` so those
references resolve. Re-hosting them under a different plugin name would break them,
which is one of the reasons this repository curates rather than forks.

## Deliberate exclusions

- **Anthropic's document skills** (`docx`, `pdf`, `pptx`, `xlsx` in `anthropics/skills`)
  are *source-available, not open source* — "(c) 2025 Anthropic, PBC. All rights
  reserved." They are outside this curation. To use them, install them directly from
  Anthropic's marketplace and accept their terms:
  `/plugin install document-skills@anthropic-agent-skills`.
- **`doc-coauthoring`** (`anthropics/skills`) ships without a licence file.
- Smaller specialist collections were reviewed and left out of the headline curation on
  scale grounds, not quality: [`arozumenko/sdlc-skills`](https://github.com/arozumenko/sdlc-skills)
  (MIT, ~20 stars, 27 SDLC skills) and
  [`Security-Phoenix-demo/security-skills-claude-code`](https://github.com/Security-Phoenix-demo/security-skills-claude-code)
  (MIT, ~70 stars, 27 security skills including a dedicated `threat-modeling` and
  `security-reviewer`). Both are reasonable additions for teams wanting deeper coverage
  in those areas.

## Updating a pin

Pins are explicit so installs are reproducible. To move one, edit the `ref` in
`catalog.json`, then run:

```bash
python3 scripts/verify-catalog.py
python3 scripts/validate-skills.py
```

Upstream skill *names* are part of this repository's routing table, so a rename or
removal upstream will fail verification. That is the intended behavior: fix the catalog
and the router rather than letting the map drift.
