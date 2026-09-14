# Why these sources, and not others

The catalog lists what was chosen. This page records why, so a later reader can tell a
deliberate choice from an accident. For the list itself see
[reference/catalog.md](../reference/catalog.md).

## Why `addyosmani/agent-skills` is referenced at upstream HEAD

Several catalogs vendor copies of it, and copies drift. One widely used mirror is pinned
several revisions behind, and its copy of `security-and-hardening` is missing roughly 57
lines present upstream. Referencing the origin keeps security content current.

## Two entries were replaced on measured substance

| Replaced | Size | Replacement | Size |
|---|---|---|---|
| `performance-profiler` | 2.7 KB | `performance-optimization` | 21.7 KB |
| `ci-cd-pipeline-builder` | 3.2 KB | `ci-cd-and-automation` | 11.3 KB |

## Two apparent duplicates are kept deliberately

Their triggers differ.

`security-and-hardening` is for implementation, writing secure code. `senior-security`
and `security-guidance` are for review, auditing a diff that already exists.

`api-design-reviewer` was not replaced by `api-and-interface-design` despite their
similar size, because the incumbent ships an OpenAPI linter, a breaking-change detector
and a scorecard as runnable scripts.

## One source was dropped entirely

`rohitg00/awesome-claude-code-toolkit` exposes only command-based plugins under
`./plugins/` in its marketplace; the repository's own `skills/` directory is not listed
as an installable plugin. The one skill curated from it, `database-optimization`, could
be read at its pinned ref but never installed by the documented method. It was removed
rather than left as an instruction that fails.

## Considered and deferred

`phuryn/pm-skills` (26.3k stars, MIT) has `pre-mortem` and `retro`, but at 4.1 KB and
2.8 KB they add little over `ship-gate` and `launch-readiness`.

`senior-devops` (alirezarezvani) overlaps `ci-cd-and-automation` in 34 places.
