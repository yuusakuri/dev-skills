---
name: incident-response
description: Use when something is broken in production right now - users are affected, an alert is firing, or an outage is underway. Covers stabilizing first, roles and communication, safe diagnosis under pressure, and knowing when the incident is over. Use this before debugging, because the priority during an incident is restoring service, not finding the cause.
license: MIT
metadata:
  collection: dev-skills
  phase: "9-operations"
---

# Incident Response

**Core principle: stop the bleeding first.** During an incident, restoring service
always outranks understanding the cause. Curiosity is the right instinct at every
other time and the wrong one here — every minute spent diagnosing while users are down
is a minute of impact you chose to accept.

The root cause can be found from logs after service is restored. It cannot be found
faster while everyone is panicking.

## The first ten minutes

### 1. Confirm it is real, and scope it

Is it actually broken, or is the monitoring broken? What is the **user-visible**
impact — who is affected, doing what, and how badly? Is it getting worse?

Say the scope out loud early, even if rough. "All users cannot check out" and "some
users see a slow dashboard" call for entirely different responses.

### 2. Declare it

Under-declaring is the more common and more expensive mistake. Declaring an incident
costs a few minutes of attention; not declaring costs the hour before someone realizes
how bad it was. When in doubt, declare — and stand it down cheerfully if it is minor.

Assign, even if informally and even to yourself:

- **Incident lead** — decides and coordinates. Does not debug. This separation matters:
  the person deep in a stack trace cannot also track scope and communication.
- **Operator(s)** — investigate and make changes, one at a time, announced
- **Communicator** — updates stakeholders on a schedule

### 3. Stabilize before diagnosing

Try, in order of preference:

1. **Roll back** the most recent change. Most incidents follow a deploy or a config
   change. Reverting is fast, reversible, and does not require understanding.
2. **Turn off the feature flag** for the affected path
3. **Fail over, restart, or scale** the affected component
4. **Shed load** — rate limit, disable an expensive feature, serve degraded results

If none applies, then diagnose — but keep the goal as mitigation, not explanation.

### 4. Change one thing at a time, and say so

Under pressure, several people fixing in parallel is how an incident gets worse.
Announce each action before taking it, and record the time. You will need the timeline
later, and nobody reconstructs it accurately from memory.

**Do not** make unrelated "while we're here" changes. Do not refactor. Do not clean up.

### 5. Communicate on a schedule

Update at a fixed interval even when there is nothing new — silence is read as chaos.
Say what is affected, what is being done, and when the next update comes. Do not
promise a resolution time you cannot know.

Keep internal speculation internal. External updates state impact and action, not
theories.

## Preserve evidence before it is gone

Before restarting or scaling away the failing instance, capture what you will need:
logs, metrics graphs, a heap or thread dump if relevant, the exact version running,
recent deploys and config changes. Restarting a process destroys the state that would
have explained it — an "unexplained" incident is usually one whose evidence was
discarded in the first five minutes.

## Diagnosing under pressure

Ask the highest-yield question first: **what changed?** Deploys, config, flags,
infrastructure, dependency incidents, traffic pattern, certificate expiries, scheduled
jobs, and the calendar (month end, a marketing send). The overwhelming majority of
incidents correlate with a change, and the rest correlate with a threshold crossed.

Then work from the user's symptom inward along the request path rather than guessing
at components. For methodical work once service is stable, switch to
`superpowers:systematic-debugging`.

## Closing it

The incident ends when **users are unaffected**, not when you understand it, and not
when the graph starts improving. Verify by the same user-facing signals that told you
it was broken.

Before standing down:

- Confirm recovery from the user's perspective, not just the dashboard
- Note anything still degraded or any temporary mitigation still in place
- **Write down the follow-up work while it is fresh** — a mitigation that must be
  made permanent, a missing alert, an unreadable log
- Announce the resolution to everyone who got the first message
- Schedule the `postmortem` now, while people remember

## Red flags

- **Debugging while the site is down** instead of rolling back
- **No single decision-maker** — five people changing things at once
- **No timeline recorded.** The postmortem will be fiction.
- **Restarting the evidence away** before capturing it
- **Silence toward stakeholders** because "we'll have an answer soon"
- **Declaring it over when the graph looks better**, without checking real user impact
- **A heroic manual fix nobody wrote down.** It will be needed again, by someone else,
  at 3 a.m.
