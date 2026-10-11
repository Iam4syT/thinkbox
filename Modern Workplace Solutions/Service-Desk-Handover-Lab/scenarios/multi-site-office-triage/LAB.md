# Lab 1 — Clear ticket diagnosis and useful repeat-issue guidance

## A. Purpose and present status
Make a fictional support queue easier to investigate and hand over. The offline Python tool and twelve behavioural tests were run by Codex on 11 October 2026. Bunamin has not yet reproduced this exercise. It does not connect to the fictional office or repair a real device.

## B. Fictional learning context
A fictional office team needs clear support handover and permitted access/device checks. This additional scenario is independent learning, not a report of an employer’s incidents or systems.

## C. Job requirements exercised
customer communication, diagnosis/escalation, accurate tickets/trends, sharing guidance and organisation/detail. Telephone intake is practised through written prompts; a script cannot demonstrate a real call. Python is a portable learning tool, not an advertised employer product.

## D. Candidate gap and evidence boundary
Build on reported Tek case ownership, Microsoft diagnosis and FirstBank incident tracking. Practise turning those habits into a repeatable handover and a small knowledge article. This strengthens practical evidence after personal completion; it does not replace physical deskside practice or prove knowledge of the fictional office’s systems.

## E. Repeated-use value
An analyst could use the checklist at intake and each shift handover, then review repeated categories weekly. Intended value: clearer ownership and fewer missed checks. Neither reduced ticket volume nor saved time has been measured. Compare the result with a manual four-row checklist before proposing any integration.

## F. Architecture and simpler baseline
Fictional sample.json → local validation → explicit demonstration policy → result.json → human investigation and user update. The tool retains an owner, suggests a check, keeps all tickets open and counts repeated categories. It makes no network call or access change. Security concerns go to specialist review even when a workaround exists. Other critical services without a workaround receive P1; at least five affected users receive P2; the remainder receive P3. These priorities are teaching rules, not employer service targets. Baseline: apply exactly those rules by hand. AI adds no necessary value to this small decision problem.

## G. Prerequisites, cost and time plan
Use the published scenario folder or this solution’s public folder, Python 3.10 or newer, a terminal and a text editor on a personal authorised computer. No packages, cloud account, ITSM licence or paid API is needed. Existing computer/Python use adds no lab service charge. Allow 60–90 minutes as a planning estimate, not an observed duration. On Windows, replace python3 with py -3. No Windows device is required for this offline exercise.

## H. Granular implementation steps
### H1. Find the correct folder
Start with a complete copy of public containing solution.py, test_solution.py, sample.json and evidence. Open a terminal there: on Windows use File Explorer’s address bar, type powershell and press Enter; on macOS open Terminal and use cd followed by the quoted folder path. Run python3 --version, then list files with ls (Windows: dir). Expect Python 3.10+ and the named files. Verify the version and filenames. If missing, select a known Python installation or recover the complete folder before continuing; do not alter a work computer without authority.

### H2. Make the manual baseline
Open sample.json in the editor without changing it. Write a note: OFF-01 P3; OFF-02 P2; OFF-03 P1 security review; OFF-04 P1 specialist escalation. Read users, critical, workaround and security_concern to explain each decision. Expect mail to appear twice. Verify each decision against section F. If uncertain, reread the rule rather than using an assumed real employer policy.

### H3. Run the checks
In the same terminal run python3 -m unittest -v. Expect twelve test methods and final OK. Read the method names: the suite includes security priority, the five-user boundary, missing fields, duplicate IDs and keeping tickets open. Save your actual terminal result as evidence/learner-tests.txt. If a test fails, retain its error and compare your changed source with the supplied version. Do not edit the expected result merely to obtain a pass.

### H4. Generate a reviewable queue
Run python3 solution.py sample.json learner-result.json. Expect a new JSON file with four tickets in this order: OFF-03, OFF-04, OFF-02, OFF-01. Open it; compare every priority with your manual note. Check owner, diagnostic_check and user_update are present and state is open. Expect repeat_categories to contain mail: 2. If the command reports a file error, confirm you are in the correct folder. If JSON is invalid, restore the fixture before trying again.

