---
name: postmortem
description: Use after an incident, outage, or serious production bug is resolved, or after a significant near miss - produces a blameless written analysis with an accurate timeline, contributing causes traced past the first answer, and specific committed action items that prevent recurrence.
license: MIT
metadata:
  collection: dev-skills
  phase: "9-operations"
---

# Postmortem

**Core principle:** the incident already cost you. The postmortem is how you buy
something with it. An incident without one is a cost with no return.

**Blameless is not politeness — it is accuracy.** People who expect blame report
selectively, and a postmortem built on selective reporting produces action items that
fix the wrong thing. You want the real sequence, which means making it safe to say
"I ran that command."

## Ground rules

- Describe **systems and decisions**, not people: "the deploy tool allowed a config
  change without review", not "Alex pushed a bad config"
- Assume everyone acted reasonably **given what they knew at the time**. If an action
  looks obviously wrong in hindsight, the interesting question is what made it look
  right in the moment — that is the finding
- Ban hindsight language: "should have obviously", "careless", "failed to notice".
  Replace with what information was available and what the system made easy
- Hold it soon, while memory is fresh — within days, not weeks
- **Write one for near misses too.** A near miss is a free lesson; waiting for the
  version that hurts is a strange way to learn it

## Build the timeline from evidence

Reconstruct from logs, chat transcripts, deploy history, alerts, and graphs — **not
from memory**, which reliably compresses and reorders under stress.

Record, with timestamps: when it actually started (usually earlier than anyone noticed),
when it was detected and by what, when a human engaged, each significant action and its
effect, and when impact ended.

Two gaps are almost always the most valuable findings in the document:

- **Start → detection.** How long were users affected before you knew? A large gap is a
  monitoring problem, and it is usually a bigger problem than the incident itself.
- **Detection → mitigation.** Where did the time go — reaching a human, finding a
  runbook, getting access, understanding, deciding, or acting? Each has a different fix.

## Find contributing causes, not *the* root cause

Serious incidents do not have a single cause. They have a chain, plus the defenses that
should have stopped it and did not.

Ask "why" past the first satisfying answer, and ask it in three directions:

- **Why did it break?** The technical chain
- **Why did the defenses not catch it?** Why not in review, in tests, in staging, in the
  canary? These answers produce the durable fixes.
- **Why did it take so long to detect and resolve?** Alerting, runbooks, access,
  documentation, escalation

Stopping at "a bad config was deployed" gives you an action item about that config.
Continuing to "configs are deployed without validation or review, and no alert covers
this failure mode" gives you fixes that prevent the whole class.

**"Human error" is never a root cause.** It is a prompt: what made the error easy, and
what let it reach production unchecked?

## Action items that are real

Most postmortems fail here — a strong analysis followed by vague intentions that nobody
does. An action item must have:

- A **specific change**, not a sentiment. "Add a required schema validation step to the
  config deploy pipeline", not "be more careful with configs"
- A named **owner** (a person, not a team)
- A **due date**
- A **tracked issue**, linked

Prioritize by leverage, and prefer fixes in this order:

1. **Make the failure impossible** — remove the capability, add a structural constraint
2. **Make it caught automatically** — validation, a test, a check in CI
3. **Make it detected fast** — the alert that was missing
4. **Make it recovered fast** — a runbook, an automated rollback, better access
5. **Documentation and training** — the weakest, and the one teams default to

Keep the list short. Five items that get done beat twenty that decorate a document.
**Review them at a set date** — unreviewed action items are how the same incident
happens twice, with a second postmortem noting the first one's items were never done.

## Template

```markdown
# Postmortem: <short description>
Date of incident | Duration | Severity | Author | Status: draft | reviewed | complete

## Summary
<Three sentences: what broke, who was affected, how it was resolved.>

## Impact
<Users affected, what they could not do, for how long. Numbers where possible.>

## Timeline
| Time (UTC) | Event | Source |

## Contributing causes
### Why it broke
### Why our defenses did not catch it
### Why detection and resolution took as long as they did

## What went well
<Name it. These are the practices worth keeping and reinforcing.>

## What was luck
<What could easily have been much worse — the most under-used section.>

## Action items
| # | Action | Type (prevent/detect/mitigate) | Owner | Due | Issue |

## Lessons learned
```

## Red flags

- **A person's name as a cause**
- **"Root cause: human error"** — you stopped one question too early
- **One cause, one action item** for a serious incident
- **Action items with no owner or date** — they will not happen
- **A timeline from memory**, with round numbers and no sources
- **No "what went well" or "what was luck"** — a document that only lists failures gets
  written defensively and read by nobody
- **Never published.** An unshared postmortem teaches only the people who were already
  there.
