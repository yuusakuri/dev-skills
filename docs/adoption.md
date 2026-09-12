# Adopting these skills

## In Claude Code (recommended)

```bash
/plugin marketplace add yuusakuri/dev-skills
/plugin install dev-lifecycle@dev-skills
/plugin install superpowers@dev-skills
/plugin install example-skills@dev-skills
```

Skills trigger on their descriptions, so in normal use you do not invoke them by name —
describing the task is enough. Naming one explicitly ("use requirements-definition")
always works and is useful when you want a specific phase.

## In another agent runtime

The skills are plain [Agent Skills](https://agentskills.io/specification) directories:
a folder with a `SKILL.md` carrying YAML frontmatter. Any runtime implementing the
format can use them.

```bash
git clone https://github.com/yuusakuri/dev-skills
cp -r dev-skills/plugins/dev-lifecycle/skills/* <your-skills-directory>/
```

For the upstream collections, clone them from their own repositories at the refs pinned
in `.claude-plugin/marketplace.json` — do not copy them out of a third party.

If your runtime does not support the `plugin:skill` reference form, the
`development-lifecycle` router's upstream references (`superpowers:brainstorming`) still
read correctly as names; only the automatic resolution differs.

## Making it stick in a project

Installing skills makes them *available*. Three things make them *used*:

### 1. Point at the router from the project's agent instructions

In your `CLAUDE.md` or `AGENTS.md`:

```markdown
## Working in this repository

Start with the `development-lifecycle` skill to identify the phase and the skill that
owns it. Scale the process to the change: trivial fixes go straight to implementation
and verification; anything touching <the risky areas of this project> requires a
threat model and an ADR.

Project specifics that override general practice:
- Test command: <command>
- Requirements live in: docs/requirements/
- Decisions live in: docs/decisions/
```

The last block matters most. These skills are deliberately stack-agnostic; your
`CLAUDE.md` is where the stack-specific truth goes, and it takes precedence.

### 2. Create the directories the skills write into

Several skills produce artifacts that belong in the repository rather than in a chat
log. Create them so there is an obvious place to put things:

```
docs/requirements/   # requirements-definition
docs/decisions/      # architecture-decision-records (ADR NNNN-slug.md)
docs/security/       # threat-modeling
docs/postmortems/    # postmortem
```

A skill that has nowhere to write its artifact produces a message that scrolls away.

### 3. Adopt incrementally

Do not mandate all ten phases on day one; it will be abandoned. A workable order:

1. **`superpowers:verification-before-completion` and `test-driven-development`** —
   these change day-to-day quality immediately and need no process agreement
2. **`codebase-orientation` and `superpowers:brainstorming`** — cheap, and they cut the
   rework that comes from starting in the wrong place
3. **`requirements-definition` and `architecture-decision-records`** — the first two
   that need team agreement, because they produce artifacts others must read
4. **`release-management`, `observability-instrumentation`, `incident-response`,
   `postmortem`** — when the project has users whose downtime matters
5. **`threat-modeling`, `security-review`, `accessibility-review`** — before the first
   release that handles real user data or faces the public

## Customizing

Fork, or keep this as an upstream and add a project-specific plugin alongside it. Two
rules keep customization from degrading routing:

- **Do not duplicate a trigger.** Two skills whose descriptions match the same request
  get chosen between unpredictably. Narrow one, or replace rather than add.
- **Keep project specifics in project files.** A skill that hardcodes your CI provider
  stops being reusable and starts being documentation with extra steps.

## Verifying an install

Ask the agent: *"Which skill covers deciding what to test and at which level?"* It
should answer `test-strategy`. If it cannot, the skills are not loaded — check that the
plugin is enabled and that the session was restarted.
