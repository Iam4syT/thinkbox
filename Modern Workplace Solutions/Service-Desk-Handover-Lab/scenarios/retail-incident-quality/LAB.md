# Incident quality and safe handover lab

## A Outcome and honest status
Daily incident logging, prioritisation, evidence and next-update handovers. Local read-only learning exercise with fictional data; the evaluated Python slice is separate from native ServiceNow and physical work, which remain unrun. Bunamin has not independently reproduced this new lab. Planning budget:60–90 minutes offline plus a separate reviewed sandbox session, estimate not measured time.

## B Public need and scenario basis
The official Boots Hearingcare service-desk advert names ServiceNow records, resolution notes, prioritisation and stakeholder updates. Sonova’s 23 March 2026 strategy and 18 May 2026 retail outlook support a local-service/store-readiness context. The specific fictional faults and inventory are learning hypotheses, not reports of company problems. Its 14 October product news does not establish AI work in this role.

## C Job mapping
Exercises ticket recording, prioritisation, diagnosis evidence, communication, service-agreement awareness and safe escalation. Public advert: https://jobs.sonova.com/job/Warrington-IT-Service-Desk-Associate/1443695433/ . Internal priority rules, tools beyond ServiceNow, licences and physical standards are unknown.

## D Gap and scope
Generic professional ITSM experience is transferable; actual ServiceNow operation is not yet evidenced. Practise its record/resolution boundaries without claiming product competence from this simulator. These exercises do not alter candidate capability ratings or employment history.

## E Recurring use and baseline
An analyst can repeat this at every handover and resolution review. The aim is fewer missing assumptions and more reviewable records. Compare the report with a manual checklist for the same inputs. No actual time saving, company outcome or reduction in failures measured.

## F Architecture, identity and AI decision
Fictional JSON → strict Python input checks → deterministic report → human review. No network call, authentication, API token, external model, native write or purchase. Whoever can edit the input can change reported checks; this is not an approval system. Keep real colleague and patient records out. AI is unnecessary for these explicit checks; an optional explanation assistant would need a quality/privacy evaluation and cannot approve actions. No AI advantage claimed.

## G Prerequisites and cost
Python 3.11+, terminal, text editor and a copy of this exact scenario. Standard library only, no pip installation. Local marginal service cost£0 excluding equipment/time. A native extension needs an authorised sandbox, applicable ServiceNow permissions/plugins/licences and test callers. Availability and cost unknown; no spend or new account authorised. Stop native work if these are unavailable.

## H Granular implementation

### Step 1 — Open a clean copy
Starting state/action: In a new terminal folder run git clone https://github.com/Iam 4 syT/thinkbox.git, then cd "thinkbox/Modern Workplace Solutions/Service-Desk-Handover-Lab/scenarios/retail-incident-quality". For a downloaded local package open its public folder.
Expected result: scripts/incident.py, templates/sample.json and tests/test_review.py exist.
Verification/recovery: List files with ls (Windows dir). If absent, check revision and path; do not install the parent dependencies.

### Step 2 — Check runtime and boundaries
Starting state/action: Run python 3 --version (Windows py --version, substituting py in later commands). Read README and CONTRIBUTIONS.
Expected result: Python 3.11 or later; no account, network integration or secrets required.
Verification/recovery: If unavailable use an approved Python installation; do not change a work device without permission.

### Step 3 — Establish the manual baseline
Starting state/action: Read templates/sample.json. For each row record impact, urgency, owner, next update and evidence gaps on paper. Use matrix rows [1,2,3], [2,3,4], [3,4,5], indexed by impact and urgency 1–3.
Expected result: DEMO-01 priority 1; DEMO-02 priority 4. Second ticket lacks verification and user confirmation.
Verification/recovery: This is an illustrative matrix, not Sonova policy. Do not infer contractual response deadlines.

### Step 4 — Run the complete example
Starting state/action: Run python 3 scripts/incident.py templates/sample.json.
Expected result: Two reports; first documented_for_review, second review. Neither record is closed or changed.
Verification/recovery: Compare every output with the manual baseline. If different preserve input/output and check file contents.

### Step 5 — Inspect the implementation
Starting state/action: Open scripts/incident.py. Find unique IDs, integer validation, allowed states and the resolved-state evidence check.
Expected result: You can point to the code that rejects a duplicate and flags missing checks.
Verification/recovery: Explain one branch in your own words; record uncertainties rather than claiming independent understanding.

### Step 6 — Break a handover
Starting state/action: Copy templates/sample.json to templates/practice.json. Remove the first ticket owner text and rerun using practice.json.
Expected result: owner appears in review_items.
Verification/recovery: Restore a fictional owner; rerun and confirm the gap disappears. No real assignment is made.

