---
name: sql-integrity-check
description: Review SQL queries and data-model changes for correctness, access scope, safe parameterization, and performance. Use when writing joins, filters, migrations, reports, or analytics queries.
license: MIT
---

# SQL Integrity Check

## Procedure
1. Identify the database engine, schema constraints, expected row grain, key relationships, indexes, and caller permissions.
2. For every query, state the intended output grain. Verify joins cannot silently multiply rows and filters preserve intended inclusions/exclusions.
3. Confirm user-controlled values are bound parameters, not concatenated into SQL. Review dynamic identifiers separately because they often need allowlists.
4. Check NULL semantics, timezone/date boundaries, numeric precision, collation, case sensitivity, pagination stability, and aggregate behavior.
5. Inspect query plans or EXPLAIN output on representative non-production data when performance matters. Avoid full table scans or expensive locks without understanding scale.
6. For migrations, verify constraints, backfill logic, idempotency, and compatibility with old/new application versions.
7. Test edge cases: no rows, duplicate keys, missing foreign keys, boundary dates, and values that could alter the query structure.

## Deliverable
Explain expected row grain, correctness risks, access-control assumptions, relevant plan/index observations, and tests performed.

## Boundaries
- Do not execute destructive statements or real-data exports without explicit authorization.
- Do not expose customer rows or secrets in logs or examples.
- Treat a fast query as incorrect if it returns the wrong entities or hides duplicates.
