---
name: performance-proof
description: Find and validate a measurable performance bottleneck before optimizing. Use when latency, throughput, memory use, render speed, or compute cost is a concern.
license: MIT
---

# Performance Proof

## Procedure
1. Define the metric and target: p50/p95 latency, throughput, memory, startup time, bundle size, GPU utilization, or cost per job.
2. Record a baseline under representative inputs and a repeatable environment. Note warm-up, concurrency, dataset size, hardware, and variance.
3. Profile the workload using available instrumentation before changing code. Identify the bottleneck and its evidence.
4. Form one optimization hypothesis with a predicted measurable effect. Avoid speculative rewrites.
5. Make a localized change, preserving behavior and interfaces. If several changes are necessary, isolate them so regressions can be attributed.
6. Run the same benchmark and correctness tests. Compare distributions where possible, not a single favorable measurement.
7. Check trade-offs such as memory, complexity, tail latency, warm-up, quality, and operational cost.

## Result format
Metric, baseline, environment, change, new measurement, variance or caveat, correctness check, and recommendation.

## Boundaries
- Never call an optimization successful without comparable measurements.
- Do not use production-scale load, incur cloud/GPU spend, or affect live customers without authorization.
- If no reliable baseline can be obtained, present the change as an unverified hypothesis.
