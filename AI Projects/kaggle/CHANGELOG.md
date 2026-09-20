# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: A local Atom-feed fixture and the existing Flask release-notes viewer.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: This is a learning area. Reference PDFs are third-party material, not authored portfolio applications. Google Drive/AGY automation is separate and unvalidated here.
- Lesson: The supported demo parses a synthetic Atom document without network access. The optional /api/releases endpoint fetches the official BigQuery feed; it is not run by the offline test.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
