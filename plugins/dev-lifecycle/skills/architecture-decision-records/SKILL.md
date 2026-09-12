---
name: architecture-decision-records
description: Use when a technical decision is hard or expensive to reverse, when several viable options compete, or when someone asks why the system is built this way - captures the context, the options considered, the decision, and its consequences as a durable ADR in the repository.
license: MIT
metadata:
  collection: dev-skills
  phase: "2-design"
---

# Architecture Decision Records

**Core principle:** code records *what* the system does. Nothing in the repository
records *why* — unless you write it down. The reasoning is the part that decays, and
it is the part the next person needs most.

An ADR is short, immutable, and numbered. It is not a design document; it captures
one decision.

## When a decision deserves an ADR

Write one when **any** of these is true:

- Reversing it later would cost more than a day, or require a migration
- It constrains other work (a framework, a protocol, a data model, a boundary)
- Reasonable engineers would disagree about it
- You rejected an option someone will later propose again
- It trades one quality for another (speed for consistency, cost for latency)
- You are deliberately taking on debt, and want the reason on the record

**Do not** write one for: reversible implementation details, style preferences already
settled by a linter, or decisions already covered by an existing ADR.

The test: *if someone asked "why on earth is it like this?" in a year, would the code
alone answer?* If not, write the ADR.

## Procedure

### 1. State the decision as a question

Frame it neutrally and narrowly. "How do we deliver notifications to offline clients?"
— not "Should we use Kafka?", which has already picked a side.

### 2. Write the context before the options

The forces at play: requirements and NFRs driving this, existing constraints,
team and operational realities, what is already in the system, deadlines. A reader
must be able to tell whether your context still holds — **that is what tells them
whether the decision is still valid**.

### 3. Consider at least two real options

One-option ADRs are rationalizations. Include the honest alternatives, and always
consider *do nothing* / *keep the current approach* as a baseline.

For each option, give: how it works in a sentence or two, why it might win, why it
might lose, and its cost — build effort, operational burden, and what it forecloses.

Be specific and fair. If you cannot state an option's strongest advantage, you have
not understood it well enough to reject it.

### 4. Decide and say why *this* one

Name the chosen option and the deciding factor. The useful sentence is comparative:
"chosen over B because B requires an operational component we have no one to run,"
not "A is best practice."

If the decision is provisional, say what would change your mind and when it will be
revisited.

### 5. Record consequences honestly — including the bad ones

- What becomes easier
- What becomes harder, slower, or more expensive
- What new obligations this creates (something to operate, monitor, or migrate later)
- What risks are now accepted, and how they will be detected if they bite

**An ADR with only positive consequences is marketing, not engineering.** Every real
decision costs something; naming the cost is what makes the record trustworthy.

### 6. Commit it with the work

The ADR lands in the same repository as the code it governs, ideally in the same
change. An ADR in a wiki that the code does not reference will be lost.

## Format

`docs/decisions/NNNN-short-slug.md`, numbered sequentially, never renumbered:

```markdown
# NNNN. <Decision in a short noun phrase>

Date: <YYYY-MM-DD>
Status: proposed | accepted | deprecated | superseded by ADR-NNNN
Deciders: <names>

## Context
<The forces. What is true that makes this a question now.>

## Options considered
### Option A — <name>
<How it works. For. Against. Cost.>
### Option B — <name>
...

## Decision
<What we chose, and the deciding factor versus the runner-up.>

## Consequences
### Positive
### Negative
### Follow-on work
```

## Immutability

**Never edit an accepted ADR to reflect a new decision.** Its value is as a record of
what was believed at the time. When the decision changes, write a new ADR and mark the
old one `superseded by ADR-NNNN`. The trail of superseded ADRs is the architectural
history of the system.

Correcting a typo is fine. Rewriting the reasoning is not.

## Red flags

- **Written after implementation to justify it.** Write it while the choice is still open.
- **Only one option, or strawman alternatives.** The rejected options must be ones a
  competent engineer would actually propose.
- **No negative consequences listed.** You have not finished thinking.
- **"Industry best practice" as the reason.** Best for whom, under which constraints?
  Cite the constraint in *your* context that makes it right here.
