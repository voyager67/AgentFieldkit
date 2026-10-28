---
name: model-diff-review
description: Compare two model checkpoints or prompt configurations using a consistent evaluation harness and error taxonomy. Use after fine-tuning, quantization, prompt edits, or inference-stack changes.
license: MIT
---

# Model Diff Review

## Procedure
1. Lock the comparison variables: evaluation rows, preprocessing, system prompt, chat template, decoding settings, tool access, timeouts, and scoring logic.
2. Verify artifact identity for both candidates: model revision/checksum, tokenizer, adapter/LoRA composition, quantization, inference library, and runtime flags.
3. Run baseline and candidate on identical examples. Randomize execution order if order effects, provider rate limits, or changing external state could bias results.
4. Compare overall results and meaningful slices. For small datasets, include raw counts and uncertainty; avoid false precision.
5. Bucket disagreements into clear categories: reasoning error, retrieval/tool failure, formatting, instruction following, refusal, hallucination, latency, or infrastructure error.
6. Manually inspect representative wins, losses, and regressions. Verify that scoring normalization is not hiding wrong answers.
7. Recommend ship, iterate, or reject based on predeclared criteria and risk tolerance.

## Deliverable
A comparison table, top regression examples, notable improvements, operational trade-offs, reproducibility metadata, and a recommendation tied to the original goal.

## Boundaries
- Do not change test data or rubric after seeing results to favor one candidate.
- Do not equate lower loss or faster tokens/sec with higher task quality.
- Disclose unavailable providers, failed requests, and missing samples rather than silently dropping them.
