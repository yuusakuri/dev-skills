---
name: api-contract-design
description: Use when designing or changing any interface other code depends on - REST or RPC endpoints, GraphQL schemas, event and message payloads, database-facing contracts, CLI surfaces, or public library APIs. Covers contract-first design, compatibility rules, error and pagination conventions, and how to evolve a published interface without breaking clients.
license: MIT
metadata:
  collection: dev-skills
  phase: "2-design"
---

# API Contract Design

**Core principle:** an interface is a promise you cannot take back. Internal code can
be refactored at will; a published contract is owned by its consumers. Design it as
if you will never be able to change it, then build a way to change it anyway.

Applies to every kind of consumer boundary: HTTP, RPC, GraphQL, events, webhooks,
CLI flags, exported library functions, and file formats.

## Procedure

### 1. Model the domain before the transport

Name the resources or events and their relationships first. If the nouns are wrong,
no amount of good URL design saves the API. Warning sign: resources named after your
current database tables or internal services — those leak your implementation and
will be wrong as soon as it changes.

### 2. Write the contract before the implementation

Produce the schema first — OpenAPI, GraphQL SDL, protobuf, JSON Schema, or a typed
signature — and review *that*. It is far cheaper to argue about a field name in a
schema than after three clients depend on it.

Show a consumer the contract and have them describe how they would call it. If they
get it wrong, the contract is wrong, not the consumer.

### 3. Make each operation predictable

- **Consistent naming.** One casing convention, one pluralization rule, one date
  format (ISO 8601, UTC). Consistency beats individually optimal choices.
- **Explicit types.** Never overload a field's type or meaning by context. Money is an
  integer of minor units plus a currency code, never a float. Enumerations are closed
  sets with documented values, and clients must tolerate unknown members.
- **Idempotency.** Any operation a client might retry needs a defined repeat behavior —
  naturally idempotent, or keyed by a client-supplied idempotency token. Networks
  retry whether or not you designed for it.
- **No unbounded results.** Every collection is paginated from day one; adding
  pagination later is a breaking change. Prefer cursors over offsets for anything that
  changes while being read.
- **Nullable means something.** Distinguish "absent", "null", and "empty" deliberately,
  and document which one means what.

### 4. Design errors as carefully as successes

Errors are the part consumers actually integrate against, and the part usually
designed last. Specify:

- A **stable machine-readable code** per failure mode — clients branch on this, never
  on human-readable text, which you must be free to reword
- A human-readable message for logs and developers
- Which field caused a validation failure
- Whether the error is **retryable**, and after how long
- The correct status or error class per category: bad input, unauthenticated,
  unauthorized, not found, conflict, rate limited, internal

Never return success with an error embedded in the body. Never leak stack traces,
internal hostnames, or SQL to a caller.

### 5. Decide the compatibility rules up front

Classify every future change:

**Backward compatible (safe):** adding an optional field; adding a new endpoint,
event type, or enum member *if* clients were told to tolerate unknowns; relaxing a
validation rule; adding an optional parameter with the old behavior as default.

**Breaking (never do silently):** removing or renaming anything; changing a type or
format; making an optional field required; tightening validation; changing defaults;
changing pagination, ordering, or error codes; changing the meaning of a field while
keeping its name — **the most damaging kind, because nothing fails loudly.**

### 6. Version deliberately

Choose one strategy and document it: URL versioning (`/v2/`) for large public
surfaces; media-type or header negotiation for finer control; additive-only evolution
with no versions, which works well for events and GraphQL.

Whatever you choose, the rule is the same: **existing clients keep working.**

### 7. Evolve with expand/contract

To change a published contract without a flag day:

1. **Expand** — add the new field, endpoint, or behavior alongside the old one
2. **Migrate** — update clients; if you cannot see all clients, announce and wait
3. **Verify** — confirm from telemetry that the old path has no traffic
4. **Contract** — remove the old path

Step 3 is not optional. Remove-on-schedule without checking usage is how outages
happen. Deprecation needs a date, a replacement, and a warning consumers can see —
a response header, a log line, or a compiler warning.

### 8. Specify the operational contract too

Rate limits and what happens at the limit; authentication and authorization scheme;
payload size limits; timeout and retry expectations; ordering and delivery guarantees
for events (at-least-once means consumers must deduplicate — say so).

## Checklist before publishing

- [ ] Schema written and reviewed before implementation
- [ ] Naming, dates, and types consistent across every operation
- [ ] Every collection paginated; every mutating call's retry behavior defined
- [ ] Error codes stable, categorized, and documented with retryability
- [ ] Compatibility policy and versioning strategy written down
- [ ] Auth, rate limits, and size limits specified
- [ ] Examples for the common case and at least two failure cases
- [ ] A consumer read it and used it correctly without asking you

## Red flags

- **Designing endpoints directly from database tables.** The schema is now public.
- **`POST /doEverything` with a `type` switch.** No consumer can tell what is valid.
- **Errors as free text only.** Every client will parse your prose and break on a typo fix.
- **"Just bump the version"** for a change that could have been additive. Versions
  multiply maintenance; use them when you must, not to avoid design work.
- **A field whose meaning depends on another field's value** — undocumented complexity
  that every consumer will implement slightly differently.
