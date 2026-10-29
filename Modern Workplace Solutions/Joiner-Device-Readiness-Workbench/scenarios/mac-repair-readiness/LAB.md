# Device and repair readiness lab

## A Outcome and state
Use an explicit checklist to rehearse device handover and repair escalation before a human decision. Local tool implemented; native device/MDM/AV work and Independent personal rebuild are unrun. Allow one half-day offline and one supervised practice session; planning estimate, not measured effort.

## B Public need and inference
OpenAI's IT Support Specialist advert includes repeatable device workflows and supplier/equipment coordination. Source: https://openai.com/careers/it-support-specialist-san-francisco/ , checked 29 October 2026. The fictional asset and repair request is an independent teaching scenario, not an internal OpenAI system or commissioned work.

## C Job mapping
managed Mac gap, device tools, repeatable workflows and stock/repair handover. This is process practice; it cannot prove independent professional delivery.

## D Gap and personal evidence
Build on Microsoft software support, case ownership and documentation. Managed macOS and physical repair remain explicit gaps. Intune support does not establish Jamf. Assistant implementation/tests remain separate from candidate practice.

## E Recurring value
A support engineer repeats this workflow at each joiner, return or repair handover. It makes missing evidence visible. Reduced incidents/time saved are targets only, with no workplace baseline or measured improvement.

## F Architecture and simpler baseline
Fictional local JSON goes through schema checks and pass/fail/unknown rules to a JSON report; a human reviews. No network, credentials, tenant writes, hardware probe, calendar action or AI generation. A paper checklist is the baseline. AI adds no clear value to this deterministic gate. Optional later summaries need evidence checking and must never authorise access or go/no-go.

## G Prerequisites, cost and setup
Python 3.11+ and a text editor. No packages or account required offline; marginal cloud cost £0. Clone Thinkbox when network is available, then open "Modern Workplace Solutions/Joiner-Device-Readiness-Workbench/scenarios/mac-repair-readiness". Alternatively use this prepared public folder. Run python3 --version; on Windows use py instead. Confirm scripts/check.py, tests/ and templates/sample.json exist. If Python/files are missing, install from the official Python source or recover the exact folder. Native Mac/MDM practice needs authorised test equipment, approval and a reviewer. Do not purchase hardware or start paid trials. With no access, retain the offline scope.

## H Implementation with expected results and recovery

### Step 1: Record the support request
Starting state/action: Create notes.md with fictional user Example Learner, request DEMO-01, permitted task and expected handover date. State that this is a training scenario.
Expected result/check: A bounded request with an owner and no real employee data.
Recovery/boundary: If the task is vague, define the one application or device function to verify before proceeding.

### Step 2: Inspect the synthetic inventory
Starting state/action: Open templates/sample.json. asset_id DEMO-MAC-01 is fictional; each check is pass. Read scripts/check.py. The program checks supplied records only.
Expected result/check: Five pass checks and a named owner in a valid JSON object.
Recovery/boundary: A flag is not an observed device state. Keep any unobserved native check unknown.

### Step 3: Run the baseline report
Starting state/action: Run python3 scripts/check.py templates/sample.json. Compare its five checks with a paper checklist.
Expected result/check: ready_for_human_review, with no issues. This is not authorisation to issue a device.
Recovery/boundary: If parsing fails, run python3 -m json.tool templates/sample.json and correct the syntax in a copy.

### Step 4: Expose a missing asset match
Starting state/action: Copy sample.json to templates/broken.json. Set asset_matched to fail and run the same command using broken.json.
Expected result/check: hold with asset_matched in issues.
Recovery/boundary: Compare the fictional asset tag to the fictional receipt; correct the fixture only when the mismatch is explained. Rerun and retain both outputs.

### Step 5: Expose unverified management
Starting state/action: Restore asset_matched to pass; set enrolment_reviewed to unknown. Run again.
Expected result/check: review with enrolment_reviewed listed.
Recovery/boundary: Unknown management state must not pass. Obtain an authorised reviewer or keep the handover blocked.

