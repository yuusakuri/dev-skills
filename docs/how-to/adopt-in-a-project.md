# Adopt this in a project

Installing skills makes them available.
Three things make them used.

## Point at the router from the project's agent instructions

In `AGENTS.md`, or whichever instructions file your agent reads:

```markdown
## Working in this repository

Start with the `development-lifecycle` skill to identify the phase and the skill that
owns it. Scale the process to the change: trivial fixes go straight to implementation
and verification; anything touching <the risky areas of this project> requires a threat
model and an ADR.

Project specifics that override general practice:
- Test command: <command>
- Requirements live in: docs/requirements/
- Decisions live in: docs/decisions/
```

The last block matters most.
The curated skills are deliberately general; this file is where the stack-specific truth goes, and it takes precedence.

## Create the directories the skills write into

Several skills produce artifacts that belong in the repository rather than a chat log:

```
docs/requirements/   prd-template
docs/decisions/      architecture-decision-record
docs/security/       threat-model
docs/postmortems/    incident-postmortem
docs/runbooks/       runbook-generator
```

A skill with nowhere to write its artifact produces a message that scrolls away.

## Adopt incrementally

Mandating all ten phases on day one gets the whole thing abandoned.
A workable order:

1. `superpowers:verification-before-completion` and `test-driven-development` — visible effect on quality, and no team agreement needed.
2. `codebase-onboarding` and `superpowers:brainstorming` — cheap, and they cut the rework that comes from starting in the wrong place.
3. `prd-template` and `architecture-decision-record` — the first two that need team agreement, because they produce artifacts other people must read.
4. `ship-gate`, `observability-designer`, `incident-commander`, `incident-postmortem` — once the project has users whose downtime matters.
5. `threat-model`, `senior-security`, `a11y-audit` — before the first release that handles real user data or faces the public.

## Check that it worked

Ask the agent:

> Which skill covers deciding whether to ship a release?

It should answer `ship-gate`, or `launch-readiness`.
If it cannot, the skills are not loaded: check that the directory your agent reads is present, and restart the session.
