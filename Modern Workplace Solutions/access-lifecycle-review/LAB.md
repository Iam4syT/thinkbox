# Access lifecycle review with an Okta practice path

Status: local Python slice evaluated by Codex; native product/device path unrun; Bunamin reproduction pending.

## A. Outcome
Review proposed access changes before anyone applies them.

## B. Company research and limits
The Clio advert asks for proactive support, onboarding, access and endpoint operations. Its dated expansion provides context; this scenario is an independent learning hypothesis, not a report of an internal Clio fault.

## C. Role mapping
R3/R4/R8: access lifecycle, Okta groups/rules, Workflows and provisioning.

## D. Gap mapping
Microsoft identity/query experience transfers; Okta production support remains Not Yet Evidenced.

## E. Repeated-use test
An administrator reviews new starters, department moves and leavers repeatedly. The testable target is catching unsafe/missing actions before change, not claimed time savings.

## F. Architecture and simpler baseline
Synthetic JSON → Python validation/rules → proposed review report → human review. No network, API, login or change execution. A manual checklist is the baseline. No AI is used: deterministic checks are clearer and do not need to interpret sensitive employee data. Native practice is a separate path.

## G. Prerequisites, cost and estimate
Local: Python 3.11+, editor, three synthetic records, no packages/accounts or paid service. Estimate 60–90 minutes for personal local practice, not measured actual time. Native: separate authorised Okta training org, Workflows/lifecycle entitlement and test SCIM app; pricing/trial scope must be confirmed. Do not connect to employer systems.

## H. Granular steps

### 1. Set up the local folder
Starting state: A computer with Python 3.11+ and the downloaded package.
Action: Open Terminal or PowerShell. Change into the project folder containing scripts, templates and tests. Run python3 --version (Windows: python --version).
Expected result: Version 3.11+ displayed.
Verification: List the folder and confirm scripts/review.py and templates/sample.json exist.
Recovery: If Python is missing, use an approved official Python installation. If command name differs, use python instead of python3 throughout.

### 2. Inspect the dummy input
Starting state: Package is open; no credentials are required.
Action: Open templates/sample.json in a text editor. Identify the three demo records and their fields. Keep an unchanged copy.
Expected result: Only made-up identities or serials are present.
Verification: For access, inspect boolean active and groups; for devices, inspect OS, owner and three boolean checks.
Recovery: Do not paste tenant exports. Restore the bundled synthetic input if fields are changed accidentally.

### 3. Run the review
Starting state: Original sample is available.
Action: Run python3 scripts/review.py templates/sample.json > output.json. Open output.json.
Expected result: Access: demo-01 proposes it-tools; demo-02 proposes removing two groups; demo-03 no-change. Device: two ready-for-human-check records and one review record with three issues.
Verification: Compare the entire output with evidence/sample-output.json. Source files and real services must remain unchanged.
Recovery: Read the error. Fix malformed JSON, missing/duplicate identifiers or string booleans. Rerun; do not hide the error.

### 4. Check behaviour
Starting state: First run completed.
Action: Run python3 -m unittest discover -s tests -v.
Expected result: Eight test methods pass for this package.
Verification: Read all eight names and the OK summary; compare with evidence/tests.txt.
Recovery: If a test fails, keep its output, restore the source/sample and rerun the affected case before the complete suite.

### 5. Break and repair a realistic case
Starting state: Copy sample.json to a temporary scratch.json; preserve the original.
Action: Access: duplicate a record ID, run review and capture the failure; then remove the duplicate. Device: duplicate a serial, capture the failure and restore uniqueness. Run again.
Expected result: Invalid identity/asset input is rejected; the repaired input produces a review.
Verification: A rejected run has a non-zero exit code and names the duplicate; the repaired output matches the intended records.
Recovery: If an invalid input passes, stop and fix validation before trusting the report. Delete scratch.json only after capturing the learning.

### 6. Check a change without changing a service
Starting state: Use a separate scratch copy.
Action: Access: put demo-01 in both expected groups and remove all groups for the inactive demo-02, then rerun. Device: set the iOS record owner to demo-02, managed and patched to true, then rerun.
Expected result: Access now proposes no changes; device now has no listed issues. These are changes to dummy data only.
Verification: Confirm the original sample file is unchanged and explain why the dummy correction changes the output.
Recovery: A clean model output is not actual account removal or device security. Keep service/device verification separate.

### 7. Write the handover
Starting state: Local normal and failure runs captured.
Action: Create a short note: request, input version, proposed action, reviewer, user check, failure and repair. Attach permitted test output.
Expected result: A colleague can explain the report and why review is required.
Verification: Ask yourself to trace one result to source logic and one failed case to the input.
Recovery: If you cannot explain it, review the function line by line before presenting this as your own learning evidence.