### Step 6: Plan the native Mac session
Starting state/action: Obtain a dedicated permitted test Mac and a mentor. Record OS version, owner approval and rollback. Read Apple device-enrolment guidance before considering a profile. Do not enrol a personal/work Mac to an unknown MDM.
Expected result/check: A session plan distinguishing local practice from organisation-owned automated enrolment. Native stage remains unrun here.
Recovery/boundary: If device or approved MDM/trial access is absent, continue the offline exercise and retain the product gap.

### Step 7: Practise non-destructive inspection
Starting state/action: On that permitted test Mac, open Apple menu > About This Mac and System Settings. Record version and a fictional local asset reference. Inspect Privacy & Security and, if present, Device Management. Do not remove profiles, disable FileVault or record recovery keys.
Expected result/check: Notes identify observed state and which checks need an administrator. No management change.
Recovery/boundary: If a menu differs by OS or a setting is enforced, use the current Apple guide and stop at the permission boundary.

### Step 8: Rehearse repair and supplier handover
Starting state/action: Simulate a failed display or application request using written scenario cards. Log symptom, user impact, permitted checks, asset reference, warranty/repair question, owner and next update. Make no purchase or supplier contact.
Expected result/check: A repair request with accountable owner and handover checks, not a claimed physical repair.
Recovery/boundary: If the cause is unknown, report observations and escalation need rather than diagnosing a failed component.

### Step 9: Verify the handover task
Starting state/action: Ask a peer to read the runbook and repeat a harmless test task on the permitted device. Record expected/actual result and their questions. Change fixture checks to pass only for the simulated case being assessed.
Expected result/check: A repeatable check plus an honest list of unrun management/repair steps.
Recovery/boundary: A successful sign-in alone does not establish every security or inventory check. Keep remaining states unknown.

### Run the behavioural checks
From this scenario folder run python3 -m unittest discover -s tests -v. Expect 12 passing tests. Save complete output and runtime. If a test fails, preserve input and traceback, explain the mismatch and fix the cause before rerunning. Never delete a failing assertion simply to make the report green.

## I Break, fix and observe
Repeat the fail and unknown cases without overwriting the baseline. Save original input, failed report, cause, corrective action, rerun and remaining limits. Include one invalid input such as removing owner: expect visible input error/exit 2. Restore the copy and verify the normal result. Do not claim that changing a fixture repaired real hardware or a meeting.

## J Acceptance checks
Normal fixture: ready_for_human_review. Any fail: hold. Unknown without fail: review. Missing ID/owner/check or unsupported values: reject. Failed checks take priority over unknowns. Review does not alter inputs. CLI input failures exit 2. Manually compare each result with the paper checklist. Real-world acceptance additionally needs observed native evidence, accountable approval and peer replay; these remain unrun. No live security, device or AV reliability claim follows from local tests.

## K Evidence and cleanup
Keep LAB, README, source/tests, synthetic input, architecture, failed/normal outputs, runtime/source hashes, peer questions and a short demo. Export no personal data, serial number, email, recovery key, recording or tenant screenshot. Delete only templates/broken.json and disposable outputs after preserving useful evidence. Restore any authorised test-session settings to the recorded starting state and leave calls. Do not remove management profiles or parent-project files. Verify no account/subscription was created.

## L Interview explanation
Problem: missing observations can hide a support risk. Constraint: no employer access and unproven native skills. Design: a small explicit checklist instead of AI. Build: explain your actual contribution. Failure: show an unknown and a fail case. Verification: compare actual outputs, repeat a peer-observed native check only after doing it. Value: more reviewable handovers, not claimed savings. Next: close the native gap under review.

## M Wording only after personal completion
Use only after Bunamin independently runs and explains the work: "Built and checked a synthetic workplace readiness workflow, recorded failure and unknown cases, and documented an operator handover." Replace with exact personal actions and links. Add native Mac/AV scope only when actually practised and evidenced. Do not call it production or commissioned work. LinkedIn wording remains a draft.

## N Extension and technical references
Add a read-only approved inventory or rehearsal-record adapter only after entitlement, owner approval and data rules are checked. Compare actual observations against reported values and test stale/missing evidence before considering automation. No direct live actions or purchases are part of this lab.
Apple device-enrolment reference: https://support.apple.com/en-gb/guide/deployment/dep73069dd57/web . Automated organisation-owned enrolment differs from a local simulation.
Sources reviewed 29 October 2026. Menu/version and licensing details must be checked before the native session.
