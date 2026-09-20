# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: FastAPI simulation and deterministic synthetic Random Forest training.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: No Intune, JAMF or directory changes. The class probability describes synthetic labels; it is not real device-failure risk.
- Lesson: 2,500 synthetic records; 2,000 training and 500 test rows. The generating rule is the baseline. A fresh small model is built in memory; no committed pickle is loaded.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
