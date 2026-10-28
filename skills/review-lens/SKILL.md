---
name: review-lens
description: Review a diff for actionable correctness, security, reliability, and maintainability defects. Use before merging a change or when asked for an independent code review.
license: MIT
---

# Review Lens

## Review method
1. Read the task or issue first; identify the intended behavior and compatibility promises.
2. Inspect the diff and relevant surrounding code. Do not review only the patch if callers or invariants matter.
3. Look for defects in this order: data loss/security, incorrect behavior, broken compatibility, race conditions, poor error handling, performance regressions, then maintainability.
4. Check tests against acceptance criteria. Look for untested branches, assertions that cannot fail, brittle timing, hidden reliance on mocks, and snapshots that obscure behavior.
5. Validate each suspected issue against an actual execution path or invariant. Do not report style preferences as bugs.
6. Consider what happens for empty, malformed, duplicated, stale, unauthorized, or unexpectedly large input where appropriate.

## Finding format
For every finding include:
- **Severity:** Critical / High / Medium / Low
- **Location:** file and line or symbol
- **Condition:** when it occurs
- **Impact:** user-visible or operational consequence
- **Evidence:** why the code causes it
- **Fix direction:** the smallest practical remedy

## Boundaries
- Report findings before praise or summary. If no actionable issue is found, say so and mention the reviewed scope.
- Never fabricate line numbers or imply a test was run when it was not.
- Do not rewrite the patch as part of a review unless asked to fix findings.
