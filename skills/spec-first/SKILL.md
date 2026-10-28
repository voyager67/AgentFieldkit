---
name: spec-first
description: Turn a feature request into testable acceptance criteria and a small implementation plan before editing. Use when requirements are ambiguous, a task spans several files, or a change may affect existing behavior.
license: MIT
---

# Spec First

## Outcome
A compact implementation brief that makes the requested behavior observable and defines what must remain unchanged.

## Procedure
1. Restate the requested outcome in plain language. Separate the user's goal from any proposed implementation.
2. Inspect the relevant code and docs before proposing changes. Reuse repository conventions where possible.
3. List acceptance criteria that can be checked through tests, commands, UI behavior, logs, or documented output.
4. Record non-goals and compatibility constraints. Call out assumptions that would materially change the design.
5. Identify the smallest safe change set. Group files into implementation, tests, and docs.
6. Define verification in advance: the targeted test, broader regression checks, and any manual check that cannot be automated.
7. For a large task, split work into independent slices with a clear integration point. Do not create artificial subtasks for a trivial change.

## Deliverable
Use a short brief:
- Goal
- Acceptance criteria
- Non-goals
- Key files and design choice
- Risks / assumptions
- Verification plan

## Boundaries
- Ask a focused question only when a missing decision blocks safe progress. Otherwise state a reversible assumption and continue.
- Do not silently broaden scope or redesign unrelated systems.
- Planning is not permission to deploy, spend money, contact people, or make destructive changes.
