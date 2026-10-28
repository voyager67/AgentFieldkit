---
name: data-quality-gate
description: Design validation checks for structured datasets and data pipelines. Use when ingesting, transforming, joining, exporting, or versioning data used by software or machine-learning systems.
license: MIT
---

# Data Quality Gate

## Procedure
1. Define the intended use, data owner, source, allowable uses, sensitivity class, and expected freshness. Do not assume data is safe to use merely because it is accessible.
2. Write down the schema: field names, types, requiredness, allowed ranges, units, identifiers, timezone conventions, and null semantics.
3. Profile representative samples for missingness, duplicates, outliers, inconsistent categories, encoding problems, invalid dates, and suspicious distribution shifts.
4. Validate joins and identifiers. Check row counts before and after transformations to detect accidental fan-out or dropped records.
5. Define hard failures versus warnings. Make thresholds explicit and explain why they matter to downstream decisions.
6. Preserve lineage: source snapshot, transformation version, timestamps, and deterministic parameters. Avoid recording secrets or personal records in logs.
7. Run validation on a sample first, then on the intended dataset. Save a compact machine-readable summary and meaningful failure examples.

## Deliverable
Include schema contract, validation checks, counts, examples of failed rows with sensitive values redacted, and the go/no-go decision.

## Boundaries
- Do not silently impute, delete, or rewrite data to make validation pass.
- Never upload sensitive datasets to external services without authorization and a valid data-use basis.
- Label synthetic or inferred data; never represent it as collected fact.
