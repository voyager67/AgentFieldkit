---
name: context-handoff
description: Create a reliable handoff note so another engineer or coding agent can continue work without redoing exploration. Use before switching sessions, handing off a long task, or pausing midway.
license: MIT
---

# Context Handoff

## Procedure
1. Summarize the user's goal and the acceptance criteria; keep requirements separate from assumptions.
2. Record the current repository and branch, relevant files, important symbols, current diff status, and any uncommitted user work.
3. List commands run and exact outcomes. Clearly distinguish tested facts, inferred explanations, and open hypotheses.
4. Note decisions made and alternatives rejected with brief reasons. Include links or paths to source evidence where possible.
5. Describe remaining work in a prioritized order, with a concrete next action rather than generic reminders.
6. Record safety boundaries: files/data not to modify, external actions not yet authorized, secrets to avoid, and any concurrent work or shared resource constraints.
7. Keep it short enough to rehydrate quickly; link detailed logs instead of pasting them.

## Template
- Goal / acceptance criteria
- Current state
- Files and key decisions
- Verification performed
- Remaining work (ordered)
- Risks / unknowns
- Safe next command or action

## Boundaries
- Never claim work was saved or committed if it was not.
- Never include credentials, tokens, private user data, or unnecessary personal information in the handoff.
- If repository state changed outside the agent's knowledge, tell the next agent to inspect status before editing.
