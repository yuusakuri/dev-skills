---
name: test-strategy
description: Use when deciding what to test and at which level, when a suite is slow, flaky, or passes while bugs ship, or when starting testing on a feature or an untested codebase - chooses the right test levels, defines coverage that means something, and keeps the suite fast and trustworthy.
license: MIT
metadata:
  collection: dev-skills
  phase: "3-planning"
---

# Test Strategy

`superpowers:test-driven-development` governs *how* to write a test as you implement.
This skill decides *which tests should exist at all* — the level, the scope, and what
"enough" means.

**Core principle:** a test suite's job is to let you change the code with confidence.
A suite that is slow, flaky, or coupled to implementation does the opposite: it makes
change expensive and teaches the team to ignore failures.

## Choosing the level

Push every test to the lowest level that can still catch the failure you care about.

| Level | Tests | Use for | Keep |
|---|---|---|---|
| **Unit** | One unit, no I/O | Logic, branches, edge cases, calculations, parsing | Milliseconds; the bulk of the suite |
| **Integration** | Real collaborators — DB, queue, filesystem | Queries, transactions, serialization, migrations, wiring | Seconds; one per meaningful seam |
| **Contract** | Producer and consumer agree on a schema | Service and API boundaries you do not own both sides of | Fast; one per contract |
| **End-to-end** | The whole system through its real interface | A handful of critical user journeys | Minutes total; as few as possible |

Most gaps are not "not enough tests" but **tests at the wrong level**: business rules
verified through a browser (slow, flaky, vague failures), or integration seams
verified only with mocks (fast, green, and wrong).

### The mocking rule

Mock what you do not own and cannot run: third-party APIs, payment providers, email.
Do not mock what you own — your own database, your own modules. A test suite that
mocks your database proves your mocks agree with themselves.

When you must mock an external service, add one contract test against the real thing
(or a provider-maintained fake) so drift is detected.

## What to test

Prioritize by **cost of failure × likelihood of breakage**:

1. **Money, data loss, security, and correctness of core rules** — always, thoroughly
2. **Boundaries and edges** — empty, one, many, maximum, zero, negative, null,
   duplicate, out-of-order, unicode, very long
3. **Error paths** — the code that only runs when something has gone wrong is the code
   least likely to have been exercised by hand
4. **Every fixed bug** — a regression test is the only thing that makes a fix permanent
5. **Concurrency and idempotency** — what happens when it runs twice, or at once

Do not test: framework behavior, language semantics, getters with no logic, or exact
wording of UI copy that changes weekly. Those tests cost maintenance and catch nothing.

## What a good test looks like

- **Tests behavior, not implementation.** If a pure refactor breaks it, it was testing
  the wrong thing.
- **One reason to fail.** The name states the behavior; the failure message identifies
  the bug without opening the file.
- **Arrange, act, assert** — visible in that order, with no hidden setup in shared state.
- **Independent and order-free.** No test depends on another having run. Each creates
  its own data and cleans up.
- **Deterministic.** Inject clocks, seeds, and IDs. Never sleep to wait for something;
  wait for the condition.
- **Real assertions.** `assert response.ok` proves almost nothing; assert the value.

## Coverage, honestly

Coverage tells you what was *executed*, not what was *verified* — a suite with no
assertions can reach 100%. Use it to find untested files and untested error branches,
which is a genuine signal. Never use it as a target: a mandated number is met with
tests written to touch lines, which are worse than no tests because they must be
maintained and they inspire false confidence.

Better questions: could I make a breaking change and have this suite catch it? Does
every bug we shipped have a test today?

## Keeping the suite trustworthy

**Speed is a feature.** A suite developers do not run is not a safety net. Keep the
fast tier under a couple of minutes and run it on every change; push slow checks to a
separate tier that runs before merge.

**Flakes are bugs.** A test that fails randomly destroys the meaning of a red build —
after a few, the team stops reading failures entirely. Fix or delete; never retry into
green. See `ci-and-flaky-tests`.

**Tests are production code.** They get reviewed, refactored, and deleted when
obsolete. Duplication in setup is worth extracting; cleverness in assertions is not.

## Applying this to an untested codebase

Do not attempt a coverage campaign; it will stall. Instead:

1. Add an end-to-end smoke test for the one journey that must never break — this buys
   you the ability to refactor at all
2. Write a characterization test before touching any legacy code (`refactoring-safely`)
3. Require a test with every bug fix and every new behavior, starting now
4. Let coverage grow along the paths you actually change

## Output

For a feature, state before implementing:

```
Critical behaviors (must not break): ...
Unit:        <what, roughly how many>
Integration: <which seams>
E2E:         <which journeys — keep to 1-3>
Not tested, deliberately: <what, and why that is acceptable>
Test data / fixtures: <approach>
```

## Red flags

- **Only end-to-end tests.** Slow, flaky, and they tell you *something* broke, not what.
- **Only unit tests with everything mocked.** Green suite, broken wiring.
- **A shared fixture every test mutates.** Order-dependent failures are coming.
- **`sleep()` in tests.** Flaky today, slower every time someone raises the number.
- **Coverage gate as the quality bar.** You will get the number and not the safety.
