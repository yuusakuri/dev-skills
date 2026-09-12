# Contributing

## The bar for a new skill

A skill belongs here only if it passes all five:

1. **It covers a real lifecycle phase gap.** If `obra/superpowers` or
   `anthropics/skills` already covers it competently, reference theirs instead —
   composing beats writing a worse duplicate.
2. **It is stack-agnostic.** No required framework, cloud, or vendor. A skill that only
   works for one ecosystem belongs in that ecosystem's own collection.
3. **It has a distinct trigger.** The `description` must state *when* to use it, in
   terms that do not collide with an existing skill's trigger. Overlapping triggers are
   worse than a missing skill: the agent picks unpredictably between them.
4. **It encodes judgment, not documentation.** Restating what a tool's manual already
   says adds nothing. The value is in the decision rules, the ordering, and the
   failure modes.
5. **It names its red flags.** The "Red flags" section is where most of the practical
   value lives — the symptoms that mean the practice is being done wrong.

## Conventions

Every `SKILL.md` in this repository:

- lives at `plugins/dev-lifecycle/skills/<name>/SKILL.md`, with `name` in frontmatter
  matching the directory exactly
- has a `description` that begins with the trigger ("Use when…", "Use before…")
- carries `license: MIT` and a `metadata.phase` from the known phase list
- stays under 500 lines; longer material moves to `references/`
- opens with a **core principle** stating the one idea the skill exists to enforce
- closes with **red flags**

## Required when adding a skill

1. Add the skill directory and `SKILL.md`.
2. **Add it to the phase map in `development-lifecycle/SKILL.md`.** The validator fails
   the build if a skill is not routed to — an unrouted skill is one the agent will
   rarely find.
3. Add it to the catalog in `docs/catalog.md` and the table in `README.md`.
4. Run the checks.

## Checks

```bash
python3 scripts/validate-skills.py   # frontmatter, naming, phases, router coverage
./scripts/check-upstream.sh          # pinned upstream refs still resolve
```

Both run in CI. The validator is deliberately strict about frontmatter: a malformed
`SKILL.md` does not fail loudly at runtime, it just silently never triggers.

## Changing upstream pins

See the last section of [NOTICE.md](NOTICE.md). Upstream skill names appear in this
repository's routing table, so check the upstream changelog for renames before bumping.

## Writing style

Skills are read by agents under context pressure. Prefer:

- imperative instructions over description
- tables and checklists over paragraphs
- concrete thresholds over adjectives ("p95 under 300 ms", not "fast")
- one idea per section, with the reason it matters stated once

Avoid restating general knowledge the model already has. Write down the things teams
get wrong repeatedly.
