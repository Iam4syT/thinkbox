# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Deterministic synthetic telemetry, held-out Isolation Forest and threshold comparison.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: PowerShell runbooks produce plans only. Power BI is a manual CSV-import blueprint. No measured setup-time reduction, self-healing or cost saving.
- Lesson: 1,000 synthetic records; 600 training and 400 held-out rows. The simple threshold is a required baseline, not an inferior alternative by assumption.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
