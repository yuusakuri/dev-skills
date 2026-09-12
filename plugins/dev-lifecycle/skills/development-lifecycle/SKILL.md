---
name: development-lifecycle
description: Use at the start of any software work, or whenever you are unsure which phase you are in or which skill applies - routes the task to the right lifecycle phase and names the specific community skill that owns it, covering requirements definition, design, planning, implementation, debugging, verification, review, release, and production operations.
license: MIT
metadata:
  collection: dev-skills
  phase: meta
---

# Development Lifecycle Router

This skill is a **map, not a method**. It owns no practice of its own. Its job is to
work out which lifecycle phase a task is in and hand off to the established community
skill that covers it — all of which are maintained in their own repositories.

**Invoke the skill named in the table. Do not try to do the phase's work from here.**

## How to route

Ask two questions:

1. **What artifact does this task need to produce?** A decision, a spec, a plan, code,
   a review, a release, a fix, a document?
2. **What does "done" look like, and who checks it?**

Then pick the row. If a task spans phases, run them in order — skipping earlier phases
is the most common cause of rework.

## Phase map

Names are given as `plugin:skill`. If a skill is not installed, the row still tells you
what to look for — see `docs/catalog.md` for the repository and install command.

| # | Phase | Use when | Skill |
|---|---|---|---|
| 0 | Orientation | The codebase is unfamiliar, or you are about to change code you have not read | `codebase-onboarding` |
| 1 | Discovery | The idea is vague; intent and alternatives are unexplored | `superpowers:brainstorming` |
| 1 | Requirements | The idea is agreed; you need a written spec with acceptance criteria | `prd-template` |
| 1 | Decomposition | A large requirement needs breaking into epics and stories | `epic-design` |
| 2 | Architecture | Several designs compete, or the structure constrains later work | `senior-architect` |
| 2 | Decision record | A choice is hard or expensive to reverse | `architecture-decision-record` |
| 2 | Interface design | Defining an API, schema, event, or public library surface | `api-design-reviewer` |
| 2 | Data model | Designing or reshaping a database schema | `database-schema-designer` |
| 2 | Security design | Auth, secrets, PII, payments, or untrusted input is involved | `threat-model` |
| 2 | Visual direction | Building or reshaping a user interface | `example-skills:frontend-design` |
| 3 | Planning | You have a spec and need an executable plan | `superpowers:writing-plans` |
| 3 | Test planning | Deciding what to test and at which level | `senior-qa` |
| 3 | Workspace | You need an isolated branch or worktree before implementing | `superpowers:using-git-worktrees` |
| 4 | Implementation | About to write feature or bugfix code | `superpowers:test-driven-development`, `tdd-guide` |
| 4 | Plan execution | Working through a written plan | `superpowers:executing-plans`, `superpowers:subagent-driven-development` |
| 4 | Parallel work | 2+ independent tasks with no shared state | `superpowers:dispatching-parallel-agents` |
| 4 | Schema change | Changing a schema or migrating stored data | `migration-architect` |
| 4 | Restructuring | Paying down or tracking structural debt | `tech-debt-tracker` |
| 4 | MCP server | Exposing an API or service to an agent | `example-skills:mcp-builder` |
| 5 | Debugging | Any bug, test failure, or unexplained behavior | `superpowers:systematic-debugging` |
| 5 | Slowness | Something is too slow or uses too much resource | `performance-profiler`, `database-optimization` |
| 5 | CI / pipeline | CI is red, or the pipeline needs designing | `ci-cd-pipeline-builder` |
| 5 | Resilience | Verifying behavior under failure | `chaos-engineering` |
| 6 | Verification | About to claim work is complete | `superpowers:verification-before-completion` |
| 6 | UI verification | A browser-facing change needs real-browser proof | `example-skills:webapp-testing` |
| 6 | Accessibility | The change affects a user interface | `a11y-audit` |
| 7 | Review (asking) | Work is ready to be checked | `superpowers:requesting-code-review`, `pr-review-expert` |
| 7 | Review (receiving) | Feedback has arrived | `superpowers:receiving-code-review` |
| 7 | Security review | Auditing a diff for vulnerabilities | `senior-security`, `security-guidance` |
| 7 | Dependencies | Adding, upgrading, or triaging a vulnerable dependency | `dependency-auditor` |
| 8 | Instrumentation | Shipping something whose health must be observable | `observability-designer`, `slo-architect` |
| 8 | Runbooks | An alert needs a documented response | `runbook-generator` |
| 8 | Integration | Tests pass and the branch needs to land | `superpowers:finishing-a-development-branch` |
| 8 | Release gate | Deciding whether to ship | `ship-gate`, `launch-readiness` |
| 8 | Release notes | Communicating what changed | `changelog-generator` |
| 9 | Incident (outage) | Something is broken in production **now** | `incident-commander` |
| 9 | Incident (security) | A security event needs triage, severity, and forensics | `incident-response` |
| 9 | Postmortem | An incident is resolved and needs learning captured | `incident-postmortem` |
| — | Meta | Writing or improving a skill | `example-skills:skill-creator` |

## Rules that hold in every phase

These are the collection's operating principles; the individual skills carry the detail.

1. **Evidence before assertion.** Never report a phase complete without output that
   shows it. "Tests pass" means you ran them and read the result.
2. **Reversibility decides rigor.** Cheap and reversible: just do it. Expensive or
   one-way: write the decision down first (`architecture-decision-record`).
3. **Phase 1 has no code.** If you are writing code to answer "what should this do?",
   you are in the wrong phase — unless it is an explicit throwaway spike.
4. **The user owns scope.** Surface gaps and risks; do not silently widen or narrow
   what was asked for.
5. **Leave the trail.** Requirements, decisions, and incidents belong in the repo, not
   only in a conversation that will be lost.

## Scaling to task size

Match the ceremony to the blast radius:

- **Trivial** (typo, comment, obvious one-line fix): phase 4 → 6. No spec, no ADR.
- **Small** (contained change, existing patterns, reversible): 1 → 4 → 6 → 7.
- **Standard** (new feature or endpoint): 0 → 1 → 2 → 3 → 4 → 6 → 7 → 8.
- **High-stakes** (data model, auth, money, migrations, public API): every phase, and
  `threat-model` plus `architecture-decision-record` are mandatory, not optional.

When unsure which size a task is, assume the larger one and say so.

## When a row has no installed skill

Two phases are covered less well by the community collections than the rest, so say so
rather than pretending otherwise:

- **Behavior-preserving refactoring.** `tech-debt-tracker` tracks debt but does not
  walk a safe refactor. The rule to apply directly: never mix a refactor and a
  behavior change in one commit, and never refactor code whose behavior no test pins.
- **Flaky tests.** `ci-cd-pipeline-builder` builds pipelines but does not diagnose
  intermittent failures. The rule: a flake is real non-determinism (time, ordering,
  concurrency, waiting, shared state) — never retry it into green.

If no row fits at all, say which phase the task is in and proceed with the phase's
principle above rather than guessing at a skill.
