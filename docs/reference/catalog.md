# 選定したスキルのカタログ

機械可読な選定結果である[`catalog.json`](../../catalog.json)から起こしたものです。

各項目と、以下のすべての導入コマンドは[`scripts/verify-catalog.py`](../../scripts/verify-catalog.py)が検証しています。上流のファイルはこのリポジトリへ一切コピーしていません。

## 取得元

| リポジトリ | スター | ライセンス | 選定数 |
| --- | --- | --- | --- |
| [`obra/superpowers`](https://github.com/obra/superpowers) | 285.6k | MIT | 12 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 | 4 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 93.8k | MIT | 9 |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | 26 |
| [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | 5 |

### 固定しているref

| リポジトリ | ref |
| --- | --- |
| obra/superpowers | `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`（タグ `v6.3.0`） |
| anthropics/skills | `34040c9c568585f6929bedeaad110ad08f079624` |
| alirezarezvani/claude-skills | `19392f7a08264ed00486a251f5b2098321771f94` |
| mohitagw15856/pm-claude-skills | `f67821d42c8c6db20752030e12ded030a623bee3` |
| addyosmani/agent-skills | `be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39` |

### 導入

以下のマーケットプレイス名とプラグイン名は、各上流の`.claude-plugin/marketplace.json`と照合しています。上流での改名はビルドを落とします。

```bash
# obra/superpowers  (MIT)
# 登録済み: claude-plugins-official は自動的に追加される
/plugin install superpowers@claude-plugins-official

# anthropics/skills  (Apache-2.0)
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills

# alirezarezvani/claude-skills  (MIT)
/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-advanced-skills@claude-code-skills  # ほかに engineering-skills、a11y-audit、security-guidance

# mohitagw15856/pm-claude-skills  (MIT)
/plugin marketplace add mohitagw15856/pm-claude-skills
/plugin install pm-engineering@pm-claude-skills  # ほかに pm-essentials、pm-security、pm-delivery

# addyosmani/agent-skills  (MIT)
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

プロジェクト一括の導入は[README](../../README.md#install)を参照してください。

## 工程別

### 把握

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `codebase-onboarding` | 不案内なコードベースを、変更する前に把握する | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/codebase-onboarding) | `engineering-advanced-skills` |

### 要件

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `brainstorming` | コードを書く前に意図と設計を探る | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/brainstorming) | `superpowers` |
| `prd-template` | 合意を、受け入れ基準を伴うPRDへ書き起こす | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/prd-template) | `pm-essentials` |
| `epic-design` | 大きな要求をエピックとストーリーへ分解する | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/epic-design) | `engineering-skills` |

### アーキテクチャと設計

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `senior-architect` | システム設計と、アーキテクチャ上のトレードオフ | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-architect) | `engineering-skills` |
| `architecture-decision-record` | 覆しにくい決定をADRとして記録する | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/architecture-decision-record) | `pm-engineering` |
| `api-design-reviewer` | 契約のレビュー。linterと破壊的変更の検出スクリプトを同梱 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/api-design-reviewer) | `engineering-advanced-skills` |
| `database-schema-designer` | データモデルの設計 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/database-schema-designer) | `engineering-advanced-skills` |
| `threat-model` | 設計の時点で脅威と対策を洗い出す | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/threat-model) | `pm-security` |
| `frontend-design` | UIの視覚的な方向性を意図して定める | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design) | `example-skills` |
| `tech-stack-evaluator` | 総保有コストとエコシステムの健全性からフレームワークやプラットフォームを選ぶ | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/tech-stack-evaluator) | `engineering-skills` |
| `documentation-and-adrs` | 決定を記録し、将来の保守担当が必要とする文書を書く | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/documentation-and-adrs) | `agent-skills` |

### 計画

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `writing-plans` | 仕様を実行可能な計画に落とす | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-plans) | `superpowers` |
| `senior-qa` | 何をどの層でテストするかを決める | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-qa) | `engineering-skills` |
| `using-git-worktrees` | 実装前に独立した作業環境を用意する | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-git-worktrees) | `superpowers` |
| `constraint-driven-development` | 品質基準を契約として書き、エージェントが黙ってそれを下げるのを捕らえる | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/constraint-driven-development) | `agent-skills` |

### 実装

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `test-driven-development` | 機能追加と不具合修正のすべてをレッド・グリーン・リファクタで進める | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/test-driven-development) | `superpowers` |
| `executing-plans` | レビュー地点を挟みながら、書かれた計画を進める | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/executing-plans) | `superpowers` |
| `subagent-driven-development` | 計画の各タスクをサブエージェントに進めさせる | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/subagent-driven-development) | `superpowers` |
| `dispatching-parallel-agents` | 独立した作業を並行させる | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/dispatching-parallel-agents) | `superpowers` |
| `migration-architect` | スキーマとデータの移行の順序を組む | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/migration-architect) | `engineering-advanced-skills` |
| `tech-debt-tracker` | 構造の整理作業を追跡し、優先順位を付ける | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/tech-debt-tracker) | `engineering-advanced-skills` |
| `mcp-builder` | MCPサーバーを作る | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/mcp-builder) | `example-skills` |
| `env-secrets-manager` | 環境変数の衛生、機密情報の扱い、設定のずれと更新への備え | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/env-secrets-manager) | `engineering-advanced-skills` |
| `security-and-hardening` | 書きながら安全なコードにする。入力の扱い、認証認可、保存、外部連携 | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/security-and-hardening) | `agent-skills` |
| `code-simplification` | 挙動を厳密に保ったまま、読みやすさのために整理する。機能変更とは分ける | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/code-simplification) | `agent-skills` |
| `source-driven-development` | 記憶した書き方ではなく、公式文書に基づいて実装を判断する | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/source-driven-development) | `agent-skills` |

### デバッグと性能

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `systematic-debugging` | 不具合やテストの失敗に対し、修正を提案する前に行う | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/systematic-debugging) | `superpowers` |
| `chaos-engineering` | 障害注入と耐障害性のテスト | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/chaos-engineering) | `engineering-advanced-skills` |
| `performance-optimization` | 計測を先にする性能改善。プロファイルを取り、真のボトルネックを見つけ、改善を示す | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/performance-optimization) | `agent-skills` |
| `ci-cd-and-automation` | パイプラインの設計、キャッシュ、ビルドを信用できる状態に保つこと | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/ci-cd-and-automation) | `agent-skills` |

### 検証

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `verification-before-completion` | 完了を主張する前に根拠を出す | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/verification-before-completion) | `superpowers` |
| `webapp-testing` | Playwrightによる実ブラウザでの検証 | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/webapp-testing) | `example-skills` |
| `a11y-audit` | WCAG 2.2 A/AA の監査と是正 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/a11y-audit/skills/a11y-audit) | `a11y-audit` |

### レビュー

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `requesting-code-review` | レビュアーがレビューできる形に変更を整える | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/requesting-code-review) | `superpowers` |
| `receiving-code-review` | 指摘を形式的にではなく厳密に検討する | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/receiving-code-review) | `superpowers` |
| `pr-review-expert` | 他人の変更をレビューする | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/pr-review-expert) | `engineering-advanced-skills` |
| `senior-security` | 完成した変更にセキュリティ上の欠陥がないか監査する | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-security) | `engineering-skills` |
| `security-guidance` | コードを書いている最中のセキュリティの疑問に答える | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/security-guidance/skills/security-guidance) | `security-guidance` |
| `dependency-auditor` | 依存と脆弱性情報の選別 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/dependency-auditor) | `engineering-advanced-skills` |
| `adversarial-reviewer` | 意図して批判的にレビューし、自己レビューの単一視点を崩す | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/adversarial-reviewer) | `engineering-skills` |

### リリース

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `observability-designer` | リリース前にログ、メトリクス、トレースを用意する | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/observability-designer) | `engineering-advanced-skills` |
| `slo-architect` | SLO、エラーバジェット、アラートのしきい値 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/slo-architect) | `engineering-advanced-skills` |
| `runbook-generator` | アラートごとの運用手順書 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/runbook-generator) | `engineering-advanced-skills` |
| `finishing-a-development-branch` | 完了した作業を統合する | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/finishing-a-development-branch) | `superpowers` |
| `ship-gate` | リリースの可否判断 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/ship-gate) | `engineering-advanced-skills` |
| `changelog-generator` | 変更履歴とリリースノート | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/changelog-generator) | `engineering-advanced-skills` |
| `launch-readiness` | リリース準備の確認項目 | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/launch-readiness) | `pm-delivery` |
| `feature-flags-architect` | フラグの背後で出す。段階的公開、停止スイッチ、放置フラグの負債 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/feature-flags-architect) | `engineering-advanced-skills` |
| `deprecation-and-migration` | API、機能、システムの提供を終え、利用者を安全に移す | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/deprecation-and-migration) | `agent-skills` |

### 運用

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `incident-commander` | 本番障害の最中にサービスを復旧させる | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/incident-commander) | `engineering-skills` |
| `incident-response` | セキュリティ事案を扱う。切り分け、深刻度、調査 | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/incident-response) | `engineering-skills` |
| `incident-postmortem` | 個人を責めない振り返りと対策項目 | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/incident-postmortem) | `pm-engineering` |

### メタ

| スキル | 役割 | 取得元 | 導入プラグイン |
| --- | --- | --- | --- |
| `skill-creator` | スキルを作り、直し、評価する | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator) | `example-skills` |
| `context-engineering` | 出力の質が落ちてきたときに、エージェントの文脈を整える | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/skills/context-engineering) | `agent-skills` |
