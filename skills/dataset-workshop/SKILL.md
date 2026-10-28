---
name: dataset-workshop
description: Prepare consistent, traceable instruction-tuning or evaluation datasets with reproducible cleaning rules. Use for JSONL corpora, reasoning examples, SFT data, or team-based dataset contributions.
license: MIT
---

# Dataset Workshop

## Standard record contract
Choose one canonical format for the entire project before contributors create data. For chat-style supervised fine-tuning, prefer one JSON object per line with a `messages` array containing role/content objects, unless the target model or training library requires another documented schema. Keep optional metadata in consistently named fields such as `source`, `source_license`, `split`, `difficulty`, and `record_id`.

## Procedure
1. Read the model card, tokenizer/chat template, trainer requirements, source dataset licenses, and intended deployment policy. Record what data may legally and ethically be used.
2. Publish one schema, one encoding convention (UTF-8), one newline policy, one normalization policy, and a set of positive/negative examples before splitting work across contributors.
3. Validate every row against the schema. Reject malformed JSON, missing required roles, blank prompts, truncated answers, unsupported fields, and invalid role order.
4. Deduplicate exact and near-duplicate examples. Keep provenance for removed or merged items without copying sensitive content into logs.
5. Check answer correctness with a defined rubric. For math/reasoning examples, validate final answers independently when possible. Do not fabricate hidden reasoning or claim a generated explanation is a verified trace.
6. Split train/validation/test before augmentation. Group related templates, source questions, paraphrases, users, or documents in one split to reduce leakage.
7. Normalize only superficial formatting. Preserve mathematical symbols, code, units, language, and meaningful structure. Avoid lossy whitespace cleanup in code or structured output.
8. Produce counts and checksums: rows by source/split/category, invalid records, duplicate rate, token-length distribution, and license/provenance coverage.
9. Freeze a dataset version and document the exact command, schema version, source snapshots, and any manual review.

## Deliverable
Return a dataset card, schema, validation results, split rationale, known contamination risks, and a reproducible preprocessing command.

## Boundaries
- Do not merge test examples into training data or tune on a held-out test set.
- Do not remove provenance just to make distribution simpler.
- Do not treat a famous public dataset as automatically license-compatible or contamination-free.
