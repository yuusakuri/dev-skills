---
name: data-migration-safety
description: Use when changing a database schema, altering stored data shape, backfilling or transforming existing records, or moving data between stores - covers expand/contract sequencing, zero-downtime deploys, safe backfills, locking hazards, and rollback. Use before writing the migration, not after.
license: MIT
metadata:
  collection: dev-skills
  phase: "4-implementation"
---

# Data Migration Safety

**Core principle:** code can be rolled back. Data usually cannot. A bad deploy is an
outage; a bad migration is a data-loss incident, and the backup you have not tested
restoring is not a backup.

## Two rules that prevent most incidents

1. **The old code and the new code will run at the same time.** During any rolling
   deploy, both versions talk to one database. A schema the old code cannot read
   breaks production before the new code finishes rolling out — and it breaks the
   rollback path too.
2. **Destructive and constructive steps never ship together.** Adding is safe.
   Removing is not. They belong to different releases, with verification in between.

## Expand / migrate / contract

The only reliably safe sequence for changing a schema in a live system. Each phase is
a **separate deploy**.

### Phase 1 — Expand (additive only)

Add the new column, table, or index. New columns are nullable or have a default.
Write nothing that the old code cannot tolerate. Deploy, and confirm the old code is
still healthy.

### Phase 2 — Write both

Deploy code that writes to **both** old and new locations, and still reads the old one.
Now every new record is correct in both places. Rollback is still free.

### Phase 3 — Backfill

Migrate historical rows in **batches** (see below), leaving new writes to the
dual-write path. Verify: count rows, compare checksums, sample and compare records.

### Phase 4 — Read new

Deploy code that reads the new location, still writing both. Watch error rates and
data-quality metrics. **This is the step to roll back from if anything is wrong** —
the old data is still being maintained, so rollback is safe.

### Phase 5 — Contract

Only after the new path has been healthy for long enough to trust it: stop writing the
old location, then, in a later release, drop it. Before dropping anything, confirm from
logs or query statistics that nothing reads it.

Shortcut this sequence only when the table is provably not in use, or the system is
genuinely offline and you have a tested restore.

## Backfills

- **Batch it.** Small chunks with a bounded key range, a short pause between them.
  A single `UPDATE` over a large table locks rows, blows up the transaction log or
  replication lag, and cannot be stopped cleanly.
- **Make it resumable and idempotent.** Track progress durably; re-running a batch must
  be harmless. Backfills get interrupted — assume it.
- **Make it throttleable and killable.** Someone must be able to slow or stop it during
  a traffic spike without losing progress.
- **Never backfill inside the schema migration.** Schema changes should be fast; a
  backfill is a job, run and monitored separately.
- **Log what it did**, including rows it skipped and why.

## Locking hazards

Know what your database actually locks, on your version, at your table size — the
answer differs by engine and by release, so **check the documentation for yours**
rather than trusting a habit formed elsewhere.

Usually cheap: adding a nullable column; creating an index concurrently; adding a
constraint as not-validated, then validating separately.

Usually dangerous on a large table: adding a column with a non-constant default;
changing a column type; adding an index non-concurrently; adding a foreign key or
check constraint that validates immediately; anything requiring a full table rewrite.

Always set a **lock timeout** on migrations, so a migration that cannot acquire its
lock fails fast instead of queueing every query behind it and taking the site down.
Test the migration against a realistic copy of production data — a change that is
instant on 100 rows can take an hour on 100 million.

## Before you run it

- [ ] Backup exists, is recent, and the **restore has been tested** — an untested
      backup is a hope
- [ ] The migration is reversible, or the irreversibility is explicit and accepted
- [ ] A `down` path exists and has been run, or you have documented why there is none
- [ ] Timed against production-scale data
- [ ] Lock timeout and statement timeout set
- [ ] Old code tested against the new schema (the rolling-deploy overlap)
- [ ] Batch size, throttle, and kill switch decided for any backfill
- [ ] Verification queries written *before* the run — row counts, checksums, spot checks
- [ ] Someone is watching replication lag, error rate, and latency during the run

## Rollback thinking

Ask "how do I undo this?" before you run it, not while it is failing.

A dropped column cannot be restored by a migration — only from a backup, losing
everything written since. That asymmetry is the whole reason for expand/contract: it
keeps you in the reversible region until the new path is proven.

For genuinely irreversible steps, take a verified snapshot immediately before, and say
explicitly who approved proceeding without a rollback path.

## Red flags

- **One migration that adds the new column, backfills it, and drops the old one.**
  Three phases in one deploy, and no rollback exists after it.
- **`DROP` or `DELETE` in the same release that adds the replacement.**
- **A migration with no `down` and no note explaining why.**
- **Tested only on an empty dev database.** You have measured nothing.
- **"It's just a rename."** A rename is a drop plus an add to every client that has not
  deployed yet.
- **A backfill run by hand from someone's laptop**, with no logs and no resume point.
