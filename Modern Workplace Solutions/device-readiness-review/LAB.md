# Device readiness and asset handover with an Apple practice path

Status: local Python slice evaluated by Codex; native product/device path unrun; Bunamin reproduction pending.

## A. Outcome
Find missing asset and readiness checks before handing over a device.

## B. Company research and limits
The Clio advert asks for proactive support, onboarding, access and endpoint operations. Its dated expansion provides context; this scenario is an independent learning hypothesis, not a report of an internal Clio fault.

## C. Role mapping
R5/R6/R2: mixed-device support, asset lifecycle, procurement/repair handover and clear tickets.

## D. Gap mapping
First-line Intune transfers; managed Apple and physical/asset operations remain Not Yet Evidenced.

## E. Repeated-use test
An IT specialist checks each allocation/return and daily exceptions. The testable target is catching missing ownership/management/update checks; no real fleet efficiency is measured.

## F. Architecture and simpler baseline
Synthetic JSON → Python validation/rules → proposed review report → human review. No network, API, login or change execution. A manual checklist is the baseline. No AI is used: deterministic checks are clearer and do not need to interpret sensitive employee data. Native practice is a separate path.

## G. Prerequisites, cost and estimate
Local: Python 3.11+, editor, three synthetic records, no packages/accounts or paid service. Estimate 60–90 minutes for personal local practice, not measured actual time. Native: separate authorised spare Apple device, backup and test management service; hardware/licence cost unknown and no spend authorised. Do not connect to employer systems.

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

### 8. Prepare a device practice environment — unrun
Starting state: An owned spare Mac/iPhone or iPad, consent, backup and an authorised test device-management service.
Action: Record device serial, OS, owner, backup and enrolment permissions in a private lab inventory. Confirm test service costs and that remote erase is excluded from this exercise. Do not assume Clio uses Intune or Jamf; the advert does not name its management product.
Expected result: An approved, backed-up practice device and known management boundary.
Verification: Confirm the device/service owner and follow current Apple enrolment guidance.
Recovery: If no spare device or test service exists, stop the native path. Reading the local dummy inventory is not Apple management experience.

### 9. Inspect the Apple device — unrun
Starting state: Backed-up authorised device; no enrolment change yet.
Action: On a Mac, record OS in About This Mac, check Software Update and FileVault status in System Settings, and inspect device-management/profile settings. On iPhone/iPad, inspect General > About, Software Update and VPN & Device Management. Do not infer encryption status solely from the JSON model.
Expected result: Actual device observations recorded with timestamp and model/OS.
Verification: Compare observations with the private inventory and record unknown values; current UI routes may vary with OS.
Recovery: If settings are missing, use current Apple documentation for that OS. Do not disable security or change an unknown profile.

### 10. Enrol and verify a test device — unrun
Starting state: Owner-approved isolated service and current vendor enrolment guide.
Action: Follow that test service’s Apple enrolment guide, install only its authorised enrolment profile, and confirm the device appears with the same serial. Apply a harmless test setting chosen with the owner; record before/after and service check-in.
Expected result: An actual management check-in and observed test setting.
Verification: Compare service record, serial, timestamp and device setting; keep the exact vendor route in the evidence.
Recovery: If check-in fails, inspect enrolment and connectivity. Remove only the authorised lab profile through the approved route; do not erase or reset the device.

### 11. Practise ticket and vendor handover — unrun
Starting state: A synthetic readiness issue is documented.
Action: Create a dummy ticket with asset ID, symptom, checks, proposed next step, owner and next update. Prepare a dummy repair request with warranty and delivery/return checks; do not send it. Review serial and user-access fields for mistakes.
Expected result: A traceable ticket and draft vendor handover; no purchase or vendor contact.
Verification: A reviewer can match ticket, asset record and expected repair/return step.
Recovery: If owner/serial mismatch, hold handover and correct records before any real procurement or shipment.

### 12. Clean up device practice — unrun
Starting state: Authorised test completed.
Action: Remove the lab setting/profile using the service’s authorised unenrolment route; confirm the device no longer checks in and private inventory records return/closure. Preserve backups and personal content.
Expected result: Test management removed without data loss, or an explicit pending cleanup task.
Verification: Check both device profiles and service record; record the owner’s acknowledgement.
Recovery: Do not erase to force cleanup. Escalate if the owner-approved removal path fails.

## I. Break/fix
Duplicate identity/serial rejection and repair; malformed booleans and unknown categories rejected by tests. Native fault paths are unrun until permitted access is available.

## J. Acceptance
Eight passing local behavioural tests, output matches the three synthetic records, no input mutation and no real changes. Native completion requires real permitted product/device logs and a demonstrated failure/repair. Local tests cannot satisfy that requirement.

## K. Artefacts and actual evaluation
scripts/review.py, templates/sample.json, tests, evidence/sample-output.json, evidence/tests.txt and narrative files. Codex authored and ran the local slice. Bunamin’s independent reproduction, native integration and workplace outcome remain pending. No baseline timing or savings measured.

## L. Interview story
Explain recurring need → limited dummy data → rule choice → one result → rejected input → repair → verified scope. Explain why a ready report is not proof of live access/device readiness. State what you personally changed or checked.

## M. Conditional wording
Use only after Bunamin personally reproduces and saves evidence: “Reproduced a synthetic device-readiness review lab, tested normal and invalid inputs and documented human-review boundaries.” Native product experience needs separate exact evidence. Do not call it commercial delivery.

## N. Extension and cleanup
Add a reviewed read-only integration only after authorisation and licence checks; retain the rule baseline. Local cleanup: remove your scratch files/output and optional virtual environment, retain permitted evidence and original sample. Native cleanup is the final unrun step above. No autonomous remediation or access grants.
