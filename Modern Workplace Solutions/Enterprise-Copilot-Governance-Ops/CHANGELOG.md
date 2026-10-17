# Change record

## 2026-09-13 — Core policy engine and fixture pipeline

- Scope: Explicit metadata rules, synthetic tenant fixture and matplotlib report.
- Implemented deterministic policy engine (`allowed`, `exposed`, `review`).
- Added repeatable lab and demo guidance with automated unit testing suite.
- Actual validation: see [EVALUATION.md](EVALUATION.md) and [evaluation.json](evidence/evaluation.json).
- Scope boundaries: No live Microsoft tenant mutation, semantic query evaluation, or direct Power BI gateway push.

## 2026-09-20 — Repository verification and test harness

- Reran local verification checks, unit test suites, and evaluation harness.
- Verified deterministic 3-state decisions across all 10 hand-labelled benchmark cases.
- Recorded actual results in [docs/VERIFICATION.md](../../docs/VERIFICATION.md).

## 2026-10-17 — Governance documentation and tenant demo architecture

- Designed live Microsoft 365 tenant integration blueprint and Entra ID zero-trust app registration architecture.
- Cleaned and aligned project documentation and verified local evaluation suites.
