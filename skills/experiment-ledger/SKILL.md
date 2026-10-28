---
name: experiment-ledger
description: Make ML training experiments reproducible and comparable. Use when fine-tuning models, comparing hyperparameters, changing datasets, or sharing GPU resources across contributors.
license: MIT
---

# Experiment Ledger

## Before a run
1. Record the hypothesis and the single or small set of variables being tested.
2. Identify base model and immutable revision, tokenizer/chat template, training code commit, dataset version/checksum, train/validation split, seed, precision, optimizer, learning rate, schedule, batch size, gradient accumulation, epochs/steps, context length, and checkpoint policy.
3. Estimate VRAM, disk, runtime, and approximate cost. Confirm the run will not interfere with another team member's GPU job or overwrite their checkpoints.
4. Define baseline metrics and a stopping rule before inspecting results.

## During a run
- Capture actual configuration, environment/library versions, host/device type, start/end time, logs, throughput, GPU memory, failures, and checkpoint paths.
- Track training and validation metrics with step numbers. Watch for divergence, collapsed output, data-loader stalls, and unexpectedly high memory.
- Do not change training settings mid-run without recording a new experiment identity.

## After a run
1. Evaluate with the same frozen evaluation harness used for the baseline.
2. Compare quality, latency, memory, and cost. Include uncertainty and sample sizes where relevant.
3. Keep model checkpoints linked to their data and code versions. Store only artifacts approved for the project.
4. Record what to try next, even if the run failed.

## Deliverable
A compact experiment card with ID, hypothesis, immutable inputs, config, resource usage, metrics, caveats, artifacts, and conclusion.

## Boundaries
- Do not claim a model improved from training loss alone.
- Never publish weights or datasets with unknown license, privacy, or safety status.
- Avoid expensive repeated runs when a small diagnostic can test the hypothesis.
