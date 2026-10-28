---
name: repo-scout
description: Map an unfamiliar codebase before changing it. Use when joining a repository, debugging an unclear subsystem, or planning work that depends on understanding project structure.
license: MIT
---

# Repo Scout

## Outcome
Produce a short, evidence-backed map of the repository that helps the next task start in the right place without making changes.

## Procedure
1. Read the project entry points first: README, package or build manifests, contribution guidance, agent instructions, CI workflows, and test configuration.
2. Inspect the top-level tree, then follow imports and scripts from the likely application entry point. Avoid dumping huge directories or generated files.
3. Identify the main runtime, important modules, public interfaces, configuration sources, data stores, test commands, lint/type-check commands, and build/deploy paths.
4. Trace one representative request or execution path end-to-end. Cite concrete paths and symbols, not guesses.
5. Note conventions that already exist: error handling, logging, dependency injection, naming, test fixtures, and architectural boundaries.
6. List unknowns separately from findings. Never infer that a feature exists merely because its name appears in documentation.

## Deliverable
Return:
- **System map:** entry points and key directories.
- **Change hotspots:** likely files for the user's task, with reasons.
- **Verification commands:** exact commands discovered in project files.
- **Constraints and unknowns:** risks, missing docs, unverified assumptions.

## Boundaries
- Read-only by default. Do not edit files, install packages, run migrations, or access production systems during reconnaissance.
- Do not print secrets. If a credential file appears, report its path and stop inspecting its contents.
- Keep the map concise enough to be useful in a later session.
