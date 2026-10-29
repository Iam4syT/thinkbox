# Stock allocation and store-opening readiness lab

## A Outcome and honest status
Stock availability at each allocation and readiness checks before each store opening/change. Local read-only learning exercise with fictional data; the evaluated Python slice is separate from native ServiceNow and physical work, which remain unrun. Bunamin has not independently reproduced this new lab. Planning budget: 60–90 minutes offline plus a separate reviewed sandbox session, estimate not measured time.

## B Public need and scenario basis
The official Boots Hearingcare service-desk advert names stock levels, system testing, projects and infrastructure for new store openings. Sonova’s 23 March 2026 strategy and 18 May 2026 retail outlook support a local-service/store-readiness context. The specific fictional faults and inventory are learning hypotheses, not reports of company problems. Its 14 October product news does not establish AI work in this role.

## C Job mapping
Exercises stock arithmetic, reservations, damaged-stock exclusion, project testing, supplier questions, handover and opening readiness. Public advert: https://jobs.sonova.com/job/Warrington-IT-Service-Desk-Associate/1443695433/ . Internal priority rules, tools beyond ServiceNow, licences and physical standards are unknown.

## D Gap and scope
Professional physical laptop/server/network work and stock operations remain unestablished. A local calculation is not practical hardware delivery. Separate authorised physical rehearsal is required. These exercises do not alter candidate capability ratings or employment history.

## E Recurring use and baseline
An analyst can repeat this at each allocation, receipt, return and opening review. The aim is fewer missing assumptions and more reviewable records. Compare the report with a manual checklist for the same inputs. No actual time saving, company outcome or reduction in failures measured.

## F Architecture, identity and AI decision
Fictional JSON → strict Python input checks → deterministic report → human review. No network call, authentication, API token, external model, native write or purchase. Whoever can edit the input can change reported checks; this is not an approval system. Keep real colleague and patient records out. AI is unnecessary for these explicit checks; an optional explanation assistant would need a quality/privacy evaluation and cannot approve actions. No AI advantage claimed.

## G Prerequisites and cost
Python 3.11+, terminal, text editor and a copy of this exact scenario. Standard library only, no pip installation. Local marginal service cost £0 excluding equipment/time. A native extension needs an authorised sandbox, applicable ServiceNow permissions/plugins/licences and approved spare equipment, safe test network and a competent reviewer. Availability and cost unknown; no spend or new account authorised. Stop native work if these are unavailable.

## H Granular implementation

### Step 1 — Open the stock scenario
Starting state/action: From a clean Thinkbox clone open "Modern Workplace Solutions/device-readiness-review/scenarios/retail-stock-opening" or its supplied public folder. Run python3 --version (Windows py --version).
Expected result: Python 3.11+; scripts/readiness.py, templates/sample.json and tests present.
Verification/recovery: Check path and checkout if files are missing; no pip packages or cloud account required.

### Step 2 — Write the opening plan
Starting state/action: In a local note define a fictional two-desk store opening. List devices, network, authorised test user, software/licences, supplier contact, sign-off owner and rollback/escalation.
Expected result: A test plan labels every physical and native task unrun until actually done.
Verification/recovery: Use synthetic identifiers; do not invent an actual Boots store or procurement approval.

### Step 3 — Inspect stock and reservations
Starting state/action: Read sample.json. DEMO-LAPTOP has 5 on hand,2 reserved,1 quarantined; demand 3. DEMO-DOCK has 4 on hand, no unavailable units; demand 2.
Expected result: Manual available values 2 and 4; laptop shortage 1.
Verification/recovery: Do not count reserved or broken stock as available. A spreadsheet or paper checklist is the simpler baseline.

### Step 4 — Run readiness review
Starting state/action: Run python3 scripts/readiness.py templates/sample.json.
Expected result: review_required; laptop shortage 1; device_test and owner_signoff pending.
Verification/recovery: Compare manual arithmetic and all four check states. The output never reserves stock or approves opening.

### Step 5 — Resolve a fictional shortage
Starting state/action: Copy sample.json to templates/practice.json. Change demand for laptop from 3 to 2 and rerun.
Expected result: No shortage; still review_required because checks are pending.
Verification/recovery: This reduces fictional demand, not a genuine business requirement. In practice request approved extra stock or a revised plan; do not hide unmet needs.

### Step 6 — Keep unknown tests visible
Starting state/action: Set device_test to null, then false; run after each change.
Expected result: Both remain pending.
Verification/recovery: Unknown means not checked; false means failed. Record the difference in your notes even though both block readiness.

### Step 7 — Record a fully checked simulation
Starting state/action: With demand 2, set all four checks true and run again.
Expected result: recorded_checks_complete.
Verification/recovery: This trusts fixture statements; it does not test a device or authorise a store opening. Retain evidence for each real check separately.

