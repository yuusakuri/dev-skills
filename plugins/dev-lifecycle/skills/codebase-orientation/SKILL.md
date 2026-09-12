---
name: codebase-orientation
description: Use before changing code in an unfamiliar repository, package, or subsystem - builds an accurate map of how the project is built, tested, and structured, and finds the existing pattern to follow, so the change fits the codebase instead of fighting it.
license: MIT
metadata:
  collection: dev-skills
  phase: "0-orientation"
---

# Codebase Orientation

**Core principle:** the most expensive code review comment is "we already have one
of these." Spend ten minutes reading before you spend two hours writing.

Stop when you can answer all five questions in the checklist. Do not read the whole
repository — that is procrastination, not orientation.

## The five questions

You are oriented when you can answer these from evidence, not assumption:

1. **How is it run and built?** The entry point, the build command, the dev loop.
2. **How is it tested?** The command, the framework, where tests live, what a typical
   test looks like.
3. **Where does my change go?** The module that owns this concern, and why that one.
4. **What is the local idiom?** How this codebase does errors, config, logging,
   dependency injection, and naming — which is often *not* the language's default.
5. **What will my change break?** Who calls the code I am about to touch.

## Procedure

### 1. Read the project's own words first

In order, and stop early if they answer the questions:

- `README`, `CONTRIBUTING`, `docs/`
- `CLAUDE.md` / `AGENTS.md` — these are instructions to you and override general habits
- `architecture/`, `adr/`, `docs/decisions/` — past decisions explain present oddities
- The build/package manifest, which names the real toolchain, scripts, and dependencies
- CI configuration — **the most reliable spec of "correct"**, because it is enforced.
  Whatever CI runs is what the project actually requires.

### 2. Map the structure, not the files

Get the shape of the tree to a depth of two or three. Name the top-level modules and
what each owns. Ignore vendored, generated, and build output directories.

### 3. Find the nearest neighbor

Locate an existing feature that resembles what you are about to build — the same kind
of endpoint, job, component, or command. Read it end to end, including its tests.

**This is the highest-value step.** One complete vertical slice teaches more than
fifty files skimmed, and it gives you a template that is already correct here.

### 4. Trace one path end to end

Follow a single request, command, or event from its entry point to its persistence or
output. You are learning the layers and where they hand off, not the details.

### 5. Establish a green baseline

Run the build and the test suite before changing anything.

If it is already red, **stop and say so**. Never start work on a red baseline: you
will not be able to tell your breakage from the pre-existing breakage, and you will
end up debugging someone else's problem while believing it is yours.

### 6. Check history where code is confusing

For a file that looks strange, read its recent history and the commit messages. Odd
code is usually a fixed bug wearing a disguise — reverting it "for cleanliness"
reintroduces the bug.

## Output

Before starting work, state briefly:

```
Build/run:     <command>
Test:          <command>       Baseline: <green | red — do not proceed>
Change goes:   <module> — because <reason>
Pattern to follow: <file:line of the nearest neighbor>
Local idioms:  <errors / config / logging conventions that differ from the default>
Callers at risk: <list, or "none — new surface">
Unknowns:      <what you could not determine>
```

Carry the unknowns into the next phase as explicit questions. An unknown you named is
a risk; an unknown you glossed over is a bug.

## Red flags

- **"I'll just add a new utility file."** You have not looked for the existing one.
- **"The tests are slow, I'll run them at the end."** You have no baseline, so you
  cannot attribute failures.
- **Your diff is the only place in the repo that does it that way.** Either follow the
  local idiom or make the case for changing it everywhere (`architecture-decision-records`).
- **Copying a pattern you do not understand.** If you cannot say why the neighbor does
  something, you cannot know whether your case needs it.
