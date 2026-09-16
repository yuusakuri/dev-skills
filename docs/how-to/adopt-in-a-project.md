# プロジェクトへ定着させる方法

スキルをインストールすれば、使える状態にはなる。
実際に使われるかどうかを決めるのは、次の3つである。

## エージェントへの指示からルーターを指す

`AGENTS.md`、または使っているエージェントが読む指示ファイルに次を置く。

```markdown
## Working in this repository

Start with the `development-lifecycle` skill to identify the phase and the skill that
owns it. Scale the process to the change: trivial fixes go straight to implementation
and verification; anything touching <the risky areas of this project> requires a threat
model and an ADR.

Project specifics that override general practice:
- Test command: <command>
- Requirements live in: docs/requirements/
- Decisions live in: docs/decisions/
```

最後の段落が最も重要である。
選定したスキルは意図的に汎用である。技術構成に固有の事実はこのファイルに書き、そちらが優先される。

## スキルが書き込む先のディレクトリを作る

いくつかのスキルは、会話ログではなくリポジトリに置くべき成果物を生む。

```
docs/requirements/   prd-template
docs/decisions/      architecture-decision-record
docs/security/       threat-model
docs/postmortems/    incident-postmortem
docs/runbooks/       runbook-generator
```

成果物の置き場がないスキルは、流れて消えるメッセージを出すだけになる。

## 段階的に導入する

初日から10工程すべてを義務づけると、全体が放棄される。
現実的な順序は次のとおり。

1. `superpowers:verification-before-completion`と`test-driven-development`。品質への効果が目に見え、チームの合意も要らない。
2. `codebase-onboarding`と`superpowers:brainstorming`。負担が軽く、見当違いの場所から始めることによる手戻りを減らす。
3. `prd-template`と`architecture-decision-record`。チームの合意が要る最初の2つである。他人が読む成果物を生むためである。
4. `ship-gate`、`observability-designer`、`incident-commander`、`incident-postmortem`。停止時間が問題になる利用者がついた時点で。
5. `threat-model`、`senior-security`、`a11y-audit`。実際の利用者データを扱う、あるいは公開する最初のリリースの前に。

## 動作を確認する

エージェントに次を尋ねる。

> リリースするかどうかを判断するのはどのスキル？

`ship-gate`または`launch-readiness`と答えるはずである。
答えられない場合、スキルが読み込まれていない。エージェントが読むディレクトリが存在するかを確認し、セッションを再起動する。
