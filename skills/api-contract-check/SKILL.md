---
name: api-contract-check
description: Check API and schema changes for compatibility with existing clients and stored data. Use when editing public endpoints, CLI flags, event payloads, database schemas, or serialized formats.
license: MIT
---

# API Contract Check

## Procedure
1. Identify the contract: routes, method, status codes, auth, request/response schemas, CLI behavior, event topics, database fields, or file formats.
2. Search for callers and consumers. Include generated clients, tests, docs, examples, scripts, downstream jobs, and stored historical data.
3. Classify each change as additive, behavior-changing, or breaking. Check nullability, defaults, enum expansion, ordering, error semantics, pagination, and numeric/string representation.
4. For database migrations, consider both old-code/new-schema and new-code/old-schema compatibility during rolling deployment.
5. Prefer additive transitions: introduce a new field or endpoint, migrate consumers, observe adoption, then remove the old path only through an approved deprecation plan.
6. Add contract tests or fixtures representing real documented behavior. Avoid relying only on implementation-specific unit tests.
7. Update versioning, changelog, examples, and migration notes when the public contract changes.

## Deliverable
Provide a compatibility matrix: old client/new server, new client/old server, existing data/new code, and rollback path.

## Boundaries
- Do not run schema migrations against production or delete legacy data without explicit authorization.
- Treat undocumented behavior as uncertain; search usage before declaring it safe to break.
