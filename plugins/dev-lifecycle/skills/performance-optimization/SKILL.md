---
name: performance-optimization
description: Use when something is too slow, uses too much memory, costs too much to run, or when a latency or throughput target must be met - enforces measure-first discipline, finding the real bottleneck with profiling and benchmarks before changing code, and proving the improvement afterwards.
license: MIT
metadata:
  collection: dev-skills
  phase: "5-quality"
---

# Performance Optimization

**Core principle:** you cannot optimize what you have not measured. Intuition about
bottlenecks is wrong often enough that acting on it wastes effort, adds complexity,
and frequently makes things slower.

**Never change code for performance before you have a measurement showing where the
time or memory actually goes.**

## Procedure

### 1. Define the target first

"Make it faster" has no end. Write down:

- **The metric** — latency, throughput, memory, cost per operation
- **Where it is measured** — user-perceived, server-side, per job
- **Which percentile** — p50 hides the problem; p95/p99 is what users complain about
- **Under what load** — a number that is fine at 10 rps may collapse at 1,000
- **The number that means done**

Without a target you will either stop too early or optimize forever.

### 2. Reproduce and measure the current state

Build a repeatable benchmark or a realistic load test. Record the baseline. If you
cannot reproduce the slowness, you cannot verify a fix — and production telemetry may
be your only honest source (`observability-instrumentation`).

Measure with **production-like data volumes**. Most performance bugs are invisible at
development scale: the query with no index is fast on a thousand rows.

### 3. Profile to find the real bottleneck

Use a profiler, a tracer, or database query statistics — not reading. Find where the
time actually goes, then attack the largest contributor first.

Amdahl's law is the discipline here: making a component that accounts for 5% of
runtime twice as fast buys you 2.5%. Optimizing the wrong thing perfectly is still
nothing.

### 4. Check the usual suspects before micro-optimizing

Orders of magnitude usually hide in a handful of places:

- **N+1 queries and requests** — a loop issuing one call per item. The most common
  serious performance bug in application code by a wide margin.
- **Missing index** — read the query plan, do not guess. A sequential scan on a large
  table is the answer surprisingly often.
- **Doing work that could be avoided** — recomputing what could be cached, fetching
  columns or fields nobody uses, serializing data that is discarded.
- **Doing work serially that could overlap** — independent I/O waiting in sequence.
- **The wrong algorithmic complexity** — an accidental quadratic that is fine in
  testing and fatal at scale.
- **Chatty boundaries** — many small calls across a network or process boundary where
  one batched call would do.
- **Unbounded results** — pagination missing, so cost grows with the data set.

### 5. Change one thing, then measure again

One change per measurement. Batched changes make it impossible to tell which helped —
and some will have hurt. Keep the change if it moves the metric meaningfully; revert
it if it does not. An optimization that adds complexity for a 2% gain is a net loss.

### 6. Guard against regression

Add a test or a monitor for the property that mattered: an assertion on query count to
prevent the N+1 returning, a benchmark in CI with a threshold, or an alert on the
production percentile. Optimizations rot silently without a guard.

## Caching, carefully

Caching is the most reached-for and most dangerous tool here, because it converts a
performance problem into a correctness problem. Before adding one, answer: what is the
invalidation rule; what is served if it is stale; what happens when it is empty (can
the system survive a cold start, or does it stampede); and is it correct per user,
per tenant, per locale?

Do not cache to hide an N+1 or a missing index. Fix the underlying cost first — you
will need it fixed anyway the moment the cache misses.

## Report what you did

```
Target:    <metric, percentile, load> — goal <n>
Baseline:  <measured, with how>
Bottleneck: <what the profile showed>
Change:    <one sentence>
Result:    <new measurement> — <met | not met>
Trade-off: <complexity, memory, staleness, cost>
Guard:     <test, benchmark, or alert added>
```

## Red flags

- **Optimizing without a profile.** You are guessing, and probably wrong.
- **Measuring on development-sized data.** The real bottleneck is invisible there.
- **Several changes, one measurement.** No idea what worked.
- **Reporting an improvement with no number.** "Feels faster" is not a result.
- **Micro-optimizing hot-looking code** while an N+1 query dominates the request.
- **Caching as the first move.** You have added invalidation bugs and kept the cost.
- **Sacrificing correctness for speed** without saying so and getting agreement.
