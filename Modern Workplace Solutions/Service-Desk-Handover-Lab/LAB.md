# Service desk triage and call ownership lab

Status: Codex-authored local learning asset. Fixture tests can be executed by Codex; Bunamin completion and Windows/live work remain unrun.

## Outcome and role relevance

Produce a consistent offline triage queue and traceable handover for repeated support incidents. the general first-line support workflow asks for accurate ITSM recording, prioritisation and lifecycle ownership. This is a proposed learning solution, not evidence of a healthcare service desk’s internal ticket problems or actual priority rules.

## Architecture and baseline

Synthetic sample.json → Python validation and demonstration priority rule → output.json → analyst-owned state updates. No ITSM connection, patient information, credentials or AI. Baseline: read the three tickets manually and record priority/owner/next action in a simple table. The script should agree with that demonstration policy and reject incomplete inputs.

## Prerequisites and cost

Use Python 3.10 or later on a personal computer and a text editor. No extra packages, licences, cloud account or API bill. Run only the public folder copied from this private solution. Planning budget: one short practice session for the offline flow, followed by a separate employer-approved tool orientation; time is not measured or guaranteed.

## Step 1 Start in the project folder

Starting state: a copy of the public folder, with triage.py, test_solution.py and sample.json. Open a terminal there. Run python3 --version (Windows: py --version). Expected: 3.10 or newer. Verify the displayed version, then list files with ls (Windows: dir). Recovery: select a Python 3 installation; do not install packages or change a work computer without authority.

## Step 2 Establish a manual baseline

Open sample.json in an editor; do not change it. Write DEMO-01 P1, DEMO-02 P2 and DEMO-03 P3 in a scratch note. Rule: critical service without workaround P1; otherwise at least five affected users P2; otherwise P3. Verify users and booleans for each case. Recovery: reread the fixture. These priorities are illustrative, not a clinical or employer policy.

## Step 3 Run the behaviour checks

From the same folder run python3 -m unittest -v. Expected: seven test methods pass, including invalid input, ownership and verification before closure. Verify the final OK and exit code. Recovery: inspect the failing method and restore the supplied source/fixture; do not change an expected outcome merely to obtain a pass.

## Step 4 Generate the queue

Run python3 triage.py triage sample.json output.json. Expected: three records sorted P1 to P3, state new, owner null, next action requesting human confirmation. Open output.json and compare each ID/priority with the manual baseline. Recovery: invalid JSON or missing fields causes an error without publishing a partial output; repair a copy of the synthetic input and retry.

## Step 5 Assign a case

Run python3 triage.py update output.json DEMO-01 assigned --owner analyst-demo --note "Accepted synthetic case and confirmed impact". Expected: DEMO-01 assigned with owner and one history item. Verify DEMO-02/03 are unchanged. Recovery: missing owner or an unknown ID is rejected; use the correct ID and a non-empty note.

## Step 6 Escalate with ownership retained

Run python3 triage.py update output.json DEMO-01 escalated --note "Synthetic application remains unavailable specialist review needed". Expected: state escalated and owner analyst-demo retained. Verify two history entries. Recovery: direct new-to-escalated is intentionally unsupported; assign first. Real escalation routes and SLAs must come from the employer.

## Step 7 Demonstrate verification before closure

Attempt python3 triage.py update output.json DEMO-01 resolved --note "Fixed". Expected: explicit-verification error. Confirm output.json still shows escalated. Then use --verified with the note "Synthetic retest confirms the test task works". Expected: resolved, not closed. The flag is a recorded assertion, not proof that a real user or system was checked.

## Step 8 Record closure separately

Run python3 triage.py update output.json DEMO-01 closed --note "Synthetic user confirms test task works" --verified. Expected: closed with complete history. Verify original summary and owner remain visible. Recovery: if confirmation is absent, leave unresolved/escalated; never invent a user confirmation to close a real ticket.

## Step 9 Break input and recover

Copy sample.json to broken.json. Set users on DEMO-02 to 0 and run triage broken.json broken-output.json. Expected: validation error and no output file. Restore users to 8. Then duplicate DEMO-01’s ID on another record; expected duplicate-id error. Restore distinct IDs. Finally remove critical_service; expected boolean error. Rerun valid input to a different output file, preserving the lifecycle evidence.

## Step 10 Compare and capture evidence

Save command output, test log and a sanitised queue screenshot in evidence/. Compare manual and script priority on all three fixtures, and confirm invalid/duplicate input does not overwrite prior output. Expected: agreement on three illustrative cases and traceable state changes. Recovery: record discrepancy and revise logic only after explaining which policy should apply; do not report live SLA or care outcomes.

## Acceptance and failure cases

Accept the offline learning baseline only when three fixture priorities match, owner/history survive escalation, resolution/closure require explicit verification, missing/invalid/duplicate fields reject, and no real data is used. Further cases to add: multi-site criticality, unavailable workaround, urgent single-user clinical task and policy changes. This tiny sample does not validate operational prioritisation.

## Cleanup and operating handover

Keep sample.json, source, tests and sanitised evidence. Delete only generated output.json, broken.json and broken-output.json when finished. Review a copy of output before deletion. To hand over, explain the demonstration rule, required fields, permitted states and human approval boundary. No tenant, ITSM account or cloud resource needs removal.

## Toothbrush test and limitations

The repeated task is making each incident’s impact, owner, checks and next action understandable during every shift. This prototype is single-user and offline; it lacks concurrency, authentication, retention controls, timestamps and real SLA calculations. An operational tool requires employer review, real policy mapping and secure integration.

## Interview story and conditional wording

After personally completing the lab: explain the need, your changes, rule rationale, refused inputs, closure guard and limitations. Conditional CV wording: Built and tested an offline synthetic incident handover prototype with explicit ownership and verification checks. Use only after Bunamin performs and can explain the work; Codex authoring is disclosed in CONTRIBUTIONS.md.

## Optional AI extension

Only after the deterministic baseline: propose a draft incident-summary assistant using synthetic tickets. Evaluate factual completeness and unsafe omissions against the manual summary; require analyst approval. Do not send real NHS or patient data to an unapproved service. No AI component was built or evaluated in this run.
