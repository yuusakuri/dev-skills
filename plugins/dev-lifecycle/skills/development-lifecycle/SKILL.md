---
name: development-lifecycle
description: Use at the start of any software work, or whenever you are unsure which phase you are in or which skill applies - routes the task to the right lifecycle phase and names the skill that owns it, from requirements definition through design, implementation, verification, review, release, and production operations.
license: MIT
metadata:
  collection: dev-skills
  phase: meta
---

# Development Lifecycle Router

This collection covers the whole lifecycle. Its skills are stack-agnostic: nothing
here assumes a language, framework, cloud, or ticketing tool.

**Your job in this skill is to work out which phase the task is in, then invoke the
skill that owns that phase.** Do not try to do the phase's work from this file.

## How to route

Ask two questions:

1. **What artifact does this task need to produce?** A decision, a spec, a plan,
   code, a review, a release, a fix, a document?
2. **What does "done" look like, and who checks it?**

Then pick the row below. If a task spans phases, run them in order — skipping
earlier phases is the single most common cause of rework.

## Phase map

| # | Phase | Use when | Skill |
|---|---|---|---|
| 0 | Orientation | The codebase is unfamiliar, or you are about to change code you have not read | `codebase-orientation` |
| 1 | Discovery | The idea is still vague; intent and alternatives are unexplored | `superpowers:brainstorming` |
| 1 | Requirements | The idea is agreed; you need a written, testable spec | `requirements-definition` |
| 2 | Architecture | A choice is hard to reverse, or several designs compete | `architecture-decision-records` |
| 2 | Interface design | You are defining an API, schema, event, or public library surface | `api-contract-design` |
| 2 | Security design | The feature touches auth, secrets, PII, payments, or untrusted input | `threat-modeling` |
| 3 | Planning | You have a spec and need an executable plan | `superpowers:writing-plans` |
| 3 | Test planning | You need to decide what to test and at which level | `test-strategy` |
| 3 | Workspace | You need an isolated branch/worktree before implementing | `superpowers:using-git-worktrees` |
| 4 | Implementation | You are about to write feature or bugfix code | `superpowers:test-driven-development` |
| 4 | Plan execution | You are working through a written plan | `superpowers:executing-plans`, `superpowers:subagent-driven-development` |
| 4 | Parallel work | 2+ independent tasks with no shared state | `superpowers:dispatching-parallel-agents` |
| 4 | Restructuring | Changing structure without changing behavior | `refactoring-safely` |
| 4 | Schema change | Changing a database schema or stored data shape | `data-migration-safety` |
| 5 | Debugging | Any bug, test failure, or unexplained behavior | `superpowers:systematic-debugging` |
| 5 | Slowness | Something is too slow or uses too much resource | `performance-optimization` |
| 5 | CI trouble | CI is red, or tests pass and fail without code changes | `ci-and-flaky-tests` |
| 6 | Verification | You are about to claim work is complete | `superpowers:verification-before-completion` |
| 6 | UI verification | A browser-facing change needs real-browser proof | `example-skills:webapp-testing` |
| 6 | Accessibility | The change affects a user interface | `accessibility-review` |
| 7 | Review (asking) | Work is ready to be checked | `superpowers:requesting-code-review` |
| 7 | Review (receiving) | Feedback has arrived | `superpowers:receiving-code-review` |
| 7 | Security review | Reviewing a diff for vulnerabilities | `security-review` |
| 7 | Dependencies | Upgrading, adding, or triaging a vulnerable dependency | `dependency-upgrades` |
| 8 | Instrumentation | Shipping something whose health must be observable | `observability-instrumentation` |
| 8 | Integration | Tests pass and the branch needs to land | `superpowers:finishing-a-development-branch` |
| 8 | Release | Versioning, changelog, rollout, rollback | `release-management` |
| 9 | Incident | Something is broken in production **now** | `incident-response` |
| 9 | Postmortem | An incident is resolved and needs learning captured | `postmortem` |
| — | Specialized | Building an MCP server / designing a UI's visual language | `example-skills:mcp-builder`, `example-skills:frontend-design` |
| — | Meta | Writing or improving a skill | `example-skills:skill-creator` |

## Rules that hold in every phase

1. **Evidence before assertion.** Never report a phase complete without output that
   shows it. "Tests pass" means you ran them and read the result.
2. **Reversibility decides rigor.** Cheap and reversible: just do it. Expensive or
   one-way: write the decision down first (`architecture-decision-records`).
3. **Phase 1 has no code.** If you are writing code to answer "what should this do?",
   you are in the wrong phase — unless it is an explicit throwaway spike, which you
   say out loud and then delete.
4. **The user owns scope.** Surface gaps and risks; do not silently widen or narrow
   what was asked for.
5. **Leave the trail.** Requirements, decisions, and incidents belong in the repo,
   not only in a conversation that will be lost.

## Scaling to task size

Not every task needs ten phases. Match the ceremony to the blast radius:

- **Trivial** (typo, comment, obvious one-line fix): phase 4 → 6. No spec, no ADR.
- **Small** (contained change, existing patterns, reversible): phases 1 → 4 → 6 → 7.
- **Standard** (new feature or endpoint): 0 → 1 → 2 → 3 → 4 → 6 → 7 → 8.
- **High-stakes** (data model, auth, money, migrations, public API): every phase,
  and `threat-modeling` plus `architecture-decision-records` are mandatory, not optional.

When you are unsure which size a task is, assume the larger one and say so. It is
cheaper to write a spec you did not strictly need than to rebuild a shipped mistake.
