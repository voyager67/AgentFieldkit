---
name: release-readiness
description: Assess whether a change is ready for a tagged release or deployment. Use before publishing a package, shipping a production build, or announcing a new version.
license: MIT
---

# Release Readiness

## Procedure
1. Identify what is being released, release method, target environment, versioning rules, and person authorized to approve publication.
2. Inspect diff, changelog, version metadata, lockfiles, release notes, migration instructions, supported platforms, and known issues.
3. Run the documented validation suite: tests, type checking, linting, build/package, and security checks relevant to the project.
4. Verify distribution contents: no debug credentials, local paths, temporary datasets, internal notes, build artifacts that should not ship, or unlicensed assets.
5. Check compatibility and rollback: database changes, environment variables, config defaults, API changes, and package installation/uninstallation.
6. Validate release notes against the real diff. Clearly separate new features, fixes, breaking changes, and known limitations.
7. Present a gate decision: ready, blocked, or ready with explicitly accepted risk. Include proof and the owner of unresolved items.

## Approval boundary
Prepare release commands and artifacts, but stop before creating a tag, publishing a package, deploying, or sending external announcements unless the user explicitly authorizes that exact action.

## Deliverable
Checklist of passed/failed/not-run checks, changed version, release notes draft, unresolved risk, rollback path, and the next authorized action.
