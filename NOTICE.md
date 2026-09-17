# 権利表示と帰属

## このリポジトリ

MIT（[LICENSE](LICENSE)）、(c) 2026 yuusakuri。

対象はこのリポジトリ自身の内容に限ります。`development-lifecycle`ルータースキル、`catalog.json`、各スクリプト、ドキュメントです。

## 選定した上流のスキル

このリポジトリは上流の内容を一切再配布しません。

`catalog.json`は各上流リポジトリを固定したコミットで参照するだけで、`/plugin marketplace add`が導入時にそれぞれのリポジトリから取得します。上流のライセンス、帰属、更新はそのまま直接適用され、各著者が自身の成果物の配布者であり続けます。

`python3 scripts/verify-catalog.py`でいつでも確認できます。参照している`SKILL.md`をすべて固定コミットから取得し、記載した導入コマンドが実在するマーケットプレイスとプラグインを指しているかを検査します。

### obra/superpowers

- リポジトリ: <https://github.com/obra/superpowers>
- 著者: Jesse Vincent
- ライセンス: MIT
- 固定コミット: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` （タグ `v6.3.0`）
- 選定数: 12

### anthropics/skills

- リポジトリ: <https://github.com/anthropics/skills>
- 著者: Anthropic
- ライセンス: Apache-2.0
- 固定コミット: `34040c9c568585f6929bedeaad110ad08f079624`
- 選定数: 4

### addyosmani/agent-skills

- リポジトリ: <https://github.com/addyosmani/agent-skills>
- 著者: Addy Osmani
- ライセンス: MIT
- 固定コミット: `be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39`
- 選定数: 9
- 備考: 実務水準のエンジニアリング用スキル。ミラー経由ではなく上流のHEADを参照している

### alirezarezvani/claude-skills

- リポジトリ: <https://github.com/alirezarezvani/claude-skills>
- 著者: Alireza Rezvani
- ライセンス: MIT
- 固定コミット: `19392f7a08264ed00486a251f5b2098321771f94`
- 選定数: 26

### mohitagw15856/pm-claude-skills

- リポジトリ: <https://github.com/mohitagw15856/pm-claude-skills>
- 著者: mohitagw15856
- ライセンス: MIT
- 固定コミット: `f67821d42c8c6db20752030e12ded030a623bee3`
- 選定数: 5
- 備考: Anthropicの公式プラグイン一覧に掲載されている

## ミラーではなく本家を参照する理由

スキルは、それを書いたリポジトリから参照します。複製を取り込んだカタログ経由では参照しません。

取り込んだ複製はずれていきます。広く使われている`addyosmani/agent-skills`のミラーの1つは上流より数リビジョン遅れていて、その`security-and-hardening`は上流に存在する約57行を欠いています。

取り込むこと自体は正当な方式です。オフラインで動きますし、固定も厳密になります。ただし、最新に保つ責任が取り込む側のカタログに移ります。このリポジトリはもう一方のトレードオフを選んでいます。

## プラグイン名を保っている理由

superpowersのスキルは互いを`superpowers:<skill-name>`の形で相互参照します。そのため`superpowers`というプラグイン名で導入し、その参照が解決するようにしています。

## 選定から外したもの

| 対象 | 外した理由 |
| --- | --- |
| Anthropicの文書スキル（`docx`、`pdf`、`pptx`、`xlsx`） | ソース公開であってオープンソースではない。"(c) 2025 Anthropic, PBC. All rights reserved."<br>必要ならAnthropic自身のマーケットプレイスから導入し、その条件に同意すること |
| `doc-coauthoring`（`anthropics/skills`） | ライセンスファイルが同梱されていない |
| [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit)（2.6kスター、Apache-2.0） | マーケットプレイスがコマンド型のプラグインしか公開しておらず、リポジトリ自身の`skills/`ディレクトリが導入可能なプラグインになっていない |
| [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills)（26.3kスター、MIT） | `pre-mortem`と`retro`が、`ship-gate`と`launch-readiness`に対して足すものが少ない |
| [`arozumenko/sdlc-skills`](https://github.com/arozumenko/sdlc-skills)、[`Security-Phoenix-demo/security-skills-claude-code`](https://github.com/Security-Phoenix-demo/security-skills-claude-code) | 品質ではなく規模を理由に見送った |

## 固定先の更新

`catalog.json`の`ref`を編集し、次を実行します。

```bash
python3 scripts/verify-catalog.py
python3 scripts/validate-skills.py
```

上流のスキル名とプラグイン名は、このリポジトリの割り当てと導入手順の一部です。上流での改名は、設計どおり検証を失敗させます。
