---
name: failure-forensics
description: Diagnose a reproducible software failure by narrowing symptoms to a root cause and verifying the repair. Use for crashes, incorrect results, flaky tests, and hard-to-explain regressions.
license: MIT
---

# Failure Forensics

## Procedure
1. Capture the exact symptom: error message, stack trace, inputs, environment, frequency, and when it started. Redact secrets and personal data.
2. Reproduce the failure with the smallest reliable command or test. If reproduction is impossible, say so and gather the best available evidence.
3. Form a few competing hypotheses. Rank them by consistency with observed evidence, not by familiarity.
4. Trace values from input to failure. Inspect recent changes, boundary conditions, async ordering, state mutation, configuration, and dependency behavior where relevant.
5. Use a minimal experiment to falsify the leading hypothesis. Change one variable at a time when practical.
6. Fix the root cause rather than masking the symptom. Add a regression test that would have caught it.
7. Repeat the reproduction and run neighboring tests. Inspect logs and output to ensure no new error path was introduced.

## Report
- Reproduction steps and observed result
- Root cause, with specific file/symbol evidence
- Minimal repair
- Regression test and verification results
- Remaining uncertainty, if any

## Boundaries
- Do not delete user data, reset a database, clear caches with side effects, or change production state to diagnose a local bug without explicit authorization.
- Preserve failing artifacts and logs when they are needed to understand the issue.
- Treat timing correlation as a clue, not proof of causation.
