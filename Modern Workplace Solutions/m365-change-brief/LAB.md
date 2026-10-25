# Change Brief Check

## A. Outcome and status
Build and check a small offline decision aid. Source and seven automated checks were run locally on 25 October 2026. Fictional services/data only; native Microsoft 365 integration and Bunamin’s independent rebuild are unrun/unobserved.

## B. Research basis and company problem
Service owners need to turn release notices into clear actions with a named reviewer. Microsoft Message center documentation and the advertised release/communications duties support the topic. This fictional queue does not reproduce an employer process.

## C. Capability mapping
Change review, risk tracking and user guidance.

## D. Gap mapping
Strengthens change planning, risk tracking and colleague guidance. Support documentation and peer teaching are adjacent skills; enterprise change-process ownership and organisation-wide training need separate evidence.

## E. Recurring-use value
A service analyst reviews new notices weekly and before each communication. Measure whether affected users can explain the action and whether owner/source/deadline are complete; no workplace benefit has been measured.

## F. Architecture and simpler baseline
Fictional CSV → Python validation → local JSON report → human review. There are no network calls, user identities, secrets or automated changes. Manual spreadsheet/review is the baseline. AI is unnecessary for these deterministic checks; an optional future summary must retain source references and human approval. Output text is data, not permission to act.

## G. Prerequisites, cost and time budget
Python 3.10+, terminal and text editor. Standard library only; no pip install, tenant, licence, API key or paid service is needed. Offline cost £0 excluding your device/time. Suggested learning budget 2–3 hours, not a measured duration. Optional tenant reporting depends on an eligible subscription, approved roles, available reports and organisation policy; do not start a trial or buy resources for this guide without a separate decision.

## H. Granular implementation and checks

### Step 1: Open the project
Start from the project folder. Run python3 --version in a terminal. Expect Python 3.10 or newer. If absent, install from python.org. No account, cloud subscription or additional package is needed for this offline exercise.

### Step 2: Read the input
Open templates/sample.csv. The three changes are fictional, including owners and approval states. Check the columns id, service, summary, due, impact, owner, status. Never treat this fixture as a real Microsoft roadmap notice.

### Step 3: Make a manual baseline
Using 25 October 2026 as the reference date, identify DEMO-2 as overdue, DEMO-1 as due within seven days, DEMO-3 as later. Record owner and status manually. If dates are ambiguous, use YYYY-MM-DD rather than guessing locale.

### Step 4: Run the queue
Run python3 scripts/check.py templates/sample.csv 2026-10-25 > output.json from the project root. Expect exit 0, three items sorted by due date, with DEMO-2 first. Open output.json and compare each urgency with your manual baseline. If a file is missing, check the working directory and spelling.

### Step 5: Check the approval boundary
Read DEMO-1 review text. Expect owner approval needed. DEMO-2 has only a fictional recorded approval and still requires source/audience review before communication. Verify the script has no email/Graph call. If a connection is added, do not run it without separate authorisation.

### Step 6: Draft the colleague brief
Create a private text note: what changes, who is affected, what they need to do, the deadline, help route and source. Label unverified facts Pending. Keep technical detail in an owner appendix. Do not send it. Ask a colleague to explain the required action back; record what they found unclear.

### Step 7: Break the owner field
Copy sample.csv to scratch.csv and clear the DEMO-1 owner. Run python3 scripts/check.py scratch.csv 2026-10-25. Expect exit 2 and Required field missing. Restore the fictional owner; expect exit 0. No valid output means no communication should proceed.

### Step 8: Check other failures
Run python3 -B -m unittest discover -s tests -v. Expect seven tests and OK. They cover overdue/due-soon items, approval wording, missing owner, invalid date, duplicate ID and unknown status. Retain failures before fixing them; do not equate a passed fixture test with a real release approval.

### Step 9: Prepare the Microsoft 365 extension
Unrun dependency: with approved read-only access, open admin.microsoft.com → Health → Message center. Select one actual notice, read its ID, dates, affected services and available actions. Use the least-privilege Message Center Reader role where appropriate. A public roadmap item is not confirmation that a tenant has received a release. If details are unavailable, record Pending and keep the local sample.

### Step 10: Plan a safe review
Ask the technical owner to verify impact, pilot, support guidance, any rollback and the audience. Save approval through the organisation’s existing process; a CSV status is not that process. If there is no owner or recovery route, hold the communication and escalate. This tool implements a review queue only.

### Step 11: Demonstrate and hand over
Show one normal item and the missing-owner failure. Explain why neither an overdue date nor recorded approval sends anything. Record your own edit, prediction, test and explanation privately. Rebuild from a clean folder before claiming independent practical evidence.

### Step 12: Clean up
Remove only scratch.csv, output.json and draft notes created for the exercise when no longer needed. Retain source fixtures and test evidence. Keep actual notices and approved internal communications in the organisation’s authorised store. No live change or email needs rollback because this exercise made none.

## I. Break/fix
The deliberate invalid-input step and tests cover failures that could produce an unsafe recommendation. Keep the rejected input, error and corrected result in a private exercise record. Automated tests do not test Microsoft 365 APIs or production permissions.

## J. Acceptance and evaluation
The sample command exits 0; seven behaviour tests pass; the invalid fixture exits 2; the manual baseline agrees with the normal output; no network connection or real user data appears. Read EVALUATION.md and evidence files for the actual local run. Workplace value, learner skill and native access remain unmeasured.

## K. Artefacts and handover
README.md, scripts/check.py, templates/sample.csv, tests/test_behaviour.py, docs/architecture.md, evidence/sample-output.json, evidence/test-output.txt, EVALUATION.md, DEMO SCRIPT.md, CONTRIBUTIONS.md and CHANGELOG.md. Capture only permitted fictional screenshots; no video has been recorded. Public destination: Modern Workplace Solutions/m365-change-brief in Iam4syT/thinkbox. Publication needs a verified remote commit; this guide does not establish it.

## L. Interview story
Explain the recurring need, why the manual baseline is useful, the choice to keep a human decision, one failed input, the check that caught it and what remained untested. Explain your own edit and test; do not claim that preparing this guide establishes independent execution or professional delivery.

## M. Conditional CV/LinkedIn wording
Use only after your own completion and evidence: “Built and tested an offline change brief check using fictional Microsoft 365-related records; checked normal and invalid inputs and documented the limits of the recommendation.” Add your actual contribution and measured result, if any. This wording is excluded from the current CV and letter.

## N. Extension
With separately authorised test-tenant access, capture one real notice into an approved private store, test a review/approval handoff and rehearse a short training brief. Do not automate sending or tenant changes.

## Technical sources
Checked 25 October 2026. Microsoft 365 usage reports: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide
Microsoft Message center: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center?view=o365-worldwide
These sources describe the optional native steps; the implemented tool is offline.
