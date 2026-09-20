# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Bounded page extraction, LLM prompt and validated JSON-to-workbook fields.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: Fetch-and-prompt workflow, not indexed RAG or an autonomous strategy engine. Proposed objectives and targets are drafts, not achieved business results.
- Lesson: Tests cover malformed results, missing pages and separation of hostile page text from trusted instructions. They do not establish immunity to prompt injection. Live workbook processing requires permitted URLs and a model key.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
