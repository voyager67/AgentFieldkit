---
name: model-eval-design
description: Build an evaluation plan that measures a model capability rather than a single attractive example. Use when comparing base and fine-tuned models, reasoning systems, prompts, or agent workflows.
license: MIT
---

# Model Evaluation Design

## Procedure
1. Define the capability and failure modes in plain language. Make success measurable and relevant to actual users.
2. Create a locked evaluation set with explicit inclusion rules, source provenance, and a clear split from training and prompt-tuning examples.
3. Establish a baseline using the same inference settings, tokenizer/template, context length, tool permissions, and retry policy.
4. Select metrics that match the task: exact match, normalized answer accuracy, structured-output validity, calibration, pass@k, latency, tool-use success, or human rubric scores. Define normalization carefully.
5. Include easy, typical, boundary, adversarial, out-of-domain, and refusal/safety cases where relevant.
6. Use deterministic execution where possible. For stochastic models, specify sampling settings and repeat counts; report variability rather than cherry-picking runs.
7. Inspect error categories and examples, not only an aggregate score. Check whether gains are concentrated in one slice or come from leaking expected answers.
8. Keep the test set fixed for final comparison. Use a separate development set for iteration.

## Report
Dataset/version, sample size, metric definitions, baseline, candidate, per-slice results, confidence/variance, qualitative error analysis, cost/latency, and limitations.

## Boundaries
- Do not claim a broad capability from a tiny or unrepresentative benchmark.
- Do not treat model self-judgment as an unbiased ground truth without validation.
- If scoring rules or test samples changed, mark results as not directly comparable.
