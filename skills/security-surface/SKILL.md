---
name: security-surface
description: Perform a focused threat review of code, APIs, configuration, and dependencies. Use when a change touches authentication, authorization, uploads, external input, secrets, payments, or sensitive data.
license: MIT
---

# Security Surface

## Procedure
1. Sketch the relevant trust boundaries: user, browser, service, background job, database, third party, and operator.
2. Trace untrusted input through parsing, validation, authorization, storage, rendering, and execution.
3. Verify authentication and authorization separately. Confirm access is checked server-side at the resource boundary, not only in the UI.
4. Inspect secret handling, logs, error messages, cryptographic use, session/cookie settings, rate limits, file paths, uploads, URL fetching, command execution, and injection risks as applicable.
5. Review dependency and configuration changes for unsafe defaults or newly exposed capabilities.
6. Check that sensitive data is minimized, access-scoped, and retained only as needed. Verify errors fail closed when that is the safe behavior.
7. Propose a minimal fix and a test that proves the attack path is closed. Use safe local fixtures rather than real secrets or live targets.

## Report
Separate confirmed vulnerabilities from defense-in-depth suggestions. Include attack preconditions, impact, affected boundary, and verification evidence.

## Boundaries
- Never exfiltrate secrets, probe systems outside the authorized scope, or run destructive exploit payloads.
- Do not claim that a quick review is a formal penetration test or comprehensive security certification.
- Keep any discovered secret out of the report; identify its location and recommend rotation through the proper owner.
