# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Builder/Factory/Strategy design, SQLite history, cost-calculation service and JUnit tests.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: Inputs and source switching are software scenarios. No physical grid or live sensor integration. Cost/carbon coefficients and demand-to-energy conversion are assumptions, not validated savings.
- Lesson: Java 24+ and Maven 3.9+ required. run.sh uses Maven from the project directory; ./run.sh gui is optional. Tests target the current CostCalculationService, not removed SwitchReport methods.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
