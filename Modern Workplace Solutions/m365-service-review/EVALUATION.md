# Evaluation — service review

Date: 30 September 2026. Environment: Python 3.11.9 on macOS arm64; exact source SHA-256 and runtime are in evidence/run-metadata.json. Evaluation performed by Codex. Bunamin independent reproduction remains pending.

## Baseline, target and inputs

Baseline: manual checklist of four service statuses, freshness, declared activity/capacity, ownership and audit completeness. The program standardises that checklist; no manual-versus-program timing experiment was performed. Targets: an explicit review for the supplied problematic snapshot, no threshold finding for the normal fixture, and unknown/invalid input must never report a clean result.

Two synthetic CLI inputs each declare four services, one activity row, one capacity row and one audit observation. The review fixture contains five intended review conditions. These are authored examples, not a sampled enterprise dataset or held-out predictive benchmark. Thresholds are illustrative: 48 hours, 90% storage and 20% activity.

## Observed results

| Check | Actual result | Meaning |
|---|---|---|
| Behaviour suite | 14 passed, exit 0 | Covers status, missing/stale/future data, invalid numbers, denominator/threshold boundary, duplicate service, incomplete audit and deterministic read-only behaviour |
| Normal CLI | NO_RULE_FINDINGS, exit 0, zero findings | Complete declared synthetic example passed the implemented rules |
| Review CLI | REVIEW, exit 1, five findings | All five designed review conditions appear |
| Missing/unknown/stale audit or workload | INCOMPLETE in behavioural tests | Missing evidence does not become healthy state |

Read evidence/test-output.txt, evidence/normal-report.json and evidence/review-report.json. Program stdout is the exact recorded report; inputs were not mutated. No failed test was observed in the recorded run. Tests deliberately inject invalid and incomplete states and verify recovery boundaries.

## Limits and next evidence

No tenant connection, actual audit ingestion, reporting-role test, paginated collection, AI comparison, commercial delivery, measured saving, latency benchmark, cost study or uptime outcome. The rule set is a small learning slice, not comprehensive M365 monitoring/security coverage. Reporting delays, privacy masking and workload/provider naming need a separately validated adapter. A live no-finding output would still need source completeness and human review.

Next: Bunamin independently reruns and explains the faults. A later approved read-only collector must be checked against the manual baseline, source window and a denied-access case before operational use. Keep AI optional and evaluate actual benefit rather than adding it for appearance.
