---
name: test-driven-change
description: Implement a behavior change with tests that demonstrate the requirement and protect regressions. Use for bug fixes, new features, and changes with observable inputs and outputs.
license: MIT
---

# Test-Driven Change

## Operating rule
A test is evidence only if it can fail for the defect or missing behavior being addressed. Do not add tests that merely repeat the implementation.

## Procedure
1. Find the project's existing test framework and nearest representative tests. Preserve local conventions.
2. Write or adapt the smallest test that captures the desired behavior. For a reported bug, make sure it fails before the fix when practical.
3. Run the targeted test and record the initial result. If it does not fail, explain why and improve the test.
4. Implement the smallest production change that makes the test pass. Avoid unrelated refactors in the same diff.
5. Add edge cases around boundaries, invalid input, empty states, errors, and backwards compatibility where relevant.
6. Run targeted tests, then the appropriate broader suite, formatter, linter, and type checker when available.
7. Inspect the final diff for changed behavior not covered by tests.

## Evidence to report
State which tests were run, their actual results, and any checks not run. Include commands when useful.

## Boundaries
- Do not weaken assertions, skip failing tests, or mock away the behavior under test just to obtain a green result.
- Do not claim a test passed if it was not executed.
- If the repository has no test infrastructure, propose the smallest useful check and disclose the limitation.
