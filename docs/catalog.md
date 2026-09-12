# Curated skill catalog

Generated from [`catalog.json`](../catalog.json) — the machine-readable curation.
Every entry is verified to exist at its pinned upstream ref by
[`scripts/verify-catalog.py`](../scripts/verify-catalog.py). **No upstream file is
copied into this repository.**

## Sources

| Repository | Stars | License | Format | Skills curated |
|---|---|---|---|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | 285.6k | MIT | Agent Skills | 12 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 | Agent Skills | 4 |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | Agent Skills | 28 |
| [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | Agent Skills | 5 |
| [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) | 2.6k | Apache-2.0 | slash commands + agents (NOT Agent Skills) | 1 |

### Pinned refs

- **obra/superpowers** — `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (`v6.3.0`)
- **anthropics/skills** — `34040c9c568585f6929bedeaad110ad08f079624`
- **alirezarezvani/claude-skills** — `19392f7a08264ed00486a251f5b2098321771f94`
- **mohitagw15856/pm-claude-skills** — `f67821d42c8c6db20752030e12ded030a623bee3`
  - *Listed in Anthropic's official plugin directory*
- **rohitg00/awesome-claude-code-toolkit** — `ebdf1d596d2cde5c5cceb32177e8d1cf4829e7d9`
  - *Its marketplace exposes command-based plugins; the repo's own skills/ directory is not listed as an installable plugin. Referenced only as an optional supplement.*

### Install

Each upstream is installed from its own marketplace, under its own plugin names:

```bash
# obra/superpowers  (MIT)
/plugin marketplace add obra/superpowers
/plugin install superpowers@claude-plugins-official

# anthropics/skills  (Apache-2.0)
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills

# alirezarezvani/claude-skills  (MIT)
/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-advanced-skills@claude-code-skills  # plus engineering-skills, a11y-audit, security-guidance

# mohitagw15856/pm-claude-skills  (MIT)
/plugin marketplace add mohitagw15856/pm-claude-skills
/plugin install pm-engineering@pm-skills  # plus pm-essentials, pm-security, pm-delivery

# rohitg00/awesome-claude-code-toolkit  (Apache-2.0)
/plugin marketplace add rohitg00/awesome-claude-code-toolkit
/plugin install adr-writer@claude-code-toolkit

```

## By phase

### Orientation

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `codebase-onboarding` | Map an unfamiliar codebase before changing it | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/codebase-onboarding) | `engineering-advanced-skills` |

### Requirements

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `brainstorming` | Explore intent and design before any code | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/brainstorming) | `superpowers` |
| `prd-template` | Turn agreement into a written PRD with acceptance criteria | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/prd-template) | `pm-essentials` |
| `epic-design` | Decompose a large requirement into epics and stories | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/epic-design) | `engineering-skills` |

### Architecture and design

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `senior-architect` | System design and architectural trade-offs | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-architect) | `engineering-skills` |
| `architecture-decision-record` | Record a hard-to-reverse decision as an ADR | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/architecture-decision-record) | `pm-engineering` |
| `api-design-reviewer` | Contract review with linting and breaking-change detection scripts | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/api-design-reviewer) | `engineering-advanced-skills` |
| `database-schema-designer` | Data model design | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/database-schema-designer) | `engineering-advanced-skills` |
| `threat-model` | Identify threats and mitigations at design time | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/threat-model) | `pm-security` |
| `frontend-design` | Deliberate visual direction for a UI | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design) | `example-skills` |
| `tech-stack-evaluator` | Choose between frameworks or platforms with TCO and ecosystem-health analysis | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/tech-stack-evaluator) | `engineering-skills` |

### Planning

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `writing-plans` | Turn a spec into an executable plan | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-plans) | `superpowers` |
| `senior-qa` | Decide what to test and at which level | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-qa) | `engineering-skills` |
| `using-git-worktrees` | Isolated workspace before implementing | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-git-worktrees) | `superpowers` |

### Implementation

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `test-driven-development` | Red-green-refactor for every feature and bugfix | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/test-driven-development) | `superpowers` |
| `tdd-guide` | Alternative TDD walkthrough | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/tdd-guide) | `engineering-skills` |
| `executing-plans` | Work a written plan with review checkpoints | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/executing-plans) | `superpowers` |
| `subagent-driven-development` | Drive plan tasks through subagents | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/subagent-driven-development) | `superpowers` |
| `dispatching-parallel-agents` | Independent tasks in parallel | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/dispatching-parallel-agents) | `superpowers` |
| `migration-architect` | Schema and data migration sequencing | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/migration-architect) | `engineering-advanced-skills` |
| `tech-debt-tracker` | Track and prioritize restructuring work | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/tech-debt-tracker) | `engineering-advanced-skills` |
| `mcp-builder` | Build an MCP server | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/mcp-builder) | `example-skills` |
| `env-secrets-manager` | Environment-variable hygiene, secret handling, drift and rotation readiness | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/env-secrets-manager) | `engineering-advanced-skills` |

### Debugging and performance

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `systematic-debugging` | Any bug or test failure, before proposing fixes | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/systematic-debugging) | `superpowers` |
| `performance-profiler` | Profile before optimizing | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/performance-profiler) | `engineering-advanced-skills` |
| `database-optimization` | Query and index tuning (command-based repo; see note) | [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit/tree/ebdf1d596d2cde5c5cceb32177e8d1cf4829e7d9/skills/database-optimization) | — |
| `ci-cd-pipeline-builder` | Pipeline design and CI health | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/ci-cd-pipeline-builder) | `engineering-advanced-skills` |
| `chaos-engineering` | Fault injection and resilience testing | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/chaos-engineering) | `engineering-advanced-skills` |

### Verification

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `verification-before-completion` | Evidence before claiming done | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/verification-before-completion) | `superpowers` |
| `webapp-testing` | Real-browser verification via Playwright | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/webapp-testing) | `example-skills` |
| `a11y-audit` | WCAG 2.2 A/AA audit and remediation | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/a11y-audit/skills/a11y-audit) | `a11y-audit` |

### Review

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `requesting-code-review` | Get work checked before merging | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/requesting-code-review) | `superpowers` |
| `receiving-code-review` | Assess feedback rigorously, not performatively | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/receiving-code-review) | `superpowers` |
| `pr-review-expert` | Structured PR review | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/pr-review-expert) | `engineering-advanced-skills` |
| `senior-security` | Security audit of a change | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/senior-security) | `engineering-skills` |
| `security-guidance` | Secure-coding guidance during review | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/security-guidance/skills/security-guidance) | `security-guidance` |
| `dependency-auditor` | Dependency and advisory triage | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/dependency-auditor) | `engineering-advanced-skills` |
| `adversarial-reviewer` | Deliberately critical review that breaks the self-review monoculture | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/adversarial-reviewer) | `engineering-skills` |

### Release

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `observability-designer` | Logs, metrics, traces before shipping | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/observability-designer) | `engineering-advanced-skills` |
| `slo-architect` | SLOs, error budgets, alert thresholds | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/slo-architect) | `engineering-advanced-skills` |
| `runbook-generator` | Operational runbooks for each alert | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/runbook-generator) | `engineering-advanced-skills` |
| `finishing-a-development-branch` | Integrate completed work | [`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/finishing-a-development-branch) | `superpowers` |
| `ship-gate` | Go/no-go release gate | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/ship-gate) | `engineering-advanced-skills` |
| `changelog-generator` | Changelog and release notes | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/changelog-generator) | `engineering-advanced-skills` |
| `launch-readiness` | Launch readiness checklist | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/launch-readiness) | `pm-delivery` |
| `feature-flags-architect` | Ship behind a flag: progressive rollout, kill switch, stale-flag debt | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering/skills/feature-flags-architect) | `engineering-advanced-skills` |

### Operations

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `incident-commander` | Lead an active production incident | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/incident-commander) | `engineering-skills` |
| `incident-response` | Security incident triage, severity, forensics (NIST SP 800-61) | [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/incident-response) | `engineering-skills` |
| `incident-postmortem` | Blameless postmortem with action items | [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills/tree/f67821d42c8c6db20752030e12ded030a623bee3/skills/incident-postmortem) | `pm-engineering` |

### Meta

| Skill | Role | Source | Install plugin |
|---|---|---|---|
| `skill-creator` | Create, edit, and evaluate skills | [`anthropics/skills`](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator) | `example-skills` |

## Known thin spots

Stated plainly rather than papered over.

**Behavior-preserving refactoring** is the one phase with no strong Skill-format option.
`superpowers:test-driven-development` has a REFACTOR step, but it is scoped to tidying
code you have just written while tests are green; `tech-debt-tracker` tracks debt
without walking a safe restructure. Neither covers reshaping existing code that no test
pins. `rohitg00/awesome-claude-code-toolkit` ships a `refactor-engine`, but as slash
commands rather than a Skill. The `development-lifecycle` router states the two
operating rules inline so the phase is not silently skipped.

**Flaky-test diagnosis is better covered than it first appears**, and an earlier version
of this catalog wrongly listed it as a gap. `superpowers:systematic-debugging` bundles
`condition-based-waiting.md` (115 lines), dedicated to the largest single cause: tests
that guess at timing with `sleep`/`setTimeout` and therefore pass locally but fail under
load or in CI. It does not cover test ordering and shared state, unseeded randomness,
unordered collection comparison, or local-versus-CI environment differences; the router
carries the rule for those.

If a good Skill-format option appears upstream for either, it belongs in
`catalog.json` — not reimplemented here.
