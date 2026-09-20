# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Three deterministic PowerShell demonstrations and expected-exit verification.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: No Microsoft Graph connection or automated remediation. Exit 1 is expected for the supplied non-compliant fixtures.
- Lesson: The harness succeeds only when all three intentionally bad fixtures report drift. A clean script exit is not a live tenant assessment.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
