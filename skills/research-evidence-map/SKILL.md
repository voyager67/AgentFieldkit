---
name: research-evidence-map
description: Turn a technical research question into a traceable evidence map with source quality, uncertainty, and actionable next experiments. Use for model architecture choices, benchmark claims, library selection, and unfamiliar technical topics.
license: MIT
---

# Research Evidence Map

## Procedure
1. Frame the question and decision it must support. Distinguish background curiosity from a choice that changes implementation.
2. Search authoritative sources first: original papers, official documentation, model cards, release notes, benchmark definitions, and source code. Use community reports as useful but lower-confidence context.
3. Record publication/release dates and the date of the measured event separately. Check whether information applies to the exact model/version/hardware being considered.
4. Extract claims into a table: claim, evidence, source, date/version, applicability, confidence, and counterevidence.
5. Separate direct measurements from author claims, marketing statements, extrapolation, and your own inference.
6. Identify missing comparisons, benchmark contamination risks, undisclosed settings, and reproducibility gaps.
7. End with the smallest experiment or code inspection that could change the decision. State what evidence would reverse the recommendation.

## Deliverable
Question, decision criteria, evidence table, uncertainty and counterarguments, recommendation, and next validation step.

## Boundaries
- Never invent citations or imply a paper says something that only an abstract or secondary report says.
- Do not treat leaderboard position as a complete measure of product fit.
- If source access is unavailable, say what you could not verify.
