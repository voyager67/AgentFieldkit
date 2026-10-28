---
name: multi-agent-crosscheck
description: Use independent reviewers or model providers to challenge a plan or diff and synthesize evidence-based disagreement. Use for high-impact, ambiguous, or research-heavy decisions when multiple agents are actually available.
license: MIT
---

# Multi-Agent Crosscheck

## When to use
Invoke multiple agents only when the decision has enough uncertainty or impact to justify the latency, token cost, and coordination burden. A single well-scoped review is better for a trivial change.

## Procedure
1. Give each reviewer the same question, relevant evidence, constraints, and output schema. Ask them to analyze independently before showing one review to another.
2. Assign genuinely distinct lenses where possible: correctness, security, compatibility, performance, or user experience.
3. Request concrete claims with file/symbol/test evidence and confidence. Ask reviewers to distinguish observation from assumption.
4. Normalize findings into a shared table. Merge duplicates, preserve meaningful disagreement, and verify claims against source code or reproducible tests.
5. Resolve conflicts with evidence, not majority vote. A model count does not establish truth; two models can share the same blind spot.
6. Record which providers/models/tools were actually used, any unavailable reviewer, and the total scope of material shared with them.
7. Produce one decision and a short rationale, or escalate unresolved high-impact disagreement to a human.

## Output
Question, reviewers and lenses, common findings, disputed findings, evidence checked, final recommendation, remaining risk, and cost/latency note when material.

## Boundaries
- Do not send private source code, secrets, personal data, or proprietary context to an external provider unless the user has authorized that data flow.
- Do not pretend a subagent or provider was called if the current host cannot invoke it.
- Never auto-approve, merge, deploy, or publish solely because agents agree.
