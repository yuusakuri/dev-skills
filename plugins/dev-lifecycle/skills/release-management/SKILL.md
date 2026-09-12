---
name: release-management
description: Use when shipping a change to users - covers versioning and changelogs, release checklists, progressive rollout with feature flags, canaries, verification after deploy, and rollback. Use before deploying anything whose failure would affect users, and when establishing a release process.
license: MIT
metadata:
  collection: dev-skills
  phase: "8-release"
---

# Release Management

**Core principle:** a deploy is not a release, and a release is not a success. The work
ends when you have verified the change is doing what it should in production — with
the ability to undo it quickly if it is not.

## Make releases small and frequent

The size of a release determines the difficulty of everything else about it. A release
containing one change has an obvious cause when it breaks and an obvious rollback.
A release containing forty changes has neither.

Large, infrequent releases feel safer and are the opposite: they concentrate risk,
make diagnosis a search problem, and make rollback a negotiation about which of the
forty changes you are also reverting.

## Versioning and changelog

Pick a scheme and hold to it. For anything with consumers, semantic versioning carries
a promise: major means "this will break you", minor means "new, compatible", patch
means "fixed, compatible". **Breaking a consumer in a minor release destroys the only
value the scheme has.**

Write the changelog for the person **upgrading**, grouped by what it means to them —
what breaks, what is new, what is fixed, what is deprecated — with migration
instructions for anything breaking. A changelog generated from commit subjects is a
commit log; it is not a changelog.

## Decouple deploy from release with flags

Shipping code and enabling behavior are separate events. A feature flag lets you deploy
dormant code, enable it for a fraction of users, and turn it off in seconds without a
rollback.

Rules that keep flags from becoming the problem:

- Default **off**; enable deliberately
- The off path must remain correct and tested, not just present
- Every flag has an owner and a removal date — **stale flags are permanent,
  untested branches** that multiply the states your system can be in
- Removing the flag after full rollout is part of the work, not a follow-up someone
  might do

## Roll out progressively

For anything with meaningful risk, do not switch all traffic at once:

1. **Canary** — a small percentage or one instance, watched closely
2. **Compare** — error rate, latency, and the business metric, canary versus baseline
   (`observability-instrumentation`). Comparing against *baseline*, not against a fixed
   threshold, is what makes a canary informative
3. **Expand in steps**, pausing at each to watch
4. **Complete**, then remove the flag and the old path

Decide the **abort criteria before you start**. During a rollout, with a graph moving,
nobody makes a good judgment call about whether a 0.3% error increase is acceptable.
Write it down while you are calm.

## Release checklist

- [ ] All checks green on the exact commit being released
- [ ] Migrations follow `data-migration-safety` and are separated from the code that
      requires them
- [ ] Backward compatible with the previous version — they will run simultaneously
- [ ] Feature flag in place and defaulted off, if risk warrants
- [ ] Rollback path known and **tested**, not assumed
- [ ] Monitoring and alerts exist for the new behavior
- [ ] Changelog and any consumer-facing docs updated
- [ ] Anyone who needs to know (support, ops, dependent teams) has been told
- [ ] Someone is available to respond — **do not release into an empty calendar**

## Verify after deploying

Deploying is the middle of the process. Then:

1. Confirm the version actually running is the one you shipped
2. Exercise the changed path yourself
3. Watch error rate, latency, and the business metric for long enough to see a
   regression — a few minutes, not a few seconds
4. Check the logs for new error types, not just error volume
5. Say explicitly that the release is verified, or roll back

## Rolling back

**Roll back first, diagnose second.** The instinct to find the cause while users are
affected is the most common way a five-minute problem becomes an hour-long one. Restore
service, then investigate from a position of safety.

Know in advance which changes are *not* simply revertible — anything that has written
data in a new shape, consumed a message, or called an external system. For those, the
rollback plan is a procedure, not a button, and it must exist before the deploy.

## Red flags

- **Deploying on Friday afternoon, or right before everyone leaves.** Not superstition:
  the cost of a failure is the response time, and nobody is there.
- **A rollback path that has never been exercised.** It does not work; you just have not
  found out yet.
- **Schema change and the code requiring it in one release.** No rollback exists.
- **"It deployed successfully"** as the completion criterion. That is not verification.
- **Flags older than the feature.** Untested code paths accumulating silently.
- **Nobody can say what is currently released.** Then nobody can reason about an incident.
