# エージェントのディレクトリ

`.agents/skills/`が共通の置き場である。
多くのエージェントがここを読む。

| `.agents/skills/`を読む |
| --- |
| Codex |
| Gemini CLI |
| OpenCode |
| GitHub Copilot |
| CommandCode |

読まないものが2つあり、それぞれ専用のディレクトリが要る。

| エージェント | ディレクトリ | `--agents`の名前 |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `claude` |
| Cursor | `.cursor/skills/` | `cursor` |

既定ではこの3つすべてに書き込む（`agents,claude,cursor`）。

エージェントによっては、より狭い範囲の置き場所も受け付ける。
指定は任意である。共通のディレクトリで既に足りている。

| ディレクトリ | `--agents`の名前 | エージェント |
| --- | --- | --- |
| `.gemini/skills/` | `gemini` | Gemini CLI、ワークスペース単位 |
| `.opencode/skills/` | `opencode` | OpenCode |
| `.github/skills/` | `copilot` | GitHub Copilot |

`codex`と`commandcode`は`agents`の別名である。
`all`はこのページにある全ディレクトリへ書き込む。
