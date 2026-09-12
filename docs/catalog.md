# Skill catalog

Every skill reachable through this collection, with its trigger. Skills marked
**upstream** are installed from their own repositories at pinned refs — see
[NOTICE.md](../NOTICE.md).

Invoke any of them by name, or start with `development-lifecycle` and let it route.

## This repository — `dev-lifecycle`

### Meta

#### `development-lifecycle`

Use at the start of any software work, or whenever you are unsure which phase you are in or which skill applies - routes the task to the right lifecycle phase and names the skill that owns it, from requirements definition through design, implementation, verification, review, release, and production operations.

### Phase 0 · Orientation

#### `codebase-orientation`

Use before changing code in an unfamiliar repository, package, or subsystem - builds an accurate map of how the project is built, tested, and structured, and finds the existing pattern to follow, so the change fits the codebase instead of fighting it.

### Phase 1 · Requirements

#### `requirements-definition`

Use when an agreed idea needs to become a written, reviewable requirements specification - produces scope boundaries, testable acceptance criteria, non-functional requirements, and explicit open questions. Use after exploration and before design or planning, whenever a feature, product, or change is large enough that "what done means" could be disputed later.

### Phase 2 · Design

#### `api-contract-design`

Use when designing or changing any interface other code depends on - REST or RPC endpoints, GraphQL schemas, event and message payloads, database-facing contracts, CLI surfaces, or public library APIs. Covers contract-first design, compatibility rules, error and pagination conventions, and how to evolve a published interface without breaking clients.

#### `architecture-decision-records`

Use when a technical decision is hard or expensive to reverse, when several viable options compete, or when someone asks why the system is built this way - captures the context, the options considered, the decision, and its consequences as a durable ADR in the repository.

#### `threat-modeling`

Use during design, before implementing anything that touches authentication, authorization, secrets, personal or financial data, file uploads, untrusted input, or external integrations - systematically identifies what can go wrong, who could cause it, and which mitigations must be built in rather than added later.

### Phase 3 · Planning

#### `test-strategy`

Use when deciding what to test and at which level, when a suite is slow, flaky, or passes while bugs ship, or when starting testing on a feature or an untested codebase - chooses the right test levels, defines coverage that means something, and keeps the suite fast and trustworthy.

### Phase 4 · Implementation

#### `data-migration-safety`

Use when changing a database schema, altering stored data shape, backfilling or transforming existing records, or moving data between stores - covers expand/contract sequencing, zero-downtime deploys, safe backfills, locking hazards, and rollback. Use before writing the migration, not after.

#### `refactoring-safely`

Use when restructuring code without changing its behavior - renaming, extracting, splitting modules, removing duplication, replacing a pattern, or making a change easier before making it. Also use before modifying legacy code that has no tests. Keeps behavior provably identical and keeps the change reviewable.

### Phase 5 · Quality

#### `ci-and-flaky-tests`

Use when CI is red, when tests pass locally but fail in CI, when a test fails intermittently without code changes, or when designing a pipeline - covers diagnosing flakes to root cause, keeping the build trustworthy and fast, and structuring pipeline stages so failures are fast and meaningful.

#### `performance-optimization`

Use when something is too slow, uses too much memory, costs too much to run, or when a latency or throughput target must be met - enforces measure-first discipline, finding the real bottleneck with profiling and benchmarks before changing code, and proving the improvement afterwards.

### Phase 6 · Verification

#### `accessibility-review`

Use when building or reviewing any user interface - web, mobile, desktop, or terminal. Covers keyboard operability, semantics and screen reader support, contrast and text sizing, motion, forms and error messaging, and how to actually test rather than assume. Use during implementation and before shipping UI, not as a late audit.

### Phase 7 · Review

#### `dependency-upgrades`

Use when adding, upgrading, or removing a third-party dependency, when triaging a vulnerability advisory, or when a lockfile or supply-chain alert needs a decision - covers evaluating a new dependency, upgrading safely, assessing whether an advisory actually affects you, and keeping upgrades routine rather than terrifying.

#### `security-review`

Use when reviewing a change for vulnerabilities before it merges or ships, or when auditing existing code for security defects - a systematic pass over input handling, authorization, secrets, injection, and dependencies that reports exploitable findings with evidence rather than generic warnings.

