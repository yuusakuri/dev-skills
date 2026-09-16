# 権利表示と帰属

## このリポジトリ

MIT（[LICENSE](LICENSE)）、(c) 2026 yuusakuri。
対象はこのリポジトリ自身の内容に限る。`development-lifecycle`ルータースキル、`catalog.json`、各スクリプト、ドキュメント。

## 選定した上流のスキル

このリポジトリは上流の内容を一切再配布しない。`catalog.json`は各上流リポジトリを固定したコミットで参照するだけで、`/plugin marketplace add`が導入時にそれぞれのリポジトリから取得する。
したがって上流のライセンス、帰属、更新はそのまま直接適用され、各著者が自身の成果物の配布者であり続ける。

`python3 scripts/verify-catalog.py`でいつでも確認できる。参照している`SKILL.md`をすべて固定コミットから取得し、記載した導入コマンドが実在するマーケットプレイスとプラグインを指しているかを検査する。

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
- 備考: 実務水準のエンジニアリング用スキル。
  ミラー経由ではなく上流のHEADを参照している。出回っている複製は既に数リビジョン遅れているためである。

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

スキルは、それを書いたリポジトリから参照する。複製を取り込んだカタログ経由では参照しない。
取り込んだ複製はずれていく。本稿の執筆時点で、広く使われている`addyosmani/agent-skills`のミラーの1つは上流より数リビジョン遅れており、その`security-and-hardening`は上流に存在する約57行を欠いている。

取り込むこと自体は正当な方式である。オフラインで動き、固定も厳密になる。ただし、最新に保つ責任が取り込む側のカタログに移る。
このリポジトリはもう一方のトレードオフを選んだ。

## プラグイン名を意図して保っている

superpowersのスキルは互いを`superpowers:<skill-name>`の形で相互参照する。したがって`superpowers`というプラグイン名で導入し、その参照が解決するようにしている。

## 意図的に除外したもの

- **Anthropicの文書スキル**（`docx`、`pdf`、`pptx`、`xlsx`）はソース公開であってオープンソースではない。
  "(c) 2025 Anthropic, PBC. All rights reserved." 必要ならAnthropic自身のマーケットプレイスから導入し、その条件に同意すること。
- **`doc-coauthoring`**（`anthropics/skills`）にはライセンスファイルが同梱されていない。
- **`rohitg00/awesome-claude-code-toolkit`**（2.6kスター、Apache-2.0）は一度選定したのち削除した。マーケットプレイスがコマンド型のプラグインしか公開しておらず、リポジトリ自身の`skills/`ディレクトリは導入可能なプラグインになっていない。そのため、そこから採った1件は、記載した方法では決して導入できなかった。
- **`phuryn/pm-skills`**（26.3kスター、MIT）。`pre-mortem`（4.1 KB）と`retro`（2.8 KB）は、`ship-gate`と`launch-readiness`に対して足すものが少ない。
- 規模を理由に見送った、品質ではない理由での小規模な専門コレクション。[`arozumenko/sdlc-skills`](https://github.com/arozumenko/sdlc-skills)と[`Security-Phoenix-demo/security-skills-claude-code`](https://github.com/Security-Phoenix-demo/security-skills-claude-code)。

## 固定先の更新

`catalog.json`の`ref`を編集し、次を実行する。

```bash
python3 scripts/verify-catalog.py
python3 scripts/validate-skills.py
```

上流のスキル名とプラグイン名は、このリポジトリの割り当てと導入手順の一部である。したがって上流での改名は、設計どおり検証を失敗させる。
