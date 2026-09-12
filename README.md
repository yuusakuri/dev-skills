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
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | Agent Skills | 24 |
| [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) | 2.6k | Apache-2.0 | commands + agents | 1 |
| [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | Agent Skills | 5 |

**46 skills across 11 phases**, each pinned to a specific upstream commit and verified
to resolve. Star counts are as shown on each repository page at the time of curation.

## What this repository actually contains

Only three things — and deliberately nothing else:

1. **[`catalog.json`](catalog.json)** — the machine-readable curation: which upstream
   skill owns which lifecycle phase, at which pinned commit.
2. **One skill, [`development-lifecycle`](plugins/dev-lifecycle/skills/development-lifecycle/SKILL.md)**
   — a router. It owns no practice of its own; it works out which phase a task is in and
   hands off to the community skill that covers it.
3. **[`scripts/verify-catalog.py`](scripts/verify-catalog.py)** — fetches all 46
   referenced `SKILL.md` files from their pinned commits and fails if any has been
   renamed, moved, or deleted. This is the only way a curation can rot, so it runs in CI.

## Why curate instead of fork

- Upstream skills keep receiving their authors' fixes; a fork freezes them.
- Cross-references keep resolving. Superpowers skills reference each other as
  `superpowers:test-driven-development`; re-hosting them under another plugin name
  breaks that.
- Licence and attribution stay simple, because nothing is redistributed.

## Install

```bash
# The router (this repo)
/plugin marketplace add yuusakuri/dev-skills
/plugin install dev-lifecycle@dev-skills

# The skills it routes to, each from its own marketplace
/plugin marketplace add obra/superpowers
/plugin install superpowers@claude-plugins-official

/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills

/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-advanced-skills@claude-code-skills
/plugin install engineering-skills@claude-code-skills
/plugin install a11y-audit@claude-code-skills
/plugin install security-guidance@claude-code-skills

/plugin marketplace add mohitagw15856/pm-claude-skills
/plugin install pm-engineering@pm-skills
/plugin install pm-essentials@pm-skills
/plugin install pm-security@pm-skills
/plugin install pm-delivery@pm-skills
```

Exact per-phase install targets: [docs/catalog.md](docs/catalog.md).

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
| **1 · Requirements** | `superpowers:brainstorming` · `prd-template` · `epic-design` |
| **2 · Design** | `senior-architect` · `architecture-decision-record` · `api-design-reviewer` · `database-schema-designer` · `threat-model` · `example-skills:frontend-design` |
| **3 · Planning** | `superpowers:writing-plans` · `senior-qa` · `superpowers:using-git-worktrees` |
| **4 · Implementation** | `superpowers:test-driven-development` · `tdd-guide` · `superpowers:executing-plans` · `superpowers:subagent-driven-development` · `superpowers:dispatching-parallel-agents` · `migration-architect` · `tech-debt-tracker` · `example-skills:mcp-builder` |
| **5 · Quality** | `superpowers:systematic-debugging` · `performance-profiler` · `database-optimization` · `ci-cd-pipeline-builder` · `chaos-engineering` |
| **6 · Verification** | `superpowers:verification-before-completion` · `example-skills:webapp-testing` · `a11y-audit` |
| **7 · Review** | `superpowers:requesting-code-review` · `superpowers:receiving-code-review` · `pr-review-expert` · `senior-security` · `security-guidance` · `dependency-auditor` |
| **8 · Release** | `observability-designer` · `slo-architect` · `runbook-generator` · `superpowers:finishing-a-development-branch` · `ship-gate` · `changelog-generator` · `launch-readiness` |
| **9 · Operations** | `incident-commander` · `incident-response` · `incident-postmortem` |
| **Meta** | `development-lifecycle` · `example-skills:skill-creator` |

Phase-by-phase rationale and handoffs: [docs/lifecycle.md](docs/lifecycle.md).

## Known thin spots

Stated rather than papered over: **behavior-preserving refactoring** and **flaky-test
diagnosis** have no strong Skill-format option upstream — the nearest options
(`refactor-engine`, `ci-debugger`) are slash commands. The router states the operating
rule for both inline so the phase is not silently skipped. See
[docs/catalog.md](docs/catalog.md#known-thin-spots).

## Maintenance

```bash
python3 scripts/verify-catalog.py   # all 46 upstream refs still resolve
python3 scripts/validate-skills.py  # spec conformance + router covers every catalog entry
./scripts/check-upstream.sh         # pinned refs are immutable, not moving branches
```

All three run in CI on every push, and weekly on a schedule to catch upstream drift.

## Licence

This repository's own content (the router skill, catalog, scripts, docs) is MIT —
see [LICENSE](LICENSE). Curated skills remain under their own repositories' licences;
see [NOTICE.md](NOTICE.md).

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
