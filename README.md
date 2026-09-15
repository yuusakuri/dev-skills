# dev-skills

A curated map of community [Agent Skills](https://agentskills.io/specification) covering software work from requirements to production.

It curates existing skills and copies none of them.
Each skill stays in the repository that maintains it.
This repository contributes the map, the pinned commit for each entry, and a check that both are still true.

## Table of Contents

- [Sources](#sources)
- [Install](#install)
- [Usage](#usage)
- [What is here](#what-is-here)
- [Contributing](#contributing)
- [License](#license)

## Sources

| Repository | Stars | License |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 285.6k | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 93.8k | MIT |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT |

Every entry is pinned to a commit, and the pin is checked weekly.
The full list is in [docs/reference/catalog.md](docs/reference/catalog.md).

## Install

Copy the skills into a project.
Anyone who clones it then has them, with no further setup.

```bash
git clone https://github.com/yuusakuri/dev-skills
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project

cd /path/to/your-project
git add .agents/skills .claude/skills .cursor/skills
git commit -m "Add agent skills"
```

The default installs one skill per phase, plus the router.

They go to `.agents/skills/`, the shared convention most agents read.
Claude Code and Cursor do not read it, so they get their own directories too.

| Flag | Effect |
|---|---|
| `--agents agents` | the shared directory only |
| `--agents all` | every directory in [docs/reference/agent-directories.md](docs/reference/agent-directories.md) |
| `--full` | every curated skill, not just one per phase |
| `--list` | print what would be written, write nothing |

## Usage

Start with the `development-lifecycle` skill.
It identifies which phase a task is in and names the skill that owns it, so nobody has to recall the catalog.

Add this to the project's `AGENTS.md`, or to whichever instructions file your agent reads:

```markdown
Start with the `development-lifecycle` skill to identify the phase and the
skill that owns it. Scale the process to the change.

Test command: <command>   Decisions: docs/decisions/
```

Everything else is indexed in [docs/index.md](docs/index.md).

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

MIT for this repository's own content, see [LICENSE](LICENSE).
Curated skills keep their own licences, listed in [NOTICE.md](NOTICE.md).
