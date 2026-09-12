---
name: observability-instrumentation
description: Use when building or shipping anything whose health matters in production, or when an incident revealed that you could not tell what was happening - covers what to log, which metrics and traces to emit, how to define alerts that are worth waking someone for, and how to make a system debuggable before it breaks.
license: MIT
metadata:
  collection: dev-skills
  phase: "8-release"
---

# Observability Instrumentation

**Core principle:** you cannot add instrumentation during an incident. Whatever you
emitted before the failure is all the information you will ever have about it.

The test of observability is not "do we have dashboards" but: **can we answer a
question we did not anticipate, without deploying new code?**

## The three signals, and what each is for

- **Metrics** — aggregate numbers over time. Cheap, retained long, good for *is it
  broken and how badly*. Cannot tell you about one specific user.
- **Logs** — discrete events with detail. Expensive at volume, good for *what exactly
  happened in this case*.
- **Traces** — the path of one request across components. Good for *where the time went*
  and *which hop failed* in a distributed system.

Most teams over-invest in logs and under-invest in the other two. Reach for the
cheapest signal that answers the question.

## What to instrument

### Start with the four that describe user-facing health

For every service or endpoint: **traffic** (rate), **errors** (rate and type),
**latency** (as a distribution, not a mean), and **saturation** (how full the
constrained resource is — connections, memory, queue depth, worker pool).

A mean latency is actively misleading: it hides the tail where the complaints live.
Emit percentiles, or a histogram you can compute them from.

### Then add the business signals

Technical health can be perfect while the product is broken. Instrument what the
feature is *for*: orders placed, messages delivered, jobs completed, sign-ups
converted. A drop here catches failures no error rate will show — the silent kind,
where everything returns 200 and nothing works.

### And the queue and dependency signals

Queue depth and age of the oldest item; retry and dead-letter counts; per-dependency
error rate, latency, and timeout counts. Failures usually arrive from a dependency
before they arrive from your own code.

## Writing logs worth having

- **Structured, not prose.** Key-value or JSON, so it can be filtered and aggregated.
  A log line you can only grep is a log line you cannot analyze.
- **Include the correlation ID** on every line, propagated across services. Without it,
  a distributed system's logs are unrelated noise.
- **Log decisions and outcomes, not steps.** "Entered function" is worthless; "rejected
  payment: insufficient funds, account=…, amount=…" is an answer.
- **Include enough context to act** — which user, which tenant, which resource, which
  version. A log that says only "failed to save" costs more than it gives.
- **Never log secrets or personal data.** Tokens, passwords, keys, card numbers, health
  data. Assume logs are broadly readable and retained longer than you expect. Redact at
  the emitter, not in a downstream filter that someone will bypass.
- **Use levels meaningfully.** ERROR means a human must eventually act. If ERROR is
  routine noise, nobody reads ERROR anymore.
- **Log the error with its cause and stack**, not a re-worded message that discards it.

## Alerts

The rule: **alert on symptoms users feel, not on causes.** High CPU is not an
incident; failed checkouts are. Cause-based alerts fire constantly during normal
operation and miss the failures you did not predict.

Every alert must satisfy all four:

1. It indicates **real user impact** (or imminent, certain impact)
2. It is **actionable** — a human can do something specific
3. It has a **runbook**: what it means, how to confirm, what to try first
4. It is **urgent** — if it can wait until morning, it is a ticket, not a page

Delete anything that fails these. **Alert fatigue is a reliability risk in itself**: a
team that routinely ignores pages will ignore the one that mattered.

Set thresholds from an error budget or a stated objective, not from a number that felt
right. Define the objective first: "99.9% of requests succeed within 300 ms over 30
days" makes the alert threshold a derivation rather than a guess.

## Make it debuggable before it breaks

- Emit the **build/version identifier** in logs and metrics, so you can tell whether a
  change caused a shift
- Health and readiness endpoints that reflect real dependency status
- A way to raise log verbosity for a subset of traffic **without a deploy**
- Dashboards organized around user journeys, not around infrastructure
- Sensible cardinality: never put unbounded values (user IDs, URLs with parameters)
  into metric labels — that is how monitoring bills and outages happen

## Before shipping a feature

- [ ] Traffic, error, latency, and saturation signals exist for the new path
- [ ] At least one business-level metric shows it is doing its job
- [ ] Errors are logged with context and correlation IDs, without sensitive data
- [ ] An alert exists for the user-visible failure mode, with a runbook
- [ ] You can answer "is it working for tenant X right now?" without a deploy
- [ ] The dashboard was looked at *after* release, not just built before it

## Red flags

- **Logging everything at INFO** — cost without signal, and the real events are buried
- **Alerting on every metric you have** — fatigue, then ignored pages
- **Mean latency on the dashboard** — the tail is invisible
- **No correlation IDs** in a multi-service system
- **"We'll add metrics if there's a problem."** By then it is too late to learn anything
  about the problem you are having.
