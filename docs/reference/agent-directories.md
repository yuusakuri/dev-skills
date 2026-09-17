# エージェントのディレクトリ

`.agents/skills/`が共通の置き場所です。次のエージェントがここを読みます。

| エージェント |
| --- |
| Codex |
| Gemini CLI |
| OpenCode |
| GitHub Copilot |
| CommandCode |

読まないものが2つあり、それぞれ専用のディレクトリが要ります。

| エージェント | ディレクトリ | `--agents`の名前 |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `claude` |
| Cursor | `.cursor/skills/` | `cursor` |

既定ではこの3つすべてに書き込みます（`agents,claude,cursor`）。

エージェントによっては、より狭い範囲の置き場所も受け付けます。共通のディレクトリで足りるので、指定は任意です。

| ディレクトリ | `--agents`の名前 | エージェント |
| --- | --- | --- |
| `.gemini/skills/` | `gemini` | Gemini CLI、ワークスペース単位 |
| `.opencode/skills/` | `opencode` | OpenCode |
| `.github/skills/` | `copilot` | GitHub Copilot |

`codex`と`commandcode`は`agents`の別名です。`all`はこのページにある全ディレクトリへ書き込みます。
