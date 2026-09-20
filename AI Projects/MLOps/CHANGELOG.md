# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Local group-split benchmark with training-only imputation, mean baseline and Ridge model.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: One local holdout does not validate production serving, temporal performance, drift monitoring or causal business effects. Earlier ZenML code is retained as legacy study material.
- Lesson: Starting point credits Ayush Singh. The duplicated inner directory was flattened; see mlops-project/MIGRATION.md and data provenance. Historical dependency pins are in requirements-legacy.txt.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
