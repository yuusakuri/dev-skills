# dev-skills

**A curated, verified map of the best community [Agent Skills](https://agentskills.io/specification)
for the whole software lifecycle — requirements definition through production operations.**

This repository **curates existing published skills. It copies none of them.** Every
skill it routes to lives in, and is maintained by, its own repository; this repo
contributes the map, the pinned versions, and the verification that the map is still
true.

## Sources

All five are established, permissively licensed, public projects:

| Repository | Stars | License | Format | Curated |
|---|---|---|---|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | 285.6k | MIT | Agent Skills | 12 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 | Agent Skills | 4 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 93.8k | MIT | Agent Skills | 9 |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | Agent Skills | 26 |
| [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | Agent Skills | 5 |

**56 skills across 11 phases**, each pinned to a specific upstream commit and verified
to resolve. Star counts are as shown on each repository page at the time of curation.

## What this repository actually contains

Only three things — and deliberately nothing else:

1. **[`catalog.json`](catalog.json)** — the machine-readable curation: which upstream
   skill owns which lifecycle phase, at which pinned commit.
2. **One skill, [`development-lifecycle`](plugins/dev-lifecycle/skills/development-lifecycle/SKILL.md)**
   — a router. It owns no practice of its own; it works out which phase a task is in and
   hands off to the community skill that covers it.
3. **[`scripts/verify-catalog.py`](scripts/verify-catalog.py)** — fetches all 56
   referenced `SKILL.md` files from their pinned commits and fails if any has been
   renamed, moved, or deleted. This is the only way a curation can rot, so it runs in CI.

## Why curate instead of fork

- Upstream skills keep receiving their authors' fixes; a fork freezes them.
- Cross-references keep resolving. Superpowers skills reference each other as
  `superpowers:test-driven-development`; re-hosting them under another plugin name
  breaks that.
- Licence and attribution stay simple, because nothing is redistributed.

## Install

### Just for yourself

```bash
# The router (this repo)
/plugin marketplace add yuusakuri/dev-skills
/plugin install dev-lifecycle@dev-skills

# The skills it routes to, each from its own marketplace
/plugin install superpowers@claude-plugins-official      # already registered by Claude Code

/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills

/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-advanced-skills@claude-code-skills
/plugin install engineering-skills@claude-code-skills
/plugin install a11y-audit@claude-code-skills
/plugin install security-guidance@claude-code-skills

/plugin marketplace add mohitagw15856/pm-claude-skills
/plugin install pm-engineering@pm-claude-skills
/plugin install pm-essentials@pm-claude-skills
/plugin install pm-security@pm-claude-skills
/plugin install pm-delivery@pm-claude-skills
```

Every marketplace and plugin name above is checked against the upstream's own
`.claude-plugin/marketplace.json` by `scripts/verify-catalog.py`, so these commands
cannot silently rot.

### Into another repository, for the whole team

Commit the plugin configuration so everyone on the project gets the same skills.

**1. Generate the project settings** — run this from a clone of *this* repo, pointing at
the project you want to set up:

```bash
python3 scripts/gen-project-settings.py --write /path/to/your-project
```

That merges `extraKnownMarketplaces` and `enabledPlugins` into
`your-project/.claude/settings.json`, preserving any settings already there. To inspect
it first, run the command with no `--write`.

**2. Commit it**:

```bash
cd /path/to/your-project
git add .claude/settings.json && git commit -m "Add dev-skills plugin configuration"
```

**3. Each developer installs once.** This step is not optional, and it is the part most
people get wrong: committing the settings registers the marketplaces, but Claude Code
(v2.1.195+) **does not auto-install plugins that come from an external source**. Until
each person installs, Claude Code reports the plugins as not installed.

```bash
python3 /path/to/dev-skills/scripts/gen-project-settings.py --commands
```

That prints the exact `claude plugin install ... --scope project` lines to run. Or
install interactively with `/plugin install <name>@<marketplace>` and choose
**Project scope**.

**4. Point your agent instructions at the router.** In the project's `CLAUDE.md`:

```markdown
Start with the `development-lifecycle` skill to identify the phase and the skill that
owns it. Scale the process to the change: trivial fixes go straight to implementation
and verification; anything touching <the risky areas of this project> requires a threat
model and an ADR.

Test command: <command>   Decisions: docs/decisions/   Requirements: docs/requirements/
```

**5. Verify it took.** Ask the agent *"Which skill covers deciding whether to ship a
release?"* — it should answer `ship-gate` or `launch-readiness`. If not, run
`/plugin` and check the **Installed** tab, then `/reload-plugins`.

### Without Claude Code

Every curated skill is a plain [Agent Skills](https://agentskills.io/specification)
directory, so other agents can use them too. The
[skills CLI](https://github.com/vercel-labs/skills) installs into 70+ agents:

```bash
npx skills add addyosmani/agent-skills --skill code-simplification
```

Or clone an upstream at the ref pinned in [`catalog.json`](catalog.json) and copy the
directory. Always take skills from the repository that authors them, not from a mirror —
see [NOTICE.md](NOTICE.md#why-origins-not-mirrors).

Per-phase install targets: [docs/catalog.md](docs/catalog.md). More on adoption:
[docs/adoption.md](docs/adoption.md).

## How to use it

Start with **`development-lifecycle`**. It routes, and it scales the process to the
work — a typo does not get a requirements document:

| Task size | Phases |
|---|---|
| Trivial (typo, obvious one-liner) | implement → verify |
| Small (contained, reversible) | requirements → implement → verify → review |
| Standard (a new feature) | orientation → requirements → design → plan → implement → verify → review → release |
| High-stakes (data model, auth, money, public API) | every phase; threat model and ADR mandatory |

## Coverage

| Phase | Skills |
|---|---|
| **0 · Orientation** | `codebase-onboarding` |
| **1 · Requirements** | `brainstorming` · `prd-template` · `epic-design` |
| **2 · Design** | `senior-architect` · `architecture-decision-record` · `api-design-reviewer` · `database-schema-designer` · `threat-model` · `frontend-design` · `tech-stack-evaluator` · `documentation-and-adrs` |
| **3 · Planning** | `writing-plans` · `senior-qa` · `using-git-worktrees` · `constraint-driven-development` |
| **4 · Implementation** | `test-driven-development` · `tdd-guide` · `executing-plans` · `subagent-driven-development` · `dispatching-parallel-agents` · `migration-architect` · `tech-debt-tracker` · `mcp-builder` · `env-secrets-manager` · `security-and-hardening` · `code-simplification` · `source-driven-development` |
| **5 · Quality** | `systematic-debugging` · `chaos-engineering` · `performance-optimization` · `ci-cd-and-automation` |
| **6 · Verification** | `verification-before-completion` · `webapp-testing` · `a11y-audit` |
| **7 · Review** | `requesting-code-review` · `receiving-code-review` · `pr-review-expert` · `senior-security` · `security-guidance` · `dependency-auditor` · `adversarial-reviewer` |
| **8 · Release** | `observability-designer` · `slo-architect` · `runbook-generator` · `finishing-a-development-branch` · `ship-gate` · `changelog-generator` · `launch-readiness` · `feature-flags-architect` · `deprecation-and-migration` |
| **9 · Operations** | `incident-commander` · `incident-response` · `incident-postmortem` |
| **Meta** | `development-lifecycle` · `skill-creator` · `context-engineering` |

Phase-by-phase rationale and handoffs: [docs/lifecycle.md](docs/lifecycle.md).

## Known thin spots

Stated rather than papered over: **behavior-preserving refactoring** and **flaky-test
diagnosis** have no strong Skill-format option upstream — the nearest options
(`refactor-engine`, `ci-debugger`) are slash commands. The router states the operating
rule for both inline so the phase is not silently skipped. See
[docs/catalog.md](docs/catalog.md#known-thin-spots).

## Maintenance

```bash
python3 scripts/verify-catalog.py   # all 57 upstream refs still resolve
python3 scripts/validate-skills.py  # spec conformance + router covers every catalog entry
./scripts/check-upstream.sh         # pinned refs are immutable, not moving branches
```

All three run in CI on every push, and weekly on a schedule to catch upstream drift.

## Licence

This repository's own content (the router skill, catalog, scripts, docs) is MIT —
see [LICENSE](LICENSE). Curated skills remain under their own repositories' licences;
see [NOTICE.md](NOTICE.md).

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
