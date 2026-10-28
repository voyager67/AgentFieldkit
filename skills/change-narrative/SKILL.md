---
name: change-narrative
description: Write a useful pull request or change summary that leads with the problem, impact, and proof. Use when preparing a handoff, code review request, release note, or engineering change record.
license: MIT
---

# Change Narrative

## Procedure
1. Identify the user or operational problem in one sentence. Explain why the change matters before listing files.
2. Summarize behavior before and after the change. State what deliberately remains unchanged.
3. Include the most important design choice and any trade-off a reviewer should understand.
4. List tests and checks that were actually run with results. Mention skipped checks and why.
5. Call out schema/config/API compatibility, rollout steps, migrations, or monitoring needs when relevant.
6. Link issue, benchmark, screenshot, or log evidence when available. Do not create fake links or metrics.
7. Keep the message scannable and proportional to the diff.

## Suggested structure
**Problem** — the motivating failure or user need.

**Change** — key behavior changes, not a file-by-file inventory.

**Proof** — tests/commands/results and known limitations.

**Risk & rollout** — compatibility, migration, flag, rollback, or monitoring needs.

## Boundaries
- Never claim “fully tested,” “production-ready,” or “no risk” without evidence.
- Never hide a known regression to make a change easier to merge.
- Avoid promotional language; the purpose is to help the reviewer make a good decision.
