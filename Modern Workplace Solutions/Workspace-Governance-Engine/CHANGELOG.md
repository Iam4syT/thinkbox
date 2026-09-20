# Change record

## 2026-09-13 — Portfolio evidence and reproducibility repair

- Scope: Offline fixtures, explicit live scope, delegated label-change guard, backups and verified rollback path.
- Corrected setup paths, capability wording and personal-contribution boundaries.
- Added repeatable lab/demo guidance and meaningful checks where behaviour changed.
- Actual validation: see EVALUATION.md and the repository verification report.
- Limitation: Live Graph operations are implemented but have not been tenant-tested. Fixtures do not establish tenant security or regulatory compliance.
- Lesson: Default mode uses fixtures. Existing labels require review; replacement is a separate explicit option. Live writes require delegated access, selected group IDs and -Apply.
- Next step: collect stronger permitted evidence before making broader operational claims.

Earlier history remains in git and any pre-existing dated logs. Append corrections and new results; do not rewrite failed experiments into successes.

## 20 September 2026 — verification and release preparation

- Recovered the authorised repair into a durable isolated checkout and reran the applicable local checks.
- Recorded actual results and remaining integration limits in the [repository verification report](../../docs/VERIFICATION.md).
- Preserved upstream attribution; no professional, live-tenant or hiring outcome is inferred from these tests.
