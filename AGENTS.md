# Agent guidance for this repository

- This repository is a library of portable Agent Skills. Canonical skill sources live in `skills/<name>/SKILL.md`.
- Prefer small, focused skills with clear triggers and explicit safety boundaries.
- Validate changes with `python scripts/validate_skills.py`.
- The scripts use the Python standard library; do not add dependencies without a clear need.
- Never remove attribution or license notices from third-party material. New AgentFieldkit content should be independently written.
- Do not execute external side effects such as publishing, deployment, destructive migration, or secret transmission without explicit user authorization.
