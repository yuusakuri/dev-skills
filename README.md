# dev-skills

**Best-practice [Agent Skills](https://agentskills.io/specification) covering the whole
software lifecycle — requirements definition through production operations — for any
product and any stack.**

Nothing here assumes a language, framework, cloud, or ticketing tool. The skills encode
practice that holds whether you are shipping a mobile app, a data pipeline, a CLI, or a
service.

## What this is

A curated, installable collection built on **existing published skills** rather than a
reinvention of them:

| Source | What it brings | License |
|---|---|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | Brainstorming, planning, TDD, systematic debugging, code review, branch integration | MIT |
| [`anthropics/skills`](https://github.com/anthropics/skills) | Skill authoring, MCP servers, browser testing, frontend design | Apache-2.0 |
| **`dev-lifecycle`** (this repo) | The 18 skills upstream does not cover — requirements, architecture decisions, API contracts, threat modeling, test strategy, migrations, performance, security review, dependencies, CI health, observability, release, incidents, postmortems, accessibility | MIT |

### Composed, not forked

Upstream collections are referenced at **pinned versions** from their own repositories
and installed under their **real plugin names**. This repository contains no copies of
their files.

That matters for three reasons: upstream skills keep receiving their authors' fixes;
their internal cross-references (`superpowers:test-driven-development` and friends)
keep resolving, which they would not under a renamed fork; and the licence and
attribution story stays simple.

## Install

```bash
# In Claude Code
/plugin marketplace add yuusakuri/dev-skills

/plugin install dev-lifecycle@dev-skills     # this repo's skills
/plugin install superpowers@dev-skills       # upstream, pinned
/plugin install example-skills@dev-skills    # upstream, pinned subset
```

Install all three for full lifecycle coverage. `dev-lifecycle` is useful on its own —
its router degrades gracefully and tells you which upstream skill is missing.

Using another agent runtime? The skills are plain `SKILL.md` directories under
[`plugins/dev-lifecycle/skills/`](plugins/dev-lifecycle/skills/) and can be copied into
any tool that reads the Agent Skills format. See [docs/adoption.md](docs/adoption.md).

## How it is meant to be used

Start with **`development-lifecycle`**. It is a router: it works out which phase a task
is in and names the skill that owns it, so you do not have to remember 30 skill names.

It also scales the process to the work — a typo does not get a requirements document:

| Task size | Phases |
|---|---|
| Trivial (typo, obvious one-liner) | implement → verify |
| Small (contained, reversible) | requirements → implement → verify → review |
| Standard (a new feature) | orientation → requirements → design → plan → implement → verify → review → release |
| High-stakes (data model, auth, money, public API) | every phase; threat modeling and an ADR are mandatory |

## Lifecycle coverage

| Phase | Skills |
|---|---|
| **0 · Orientation** | `codebase-orientation` |
| **1 · Requirements** | `superpowers:brainstorming` · `requirements-definition` |
| **2 · Design** | `architecture-decision-records` · `api-contract-design` · `threat-modeling` · `example-skills:frontend-design` |
| **3 · Planning** | `superpowers:writing-plans` · `test-strategy` · `superpowers:using-git-worktrees` |
| **4 · Implementation** | `superpowers:test-driven-development` · `superpowers:executing-plans` · `superpowers:subagent-driven-development` · `superpowers:dispatching-parallel-agents` · `refactoring-safely` · `data-migration-safety` |
| **5 · Quality** | `superpowers:systematic-debugging` · `performance-optimization` · `ci-and-flaky-tests` |
| **6 · Verification** | `superpowers:verification-before-completion` · `example-skills:webapp-testing` · `accessibility-review` |
| **7 · Review** | `superpowers:requesting-code-review` · `superpowers:receiving-code-review` · `security-review` · `dependency-upgrades` |
| **8 · Release** | `observability-instrumentation` · `superpowers:finishing-a-development-branch` · `release-management` |
| **9 · Operations** | `incident-response` · `postmortem` |
| **Meta** | `development-lifecycle` · `example-skills:skill-creator` · `example-skills:mcp-builder` |

Full descriptions: [docs/catalog.md](docs/catalog.md). Phase-by-phase rationale and
handoffs: [docs/lifecycle.md](docs/lifecycle.md).

## Principles

Every skill here follows the same rules, which are also the review bar for contributions:

1. **Stack-agnostic.** No skill names a framework or vendor as a requirement.
2. **Evidence over assertion.** "Done" means output you read, not a belief.
3. **Named triggers.** Every description states *when* to use the skill, so routing works.
4. **Red flags included.** Each skill names the failure modes it exists to prevent —
   the part that is usually learned the expensive way.
5. **Composable, not duplicative.** If upstream covers it well, this repo points at it
   instead of writing a worse version.

## Maintenance

```bash
python3 scripts/validate-skills.py   # spec conformance, naming, router coverage
./scripts/check-upstream.sh          # verify pinned upstream refs still resolve
```

Both run in CI on every push and pull request.

## Licence and attribution

This repository's own content is MIT — see [LICENSE](LICENSE). Upstream collections are
installed from their own repositories under their own licences; see
[NOTICE.md](NOTICE.md) for attribution and for why Anthropic's source-available document
skills are deliberately excluded.

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
