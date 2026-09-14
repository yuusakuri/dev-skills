# Agent directories

Where each agent discovers skills, and the `--agents` name that writes it.

| `--agents` name | Directory | Read by |
|---|---|---|
| `claude` | `.claude/skills/` | Claude Code |
| `agents` | `.agents/skills/` | Codex, Gemini CLI, OpenCode, Copilot, CommandCode |
| `gemini` | `.gemini/skills/` | Gemini CLI, workspace scope |
| `cursor` | `.cursor/skills/` | Cursor |
| `opencode` | `.opencode/skills/` | OpenCode |
| `copilot` | `.github/skills/` | GitHub Copilot |

Aliases: `codex` and `commandcode` both resolve to `agents`.

`all` writes every directory in the table.

The default is `claude,agents`.

Claude Code does not read `.agents/skills/`.
