---
name: safe-migration
description: Plan and execute a controlled migration of code, schemas, frameworks, or configuration while preserving a rollback path. Use when changing formats, APIs, databases, runtimes, or major dependencies.
license: MIT
---

# Safe Migration

## Procedure
1. Define the source state, target state, users affected, deadline, data volume, downtime constraints, and success criteria.
2. Inspect all readers/writers, external consumers, scheduled jobs, and hidden operational assumptions.
3. Classify the migration as reversible, forward-only, or data-destructive. Design a backup and rollback plan before implementation.
4. Prefer staged migration: add compatible support, backfill or dual-write if required, verify parity, switch readers, monitor, then remove old support in a separate approved step.
5. Create dry-run or preview mode for any bulk operation. Report the records/files/resources that would change before applying them.
6. Add invariants and reconciliation checks: row counts, checksums, referential integrity, schema validity, and representative queries.
7. Test interruption and rerun behavior. Ensure the migration is idempotent or clearly prevents accidental repeated execution.
8. Document deployment order, feature flags, operational signals, rollback trigger, and cleanup steps.

## Deliverable
Provide a phased checklist, compatibility matrix, preflight checks, rollback plan, and exact verification evidence.

## Boundaries
- Never run a destructive or production migration without explicit authorization and a verified backup/restore path.
- Never assume rollback is safe after irreversible data transformation.
- Keep implementation and irreversible cleanup in separate steps whenever practical.
