# The lifecycle, phase by phase

This document explains *why* the phases are ordered as they are, what each one hands to
the next, and what goes wrong when one is skipped. For the one-line "which skill do I
use" answer, use the `development-lifecycle` router skill or
[docs/catalog.md](catalog.md).

The ordering principle throughout: **decisions get cheaper to change the earlier you
make them explicit.** Every phase exists to surface a class of mistake while it is
still cheap.

---

## 0 · Orientation — `codebase-orientation`

**Question:** how does this project work, and where does my change belong?

**Handoff:** the build and test commands, a green baseline, the module that owns the
change, and the existing pattern to follow.

**Skipped when** the code looks familiar enough. The cost is a change that fights the
codebase's conventions, duplicates a utility that already exists, or is built on a red
baseline where you cannot tell your breakage from the pre-existing kind.

---

## 1 · Requirements — `superpowers:brainstorming` → `requirements-definition`

Two distinct activities, in order:

**Exploration** (`brainstorming`) decides *whether and roughly what* through dialogue.
It is interactive and divergent, and its output is agreement.

**Definition** (`requirements-definition`) turns that agreement into a **written
artifact someone can disagree with**: scope in and out, testable acceptance criteria,
non-functional requirements with numbers, and open questions with owners.

**Handoff:** a spec a competent engineer who was not in the conversation could build
from, and an independent reviewer could judge the result against.

**Skipped when** the request seems obvious. The cost arrives at review time, as a
dispute about what "done" meant — which is unwinnable, because nothing was written down.

---

## 2 · Design — `architecture-decision-records` · `api-contract-design` · `threat-modeling`

Three different kinds of expensive-to-reverse decision, each with its own skill:

- **Structural choices** that constrain later work → an ADR, recording the options and
  the *negative* consequences, not only the chosen path
- **Consumer-facing interfaces** → a contract designed before implementation, with a
  written compatibility policy, because a published interface is owned by its consumers
- **Anything touching auth, secrets, personal data, money, or untrusted input** →
  a threat model producing mitigations that become implementation tasks with tests

**Handoff:** written decisions, a reviewed schema, and a list of security requirements.

**Skipped when** the design feels obvious to the person who has been thinking about it
for a week. The cost is that the reasoning is never recorded, so the next person — or
you in six months — cannot tell a deliberate trade-off from an accident, and reverses
it by "cleaning it up".

---

## 3 · Planning — `superpowers:writing-plans` · `test-strategy` · `superpowers:using-git-worktrees`

The plan turns the spec into ordered, executable tasks. The test strategy decides, in
advance, what will be tested and at which level — a decision that is made badly under
implementation pressure, when the fastest-to-write test wins regardless of whether it
is the right one.

**Handoff:** a task sequence, a test plan, and an isolated workspace.

---

## 4 · Implementation — TDD and the change-shape skills

`superpowers:test-driven-development` governs how each unit of work is written.
Alongside it, three skills cover changes whose *shape* carries specific risk:

- `refactoring-safely` — behavior must stay provably identical; never mixed with a
  behavior change in one commit
- `data-migration-safety` — the change writes data, which is the one thing a rollback
  cannot undo
- `superpowers:executing-plans` / `subagent-driven-development` /
  `dispatching-parallel-agents` — how the work is driven

**Handoff:** working code with tests, committed in reviewable steps.

---

## 5 · Quality — `superpowers:systematic-debugging` · `performance-optimization` · `ci-and-flaky-tests`

Not a stage so much as three skills for when something is wrong. All three share one
rule: **measure before changing.** Debug from evidence rather than intuition, profile
before optimizing, and find a flake's actual non-determinism rather than retrying it.

---

## 6 · Verification — `superpowers:verification-before-completion` · `example-skills:webapp-testing` · `accessibility-review`

The bar: **evidence before assertion.** "Done" means commands were run and output was
read. For a user interface, that includes real-browser verification and a keyboard-only
pass — which is where accessibility defects are actually found, not in an automated
score.

**Skipped when** the tests passed locally an hour ago. The cost is a review cycle, or a
release, spent on something that does not work.

---

## 7 · Review — `superpowers:requesting-code-review` / `receiving-code-review` · `security-review` · `dependency-upgrades`

Human and automated review of the diff, plus two specialized passes: a security audit
of what the change actually exposes, and a decision on any dependency it adds or moves.

**Handoff:** an approved change with findings addressed rather than deferred.

---

## 8 · Release — `observability-instrumentation` · `superpowers:finishing-a-development-branch` · `release-management`

Instrumentation comes **before** release, not after, for one reason: you cannot add
instrumentation during an incident, and whatever you emitted before the failure is all
the information you will ever have about it.

Then the branch lands, and the release is rolled out progressively with a tested
rollback path — and **verified in production**, because deploying is the middle of the
process, not the end.

---

## 9 · Operations — `incident-response` · `postmortem`

`incident-response` inverts the normal engineering priority: **restore service first,
understand later.** Diagnosis while users are affected is the most common way a
five-minute problem becomes an hour-long one.

`postmortem` is how the incident's cost buys something — blamelessly, with a timeline
built from evidence rather than memory, causes traced past the first satisfying answer,
and action items that have owners and dates.

**Skipped when** the incident is over and everyone is tired. The cost is the same
incident again, which is also how you discover the first postmortem's action items were
never done.

---

## Feedback loops

The lifecycle is not a one-way pipeline. The loops that matter:

- **Verification → implementation.** A failed check returns to phase 4, not forward.
- **Review → design.** A reviewer's "why is it built this way?" is often a missing ADR.
- **Incident → requirements.** Postmortem action items are real requirements and belong
  in the same backlog as features, with owners and dates. Treating them as optional
  cleanup is how the second incident happens.
- **Operations → observability.** "We could not tell what was happening" is the most
  common postmortem finding, and its fix is instrumentation shipped with the next change.
