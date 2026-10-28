# Contributing to AgentFieldkit

Thanks for improving AgentFieldkit. Keep every skill specific, portable, evidence-driven, and safe by default.

## Add a skill

1. Create `skills/<lowercase-hyphen-name>/SKILL.md`.
2. Add YAML frontmatter with `name`, `description`, and optional `license`.
3. Make the folder name match `name`. The description should name the task and its trigger conditions.
4. Give the skill a repeatable procedure, a concrete deliverable, and explicit safety boundaries.
5. Avoid provider-specific tools unless the skill explains a fallback and states the prerequisite.
6. Keep secrets and private production data out of examples. Do not include network/install scripts unless they are necessary, transparent, and safely bounded.
7. Run `python scripts/validate_skills.py` and inspect the diff.

## Quality bar

- One focused job per skill; do not create near-duplicates.
- Claims must be verifiable; distinguish findings, assumptions, and recommendations.
- Tests must be reported honestly. Do not instruct agents to bypass failing checks to obtain a green result.
- External and irreversible actions require explicit authorization.
- Do not include copied third-party skill text unless its license and required attribution are compatible and preserved.

## Pull request checklist

- [ ] Metadata validates.
- [ ] Trigger conditions are clear.
- [ ] Procedure has actionable steps, not vague advice.
- [ ] Output format is specified.
- [ ] Security, privacy, and authorization boundaries are explicit.
- [ ] Documentation/agent compatibility claims are accurate.
