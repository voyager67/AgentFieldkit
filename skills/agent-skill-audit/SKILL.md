---
name: agent-skill-audit
description: Validate a skill library for metadata correctness, discoverability, duplicate naming, risky instructions, and portability. Use when adding, reviewing, packaging, or publishing agent skills.
license: MIT
---

# Agent Skill Audit

## Procedure
1. Find each skill folder and confirm it contains one `SKILL.md` with YAML frontmatter and a focused body.
2. Check that `name` uses lowercase letters, digits, and hyphens, matches the directory name, and stays within the standard limit. Check that `description` explains the workflow and trigger conditions without being vague.
3. Look for overlapping triggers, duplicated skills, missing prerequisites, nonportable absolute paths, undocumented scripts, and agent-specific assumptions hidden in generic instructions.
4. Audit instructions and scripts for secret access, data deletion, network calls, external uploads, privilege escalation, destructive commands, and implicit merge/deploy/publish permissions.
5. Check that workflows tell the agent to distinguish observed facts from assumptions and to report commands/tests actually performed.
6. Ensure dependencies and optional resources are documented. Package each skill independently when the target host expects a skill ZIP.
7. Run repository validation and inspect a sample package listing before release.

## Deliverable
A prioritized findings list, invalid metadata list, risk assessment, portability notes, and package/validation results.

## Boundaries
- Do not modify a skill to loosen safety restrictions merely to improve its apparent capability.
- Do not claim compatibility has been tested on a host that was not available.
- Treat natural-language instructions as executable policy: inspect them with the same seriousness as code.
