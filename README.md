# dev-skills

要件定義から本番運用までのソフトウェア開発を対象に、公開されている[Agent Skills](https://agentskills.io/specification)を選び、整理した地図である。

既存のスキルを選ぶだけで、複製はしない。
各スキルは、それを保守しているリポジトリに置かれたままである。
このリポジトリが足すのは、対応表、各項目の固定コミット、そして両者がまだ正しいかを確かめる検査である。

## 目次

- [取得元](#取得元)
- [インストール](#インストール)
- [使い方](#使い方)
- [このリポジトリの中身](#このリポジトリの中身)
- [コントリビュート](#コントリビュート)
- [ライセンス](#ライセンス)

## 取得元

| リポジトリ | スター | ライセンス |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | 285.6k | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 93.8k | MIT |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT |

各項目はコミットで固定されており、週次で検査される。
一覧は[docs/reference/catalog.md](docs/reference/catalog.md)にある。

## インストール

スキルをプロジェクトへコピーする。
以降、そのリポジトリをクローンした人は、追加の設定なしに使える。

```bash
git clone https://github.com/yuusakuri/dev-skills
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project

cd /path/to/your-project
git add .agents/skills .claude/skills .cursor/skills
git commit -m "Add agent skills"
```

既定では、各工程から1つずつと、ルーターが入る。

置き場所は`.agents/skills/`である。多くのエージェントが読む共通の場所である。
Claude CodeとCursorはここを読まないので、それぞれのディレクトリにも書き込む。

| オプション | 効果 |
| --- | --- |
| `--agents agents` | 共通のディレクトリのみ |
| `--agents all` | [docs/reference/agent-directories.md](docs/reference/agent-directories.md)にある全ディレクトリ |
| `--full` | 各工程から1つではなく、選定した全スキル |
| `--list` | 書き込まずに、書き込む内容だけを表示する |

## 使い方

`development-lifecycle`スキルから始める。
作業がどの工程にあるかを判断し、その工程を担うスキルを名指しするので、一覧を覚えておく必要はない。

プロジェクトの`AGENTS.md`、または使っているエージェントが読む指示ファイルに、次を加える。

```markdown
Start with the `development-lifecycle` skill to identify the phase and the
skill that owns it. Scale the process to the change.

Test command: <command>   Decisions: docs/decisions/
```

その他は[docs/index.md](docs/index.md)から辿れる。

## このリポジトリの中身

| パス | 役割 |
| --- | --- |
| `catalog.json` | どのスキルがどの工程を担うか、どのコミットで固定しているか |
| `plugins/dev-lifecycle/` | このリポジトリが持つ唯一のスキル。ルーター |
| `scripts/install-skills.py` | 選定したスキルをプロジェクトへコピーする |
| `scripts/verify-catalog.py` | 参照と導入コマンドがまだ解決するかを確かめる |

検査は`python3 scripts/verify-catalog.py`で実行する。

## コントリビュート

[CONTRIBUTING.md](CONTRIBUTING.md)を参照する。

## ライセンス

このリポジトリ自身の内容はMIT。[LICENSE](LICENSE)を参照する。
選定したスキルはそれぞれのライセンスに従う。一覧は[NOTICE.md](NOTICE.md)にある。