### Step 7 — Try premature resolution
Starting state/action: In practice.json set the first state to resolved while keeping resolution/verification empty and user_confirmed null.
Expected result: Missing resolution, verification and confirmation are visible.
Verification/recovery: Add a fictional action/check and true confirmation only after a simulated retest. Report remains documented_for_review, never native closure.

### Step 8 — Test invalid input
Starting state/action: Change first impact to true; rerun. Then restore integer 1 and rerun.
Expected result: Input error and exit 2 for the boolean; normal report after correction.
Verification/recovery: Read the error rather than deleting validation. JSON true is not an integer impact.

### Step 9 — Run acceptance tests
Starting state/action: Run python 3 -m unittest discover -s tests -v.
Expected result: 11 tests pass across normal path, invalid input, missing evidence and duplicates.
Verification/recovery: If any fails save the failure and explain before editing; a guide does not prove you ran it.

### Step 10 — Practise native ServiceNow separately
Starting state/action: Unrun extension: obtain an authorised sandbox with incident permissions. Ask its owner which release/workspace, priority matrix and resolution/closure policy apply. In a test incident use Open/New, enter fictional caller/description, impact/urgency and assignment; save and inspect its number.
Expected result: A sandbox ticket with expected priority and traceable work notes, only if actually executed.
Verification/recovery: Current docs may redirect to another release/workspace. If access or required roles are missing stop; do not create an account, buy licences or use a live employer instance as part of this run.

### Step 11 — Verify the native resolution boundary
Starting state/action: Unrun extension: reproduce a harmless test fault, record investigation and a checked workaround/repair, fill resolution information and use Resolve only with authorised scope. Ask the test caller to retest; follow the sandbox closure rule.
Expected result: Resolved and Closed remain distinct; retain actual number, redacted notes and user check if performed.
Verification/recovery: If retest fails reopen/escalate under the local process. Do not grant admin roles or treat this local script as a ServiceNow update.

### Step 12 — Handover and clean up
Starting state/action: Save a before/after report, baseline, one failure, explanation and next-update note. Remove only templates/practice.json and disposable local outputs. Native test cleanup follows owner-approved disposition.
Expected result: Source and evaluation remain reproducible with no private caller data.
Verification/recovery: Inspect the public diff. Do not delete real incident history, change retention or remove parent files.

## I Break/fix practice
Run the documented missing-evidence and invalid-input changes without overwriting sample.json. Save failed input, actual error/report, diagnosis, correction and rerun. In native work use only fictional records in an authorised sandbox. A failure is useful evidence; concealment or changing demand to force readiness is not a fix.

## J Acceptance and limits
Normal output matches manual baseline. All 11 behaviour tests pass. Invalid inputs exit 2; unknown/failed evidence remains reviewable. No secret/private record appears. Human review and actual platform policy remain necessary. A peer can explain one failure and one limitation. Native integration, personal rebuild and physical capability are untested until separate dated evidence exists.

## K Artefacts
Retain source, original/failed fictional inputs, outputs, manual baseline, test log, architecture, this full guide, a two-minute demo and one reflection. Record runtime and source hashes. Keep candidate/application evidence privately. Public exports use fictional IDs and no account details. No real-world impact inferred.

## L Interview story
Explain the repeated task, constraints and simple design; show the normal result, failure, fix and verification. Then explain the native/physical boundary. Intended value is reliable review; actual observed result is a local test report. Practise this personally before presenting it as your work experience.

## M Conditional wording
Use only after Bunamin personally completes and evidences this exercise: “Practised incident-quality and handover checks using fictional data, documented a failure and correction, and compared the report with a manual checklist.” Replace with exact own actions and artefacts. Do not add ServiceNow production, hardware rollout or client outcomes. LinkedIn remains a draft, not posted.

## N Next extension
Add a separately authorised native sandbox run and independent rebuild/explanation, then one measured task-quality comparison with a manual process. Consider AI only for a demonstrated extra need. Keep access, cost, change authority, rollback and ownership explicit.

## References and version caveat
Checked 29 October 2026. Official ServiceNow resolve/close guidance: https://www.servicenow.com/docs/r/it-service-management/incident-management/resolve-and-close-an-incident.html ; priority fields: https://www.servicenow.com/docs/r/it-service-management/service-operations-workspace/view-update-inc-overview-tab.html ; transfer orders: https://www.servicenow.com/docs/r/it-asset-management/asset-management/create-a-transfer-order.html . Indexed pages described Australia/March 2026, while live pages identify Brazil. Recheck actual sandbox release/UI; no Sonova release inferred. Asset Management is an optional practice extension, not a confirmed Sonova module.
Strategy 23 March 2026: https://www.sonova.com/sonova-presents-renewed-strategy-to-expand-market-leadership-with-ambition-to-reach-chf-6-billion-in-revenue-by-fy-2030-31/ ; results 18 May 2026: https://www.sonova.com/sonova-delivers-strong-fy-2025-26-results-with-continued-market-outperformance-and-increased-profitability/ .
