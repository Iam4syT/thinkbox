# Microsoft 365 support change review lab
## A Outcome
Turn synthetic recurring support tickets into a short service-review report and hold a proposed change until approval, positive tests, negative tests and rollback evidence are all present. Nothing deploys.

## B Public need and limits
The selected Burges Salmon JD calls for support trends, permanent fixes, update testing, knowledge guidance and stakeholder coordination. The 10 February 2025 innovation-week announcement supports knowledge-sharing context. A weekly support-review report is a reasoned repeat-use scenario, not an observed employer problem or a reproduction of its ticket system. Technical basis: Microsoft service-health guidance https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health and Copilot service-plan diagnostic https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-service-plans ; checked20 October 2026.   A missing app is a symptom, not proof of a licence fault.

## C Requirements exercised
R4 permanent-fix reasoning; R7 IT service management/reporting; R8 acceptance/release/rollback; R9 trend analysis; R10–R12 stakeholder guidance, knowledge and adoption feedback. Actual third-line/change ownership remains outside this synthetic demonstration.

## D Candidate gap
Extends existing ticket coordination, documentation, PowerBI/reporting and scoped M365 troubleshooting toward structured problem/change review. It does not prove implementation of a real permanent fix, use of an enterprise ticket platform or measured adoption.

## E Recurring use and baseline
A service owner could review weekly grouped symptoms, then select a problem for investigation and publish a checked knowledge article. Manual baseline: count the same3 synthetic tickets by exact service+symptom, then read the four change-evidence states. Code automates that transparent checklist. No AI is needed for exact grouping. An optional AI summary could omit or distort a symptom and must be checked separately; no better result has been demonstrated. Count reduction is not a productivity benefit or proof a fix caused improvement.

## F Architecture and security
Synthetic JSON tickets/change evidence → strict field validation and duplicate-ID check → exact Counter grouping → change hold/review decision → local JSON report → human service owner. No API, user identity, real helpdesk, Microsoft deployment or AI endpoint. Two similar symptoms do not establish a shared root cause. All-pass evidence means ready_for_human_review, never permission to deploy.
## Environment and cost
Local route: Python3.11 or newer, a terminal and a text editor. It uses only the standard library, synthetic JSON and local files. No licence, API key, network call or paid service; cloud/API cost £0 for this route. Time budget: one focused session for the local slice, then one to three weekends for independent explanation and optional tenant work; estimates, not measured duration. Existing computer cost excluded.

Optional Microsoft route is separate and UNRUN. It needs an authorised isolated Microsoft 365 tenant, suitable base subscription, a Microsoft 365 Copilot licence where the test requires it, two test users and least-privilege admin roles. Purview/advanced controls may require additional entitlements. Check current Microsoft licensing/admin guidance before obtaining anything. Do not buy or start paid resources without approval. No real client files, production tenant, global-admin shortcut or live permission changes are part of this local build.

## Engineering status
This scenario is implemented and locally evaluated on synthetic data. It is an independent exercise, not commissioned client work. Independent learner reproduction and live Microsoft tenant validation remain unobserved.

