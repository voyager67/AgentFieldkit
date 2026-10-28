---
name: parallel-task-design
description: Break a multi-part engineering task into safely parallel work units with clear ownership and integration points. Use when several agents or contributors can work concurrently.
license: MIT
---

# Parallel Task Design

## Procedure
1. Map the requested outcome, shared files, dependencies, sequence constraints, and final integration tests.
2. Split work by independent deliverable or subsystem rather than by arbitrary file count. Each task needs a clear owner, boundaries, input assumptions, and completion criteria.
3. Identify conflicts: shared manifests, lockfiles, global types, generated code, schemas, snapshots, config, and common abstractions.
4. Establish contracts before parallel implementation. Agree on names, interfaces, types, file ownership, and fixture formats early.
5. Keep dependent tasks sequential. Parallelize independent research/tests/docs only when their results will not be invalidated by upstream decisions.
6. Ask each contributor to report touched files, decisions, commands/tests run, unresolved assumptions, and any edits made outside their scope.
7. Integrate one workstream at a time. Inspect the combined diff, reconcile contradictions, run cross-workstream tests, and remove duplicate or abandoned code.

## Deliverable
Workstream table with owner, input, scope, files/contracts, acceptance criteria, dependencies, and integration test.

## Boundaries
- Do not have multiple agents edit the same file concurrently unless the environment explicitly supports conflict-free coordination.
- Do not assume a successful subtask means the integrated branch works.
- Preserve all contributors' useful work; inspect repository state before reverting or overwriting.
