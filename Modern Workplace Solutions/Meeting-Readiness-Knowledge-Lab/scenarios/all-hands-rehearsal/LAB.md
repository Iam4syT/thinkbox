# All-hands AV rehearsal lab

## A Outcome and state
Use an explicit checklist to rehearse meeting preparation, remote checks and fallback before a human decision. Local tool implemented; native device/MDM/AV work and Independent personal rebuild are unrun. Allow one half-day offline and one supervised practice session; planning estimate, not measured effort.

## B Public need and inference
OpenAI's IT Support Specialist advert includes all-hands technical delivery and clear cross-team communication. Source: https://openai.com/careers/it-support-specialist-san-francisco/ , checked 29 October 2026. The fictional meeting and room is an independent teaching scenario, not an internal OpenAI system or commissioned work.

## C Job mapping
clear updates, repeatable processes and AV operations. This is process practice; it cannot prove independent professional delivery.

## D Gap and personal evidence
Build on Microsoft software support, case ownership and documentation. Weekly peer training is relevant communication experience, not high-production AV experience. Native room equipment and producer judgement remain untested. Assistant implementation/tests remain separate from candidate practice.

## E Recurring value
A support engineer repeats this workflow before every meeting/event and after equipment changes. It makes missing evidence visible. Reduced incidents/time saved are targets only, with no workplace baseline or measured improvement.

## F Architecture and simpler baseline
Fictional local JSON goes through schema checks and pass/fail/unknown rules to a JSON report; a human reviews. No network, credentials, tenant writes, hardware probe, calendar action or AI generation. A paper checklist is the baseline. AI adds no clear value to this deterministic gate. Optional later summaries need evidence checking and must never authorise access or go/no-go.

## G Prerequisites, cost and setup
Python 3.11+ and a text editor. No packages or account required offline; marginal cloud cost £0. Clone Thinkbox when network is available, then open "Modern Workplace Solutions/Meeting-Readiness-Knowledge-Lab/scenarios/all-hands-rehearsal". Alternatively use this prepared public folder. Run python3 --version; on Windows use py instead. Confirm scripts/check.py, tests/ and templates/sample.json exist. If Python/files are missing, install from the official Python source or recover the exact folder. Native room/conferencing practice needs authorised test equipment, approval and a reviewer. Do not purchase hardware or start paid trials. With no access, retain the offline scope.

## H Implementation with expected results and recovery

### Step 1: Write the event brief
Starting state/action: Create notes.md for fictional event DEMO-ALLHANDS-01. Name producer, room operator, remote checker, start/end, audience, backup and stop conditions. Use dummy slides.
Expected result/check: A rehearsal plan with responsible roles and no actual event commitment.
Recovery/boundary: If only one person is available, mark remote verification unrun and arrange a peer session.

### Step 2: Inspect the checklist
Starting state/action: Open templates/sample.json. Its five pass values are invented example observations. Read scripts/check.py.
Expected result/check: A rehearsal record with owner and event ID.
Recovery/boundary: Do not copy example passes into evidence for a real room.

### Step 3: Run the manual and tool checks
Starting state/action: Run python3 scripts/check.py templates/sample.json; tick the same five fields on paper.
Expected result/check: ready_for_human_review with no issues, identical to the manual rules.
Recovery/boundary: An event producer still decides go/no-go. The program cannot listen, see, join a call or verify cabling.

### Step 4: Break the remote path
Starting state/action: Copy sample.json to templates/broken.json. Set remote_audio_tested to fail and rerun against broken.json.
Expected result/check: hold, even if the room microphone is marked pass.
Recovery/boundary: Explain why local meter movement does not prove remote participants hear sound. Restore only after a new remote-side test.

### Step 5: Make missing evidence visible
Starting state/action: Set remote_audio_tested to unknown and rerun.
Expected result/check: review. The app must not turn a missing result into ready.
Recovery/boundary: Keep the remote check pending until a peer confirms what they heard.

### Step 6: Prepare a permitted practice space
Starting state/action: Use a test Mac, headphones, camera, external screen if available and a second participant/device. Use an approved conferencing service/account; no live all-hands or recording. Keep speaker volume low.
Expected result/check: A private rehearsal with consent and dummy content.
Recovery/boundary: If equipment/account is absent, use a storyboard and label native evidence unrun. No paid licence or new account is required for the offline part.

### Step 7: Check one route at a time
Starting state/action: In System Settings > Sound, select the intended input/output and observe a harmless spoken test. Open the approved meeting app test/prejoin screen. Inspect app microphone/camera permissions under Privacy & Security.
Expected result/check: Known input/output route and the app-specific permission state.
Recovery/boundary: An OS microphone permission and browser/site permission may differ. Request only needed access in the test session; never bypass enforced settings.

### Step 8: Rehearse the remote experience
Starting state/action: Have the remote checker join the private test call with headphones. Share dummy slides, speak one sentence, play permitted test audio only if that feature is in scope, and ask them to confirm picture, voice and display separately.
Expected result/check: Written remote observations, not just a local preview.
Recovery/boundary: For no sound, check mute, selected input/output and app/site permission in order. Change one item, repeat the same sentence and record the outcome.

### Step 9: Rehearse failure and fallback
Starting state/action: In the practice call mute the intended app microphone, confirm remote silence, restore it and repeat. Then rehearse the agreed fallback, such as a second approved host/device or audio-only handover.
Expected result/check: A recorded failure, fix and independently confirmed fallback result.
Recovery/boundary: Do not unplug unfamiliar powered room hardware or change live equipment. If backup cannot be verified, mark backup unknown and escalate to the producer.

### Step 10: Write the run of show
Starting state/action: List preflight, producer check, host handover, remote check, incident messages and closure. Ask a peer to follow it with dummy material.
Expected result/check: An operator can identify who decides go/no-go and what to do if the remote path fails.
Recovery/boundary: A home rehearsal does not establish high-production event competence. Request supervised real-room practice separately.

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
Apple privacy/microphone reference: https://support.apple.com/en-gb/guide/mac-help/mchla1b1e1fe/27/mac/27 . App and site permissions depend on version; use current vendor guidance for the approved meeting app.
Sources reviewed 29 October 2026. Menu/version and licensing details must be checked before the native session.
