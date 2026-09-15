# Agent directories

`.agents/skills/` is the shared convention. Most agents read it.

| Reads `.agents/skills/` |
|---|
| Codex |
| Gemini CLI |
| OpenCode |
| GitHub Copilot |
| CommandCode |

Two do not, and need a directory of their own.

| Agent | Directory | `--agents` name |
|---|---|---|
| Claude Code | `.claude/skills/` | `claude` |
| Cursor | `.cursor/skills/` | `cursor` |

The default writes all three: `agents,claude,cursor`.

Some agents accept a second, narrower location. Passing these is optional; the
shared directory already covers them.

| Directory | `--agents` name | Agent |
|---|---|---|
| `.gemini/skills/` | `gemini` | Gemini CLI, workspace scope |
| `.opencode/skills/` | `opencode` | OpenCode |
| `.github/skills/` | `copilot` | GitHub Copilot |

`codex` and `commandcode` are aliases for `agents`. `all` writes every directory
in this page.
