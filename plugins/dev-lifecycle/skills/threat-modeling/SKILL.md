---
name: threat-modeling
description: Use during design, before implementing anything that touches authentication, authorization, secrets, personal or financial data, file uploads, untrusted input, or external integrations - systematically identifies what can go wrong, who could cause it, and which mitigations must be built in rather than added later.
license: MIT
metadata:
  collection: dev-skills
  phase: "2-design"
---

# Threat Modeling

**Core principle:** security failures are design failures found late. A missing
mitigation costs minutes at design time, days at review time, and a breach
notification in production.

This is a *design-time* skill. To audit an existing diff, use `security-review`.

## When to run it

Always, for anything that: authenticates or authorizes; stores or transmits personal,
health, or financial data; accepts uploads or user-supplied URLs, templates, or
queries; calls or is called by a third party; handles secrets or keys; runs with
elevated privileges; or makes something publicly reachable that was not before.

## Procedure

### 1. Draw the system and its boundaries

Sketch: the components, the data flows between them, the data stores, the external
actors, and — most importantly — the **trust boundaries** the data crosses.

A trust boundary is any point where data moves from a less-trusted zone to a
more-trusted one: browser → server, internet → VPC, tenant A → shared service, third
party → your database. **Almost every vulnerability lives on a trust boundary.**

### 2. Identify what is worth attacking

List the assets: credentials and tokens, personal data, money or its equivalents,
business-critical data integrity, availability of the service, and reputation. Rank
them — you will not mitigate everything equally.

### 3. Enumerate threats with STRIDE

For each component and each flow crossing a boundary, walk the six categories. Do not
skip ones that "obviously don't apply" — that is where findings hide.

| | Threat | Ask | Typical mitigation |
|---|---|---|---|
| **S** | Spoofing | Can someone claim to be another user, service, or tenant? | Strong authN, mutual TLS, signed requests, short-lived tokens |
| **T** | Tampering | Can data be modified in transit, at rest, or in a client-held value? | TLS, integrity checks, server-side validation, signed payloads |
| **R** | Repudiation | Can someone deny doing it? Can we reconstruct what happened? | Append-only audit logs with actor, action, target, time |
| **I** | Information disclosure | Can data leak via responses, errors, logs, timing, or metadata? | Least-privilege queries, output filtering, redaction, generic errors |
| **D** | Denial of service | Can one caller degrade it for everyone? | Rate limits, quotas, timeouts, pagination, bounded work per request |
| **E** | Elevation of privilege | Can a user act beyond their role, or reach another tenant's data? | Deny-by-default authZ checked at the data layer, not the UI |

### 4. Apply the checks that catch the common cases

- **AuthZ on every access path, at the data layer.** The most common serious bug in
  modern applications is an object reference the server never checks ownership of.
  Hiding a button is not authorization.
- **Validate on the server, always.** Client validation is user experience, not security.
- **Never build queries, commands, paths, or markup by string concatenation.**
  Parameterize queries, use argument arrays for subprocesses, resolve and confine
  paths, and use context-aware output encoding.
- **Treat every server-side fetch of a user-supplied URL as SSRF** until proven
  otherwise: allowlist destinations, block internal ranges and metadata endpoints,
  and do not follow redirects blindly.
- **Uploads:** verify type by content and not extension, cap size, store outside the
  web root, and never execute or render them from your own origin.
- **Secrets** come from a secret manager or the environment — never from source, logs,
  error messages, or client-visible config. Assume anything logged will be read widely.
- **Multi-tenancy:** every query is scoped by tenant, enforced structurally (a
  mandatory filter or row-level security), not by developer discipline.

### 5. Decide on each threat, and write it down

For every identified threat choose one and record it: **mitigate** (and how, as a
requirement someone must implement), **accept** (with the reason and who accepted),
or **transfer** (to a provider — and note what their boundary actually covers).

Silence is not a decision. An unrecorded threat becomes an unmitigated one.

### 6. Feed mitigations into the plan

Each mitigation becomes an implementation task with a test. A mitigation without a
test is a comment. Write the abuse cases as tests: the request from the wrong tenant,
the expired token, the oversized payload, the traversal path.

## Artifact

Append to the design doc or ADR, or `docs/security/<feature>-threat-model.md`:

```markdown
## Threat model — <feature>
Date | Participants | Diagram or description of flows and trust boundaries

| # | Boundary/component | Threat (STRIDE) | Impact | Likelihood | Decision | Mitigation + owner | Test |
```

## Red flags

- **"It's internal, so it's fine."** Internal networks are flat and breached often.
- **"We'll add auth later."** Retrofitted authorization misses paths; it is never complete.
- **A model with no accepted risks.** Either you are not being honest, or you have not
  looked at availability and abuse.
- **Mitigations with no tests.** Nothing stops the next refactor from removing them.
- **Rolling your own crypto, tokens, or password hashing.** Use the vetted primitive.