## H Setup and execution
1. Starting state: Python installed. Run `python3 --version`, expect3.11 or later. If unavailable, obtain an approved official runtime before running the guide. No account, API key or licence is required for this route.
2. Starting state: clean repository copy. Open `Modern Workplace Solutions/Enterprise-Ops-Telemetry-Engine/scenarios/m365-support-change-review` in the terminal. Check main.py, fixtures.json and test_main.py exist. If absent, correct your path; the parent project has other dependencies not required here.
3. Starting state: input open in an editor. Read the3 tickets: T1/T2 Copilot missing_app, T3 SharePoint access_denied. Check IDs are unique and no customer content is present. If real exports were copied accidentally, stop and remove them from the exercise before any publication.
4. Starting state: baseline not yet written. Manually group exact service+symptom. Expect one recurring group Copilot/missing_app count2; the single SharePoint case should not appear in recurring groups. Save this before running the program. Repeated symptoms alone do not prove root cause or permanent-fix success.
5. Starting state: proposed-change evidence open. Read approved, positive_test, negative_test, rollback_test. Negative_test is unknown; the manual decision is hold. Explain that a positive test checks intended behaviour; a negative test checks forbidden/unwanted behaviour; rollback checks recovery. If any concept is unclear, write a simple example before proceeding.
6. Starting state: known baseline. Run `python3 -B -m unittest -v`. Expect eight tests pass, covering duplicate IDs, invalid service/evidence, recurrence, positive failure, unknown negative, rollback failure and human-review boundary. If a test fails, capture its message and investigate; do not relabel unknown as pass to silence it.
7. Starting state: checks pass. Run `python3 -B main.py --input fixtures.json --output report.json`. Expect recurring count2 and change_status hold with unresolved negative_test. Compare against manual baseline. If file writing fails, use a writable local path; no tenant access can fix a local path error.
8. Starting state: report inspected. Write a problem note: observed symptom, affected synthetic IDs, missing evidence, possible investigations and owner. Do not state root cause is licensing merely because the symptom is missing_app. In an authorised real workflow, check entitlement, health, app version and access with the responsible admins before deciding.
9. Starting state: disposable copy `review.json`. Change negative_test from unknown to pass, leaving other evidence pass. Run using review.json and a new review-report.json. Expect ready_for_human_review and deployment_authorised false. This represents asserted synthetic evidence only; editing a JSON flag does not mean a real test happened.
10. Starting state: another disposable copy. Change rollback_test to fail. Run to rollback-report.json. Expect hold and rollback_test in unresolved. Restore the known fixture and rerun. If a real rollback failed, stop rollout and escalate with the actual recovery evidence.
11. Starting state: disposable malformed input. Duplicate T1 without changing ID; use a fresh output filename. Expect exit2 Duplicate ticket ID and no new report. Restore IDs and rerun. This prevents accidental duplicate export rows inflating the recurrence count.
12. Starting state: output known. Change a service to an unsupported value in a disposable copy. Expect rejection. Restore an allowed value. Do not silently map an unfamiliar product to Copilot; document any future schema extension and add tests for it.
13. Starting state: problem note drafted. Add an approval owner, test evidence location, review date and rollback owner. Create a simple knowledge article with symptom, checks, safe workaround, escalation boundary and validation. Keep all tenant-specific commands proposed/unrun; no automatic permanent fix is included.
14. Starting state: report and note ready. Re-run tests, then compare report with baseline and save runtime, input/output hashes and actual failures. A future week's lower count needs comparable collection window and denominator; do not claim a percentage reduction from3 fixtures.
15. Starting state: learning review. Ask another reader to explain why all-pass only reaches human review and why a recurring group is not a root cause. If explanation fails, improve the guide and repeat with an unseen failure case. Record this separately from today's automated checks.

## I Break and fix
Implemented exercises include missing negative evidence, failed rollback, duplicate ticket IDs, invalid service, invalid approval state and positive-test failure. Use fresh output names after failed runs; otherwise old reports may look current. Recovery restores the known fixture and runs the automated suite plus a manual report comparison.

## J Acceptance and actual result
Acceptance: correct exact grouping; no duplicate inflation; any unknown/failing evidence holds change; malformed values fail; all-pass remains human-review-only; deployment_authorised always false. Actual automated local result20 October 2026: eight tests passed and3-ticket report generated. No AI comparison, service API, live change, root-cause confirmation, adoption survey or measured saving was performed. Evidence: evidence/tests.txt and evidence/report.json. These hand-designed tests cannot estimate workplace effectiveness.

## K Artefacts and cleanup
Keep README, source, synthetic fixtures, tests, report, change checklist and a knowledge-note example. Architecture is the local flow above; demo script shows the hold and all-pass cases. No video recorded. Delete only your generated report/disposable broken files; preserve committed fixtures and historical evidence. No cloud resources or licence assignments are created. Later authorised tenant validation requires its own reversible plan and billing/access cleanup checks.

## L Interview story and native extension
Problem: repeat symptoms and incomplete change evidence can hide risk. Constraint: no actual helpdesk or tenant. Design: exact grouping and explicit evidence states. Build: report/checklist. Failure: unknown negative test blocks review. Verification: eight checks and manual grouping. Intended value: more consistent handover; no real-world outcome inferred.
Optional native extension, UNRUN: obtain permitted sanitised ticket export with stable IDs and approved retention; map actual services/symptoms without guessing product; inspect Microsoft admin service health and current Copilot plan diagnostics under authorised roles; select a test change in an isolated tenant; define positive/negative/rollback checks and approvals before touching configuration; record version/timing and results; have the change owner decide. Never change an evidence flag to stand in for an unperformed test. An approved live change still needs separate authority.

## M Conditional wording
Use only after independently completing and evidencing it: Built a synthetic support-trend report with duplicate checks and a change-review gate covering approval, negative tests and rollback. Do not claim reduced incidents, automated production releases or enterprise permanent-fix ownership.

## N Next version
Add a read-only import adapter for a permitted ticket format and comparison periods with explicit denominator, missing-data and duplicate rules. Keep deployment out of the reporting process. Evaluate optional summaries against human notes before adopting AI.
