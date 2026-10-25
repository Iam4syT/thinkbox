# Adoption Insight Check

## A. Outcome and status
Build and check a small offline decision aid. Source and seven automated checks were run locally on 25 October 2026. Fictional services/data only; native Microsoft 365 integration and Bunamin’s independent rebuild are unrun/unobserved.

## B. Research basis and company problem
Analysts need to distinguish a change in tool usage from improved colleague outcomes. Public Microsoft reporting documentation and the advertised service/adoption duties support the topic. The fictional cohorts and thresholds are a design hypothesis, not an employer policy.

## C. Capability mapping
Service data interpretation, reporting and user guidance.

## D. Gap mapping
Strengthens interpreting adoption data, validating denominators and explaining a proportionate next action. Professional reporting is adjacent evidence; adoption-campaign outcomes remain unestablished.

## E. Recurring-use value
A service analyst repeats this after each reporting window, comparing defined groups and selecting a feedback/training question. Measure correct decisions and verified task outcomes; do not infer productivity from activity.

## F. Architecture and simpler baseline
Fictional CSV → Python validation → local JSON report → human review. There are no network calls, user identities, secrets or automated changes. Manual spreadsheet/review is the baseline. AI is unnecessary for these deterministic checks; an optional future summary must retain source references and human approval. Output text is data, not permission to act.

## G. Prerequisites, cost and time budget
Python 3.10+, terminal and text editor. Standard library only; no pip install, tenant, licence, API key or paid service is needed. Offline cost £0 excluding your device/time. Suggested learning budget 2–3 hours, not a measured duration. Optional tenant reporting depends on an eligible subscription, approved roles, available reports and organisation policy; do not start a trial or buy resources for this guide without a separate decision.

## H. Granular implementation and checks

### Step 1: Open the project
Start from an extracted project folder. Open a terminal there and run python3 --version. Expect Python 3.10 or newer. Check the version text. If Python is absent, install it from python.org before continuing; do not change any tenant.

### Step 2: Inspect fictional input
Open templates/sample.csv in a text editor. It has four cohort/service rows and only aggregate counts. Check there are no personal identifiers. If a real export has been substituted, stop and restore the sample.

### Step 3: Check definitions
Read docs/architecture.md. licensed is the eligible licensed group for the service; active is a count in a matched 30-day window. Verify active never exceeds licensed. If definitions differ, correct them before comparing periods.

### Step 4: Run the baseline
Calculate Office-A manually: 12/20×100=60%; previous 10/20×100=50%; change +10 percentage points. Record that comparison in your notes. If you get 10% relative growth, distinguish that from 10 percentage points.

### Step 5: Run the check
From the project root run python3 scripts/check.py templates/sample.csv > output.json. Expect exit 0 and four findings. Open output.json: Office-A is 60%, Office-B is 40%; the two small/zero groups are suppressed. If the path fails, confirm the terminal is in the folder containing scripts and templates.

### Step 6: Protect small groups
Inspect Small-group and No-licences findings. Expect no counts or rates. Check that a small previous cohort is also suppressed by running the tests. If either rate appears, stop sharing output and fix the suppression rule.

### Step 7: Break and recover
Copy sample.csv to scratch.csv. Change Office-A active to 21. Run python3 scripts/check.py scratch.csv. Expect exit 2 with Input rejected; do not use the result. Restore 12 and rerun; expect exit 0. The tests also reject negative counts, duplicate rows and mismatched windows.

### Step 8: Check behaviour
Run python3 -B -m unittest discover -s tests -v. Expect seven tests and OK. Compare the assertions with the safety boundaries, then make one prediction before changing a fixture. If a test fails, save the failure, fix input or code and rerun; do not delete the check to get a pass.

### Step 9: Make a useful recommendation
For Office-B, draft a question about task needs, data age and colleague feedback. A 40% usage rate alone does not prove waste or justify removing licences. Compare the recommendation with manual review. No productivity saving has been measured.

### Step 10: Prepare the Microsoft 365 extension
Unrun dependency: obtain permission for a test tenant and an appropriate least-privilege reports role. Open admin.microsoft.com → Reports → Usage, review the selected report, date window and privacy settings. Keep user identifiers concealed. Use approved aggregates only and document report lag; never upload employer exports to this repository. If access is absent, remain in offline mode.

### Step 11: Close the loop
Write your own explanation of the denominator, suppression, failure and recommendation in a private learning note. Have a reviewer challenge one conclusion. Save a permitted screenshot of the fictional output if useful. Rebuild from a clean folder to establish your own reproduction; this run alone does not prove it.

### Step 12: Clean up
Delete only scratch.csv and output.json that you created for this exercise. Keep templates and checked evidence. Remove any temporary report download under its approved retention rule; revoke temporary test access through the authorised owner, not through this script.

## I. Break/fix
The deliberate invalid-input step and tests cover failures that could produce an unsafe recommendation. Keep the rejected input, error and corrected result in a private exercise record. Automated tests do not test Microsoft 365 APIs or production permissions.

## J. Acceptance and evaluation
The sample command exits 0; seven behaviour tests pass; the invalid fixture exits 2; the manual baseline agrees with the normal output; no network connection or real user data appears. Read EVALUATION.md and evidence files for the actual local run. Workplace value, learner skill and native access remain unmeasured.

## K. Artefacts and handover
README.md, scripts/check.py, templates/sample.csv, tests/test_behaviour.py, docs/architecture.md, evidence/sample-output.json, evidence/test-output.txt, EVALUATION.md, DEMO SCRIPT.md, CONTRIBUTIONS.md and CHANGELOG.md. Capture only permitted fictional screenshots; no video has been recorded. Public destination: Modern Workplace Solutions/m365-adoption-insight in Iam4syT/thinkbox. Publication needs a verified remote commit; this guide does not establish it.

## L. Interview story
Explain the recurring need, why the manual baseline is useful, the choice to keep a human decision, one failed input, the check that caught it and what remained untested. Explain your own edit and test; do not claim that preparing this guide establishes independent execution or professional delivery.

## M. Conditional CV/LinkedIn wording
Use only after your own completion and evidence: “Built and tested an offline adoption insight check using fictional Microsoft 365-related records; checked normal and invalid inputs and documented the limits of the recommendation.” Add your actual contribution and measured result, if any. This wording is excluded from the current CV and letter.

## N. Extension
With separately authorised test-tenant access, compare an approved aggregate export with manual calculations and build a Power BI view. Recheck privacy, report lag and task-level feedback; do not automate licence removal.

## Technical sources
Checked 25 October 2026. Microsoft 365 usage reports: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide
Microsoft Message center: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center?view=o365-worldwide
These sources describe the optional native steps; the implemented tool is offline.
