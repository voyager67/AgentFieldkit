---
name: build-rescue
description: Investigate and repair a failing build or CI job from logs to a verified fix. Use when compilers, linters, tests, containers, or CI workflows break.
license: MIT
---

# Build Rescue

## Procedure
1. Capture the exact failing command, exit code, full relevant log context, commit, OS/runtime, and dependency lock state.
2. Determine whether the failure is deterministic, environment-only, network-related, flaky, or introduced by a code change.
3. Reproduce locally or in the closest equivalent environment. If reproduction differs, document the gap.
4. Locate the earliest meaningful error, not just the final cascade. Check configuration, version drift, missing artifacts, permissions, and concurrency assumptions.
5. Change one cause at a time. Avoid bypassing the build step, suppressing diagnostics, disabling tests, or weakening type/lint checks without a justified migration plan.
6. Rerun the failing job, then the relevant broader checks. For flaky failures, repeat enough times to test the hypothesis and report the repeat count.
7. Inspect workflow changes for secret exposure, unsafe permissions, unpinned actions, cache poisoning, and accidental release/deploy triggers.

## Deliverable
Root cause, minimal repair, exact successful commands or CI run IDs, checks not run, and any environment-specific caveats.

## Boundaries
- Do not print CI secrets or include tokens in logs.
- Do not rerun a workflow that deploys, publishes, charges, or mutates production unless authorized.
- Never mark a failure resolved just because a retry passed once; assess flaky behavior honestly.