### 8. Prepare an authorised Okta sandbox — unrun
Starting state: Separate training organisation, no real staff, authorised admin access and confirmed Workflows/lifecycle licences.
Action: Follow current Okta guidance to obtain a training environment. Confirm the console exposes Directory > Groups and Workflow > Workflows console. Use synthetic profiles and a test app only; record entitlement/cost before starting.
Expected result: A documented isolated practice environment, or a recorded access/licence blocker.
Verification: Check the organisation URL, permissions and licence with the owner; never point this lab at a live employer tenant.
Recovery: If feature entitlement is absent, stop native steps and retain the local model. Do not assume a free plan includes every product.

### 9. Create groups and a rule — unrun
Starting state: Authorised isolated tenant.
Action: Directory > Groups: add lab-all-staff and lab-it-tools. Create two dummy users with department IT and Support. In group rules, create an IT department rule for lab-it-tools, preview matching users, then activate only after reviewing the two expected matches/non-matches.
Expected result: IT test user joins the IT group; Support test user does not.
Verification: Capture permitted group membership and rule preview; change department on a test profile and recheck.
Recovery: Disable the lab rule if scope differs from expectation; remove accidental test membership and fix the condition.

### 10. Build a small flow — unrun
Starting state: Lab users/groups exist; Workflows access confirmed.
Action: In Workflows console create a folder and a new flow. Add an Okta user-created event, read the test user, compare department with IT, and add only the matching user to the lab group using the Okta connector. Keep flow off while testing cards; use exact IDs from your lab console.
Expected result: A tested flow handles a synthetic IT user and ignores Support; each run has visible history.
Verification: Inspect card inputs/outputs and group membership; record a failed connection and corrected run.
Recovery: If connection fails, inspect authorisation and permitted scopes with the tenant owner. Do not add broad privileges just to remove an error.

### 11. Test SCIM provisioning and deactivation — unrun
Starting state: An authorised test SCIM-capable app with licensing, synthetic accounts and administrator review.
Action: Add the app using its vendor guide. Enable only required create/update/deactivate features in Provisioning, map required profile attributes and assign a lab group. Verify downstream account creation, then deactivate a synthetic user and verify downstream active=false and denied login. Record app-specific routes and logs.
Expected result: A verified joiner and leaver path in an actual training integration. The local package is not a SCIM server.
Verification: Compare Okta assignment, provisioning task and downstream account/login result; confirm no real user is in scope.
Recovery: If provisioning fails, inspect mapping, test-app connection and task logs; do not retry blindly or delete account data. Deactivation and deletion are different actions.

### 12. Clean up native practice — unrun
Starting state: Native tests completed or stopped.
Action: Turn off lab flows and rules. Remove lab app assignments, confirm downstream deactivation, then remove synthetic users/groups and revoke temporary connections according to the lab owner’s rules. Keep sanitised evidence.
Expected result: No lab access or temporary integration remains.
Verification: Review remaining lab users/groups/apps and the downstream account state.
Recovery: If you cannot confirm removal, leave an owned cleanup task and do not declare cleanup complete.

## I. Break/fix
Duplicate identity/serial rejection and repair; malformed booleans and unknown categories rejected by tests. Native fault paths are unrun until permitted access is available.

## J. Acceptance
Eight passing local behavioural tests, output matches the three synthetic records, no input mutation and no real changes. Native completion requires real permitted product/device logs and a demonstrated failure/repair. Local tests cannot satisfy that requirement.

## K. Artefacts and actual evaluation
scripts/review.py, templates/sample.json, tests, evidence/sample-output.json, evidence/tests.txt and narrative files. Codex authored and ran the local slice. Bunamin’s independent reproduction, native integration and workplace outcome remain pending. No baseline timing or savings measured.

## L. Interview story
Explain recurring need → limited dummy data → rule choice → one result → rejected input → repair → verified scope. Explain why a ready report is not proof of live access/device readiness. State what you personally changed or checked.

## M. Conditional wording
Use only after Bunamin personally reproduces and saves evidence: “Reproduced a synthetic access-lifecycle review lab, tested normal and invalid inputs and documented human-review boundaries.” Native product experience needs separate exact evidence. Do not call it commercial delivery.

## N. Extension and cleanup
Add a reviewed read-only integration only after authorisation and licence checks; retain the rule baseline. Local cleanup: remove your scratch files/output and optional virtual environment, retain permitted evidence and original sample. Native cleanup is the final unrun step above. No autonomous remediation or access grants.
