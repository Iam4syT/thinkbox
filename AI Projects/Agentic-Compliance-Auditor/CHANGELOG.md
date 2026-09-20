# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: FastAPI contract, static policy context, strict output validation and mandatory human-review state.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: No legal/regulatory certification or automatic approval. Local tests mock the provider; live model false-approval and false-rejection rates remain unmeasured.
- Lesson: Health and mocked contract tests need no key. A real audit request needs configured OpenAI/Azure access and may incur costs; it is outside the offline lab. Evaluation cases live in docs/evaluation-cases.json.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