### H5. Investigate one fictional mail call
Use OFF-01. Write a ticket note with the symptom, number affected, start time marked unknown, any error marked unknown, the permitted web-access check, workaround status, owner and next update. Do not invent facts the fixture lacks. Explain to a role-playing user: “I will check whether web access works and record the desktop error. I will explain the next step after that check.” Expect a usable note with unknowns visible. Verify it separates an observed check from a proposed check. If you cannot check the application, leave the test pending and explain the escalation; do not claim a repair.

### H6. Hand over a security concern
Use OFF-03. Read the suggested security route. Draft a handover containing the fictional ID, reported concern, impact, available evidence and owner. Preserve evidence and involve the designated specialist; do not ask for passwords or alter forwarding rules without authority. Expect the analyst to retain case ownership while requesting review. Verify no automatic fix or closure is stated. If authority or route is unclear, record that as the next question.

### H7. Turn a repeated category into useful guidance
Create a short knowledge note for the two mail cases: symptom; safe initial questions; permitted web check; evidence to record; when to escalate; how the user confirms the original task works. Add an owner and a review date. Expect a proposal for review, not an approved article. Have another reader explain its next step without help. If they cannot, simplify the wording and keep the failed version as learning evidence. Two mail cases are only a category signal, not proof of one shared cause.

### H8. Capture and prepare the demo
Save your manual note, learner result, handover and knowledge note under evidence/ with fictional names. Compare input and output: source input remains unchanged and all cases remain open. Capture a screenshot showing one ordinary and one security case. Expect a reader to see the policy and its limit. Remove private names, actual tickets or tenant IDs if any were accidentally added; keep private evidence outside the public project.

## I. Break, diagnose, fix and verify
Copy sample.json to broken.json. Change OFF-02 users to true, then run python3 solution.py broken.json rejected.json. Expect Invalid users and no new rejected.json. Restore 8 and repeat: expect a valid output. Next duplicate OFF-01’s ID onto OFF-02; expect Duplicate id. Restore its distinct ID and verify success. Finally change OFF-03 security_concern from true to false in a separate copy: its lower priority shows why accurate intake matters. Restore true and verify security review returns. Record the failed inputs and actual errors; never change a real ticket to manufacture an outcome.

## J. Acceptance checks and limits
Accept the offline exercise only when the four decisions match your manual baseline, twelve tests pass, security overrides the workaround, ownership/updates remain visible, invalid inputs are refused and the original input is unchanged. A local declared flag is not proof of a customer check. A production system would need real policy, identity controls, retention, audit history, concurrency and approved integration; none is implemented. No live repair, service improvement or learner proficiency is established by Codex’s test run.

## K. Artefacts and cleanup
Keep source, fixture, test log, result, architecture note, knowledge note and a short case study. A video is optional and unrecorded. Delete only your disposable broken.json, rejected.json and learner-result.json after keeping permitted evidence. Do not remove the supplied evidence or unrelated files. No tenant, licence or cloud resource was created. The public package credits Codex; this private company mapping stays outside it.

## L. Interview story after personal completion
Explain the recurring intake/handover need; the constraint that no real system was available; why transparent rules were chosen; what you changed; how a security concern outranked a workaround; the invalid input you diagnosed; how you checked the result; and the intended value of understandable ownership. End with the real limitation and your next policy test. Do not say the fictional office adopted the tool.

## M. Conditional CV or LinkedIn wording
Use only after Bunamin completes, changes and can explain the exercise: “Adapted and tested a Codex-assisted offline ticket exercise using fictional cases, with explicit escalation, ownership and repeat-issue checks.” Name the actual contribution. This wording is excluded from today’s CV and letter. A social draft requires personal review and separate publishing permission.

## N. Optional extension
Propose a summary assistant only after the baseline works. Use fictional tickets, preserve IDs/unknowns and require analyst review. Compare omitted facts, invented facts and clarity against the manual note on a larger held-out sample. Set a budget before selecting a service. No AI component, API use or measured improvement is part of this run.

## Technical sources
Reviewed 11 October 2026.
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/get-localgroupmember
https://support.microsoft.com/en-us/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows
