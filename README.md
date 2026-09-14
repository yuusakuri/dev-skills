# dev-skills

**A curated, verified map of the best community [Agent Skills](https://agentskills.io/specification)
for the whole software lifecycle — requirements definition through production operations.**

This repository **curates existing published skills. It copies none of them.** Every
skill it routes to lives in, and is maintained by, its own repository; this repo
contributes the map, the pinned versions, and the verification that the map is still
true.

## Sources

All five are established, permissively licensed, public projects:

| Repository | Stars | License | Format | Curated |
|---|---|---|---|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | 285.6k | MIT | Agent Skills | 12 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 175.9k | Apache-2.0 | Agent Skills | 4 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 93.8k | MIT | Agent Skills | 9 |
| [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) | 25.9k | MIT | Agent Skills | 26 |
| [`mohitagw15856/pm-claude-skills`](https://github.com/mohitagw15856/pm-claude-skills) | 1.4k | MIT | Agent Skills | 5 |

**56 skills across 11 phases**, each pinned to a specific upstream commit and verified
to resolve. Star counts are as shown on each repository page at the time of curation.

## What this repository actually contains

Only three things — and deliberately nothing else:

1. **[`catalog.json`](catalog.json)** — the machine-readable curation: which upstream
   skill owns which lifecycle phase, at which pinned commit.
2. **One skill, [`development-lifecycle`](plugins/dev-lifecycle/skills/development-lifecycle/SKILL.md)**
   — a router. It owns no practice of its own; it works out which phase a task is in and
   hands off to the community skill that covers it.
3. **[`scripts/install-skills.py`](scripts/install-skills.py)** — copies the curated
   skills into a project's `.claude/skills/`, fetched from their own upstreams at the
   pinned commits, with attribution and licence texts written alongside them.
4. **[`scripts/verify-catalog.py`](scripts/verify-catalog.py)** — fetches all 56
   referenced `SKILL.md` files from their pinned commits, and checks that every
   documented install command names a marketplace and plugin that exist. This is the
   only way a curation can rot, so it runs in CI.

## Why curate instead of fork

- Upstream skills keep receiving their authors' fixes; a fork freezes them.
- Cross-references keep resolving. Superpowers skills reference each other as
  `superpowers:test-driven-development`; re-hosting them under another plugin name
  breaks that.
- Licence and attribution stay simple, because nothing is redistributed.

## Install

There are two ways in, and they trade off differently. **For a team project, use the
first one.**

| | Copy into the repo | Install plugins |
|---|---|---|
| Setup | one command, by one person | one command, by one person |
| **What each teammate does** | **nothing** | runs `claude plugin install` once, per plugin |
| Works in | Claude Code, Codex, Cursor, OpenCode (`--agents all`) | Claude Code |
| Offline | yes | no |
| Staying current | re-run the installer | automatic |
| Repo size | ~1.7 MB for the core set | nothing added |
| Licence duty | you are redistributing (handled for you) | none |

### Into a repository, for the whole team (recommended)

Skills committed under `.claude/skills/` load automatically for anyone who clones the
repository. There is no marketplace and no per-developer step.

```bash
git clone https://github.com/yuusakuri/dev-skills
python3 dev-skills/scripts/install-skills.py --project /path/to/your-project

cd /path/to/your-project
git add .claude/skills && git commit -m "Add curated agent skills"
```

That is the whole setup. Everyone who pulls now has the skills.

The default is a **core set of 20 skills** covering every phase once. Options:

```bash
--list             # show what would be installed, change nothing
--full             # all 56
--skills a,b,c     # pick exactly these
--agents all       # install for every supported agent, not just Claude Code
```

The installer fetches each skill from its own upstream repository at the commit pinned
in [`catalog.json`](catalog.json), using a sparse checkout so it pulls only the files it
needs — about 9 seconds for the core set. Re-run it to update. It also writes
`.claude/skills/.dev-skills.json` recording the exact commit behind every skill, so the
result is reproducible and auditable.

**Licensing is handled.** Committing these skills into your repository is
redistribution, which MIT and Apache-2.0 both permit but require notices for. The
installer writes `ATTRIBUTION.md` (every skill, its upstream, its commit, its licence)
and fetches each upstream `LICENSE` into `.claude/skills/licenses/`. Commit those too.

### As plugins, for yourself

Lighter on the repository, heavier on each person. Nothing is copied, and updates arrive
on their own.

```bash
/plugin install superpowers@claude-plugins-official      # already registered

/plugin marketplace add yuusakuri/dev-skills
/plugin install dev-lifecycle@dev-skills

/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills

/plugin marketplace add alirezarezvani/claude-skills
/plugin install engineering-advanced-skills@claude-code-skills
/plugin install engineering-skills@claude-code-skills
/plugin install a11y-audit@claude-code-skills
/plugin install security-guidance@claude-code-skills

/plugin marketplace add mohitagw15856/pm-claude-skills
/plugin install pm-engineering@pm-claude-skills
/plugin install pm-essentials@pm-claude-skills
/plugin install pm-security@pm-claude-skills
/plugin install pm-delivery@pm-claude-skills
```

Every marketplace and plugin name above is checked against the upstream's own
`.claude-plugin/marketplace.json` by `scripts/verify-catalog.py`, so these commands
cannot silently rot.

To declare the plugins for a project rather than installing them yourself:

```bash
python3 scripts/gen-project-settings.py --write /path/to/your-project
```

That merges `extraKnownMarketplaces` and `enabledPlugins` into the project's
`.claude/settings.json`. Be aware of the catch: committing that file registers the
marketplaces, but Claude Code (v2.1.195+) **does not auto-install plugins from an
external source** — each developer still runs the install commands once
(`gen-project-settings.py --commands` prints them). That step is why the copy-into-repo
route above is recommended for teams.

### Point your agent instructions at the router

Either way, add this to the project's `CLAUDE.md`:

```markdown
Start with the `development-lifecycle` skill to identify the phase and the skill that
owns it. Scale the process to the change: trivial fixes go straight to implementation
and verification; anything touching <the risky areas of this project> requires a threat
model and an ADR.

Test command: <command>   Decisions: docs/decisions/   Requirements: docs/requirements/
```

Verify it took by asking *"Which skill covers deciding whether to ship a release?"* —
the answer should be `ship-gate`.

### Other agents

Agent Skills are a portable format, and nothing in this curation is Claude-specific:
every skill is a directory with a `SKILL.md`. Only the directory an agent reads differs,
so the installer writes whichever ones you ask for.

```bash
python3 dev-skills/scripts/install-skills.py --project . --agents all
```

| Agent | Directory | |
|---|---|---|
| Claude Code | `.claude/skills/` | default |
| Codex (and any `AGENTS.md` runtime) | `.agents/skills/` | `--agents codex` |
| Cursor | `.cursor/skills/` | `--agents cursor` |
| OpenCode | `.opencode/skills/` | `--agents opencode` |

The directories hold identical copies rather than symlinks, because symlinks are
unreliable on Windows checkouts. That costs nothing in the repository: git stores
content by hash, so the same skill committed to four directories is one blob with four
tree entries. Installing 3 skills for all four agents produced 40 tracked files from 10
unique blobs.

Gemini CLI installs skills itself, so point it at an upstream rather than copying:

```bash
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills
```

The [skills CLI](https://github.com/vercel-labs/skills) covers 70+ other agents one
skill at a time:

```bash
npx skills add addyosmani/agent-skills --skill code-simplification
```

Always take skills from the repository that authors them, not from a mirror — see
[NOTICE.md](NOTICE.md#why-origins-not-mirrors).

Per-phase install targets: [docs/catalog.md](docs/catalog.md). More on adoption:
[docs/adoption.md](docs/adoption.md).

## How to use it

Start with **`development-lifecycle`**. It routes, and it scales the process to the
work — a typo does not get a requirements document:

| Task size | Phases |
|---|---|
| Trivial (typo, obvious one-liner) | implement → verify |
| Small (contained, reversible) | requirements → implement → verify → review |
| Standard (a new feature) | orientation → requirements → design → plan → implement → verify → review → release |
| High-stakes (data model, auth, money, public API) | every phase; threat model and ADR mandatory |

## Coverage

| Phase | Skills |
|---|---|
| **0 · Orientation** | `codebase-onboarding` |
| **1 · Requirements** | `brainstorming` · `prd-template` · `epic-design` |
| **2 · Design** | `senior-architect` · `architecture-decision-record` · `api-design-reviewer` · `database-schema-designer` · `threat-model` · `frontend-design` · `tech-stack-evaluator` · `documentation-and-adrs` |
| **3 · Planning** | `writing-plans` · `senior-qa` · `using-git-worktrees` · `constraint-driven-development` |
| **4 · Implementation** | `test-driven-development` · `tdd-guide` · `executing-plans` · `subagent-driven-development` · `dispatching-parallel-agents` · `migration-architect` · `tech-debt-tracker` · `mcp-builder` · `env-secrets-manager` · `security-and-hardening` · `code-simplification` · `source-driven-development` |
| **5 · Quality** | `systematic-debugging` · `chaos-engineering` · `performance-optimization` · `ci-cd-and-automation` |
| **6 · Verification** | `verification-before-completion` · `webapp-testing` · `a11y-audit` |
| **7 · Review** | `requesting-code-review` · `receiving-code-review` · `pr-review-expert` · `senior-security` · `security-guidance` · `dependency-auditor` · `adversarial-reviewer` |
| **8 · Release** | `observability-designer` · `slo-architect` · `runbook-generator` · `finishing-a-development-branch` · `ship-gate` · `changelog-generator` · `launch-readiness` · `feature-flags-architect` · `deprecation-and-migration` |
| **9 · Operations** | `incident-commander` · `incident-response` · `incident-postmortem` |
| **Meta** | `development-lifecycle` · `skill-creator` · `context-engineering` |

Phase-by-phase rationale and handoffs: [docs/lifecycle.md](docs/lifecycle.md).

## Known thin spots

Stated rather than papered over: **behavior-preserving refactoring** and **flaky-test
diagnosis** have no strong Skill-format option upstream — the nearest options
(`refactor-engine`, `ci-debugger`) are slash commands. The router states the operating
rule for both inline so the phase is not silently skipped. See
[docs/catalog.md](docs/catalog.md#known-thin-spots).

## Maintenance

```bash
python3 scripts/verify-catalog.py   # all 57 upstream refs still resolve
python3 scripts/validate-skills.py  # spec conformance + router covers every catalog entry
./scripts/check-upstream.sh         # pinned refs are immutable, not moving branches
```

All three run in CI on every push, and weekly on a schedule to catch upstream drift.

## Licence

This repository's own content (the router skill, catalog, scripts, docs) is MIT —
see [LICENSE](LICENSE). Curated skills remain under their own repositories' licences;
see [NOTICE.md](NOTICE.md).

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
