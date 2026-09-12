---
name: dependency-upgrades
description: Use when adding, upgrading, or removing a third-party dependency, when triaging a vulnerability advisory, or when a lockfile or supply-chain alert needs a decision - covers evaluating a new dependency, upgrading safely, assessing whether an advisory actually affects you, and keeping upgrades routine rather than terrifying.
license: MIT
metadata:
  collection: dev-skills
  phase: "7-review"
---

# Dependency Upgrades

**Core principle:** every dependency is code you ship, maintain, and are responsible
for, written by someone you cannot call. The decision to add one is permanent in
practice — removing it later is a project, not a commit.

## Adding a dependency

Before adding, answer honestly:

1. **Could we write this ourselves in an hour?** If yes, and the surface is small,
   write it. A left-pad-sized dependency is not worth a supply chain.
2. **Is it maintained?** Recent releases, issues answered, more than one maintainer.
   Archived or single-maintainer packages are a future migration you have scheduled
   without knowing it.
3. **How big is it really?** Count transitive dependencies, not just the top-level one.
   Each is another party that can break or compromise you.
4. **What is its license,** and is it compatible with how you distribute your product?
   This is the question teams skip and lawyers find later.
5. **What does it do at install time?** Post-install scripts run with your
   credentials on your machine and in CI.
6. **What happens when it is abandoned?** Could you fork or replace it, or would it be
   load-bearing and irreplaceable?

Then **pin it and commit the lockfile.** Reproducible builds are the baseline; without
a lockfile you do not know what you shipped.

## Upgrading

**Upgrade routinely and in small steps.** The reason upgrades are frightening is that
they are rare: a two-year gap means a dozen breaking changes at once with no way to
tell which one broke you. Frequent small upgrades are individually boring, which is
the goal.

Procedure:

1. **One dependency per change.** A batch that fails tells you nothing about which
   caused it. Group only patch-level updates of unrelated packages.
2. **Read the changelog** between your version and the target — especially for a major
   bump. Note deprecations and behavior changes, not just breaking API changes.
3. **Upgrade, run the full suite, and read the output.** Silent behavior changes are
   the dangerous ones: a default that changed, a format that shifted, an error that
   became a warning.
4. **Check what else moved.** A single upgrade can pull in a new transitive tree;
   review the lockfile diff, not just the manifest diff.
5. **Verify at runtime, not only in tests.** Start the application and exercise a path
   that uses the dependency.
6. **Deploy separately from feature work,** so a problem is attributable and revertible.

Prefer the current major of a runtime or framework to be within the supported window —
staying on an unsupported version means security fixes stop arriving, and the eventual
jump is a project.

## Triaging a vulnerability advisory

An advisory is not automatically an emergency, and treating every one as critical
guarantees real ones get lost. Assess in this order:

1. **Do we actually use the vulnerable code path?** Many advisories affect a function
   or configuration you never call. Verify by looking, not by assuming.
2. **Is it reachable by untrusted input?** A parsing flaw in a library you only feed
   internal, trusted data is a different risk from one on a public endpoint.
3. **What is the real impact here** — remote code execution, data disclosure, denial of
   service — in *your* deployment?
4. **Is it a direct or transitive dependency?** Transitive ones may need the direct
   parent upgraded, or an override.

Then act: patch immediately for anything reachable and serious; schedule the rest into
routine upgrades; and if no fix exists, mitigate (disable the feature, filter the input,
restrict access) and record the accepted risk with a date to revisit.

**Record the decision either way.** An advisory dismissed without a written reason will
be re-triaged from scratch by the next person, every time.

## Keeping it sustainable

- Automate detection — an audit/scan step in CI, and automated update PRs for patches
- Do not auto-merge anything but patch updates with a green suite
- Review the dependency tree periodically and delete what is no longer used; unused
  dependencies still carry vulnerabilities and still get flagged
- Treat "we can't upgrade because of X" as a tracked issue, not a permanent state

## Red flags

- **A lockfile that is not committed,** or is regenerated casually in unrelated PRs
- **A giant "update all dependencies" PR.** Nothing in it can be reviewed or bisected
- **Upgrading to silence a scanner without reading what changed**
- **A dependency added for one utility function**
- **Suppressing an advisory with no written justification or expiry**
- **Copying a package name from a suggestion without checking it exists and is the one
  you meant** — typosquatting is a live attack, not a theoretical one
