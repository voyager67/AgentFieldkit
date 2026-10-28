---
name: dependency-care
description: Evaluate dependency updates and vulnerabilities without creating avoidable breakage. Use when upgrading packages, responding to advisories, or cleaning dependency drift.
license: MIT
---

# Dependency Care

## Procedure
1. Identify package manager, lockfile, supported runtime versions, direct versus transitive dependencies, and existing update policy.
2. Determine the reason for the update: security fix, bug fix, feature, compatibility, or maintenance. Find authoritative release notes and advisory details when network access is available.
3. Inspect semver impact, deprecations, peer constraints, native modules, license changes, and minimum runtime requirements.
4. Prefer the smallest version change that resolves the stated problem. Do not combine unrelated dependency churn with application changes.
5. Update manifests and lockfiles through the repository's package manager; never hand-edit generated lock data unless the project explicitly requires it.
6. Run install in the intended mode, relevant tests, type checking, build, and any package-specific smoke test.
7. Summarize packages changed, reason, behavior changes, compatibility concerns, and verification outcomes.

## Boundaries
- Do not run untrusted install scripts, elevate permissions, or point package managers at unknown registries without explicit approval.
- Do not automatically upgrade every package to latest just because an audit command reports updates.
- A clean vulnerability scan does not prove a dependency set is risk-free; disclose tool and database limits.
