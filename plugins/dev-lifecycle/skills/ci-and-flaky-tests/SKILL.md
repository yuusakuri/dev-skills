---
name: ci-and-flaky-tests
description: Use when CI is red, when tests pass locally but fail in CI, when a test fails intermittently without code changes, or when designing a pipeline - covers diagnosing flakes to root cause, keeping the build trustworthy and fast, and structuring pipeline stages so failures are fast and meaningful.
license: MIT
metadata:
  collection: dev-skills
  phase: "5-quality"
---

# CI and Flaky Tests

**Core principle:** a red build must always mean something is broken. The moment a team
learns that failures are sometimes noise, the build stops being a signal, and every
real failure after that is at risk of being re-run away.

**"Flaky" is a symptom, never a root cause.** A test that fails intermittently has
found real non-determinism — in the test, or in the code. Sometimes the non-determinism
is only in the test; often it is a genuine race that will happen in production, at the
worst time, and be much harder to diagnose there.

## Diagnosing a flake

### 1. Capture the evidence before it rotates away

Save the full failure output, the logs, the timing, and the commit. CI logs expire;
a flake you cannot reproduce and did not record is one you will meet again from zero.

### 2. Determine whether it is genuinely intermittent

Re-run the **same commit**. Failing consistently means it is not a flake — it is a
real failure, and the "flaky" label is hiding a bug. Confirm the base branch is green
before blaming your change.

### 3. Find the source of non-determinism

Flakes come from a short list. Work through it:

| Source | Signature | Fix |
|---|---|---|
| **Time** | Fails near midnight, month end, DST, or in another timezone | Inject a clock; never use the real one in tests |
| **Ordering** | Fails only in a particular order or with a particular seed | Each test creates its own data and cleans up; never share mutable state |
| **Concurrency** | Fails under parallel execution or on a loaded machine | Find the real race; isolate resources per worker (ports, DBs, temp dirs) |
| **Waiting** | `sleep` in the test; fails on a slow runner | Poll for the condition with a timeout; never sleep a fixed duration |
| **External service** | Fails when a network or third party is involved | Stub it; keep one contract test that is allowed to be slow |
| **Resource leak** | Fails later in the run, or only in long runs | Close connections, files, and servers; assert cleanup |
| **Randomness** | Fails rarely with no pattern | Seed it, and log the seed on failure so it is reproducible |
| **Unordered results** | Fails on collection comparison | Sort, or compare as sets — a query without `ORDER BY` has no order |

### 4. Reproduce it deliberately

Run the test in a loop, under parallelism, with a shuffled order, on a constrained
machine. A flake you can reproduce is an ordinary bug.

### 5. Fix the cause, then prove it

Run it many times in the conditions that used to fail. One green run proves nothing
about a test that failed one time in fifty.

## What never to do

- **Never add a retry to make it green.** Retries hide the race and it lands in
  production. (An exception, stated explicitly: retrying a genuinely external,
  unavoidable network step — not a test of your own code.)
- **Never skip, disable, or quarantine a test to unblock a merge** without a tracked
  issue and an owner. A quarantined test is a deleted test that still costs runtime.
- **Never increase a sleep until it passes.** You have made the suite slower and the
  flake rarer, not absent.
- **Never re-run until green and merge.** That is how the race reaches users.

## Local passes, CI fails

The difference is always environment. Check, in order: environment variables and
secrets; timezone and locale; filesystem case sensitivity and path separators;
dependency versions (is the lockfile respected in CI?); available CPU and memory —
CI runners are usually slower and more parallel, which is why they surface races;
leftover local state (a database, a cache, a build artifact) that CI does not have;
and clean-checkout assumptions — CI has no uncommitted files.

## Designing the pipeline

- **Fast feedback first.** Order stages cheapest-and-most-likely-to-fail first: lint
  and typecheck, then unit tests, then integration, then end-to-end. Fail fast.
- **Every check is either required or deleted.** An advisory check that is always
  slightly red teaches people to ignore red.
- **Reproducible.** Pinned tool versions, committed lockfiles, no dependence on
  runner-cached state for correctness. Caching may make it faster, never different.
- **Readable failures.** The output should name what failed and where without anyone
  opening a machine. Upload artifacts — screenshots, logs, reports — on failure.
- **Keep the main path green.** A long-red main branch means nobody can tell whether
  their own change is safe, and everything after it is guesswork.
- **Fix the base first.** If the base branch is red, that is the priority — work on top
  of it cannot be verified.

## Red flags

- A retry count anywhere in the test configuration
- A `skip` with no issue link, or one linking to a closed ticket
- "Just re-run it" as the normal response to a failure
- CI taking long enough that people stop waiting for it
- Tests that pass individually but fail as a suite — shared state
- A green build that nobody trusts enough to deploy from