### Phase 8 · Release

#### `observability-instrumentation`

Use when building or shipping anything whose health matters in production, or when an incident revealed that you could not tell what was happening - covers what to log, which metrics and traces to emit, how to define alerts that are worth waking someone for, and how to make a system debuggable before it breaks.

#### `release-management`

Use when shipping a change to users - covers versioning and changelogs, release checklists, progressive rollout with feature flags, canaries, verification after deploy, and rollback. Use before deploying anything whose failure would affect users, and when establishing a release process.

### Phase 9 · Operations

#### `incident-response`

Use when something is broken in production right now - users are affected, an alert is firing, or an outage is underway. Covers stabilizing first, roles and communication, safe diagnosis under pressure, and knowing when the incident is over. Use this before debugging, because the priority during an incident is restoring service, not finding the cause.

#### `postmortem`

Use after an incident, outage, or serious production bug is resolved, or after a significant near miss - produces a blameless written analysis with an accurate timeline, contributing causes traced past the first answer, and specific committed action items that prevent recurrence.

## Upstream — `superpowers` (MIT, Jesse Vincent)

Installed from [`obra/superpowers`](https://github.com/obra/superpowers) at `v6.3.0`.

| Skill | Use when |
|---|---|
| `superpowers:brainstorming` | Before any creative work — explores intent, requirements, and design before implementation |
| `superpowers:writing-plans` | You have a spec and need a multi-step implementation plan, before touching code |
| `superpowers:executing-plans` | You have a written plan to execute with review checkpoints |
| `superpowers:subagent-driven-development` | Executing a plan's independent tasks in the current session |
| `superpowers:dispatching-parallel-agents` | 2+ independent tasks with no shared state or sequencing |
| `superpowers:using-git-worktrees` | Feature work needs isolation from the current workspace |
| `superpowers:test-driven-development` | Implementing any feature or bugfix, before writing implementation code |
| `superpowers:systematic-debugging` | Any bug, test failure, or unexpected behavior, before proposing fixes |
| `superpowers:requesting-code-review` | Completing a task or feature, before merging |
| `superpowers:receiving-code-review` | Feedback has arrived and needs rigorous assessment rather than blind agreement |
| `superpowers:verification-before-completion` | About to claim work is complete, fixed, or passing |
| `superpowers:finishing-a-development-branch` | Implementation is complete and the work needs to integrate |

The collection also ships `using-superpowers` and `writing-skills`, which are installed
with it but not routed to here — skill authoring is routed to `skill-creator` instead,
to keep a single trigger for that job.

## Upstream — `example-skills` (Apache-2.0, Anthropic)

Installed from [`anthropics/skills`](https://github.com/anthropics/skills) at a pinned
commit. Only the development-relevant subset is referenced.

| Skill | Use when |
|---|---|
| `example-skills:skill-creator` | Creating, editing, or evaluating a skill |
| `example-skills:mcp-builder` | Building an MCP server to expose an API or service to an agent |
| `example-skills:webapp-testing` | Verifying a local web app in a real browser with Playwright |
| `example-skills:frontend-design` | Giving a new or reshaped UI a deliberate visual direction |

## Deliberate overlaps and how they are resolved

Two skills that could both plausibly fire on the same request are a routing hazard.
These are the pairs that come closest, and the rule that separates them:

| Pair | Rule |
|---|---|
| `brainstorming` vs `requirements-definition` | Exploration is a conversation producing agreement; definition produces the written, testable artifact. Explore first. |
| `threat-modeling` vs `security-review` | Design time versus a diff that exists. Model before building, review before merging. |
| `test-strategy` vs `test-driven-development` | Strategy decides which tests should exist and at what level; TDD governs writing each one. |
| `refactoring-safely` vs `performance-optimization` | Restructuring with behavior identical, versus changing behavior's cost with a measurement to prove it. |
| `incident-response` vs `systematic-debugging` | While users are affected, restore service. Once stable, debug methodically. |
| `ci-and-flaky-tests` vs `systematic-debugging` | A flake is non-determinism in the harness or environment; a consistent failure is an ordinary bug. |
