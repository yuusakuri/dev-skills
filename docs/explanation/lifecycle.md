# Why the phases are ordered as they are

This page explains the sequence: what each phase hands to the next, and what goes wrong
when one is skipped. It does not explain the practices themselves — those are maintained
upstream — and it does not list which skill to use. For that, ask the
`development-lifecycle` router or read [reference/catalog.md](../reference/catalog.md).

The ordering principle: decisions get cheaper to change the earlier you make them
explicit. Each phase surfaces a class of mistake while it is still cheap.

## 0 · Orientation

How does this project work, and where does my change belong?

Skipped when the code looks familiar enough. The cost is a change that fights the
codebase's conventions, duplicates something that already exists, or is built on a red
baseline where you cannot tell your breakage from the pre-existing kind.

## 1 · Requirements

Three distinct activities, in order. Exploration decides whether and roughly what,
through dialogue; its output is agreement. Definition turns that into a written artifact
someone can disagree with — acceptance criteria, scope, non-functional requirements.
Decomposition breaks a large requirement into epics and stories.

Skipped when the request seems obvious. The cost arrives at review time as a dispute
about what "done" meant, and it is unwinnable because nothing was written down.

## 2 · Architecture and design

Four kinds of expensive-to-reverse decision: structural choices that constrain later
work; consumer-facing interfaces, which are owned by their consumers once published; the
data model, the hardest thing to change later; and anything touching auth, secrets,
personal data, money, or untrusted input.

The architecture decision record is the thread through all of them. It is what makes the
reasoning survive, and the reasoning is the part that decays fastest.

Skipped when the design feels obvious to whoever has been thinking about it for a week.
The cost is that the next person cannot distinguish a deliberate trade-off from an
accident, and reverses it while cleaning up.

## 3 · Planning

The plan turns the spec into ordered tasks. The test strategy decides in advance what
will be tested and at which level. That decision goes badly under implementation
pressure, where the fastest test to write wins regardless of whether it is the right
one.

## 4 · Implementation

Test-driven development governs how each unit of work is written. Alongside it sit
skills for changes whose shape carries specific risk: data migrations, because a
rollback cannot undo a write, and structural work, because it accumulates silently.

## 5 · Debugging and performance

Not a stage so much as the skills for when something is wrong. They share one rule:
measure before changing. Debug from evidence rather than intuition, and profile before
optimising.

## 6 · Verification

The bar is evidence before assertion. "Done" means commands were run and their output
read. For a user interface that includes real-browser verification and a keyboard pass,
which is where accessibility defects are actually found — not in an automated score.

Skipped when the tests passed locally an hour ago. The cost is a review cycle, or a
release, spent on something that does not work.

## 7 · Review

Human and automated review of the diff, plus two specialised passes: what the change
actually exposes, and a decision on any dependency it adds or moves.

## 8 · Release

Instrumentation comes before release, for one reason: you cannot add it during an
incident, and whatever you emitted before the failure is all the information you will
ever have about it. Then the branch lands, the gate decides, and the release is verified
in production. Deploying is the middle of the process, not the end.

## 9 · Operations

Incident command inverts the normal engineering priority: restore service first,
understand later. Diagnosis while users are affected is the most common way a
five-minute problem becomes an hour-long one. A security event runs on its own track —
triage, severity, forensics — and is not the same playbook. The postmortem is how the
incident's cost buys something.

Skipped when the incident is over and everyone is tired. The cost is the same incident
again, which is also how you discover that the first postmortem's action items were
never done.

## Feedback loops

The lifecycle is not a one-way pipeline.

Verification returns to implementation: a failed check goes back to phase 4, not
forward.

Review returns to design: a reviewer asking "why is it built this way?" is usually a
missing decision record.

Incidents return to requirements: postmortem action items are real requirements and
belong in the same backlog as features. Treating them as optional cleanup is how the
second incident happens.

Operations returns to instrumentation: "we could not tell what was happening" is the
most common postmortem finding, and its fix ships with the next change.
