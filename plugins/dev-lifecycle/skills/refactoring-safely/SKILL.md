---
name: refactoring-safely
description: Use when restructuring code without changing its behavior - renaming, extracting, splitting modules, removing duplication, replacing a pattern, or making a change easier before making it. Also use before modifying legacy code that has no tests. Keeps behavior provably identical and keeps the change reviewable.
license: MIT
metadata:
  collection: dev-skills
  phase: "4-implementation"
---

# Refactoring Safely

**Definition:** refactoring changes structure while behavior stays *exactly* the same.
The moment behavior changes, it is not a refactor — it is a change, and it needs the
requirements, tests, and review that any change needs.

**Core principle:** the safety of a refactor comes entirely from the tests that existed
*before* you started. Without them you are not refactoring; you are rewriting and
hoping.

## The rule that makes it safe

**Never mix refactoring and behavior change in one commit.**

Make the refactor, commit it green. Then make the behavior change, commit it green.
Mixed commits are the single biggest cause of refactoring incidents, because a
reviewer cannot separate "moved" from "changed", so nobody actually reviews the
change — and a bisect cannot tell you which half broke.

If a refactor would make an upcoming change easy: **first make the change easy, then
make the easy change** — as two separate commits.

## Procedure

### 1. Establish a green baseline

Run the full suite and see it pass. If it is red, stop — you will not be able to tell
your damage from the existing damage.

### 2. Ensure the behavior is covered

Ask: if I broke this, would a test fail? Verify by actually breaking it — invert a
condition, return a wrong value — and confirm a test goes red. If nothing fails, you
have no safety net.

**For untested legacy code, write characterization tests first.** These do not assert
what the code *should* do; they capture what it *currently* does, bugs included:

1. Find the seam where you can observe the current behavior
2. Feed it representative inputs, including edge cases
3. Record actual outputs and assert them
4. Include outputs that look wrong — note them, but do not fix them now

Their only job is to detect change. Fix the bugs afterwards, deliberately, as separate
commits with their own tests.

### 3. Take small steps and stay green

Each step should be small enough that you can undo it without thought. Run the tests
after each one. Commit each green step — frequent commits mean a failed step costs you
minutes, not an afternoon.

Prefer automated refactorings (IDE or language tooling) for rename, extract, inline,
and move: they are mechanical and do not typo.

### 4. Preserve the public contract

If the code is used outside your module, changing its surface is not a refactor. Use
expand/contract: add the new form, migrate callers, verify nothing calls the old form,
then remove it. See `api-contract-design`.

### 5. Verify equivalence, not just green tests

For high-risk transformations, add evidence beyond the suite: compare the old and new
implementations on a corpus of real inputs, run both in production with only the old
one authoritative and log the differences, or diff the generated output where one
exists.

## When not to refactor

- **You do not have tests and cannot get them cheaply** — and the code is not in your
  way. Leave it.
- **Mid-incident.** Restore service first (`incident-response`); refactor later.
- **To satisfy taste alone.** "I would have written it differently" is not a reason to
  churn code and reviewer attention. Refactor code you are about to change, or code
  that is demonstrably causing bugs.
- **A big-bang rewrite.** Rewrites lose undocumented behavior that users depend on and
  they stay unfinished. Strangle the old implementation incrementally instead: route
  one path at a time to the new code, with the ability to switch back.

## Keeping it reviewable

A reviewer must be able to trust a refactor by inspection:

- Separate commits for mechanical moves and for anything else
- Say in the message what is being restructured and why, and assert no behavior change
- Keep pure renames and pure moves in their own commits — a diff that both moves a file
  and edits it is unreadable
- If the diff is large but mechanical, tell the reviewer how to verify it cheaply

## Red flags

- **"While I was in there, I also..."** — Stop. Separate commit.
- **Tests edited in the same commit as the refactor.** If behavior did not change, why
  did the test have to? Either it tested implementation, or you changed behavior.
- **Deleting a test that fails after your change.** That test is doing its job.
- **A "refactor" PR that fixes bugs.** Split it: the fixes need their own tests and review.
- **No test failed when you deliberately broke the code.** You have no coverage; get it
  first.
