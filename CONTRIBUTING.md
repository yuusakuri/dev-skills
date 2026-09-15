# Contributing

This repository is a **curation**.
The default contribution is an edit to [`catalog.json`](catalog.json), not a new skill.

## Adding a skill to the curation

1. It must be an existing, publicly published skill in a maintained repository with a clear permissive licence.
2. It must fill a phase gap, or beat an incumbent clearly enough to replace it.
   Two skills matching the same request is a routing hazard — the agent picks between them unpredictably.
3. Add the entry to `catalog.json` with the upstream `repo`, a **40-character commit SHA** as `ref`, the `path` to the skill directory, the install `plugin`, and a one-line `role`.
4. Add it to the phase map in `development-lifecycle/SKILL.md`.
   The validator fails the build if a catalog entry is not routed to.
5. Update `docs/reference/catalog.md` and `NOTICE.md` to match, then run the checks (below).

## Writing a new skill here — the bar

Prefer curating over authoring, and prefer contributing a skill upstream over hosting it here.
A new skill in this repository needs all of:

1. **No existing published skill covers it.** Search the ecosystem first — the awesome lists, the sources in `catalog.json`, and Claude Code's plugin directory.
   This repository previously shipped 18 hand-written skills that all turned out to have established equivalents; they were removed.
2. **It is stack-agnostic.** No required framework, cloud, or vendor.
3. **It has a distinct trigger** that does not collide with a curated skill's.
4. **It encodes judgment, not documentation.**

The `development-lifecycle` router is the one skill hosted here, because a routing map over a specific curation cannot live upstream.

## Checks

```bash
python3 scripts/verify-catalog.py   # every curated ref resolves at its pinned commit
python3 scripts/validate-skills.py  # spec conformance + router covers every entry
./scripts/check-upstream.sh         # pins are immutable commits, tags still agree
```

All three run in CI, and weekly on a schedule so upstream drift surfaces as a failing build rather than a silently wrong map.

## Keeping the catalog and its docs in step

`catalog.json` is the source of truth.
`docs/reference/catalog.md` and `NOTICE.md` restate it for readers and are maintained by hand, so an edit to the catalog is not finished until both are updated in the same commit.

Nothing enforces this yet.
`verify-catalog.py` checks that every entry in `catalog.json` resolves upstream; it does not check that the prose agrees with it.

## Updating a pin

Edit the `ref` in `catalog.json`, then run all three checks.
Review the upstream changelog first: upstream skill *names* are part of the routing table, so a rename breaks the router.
`verify-catalog.py` catches exactly that.