### Step 8 — Exercise stock failure handling
Starting state/action: Set reserved to 8 with on_hand 5 and run; then restore 2. Add a new demand SKU DEMO-MISSING with quantity 2 and rerun.
Expected result: Over-allocation is rejected; unknown SKU becomes a shortage 2 rather than disappearing.
Verification/recovery: Correct the source record only after physical count/supplier review in a real workflow. Save failed inputs for learning.

### Step 9 — Run acceptance tests
Starting state/action: Run python3 -m unittest discover -s tests -v.
Expected result: 11 tests pass, including quarantine/reservation arithmetic, unknown/failed checks, duplicates and invalid quantities.
Verification/recovery: Keep the error/output if anything fails; do not count a skipped test as passed.

### Step 10 — Practise ServiceNow inventory separately
Starting state/action: Unrun extension: in an authorised sandbox confirm Asset Management/Procurement entitlement and required role. Current official route is Inventory > Transfer Orders > Create Transfer Order; choose distinct fictional source/destination stockrooms and a delivery-by date. Add appropriate model lines under the owner’s procedure.
Expected result: A test transfer record and lines if actually performed; no real stock movement or purchase.
Verification/recovery: Plugin/role and workspace may differ. If absent keep this step unrun. Do not activate paid features or broaden your own permissions.

### Step 11 — Practise physical verification separately
Starting state/action: Unrun extension: with an approved spare device and safe test network, record asset tag/condition, power-on, authorised software, approved test-user sign-in, permitted network/app connection and a user handover check. Ask a competent reviewer to witness the first attempt.
Expected result: Dated evidence for each test, or a recorded failure and escalation.
Verification/recovery: Do not dismantle hardware, alter security/network controls or use patient data. If faulty quarantine under agreed process. Credentials/access and new live changes need separate scope.

### Step 12 — Handover, rollback and cleanup
Starting state/action: Record stock count, allocations, supplier question, four test receipts and named sign-off. Remove only practice.json/local generated copies; retain baseline/source/evidence. Sandbox records follow the owner’s cleanup policy; return spare equipment to its agreed state.
Expected result: Repeatable checklist and honest unrun/failed labels; no unexpected resources or bill.
Verification/recovery: Do not retire real assets, delete business records, change production configuration or claim fixture flags prove real checks.

## I Break/fix practice
Run the documented missing-evidence and invalid-input changes without overwriting sample.json. Save failed input, actual error/report, diagnosis, correction and rerun. In native work use only fictional records in an authorised sandbox. A failure is useful evidence; concealment or changing demand to force readiness is not a fix.

## J Acceptance and limits
Normal output matches manual baseline. All 11 behaviour tests pass. Invalid inputs exit 2; unknown/failed evidence remains reviewable. No secret/private record appears. Human review and actual platform policy remain necessary. A peer can explain one failure and one limitation. Native integration, personal rebuild and physical capability are untested until separate dated evidence exists.

## K Artefacts
Retain source, original/failed fictional inputs, outputs, manual baseline, test log, architecture, this full guide, a two-minute demo and one reflection. Record runtime and source hashes. Keep candidate/application evidence privately. Public exports use fictional IDs and no account details. No real-world impact inferred.

## L Interview story
Explain the repeated task, constraints and simple design; show the normal result, failure, fix and verification. Then explain the native/physical boundary. Intended value is reliable review; actual observed result is a local test report. Practise this personally before presenting it as your work experience.

## M Conditional wording
Use only after Bunamin personally completes and evidences this exercise: “Practised stock allocation and store-readiness checks using fictional data, documented a failure and correction, and compared the report with a manual checklist.” Replace with exact own actions and artefacts. Do not add ServiceNow production, hardware rollout or client outcomes. LinkedIn remains a draft, not posted.

## N Next extension
Add a separately authorised native sandbox run and independent rebuild/explanation, then one measured task-quality comparison with a manual process. Consider AI only for a demonstrated extra need. Keep access, cost, change authority, rollback and ownership explicit.

## References and version caveat
Checked 29 October 2026. Official ServiceNow resolve/close guidance: https://www.servicenow.com/docs/r/it-service-management/incident-management/resolve-and-close-an-incident.html ; priority fields: https://www.servicenow.com/docs/r/it-service-management/service-operations-workspace/view-update-inc-overview-tab.html ; transfer orders: https://www.servicenow.com/docs/r/it-asset-management/asset-management/create-a-transfer-order.html . Indexed pages described Australia/March 2026, while live pages identify Brazil. Recheck actual sandbox release/UI; no Sonova release inferred. Asset Management is an optional practice extension, not a confirmed Sonova module.
Strategy 23 March 2026: https://www.sonova.com/sonova-presents-renewed-strategy-to-expand-market-leadership-with-ambition-to-reach-chf-6-billion-in-revenue-by-fy-2030-31/ ; results 18 May 2026: https://www.sonova.com/sonova-delivers-strong-fy-2025-26-results-with-continued-market-outperformance-and-increased-profitability/ .
