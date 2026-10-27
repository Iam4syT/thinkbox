# Evaluation — 27 October 2026

Baseline: manually specified outcomes for 4 supplied synthetic records, compared to rule outputs. Actual result: 9 test methods passed under 3.12.14 on macOS. Sample classifications: review_failure, collect_evidence, ready_for_human_closure, review_failure. Evidence: [test log](evidence/test-output.txt), [output](evidence/sample-output.json). Invalid types/duplicate IDs/empty inputs reject; invalid CLI input cannot replace a previous report and same input/output path rejects.

Scope: tests exercise local deterministic behaviour only. No physical device, Windows guest, domain, tenant, customer workflow, Bunamin independent rebuild, time saving or business impact was evaluated. No latency benchmark or paid/API cost applies. The supplied fixtures are a small selected test set, not a representative incident population. Next test: reviewed unseen-fault practice on an authorised lab, retaining unknown values and original-task checks.
