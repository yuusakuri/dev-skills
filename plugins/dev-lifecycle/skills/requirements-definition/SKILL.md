---
name: requirements-definition
description: Use when an agreed idea needs to become a written, reviewable requirements specification - produces scope boundaries, testable acceptance criteria, non-functional requirements, and explicit open questions. Use after exploration and before design or planning, whenever a feature, product, or change is large enough that "what done means" could be disputed later.
license: MIT
metadata:
  collection: dev-skills
  phase: "1-requirements"
---

# Requirements Definition

Exploration decides *whether and roughly what* (`superpowers:brainstorming`). This
skill turns the result into a **written artifact someone can disagree with**.

**Core principle:** a requirement that cannot fail a test is not a requirement, it is
a wish. Every line you write must be checkable by someone who was not in the room.

## Why writing it down is the point

Unwritten requirements are remembered differently by each person who heard them, and
the difference surfaces at the worst moment — during review, or after release. The
document is not bureaucracy; it is the thing that makes "done" a fact rather than an
opinion.

## Procedure

### 1. Establish the problem before the solution

Write, in the user's own terms:

- **Who** has the problem (a specific role, not "users")
- **What** they cannot do today, or what it costs them
- **Why now** — what makes this worth doing in this cycle
- **How we will know it worked** — the observable outcome, ideally a metric

If you cannot fill these in, you are not ready to specify. Go back to exploration.

### 2. Draw the scope boundary in both directions

List **in scope** and **explicitly out of scope**. The out-of-scope list is the more
valuable half: it is the one that prevents the argument later. Anything a reasonable
reader might assume is included, and is not, must be named here.

### 3. Write functional requirements as testable statements

Use a consistent, checkable form. Either user-story-with-criteria:

```
As a <role>, I want <capability>, so that <outcome>.

Acceptance criteria:
  Given <initial state>
  When  <action>
  Then  <observable result>
```

...or numbered shall-statements (`FR-1: The system shall ...`). Pick one and keep it.

Each criterion must be:

- **Observable** — states what the system does, not how it is implemented
- **Binary** — passes or fails, with no judgment call
- **Independent** — does not need another criterion's outcome to be interpreted

Rewrite anything containing *fast*, *easy*, *intuitive*, *robust*, *properly*, or
*etc.* Those words mean the requirement is not yet written.

### 4. Specify non-functional requirements with numbers

NFRs are where most projects fail, because they are assumed rather than stated. Go
through this list and either give a number or write "not a constraint":

| Category | Ask |
|---|---|
| Performance | Latency target, at what percentile, under what load? |
| Scale | Expected and peak volume; growth over the next year |
| Availability | Uptime target; acceptable downtime for a deploy |
| Durability | What may never be lost? Recovery point and time objectives |
| Security | AuthN/AuthZ model; what data is sensitive; see `threat-modeling` |
| Privacy & compliance | Personal data handled, retention, deletion, jurisdiction |
| Accessibility | Standard and level to meet; see `accessibility-review` |
| Localization | Languages, locales, time zones, currencies |
| Compatibility | Browsers, OSes, API versions, minimum runtime |
| Observability | What must be measurable in production; see `observability-instrumentation` |
| Operability | Who operates it, what they need to diagnose it |
| Cost | Budget ceiling for infrastructure or third-party usage |

"As fast as possible" is not a target. "p95 under 300 ms at 1,000 rps" is.

### 5. State the edges explicitly

For each requirement, ask what happens when: input is empty, maximum, or malformed;
the user lacks permission; a dependency is down or slow; the same action is submitted
twice; the operation is interrupted halfway. Undecided edge cases become someone's
arbitrary choice at 2 a.m.

### 6. Record assumptions, dependencies, and open questions

- **Assumptions** — things you believe true and have not verified. Each one is a risk.
- **Dependencies** — teams, services, data, or approvals outside your control.
- **Open questions** — each with an owner and the date an answer is needed.

Never resolve an open question by guessing silently. Either ask, or write down the
assumption you are proceeding under so it can be challenged.

### 7. Get explicit sign-off

Walk the requester through it in sections, not as a wall of text. Ask directly:
"is anything here wrong, missing, or more than you wanted?" Record who agreed and when.

## Artifact

Store it in the repository (`docs/requirements/<slug>.md`), not in a chat log:

```markdown
# <Title>
Status: draft | agreed | superseded   Owner: <name>   Date: <date>

## Problem
## Goals / Non-goals
## In scope / Out of scope
## Functional requirements
## Non-functional requirements
## Edge cases and error behavior
## Assumptions, dependencies, open questions
## How we will know it worked
```

## Handoff

The spec is done when a competent engineer who was not in the conversation could
build from it and an independent reviewer could judge the result. Then proceed to
`architecture-decision-records` or `api-contract-design` for design, and
`superpowers:writing-plans` for execution.

## Red flags

- **No out-of-scope section.** Scope creep is now guaranteed.
- **No NFR numbers.** You have deferred the hardest constraints to after they are expensive.
- **Acceptance criteria describing implementation** ("stores a flag in Redis"). Say
  what the user observes; leave the mechanism to design.
- **"We'll figure that out during implementation."** For anything hard to reverse,
  this means the decision will be made by whoever types fastest.
