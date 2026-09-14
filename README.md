# dev-skills

A curated map of community [Agent Skills](https://agentskills.io/specification)
covering software work from requirements to production.

It curates existing skills. It copies none of them. Each one stays in the
repository that maintains it; this repository contributes the map, the pinned
versions, and a check that the map is still true.

## Table of Contents

- [Sources](#sources)
- [Install](#install)
- [Usage](#usage)
- [What is here](#what-is-here)
- [Contributing](#contributing)
- [License](#license)

## Sources

| Repository | Stars | License | Skills |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 285.6k | MIT | 12 |
| [anthropics/skills](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 | 4 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 93.8k | MIT | 9 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | 26 |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | 5 |

56 skills across 11 phases, each pinned to a commit and verified to resolve.

## Install

Copy the skills into a project. Anyone who clones it then has them, with no
further setup.

```bash
git clone https://github.com/yuusakuri/dev-skills
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project

cd /path/to/your-project
git add .claude/skills .agents/skills && git commit -m "Add agent skills"
```

The default installs 20 skills covering every phase once, for Claude Code and
for the agents that read `.agents/skills`. See
[docs/adoption.md](docs/adoption.md) for the other options, for installing as
plugins instead, and for the licence notices the installer writes.

## Usage

Start with the `development-lifecycle` skill. It identifies which phase a task
is in and names the skill that owns it, so nobody has to remember 56 names.

Add this to the project's `CLAUDE.md`:

```markdown
Start with the `development-lifecycle` skill to identify the phase and the
skill that owns it. Scale the process to the change.

Test command: <command>   Decisions: docs/decisions/
```

Full skill list by phase: [docs/catalog.md](docs/catalog.md).
Why the phases are ordered as they are: [docs/lifecycle.md](docs/lifecycle.md).

## What is here

| Path | Purpose |
|---|---|
| `catalog.json` | Which skill owns which phase, at which commit |
| `plugins/dev-lifecycle/` | The one skill hosted here: a router |
| `scripts/install-skills.py` | Copies curated skills into a project |
| `scripts/verify-catalog.py` | Checks every reference and install command still resolves |

Run the checks with `python3 scripts/verify-catalog.py`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT for this repository's own content, see [LICENSE](LICENSE). Curated skills
keep their own licences, listed in [NOTICE.md](NOTICE.md).
