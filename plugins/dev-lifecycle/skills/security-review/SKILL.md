---
name: security-review
description: Use when reviewing a change for vulnerabilities before it merges or ships, or when auditing existing code for security defects - a systematic pass over input handling, authorization, secrets, injection, and dependencies that reports exploitable findings with evidence rather than generic warnings.
license: MIT
metadata:
  collection: dev-skills
  phase: "7-review"
---

# Security Review

`threat-modeling` asks what could go wrong with a *design*. This skill audits *code
that exists* — usually a diff, sometimes a whole component.

**Core principle:** report only what you can show is reachable and exploitable. A
review full of theoretical findings trains people to ignore security reviews, which
is worse than not reviewing at all.

## Scope the review

Start by identifying, in the change: every place untrusted input enters; every
authorization decision; every place data leaves the system (response, log, third
party); and every new dependency or permission.

If the diff touches none of these, say so and stop. Do not manufacture findings.

## The review pass

Work through each category against the actual code. For each, trace a concrete path
from an attacker-controlled input to the dangerous operation.

### Input handling and injection

- Is every query, command, path, template, or markup built by **concatenating** a value
  that a user can influence? Parameterize; never escape by hand.
- Does deserialization accept arbitrary types from untrusted data?
- Is user-supplied output encoded for the context it lands in (HTML, attribute, JS,
  URL, shell, SQL)? Encoding for the wrong context is the same as not encoding.
- Does any server-side request take a user-supplied URL or host (SSRF)?
- Can a path be traversed out of its intended directory?
- Is validation on the **server**, not only the client?

### Authorization and authentication

The highest-yield category. Modern applications rarely fail at authentication; they
fail at authorization.

- Does **every** endpoint, job, and data access check who is asking — including the new
  one added in this diff?
- Is the check on the **object being accessed**, not just on the route? Taking an ID
  from the request and fetching it without verifying ownership is the classic bug.
- Is it enforced at the data layer, so a new call path cannot bypass it?
- In a multi-tenant system, is every query scoped by tenant, structurally?
- Is the default **deny**? New resources with no rule should be inaccessible, not open.
- Are tokens verified for signature, expiry, audience, and issuer — all four?

### Secrets and sensitive data

- Any credential, key, or token in source, config, fixtures, or test files?
- Does anything sensitive reach logs, error messages, analytics, or a URL?
- Is sensitive data encrypted where the requirements say it must be?
- Do error responses leak stack traces, versions, internal hosts, or query text?

### Resource and abuse handling

- Can one caller consume unbounded work — no pagination, no rate limit, no size cap,
  unbounded recursion, or a regex that backtracks catastrophically?
- Are uploads limited by size and validated by content rather than extension?
- Are timeouts set on every outbound call?

### Dependencies and configuration

- New dependency: is it maintained, widely used, and does it need the permissions it
  takes? See `dependency-upgrades`.
- Does the change loosen CORS, CSP, TLS verification, or a security header?
- Does it grant a broader IAM role, open a port, or make a resource public?
- Is anything set to a development default (debug mode, permissive CORS, test keys)?

### Cryptography

- Standard vetted libraries only — never a hand-rolled construction
- Passwords hashed with a slow, salted, purpose-built algorithm
- Randomness from a cryptographically secure source for anything security-relevant
- Constant-time comparison for secrets and tokens

## Reporting findings

For each finding give:

```
Severity:    critical | high | medium | low
Location:    <file>:<line>
Issue:       <one sentence — what is wrong>
Attack path: <who, with what access, sends what, and what they get>
Fix:         <the specific change>
```

Severity is **impact × reachability**. An injection in an admin-only tool behind VPN
is not the same as one on a public endpoint. Rank by exploitability, and put the
critical findings first.

If you cannot describe the attack path concretely, it is an observation, not a
finding — label it that way or leave it out.

## Verifying a fix

Re-review the fix rather than trusting the description. Confirm it addresses the root
cause and not the one input you demonstrated; check whether the same pattern exists
elsewhere in the codebase; and confirm a test now covers the abuse case, or the bug
will return.

## Red flags in the code under review

- A query, command, or path assembled with string formatting
- An ID taken from a request and used to fetch without an ownership check
- `verify=false`, disabled certificate checks, or a permissive wildcard CORS origin
- A new public route added near a group of authenticated ones
- Secrets in a commit — **treat as compromised and rotate**, removing it from history
  is not enough
- A catch-all handler that swallows errors, hiding failed security checks
