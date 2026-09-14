# The lifecycle, phase by phase

Why the phases are ordered as they are, what each hands to the next, and what goes
wrong when one is skipped. For "which skill do I use", see the `development-lifecycle`
router or [docs/catalog.md](catalog.md).

Every skill named here is maintained upstream — this document explains the *sequence*,
not the practices.

The ordering principle: **decisions get cheaper to change the earlier you make them
explicit.** Each phase surfaces a class of mistake while it is still cheap.

---

## 0 · Orientation — `codebase-onboarding`

**Question:** how does this project work, and where does my change belong?

**Skipped when** the code looks familiar enough. The cost is a change that fights the
codebase's conventions, duplicates something that already exists, or is built on a red
baseline where you cannot tell your breakage from the pre-existing kind.

---

## 1 · Requirements — `superpowers:brainstorming` → `prd-template` → `epic-design`

Three distinct activities, in order. **Exploration** decides *whether and roughly what*
through dialogue; its output is agreement. **Definition** turns that into a written
artifact someone can disagree with — acceptance criteria, scope, non-functional
requirements. **Decomposition** breaks a large requirement into epics and stories.

**Skipped when** the request seems obvious. The cost arrives at review time as a
dispute about what "done" meant — unwinnable, because nothing was written down.

---

## 2 · Design — `senior-architect` · `architecture-decision-record` · `api-design-reviewer` · `database-schema-designer` · `threat-model`

Four kinds of expensive-to-reverse decision, each with its own skill: structural
choices that constrain later work; consumer-facing interfaces, which are owned by their
consumers once published; the data model, the hardest thing to change later; and
anything touching auth, secrets, personal data, money, or untrusted input.

`architecture-decision-record` is the thread through all of them — it is what makes the
*reasoning* survive, which is the part that decays fastest.

**Skipped when** the design feels obvious to whoever has been thinking about it for a
week. The cost is that the next person cannot distinguish a deliberate trade-off from
an accident, and reverses it while "cleaning up".

---

## 3 · Planning — `superpowers:writing-plans` · `senior-qa` · `superpowers:using-git-worktrees`

The plan turns the spec into ordered tasks. The test strategy decides *in advance* what
will be tested and at which level — a decision made badly under implementation
pressure, when the fastest-to-write test wins regardless of whether it is the right one.

---

## 4 · Implementation — TDD plus the change-shape skills

`superpowers:test-driven-development` (or `tdd-guide`) governs how each unit of work is
written. Alongside it, skills for changes whose *shape* carries specific risk:
`migration-architect` for anything that writes data — the one thing a rollback cannot
undo — and `tech-debt-tracker` for structural work. `superpowers:executing-plans`,
`subagent-driven-development`, and `dispatching-parallel-agents` drive the work.

---

## 5 · Quality — `superpowers:systematic-debugging` · `performance-profiler` · `database-optimization` · `ci-cd-pipeline-builder` · `chaos-engineering`

Not a stage so much as skills for when something is wrong. They share one rule:
**measure before changing.** Debug from evidence rather than intuition; profile before
optimizing.

---

## 6 · Verification — `superpowers:verification-before-completion` · `example-skills:webapp-testing` · `a11y-audit`

The bar: **evidence before assertion.** "Done" means commands were run and output read.
For a user interface that includes real-browser verification and a keyboard pass —
where accessibility defects are actually found, not in an automated score.

**Skipped when** the tests passed locally an hour ago. The cost is a review cycle, or a
release, spent on something that does not work.

---

## 7 · Review — `superpowers:requesting-code-review` / `receiving-code-review` · `pr-review-expert` · `senior-security` · `security-guidance` · `dependency-auditor`

Human and automated review of the diff, plus two specialized passes: what the change
actually exposes, and a decision on any dependency it adds or moves.

---

## 8 · Release — `observability-designer` · `slo-architect` · `runbook-generator` · `superpowers:finishing-a-development-branch` · `ship-gate` · `changelog-generator` · `launch-readiness`

Instrumentation comes **before** release, for one reason: you cannot add it during an
incident, and whatever you emitted before the failure is all the information you will
ever have about it. Then the branch lands, the gate decides, and the release is
verified in production — deploying is the middle of the process, not the end.

---

## 9 · Operations — `incident-commander` · `incident-response` · `incident-postmortem`

`incident-commander` inverts the normal engineering priority: **restore service first,
understand later.** Diagnosis while users are affected is the most common way a
five-minute problem becomes an hour-long one. `incident-response` is the security-event
track (triage, severity, forensics). `incident-postmortem` is how the incident's cost
buys something.

**Skipped when** the incident is over and everyone is tired. The cost is the same
incident again — which is also how you discover the first postmortem's action items
were never done.

---

## Feedback loops

The lifecycle is not a one-way pipeline:

- **Verification → implementation.** A failed check returns to phase 4, not forward.
- **Review → design.** A reviewer's "why is it built this way?" is often a missing ADR.
- **Incident → requirements.** Postmortem action items are real requirements and belong
  in the same backlog as features. Treating them as optional cleanup is how the second
  incident happens.
- **Operations → observability.** "We could not tell what was happening" is the most
  common postmortem finding, and its fix ships with the next change.
