# Notices and attribution

## This repository

Everything under `plugins/dev-lifecycle/`, `docs/`, and `scripts/` is original work,
licensed under the MIT License ([LICENSE](LICENSE)), © 2026 yuusakuri.

## Upstream collections

This repository **composes** upstream skill collections rather than vendoring them. No
upstream files are copied here. `.claude-plugin/marketplace.json` references each
upstream repository at a pinned ref; the plugin manager fetches them from their own
repositories at install time, so upstream authors' licences, attribution, and updates
apply directly and unmodified.

### obra/superpowers

- Repository: <https://github.com/obra/superpowers>
- Author: Jesse Vincent
- Licence: MIT
- Pinned at: `v6.3.0`
- Installed as plugin name: `superpowers`

The plugin name is deliberately preserved. Superpowers skills cross-reference each
other as `superpowers:<skill-name>`; installing the collection under any other name
would break those references.

### anthropics/skills

- Repository: <https://github.com/anthropics/skills>
- Author: Anthropic
- Licence: Apache-2.0 (for the skills referenced here)
- Pinned at: commit `34040c9c568585f6929bedeaad110ad08f079624`
- Installed as plugin name: `example-skills`
- Subset referenced: `skill-creator`, `mcp-builder`, `webapp-testing`, `frontend-design`

**Deliberate exclusion.** That repository also contains document skills (`docx`, `pdf`,
`pptx`, `xlsx`) which are *source-available, not open source* — "© 2025 Anthropic, PBC.
All rights reserved." They are excluded from the plugin entry here. If you want them,
install them directly from Anthropic's own marketplace and accept their terms:

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

The remaining example skills in that repository (`algorithmic-art`, `brand-guidelines`,
`canvas-design`, `internal-comms`, `slack-gif-creator`, `theme-factory`,
`web-artifacts-builder`, `academy-guide`, `claude-api`, `discernment-nudge`) are
excluded only because they are outside this collection's scope, not for licensing
reasons. `doc-coauthoring` is excluded because it ships without a licence file.

## Updating a pin

Upstream pins are intentionally explicit so installs are reproducible. To move one,
edit the `ref` in `.claude-plugin/marketplace.json`, then run:

```bash
./scripts/check-upstream.sh
```

Review the upstream changelog before bumping: upstream skill *names* are part of this
repository's routing table, and a renamed or removed upstream skill breaks
`development-lifecycle`.
