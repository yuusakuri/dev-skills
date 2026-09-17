# dev-skills

要件定義から本番運用までのソフトウェア開発を対象に、公開されている[Agent Skills](https://agentskills.io/specification)を選んで整理したものです。

スキルを複製はしません。それぞれのスキルは、保守しているリポジトリに置かれたままです。

このリポジトリが足すのは、どのスキルがどの工程を担うかの対応表、各スキルを固定したコミット、そして両方がまだ正しいかを確かめる検査です。

## 取得元

| リポジトリ | スター | ライセンス |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | 285.6k | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 93.8k | MIT |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT |

各スキルはコミットで固定していて、週に一度検査しています。選んだスキルの一覧は[docs/reference/catalog.md](docs/reference/catalog.md)にあります。

## Install

スキルをプロジェクトへコピーします。以降は、そのリポジトリをクローンした人が追加の設定なしに使えます。

```bash
git clone https://github.com/yuusakuri/dev-skills
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project

cd /path/to/your-project
git add .agents/skills .claude/skills .cursor/skills
git commit -m "Add agent skills"
```

既定では、各工程から1つずつと、ルーターが入ります。

置き場所は`.agents/skills/`です。多くのエージェントが読む共通の場所です。Claude CodeとCursorはここを読まないので、それぞれのディレクトリにも書き込みます。

| オプション | 効果 |
| --- | --- |
| `--agents agents` | 共通のディレクトリだけに書き込む |
| `--agents all` | [docs/reference/agent-directories.md](docs/reference/agent-directories.md)にある全ディレクトリに書き込む |
| `--full` | 各工程から1つではなく、選んだスキルをすべて入れる |
| `--list` | 書き込まずに、書き込む内容だけを表示する |

## Usage

`development-lifecycle`スキルから始めます。作業がどの工程にあるかを判断し、その工程を担うスキルを名指しするので、一覧を覚えておく必要はありません。

プロジェクトの`AGENTS.md`、または使っているエージェントが読む指示ファイルに、次を加えてください。

```markdown
Start with the `development-lifecycle` skill to identify the phase and the
skill that owns it. Scale the process to the change.

Test command: <command>   Decisions: docs/decisions/
```

そのほかのドキュメントは[docs/index.md](docs/index.md)から辿れます。

## このリポジトリの中身

| パス | 役割 |
| --- | --- |
| `catalog.json` | どのスキルがどの工程を担い、どのコミットで固定しているか |
| `plugins/dev-lifecycle/` | このリポジトリが持つ唯一のスキル。ルーター |
| `scripts/install-skills.py` | 選んだスキルをプロジェクトへコピーする |
| `scripts/verify-catalog.py` | 参照と導入コマンドがまだ解決するかを確かめる |

検査は`python3 scripts/verify-catalog.py`で実行します。

## Contributing

貢献の手順は[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

## License

このリポジトリ自身の内容はMITです。[LICENSE](LICENSE)を参照してください。

選んだスキルはそれぞれのライセンスに従います。一覧は[NOTICE.md](NOTICE.md)にあります。
