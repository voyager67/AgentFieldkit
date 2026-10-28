---
name: docs-sync
description: Bring documentation, examples, and configuration guides into agreement with the actual code. Use after behavior changes or when instructions may have drifted.
license: MIT
---

# Documentation Sync

## Procedure
1. Find documentation entry points, API references, README instructions, examples, tutorials, CLI help, config samples, and changelog conventions.
2. Verify every claim against current code, tests, or executable commands. Flag references that cannot be verified.
3. Update the smallest set of docs that fully explains user-visible behavior: what changed, how to use it, constraints, errors, and migration steps.
4. Prefer runnable examples. When appropriate, execute code snippets or use a documentation build/test command.
5. Ensure defaults, environment variable names, flags, paths, supported versions, and output formats match implementation.
6. Remove obsolete instructions without deleting important historical migration context.
7. Check links and headings using existing tools if available. Do not introduce new dependencies just for a minor documentation check.

## Deliverable
Summarize changed pages and cite checks actually run. Explicitly state any external links you could not validate.

## Boundaries
- Never invent capabilities, performance numbers, release dates, or guarantees.
- Do not write documentation that claims an implementation is complete when it remains partial.
- Avoid duplicating a large block of source documentation into several pages; prefer one canonical explanation.
