# Adopting this curation

## In Claude Code

Install the router, then the upstream marketplaces it routes to — the full command list
is in [README](../README.md#install) and per-phase targets in [catalog.md](catalog.md).

Skills trigger on their descriptions, so in normal use you describe the task rather
than naming a skill. Naming one explicitly always works.

## In another agent runtime

The upstream skills are plain [Agent Skills](https://agentskills.io/specification)
directories. Clone each upstream repository **at the ref pinned in
[`catalog.json`](../catalog.json)** and copy the skill directories you want:

```bash
git clone https://github.com/obra/superpowers
git -C superpowers checkout b36e0829c6d0140e93cfef2ca599b1b07d4a7797
cp -r superpowers/skills/test-driven-development <your-skills-dir>/
```

Take upstream skills from their own repositories, never from a third party's copy —
that is the whole point of the pinning. `scripts/verify-catalog.py` prints every
repository, ref, and path.

## Making it stick in a project

Installing skills makes them *available*. Three things make them *used*.

### 1. Point at the router from the project's agent instructions

In your `CLAUDE.md` or `AGENTS.md`:

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

The last block matters most. The curated skills are deliberately general; your
`CLAUDE.md` is where the stack-specific truth goes, and it takes precedence.

### 2. Create the directories the skills write into

Several skills produce artifacts that belong in the repository rather than a chat log:

```
docs/requirements/   # prd-template
docs/decisions/      # architecture-decision-record
docs/security/       # threat-model
docs/postmortems/    # incident-postmortem
docs/runbooks/       # runbook-generator
```

A skill with nowhere to write its artifact produces a message that scrolls away.

### 3. Adopt incrementally

Do not mandate all ten phases on day one; it will be abandoned. A workable order:

1. **`superpowers:verification-before-completion`** and **`test-driven-development`** —
   immediate effect on quality, no team agreement needed
2. **`codebase-onboarding`** and **`superpowers:brainstorming`** — cheap, and they cut
   the rework that comes from starting in the wrong place
3. **`prd-template`** and **`architecture-decision-record`** — the first two needing
   team agreement, because they produce artifacts others must read
4. **`ship-gate`, `observability-designer`, `incident-commander`, `incident-postmortem`**
   — once the project has users whose downtime matters
5. **`threat-model`, `senior-security`, `a11y-audit`** — before the first release that
   handles real user data or faces the public

## Choosing between overlapping skills

Curating five collections means some phases have more than one option. Where that
happens the router lists both; pick on this basis:

| Overlap | Guidance |
|---|---|
| `superpowers:test-driven-development` vs `tdd-guide` | Superpowers' is stricter about watching the test fail; `tdd-guide` is a gentler walkthrough. Pick one per team and stay with it. |
| `superpowers:requesting-code-review` vs `pr-review-expert` | The former is about *asking* well; the latter is a structured reviewing pass. |
| `incident-commander` vs `incident-response` | Outage versus security event. Different playbooks — do not substitute one. |
| `senior-security` vs `security-guidance` | Audit of a change versus guidance while writing it. |

Two skills that match the same request are a routing hazard; if your team settles on
one, disable the other rather than leaving the choice to chance.

## Verifying an install

Ask the agent: *"Which skill covers deciding whether to ship a release?"* It should
answer `ship-gate` (or `launch-readiness`). If it cannot, the skills are not loaded —
check the plugin is enabled and the session was restarted.
