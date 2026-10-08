# Incident queue review
## A. Outcome
A desk agent needs to see which requests need attention first. This lab turns five dummy software requests into a sorted review list. It flags a possible major incident for a person to assess. It never declares an incident or contacts a user.
Status: source built and locally evaluated by Codex on 8 October 2026. Bunamin's independent run and explanation are pending. No live tenant or RM system was used.
## B. Company problem and research basis
RM's vacancy asks for software incident progress, knowledge use, recurring-problem identification and automation opportunities. Its public education support services make a school-software scenario plausible. Repeated teaching-portal and email issues are an invented scenario, not known RM incidents. Sources: careers.rm.com/jobs/3699 and rm.com/technology/services/support-and-management, checked 8 October 2026.
## C. Job mapping
The queue solution exercises incident priority, monitoring, service-management escalation and a possible major-incident review. The knowledge solution exercises repeat-problem review, knowledge gaps and possible automation. This lab's title identifies its main workflow. No separate essential/desirable list or exact technical stack was published.
## D. Candidate gap
Transferable Microsoft 365 diagnosis, documentation and incident coordination are supported by work-history reports. RM's major-incident and knowledge approval processes are not yet evidenced. This assistant-built exercise helps practise the logic; it does not award production experience or close the personal evidence gap by itself.
## E. Repeated use
A desk agent could review a queue each shift. A desk lead could review repeat issues each week. The intended value is more consistent attention and guidance. No time saving, service-level gain or school outcome has been measured.
## F. Design and rules
Local dummy file → validation → clear rules → JSON review report → human decision. JSON is a text file with named values. All processing stays on the computer. There are no accounts, network calls, database, passwords, live changes or customer exports.
Each row has an ID, service, impact, urgency and age in minutes. Impact is single, group or school. Urgency is normal or urgent. These are invented lab rules: school plus urgent becomes priority 1, with a 30-minute target. Group, school or urgent becomes priority 2, with 120 minutes. Other requests become priority 3, with 480 minutes. A request is overdue at the target, not only after it. These are elapsed-minute exercises, not RM's service agreement.
Inspect src/queue_check.py in your editor. Find FIELDS and analyse: these validate every row before writing. Find the major expression: both conditions must be true. Find target: this maps priority to a made-up target. Find write_atomic: it writes a temporary file and replaces the output only after validation. Do not change these rules to match a live service without its owner's approval.
## G. Before you start
Use Windows, macOS or Linux with Python 3.11 or later and a plain-text editor. Python means the program runner; no extra packages are needed. Use a personal test folder. No licence or tenant needed. Estimated direct software cost £0, excluding your existing computer and internet. Allow two focused sessions for reading, running and explaining; this is a plan, not measured time. If python3 is unavailable on Windows, try py -3 in the commands. Do not install software on an employer device without approval.
## H. Step-by-step lab
1. Get the source. Open the Thinkbox project URL below and choose Download ZIP from the repository Code menu, or use Git if already installed. Unzip it into a new test folder. Open the named project folder in your editor. Check that README.md, src, tests, data and LAB.md exist. The private public-folder copy is usable if publication is unavailable.
https://github.com/Iam4syT/thinkbox/tree/main/Modern%20Workplace%20Solutions/School-Service-Desk-Queue
2. Open a terminal in that project folder. On macOS, open Terminal, type cd followed by a space, drag the folder into the window, then press Return. On Windows, use your editor's Open in Terminal action. All following paths start here. Check Python:
python3 --version
3. Open data/requests.csv in your editor. Read the dummy labels. Do not replace them with school, pupil, staff or client records. Keep an untouched copy. Read the design rules above before running anything.
4. Run the tests. A test checks an expected behaviour automatically:
python3 -m unittest discover -s tests -v
Expected: all tests report OK. Any failure means stop and read that test's name and message before using a report. Tests must use only the local dummy fixtures.
5. Create the report. The program creates evidence if it is missing:
python3 src/queue_check.py data/requests.csv evidence/result.json
6. Open evidence/result.json in the editor. It should be readable named values, not an empty file. Compare with this answer key:
The result has five rows. Order: R001, R004, R002, R003, R005. R001 is priority 1, overdue and major_review true. R004 is priority 2 and overdue. R002 is priority 2 and not overdue. R003 is priority 3 and overdue. R005 is priority 3 and not overdue. Compare every row with the rules by hand.
7. Save evidence from your own run. Record your date, Python version, exact command, test result and one explanation of a flag. A screenshot may show the dummy report and terminal only. Do not include usernames, private folders or other windows. Keep a short screen recording only if you want one; no recording is claimed complete.
8. Follow the break/fix steps. Work on copies. Keep each error and corrected run in your notes. Do not publish a stale result as a successful new run.
## I. Break and fix
1. Copy data/requests.csv to data/broken.csv. Open only the copy in a plain-text editor. Change R001's age from 30 to -1. Run the command below. It must exit with an error saying Negative age. No output should be created.
python3 src/queue_check.py data/broken.csv evidence/broken.json
2. Change -1 back to 30. Repeat the command. Five requests should now appear. Compare broken.json with result.json.
3. Replace R002's ID with R001. Run again. Expect a duplicate-ID error. The previous output must remain unchanged. This means an old report still exists: never treat it as a fresh run after an error. Restore R002 and rerun.
4. Change R001's urgency to normal. R001 must lose the major-review flag and become priority 2. Restore urgent and rerun. Keep your diagnosis and the changed output as evidence.
## J. Acceptance and limits
Pass only when the normal output matches every answer-key value, all tests pass, the changed input causes the expected different result, invalid input fails, input files remain intact and no private data enters the package. Save your own evidence before claiming completion. Automated fixtures cover selected boundaries, not every possible input. Live service integration, access control, retention rules, performance and owner approval are untested.
## K. Evidence and handover
README.md explains use; src contains the program; tests contains checks; data contains dummy inputs; evidence holds actual fixture outputs; EVALUATION.md records the assistant's run. docs/ARCHITECTURE.md explains the flow. DEMO SCRIPT.md gives a short walkthrough. CONTRIBUTIONS.md separates authorship. CHANGELOG.md records actual changes. Read these before handover. Deploy by copying only this project folder to an authorised local test location and repeating the tests; there is no cloud deployment.
## L. Interview explanation
Explain the recurring need, the lack of live data and approved rules, the simple file-based design, one fault you introduced, the exact check that proved your fix and the intended operational value. Say which choices Codex supplied and what you personally changed or tested. Ask how RM approves priorities, major incidents and knowledge. Do not turn a synthetic result into an employer performance claim.
## M. Wording after personal completion only
Proposed future wording: “Ran and explained an offline school-support lab using dummy records, checked its normal and failure cases, and documented the limits before any live use.” Use only after Bunamin has actually run, understood and evidenced it. Keep AI assistance explicit in the contribution record. This is not yet an approved CV or LinkedIn claim.
## N. Optional next version and cleanup
Start with a spreadsheet/manual count as the simpler baseline. Rules are enough for these five records. AI is not needed for the built version. A later assistant could suggest categories or draft knowledge summaries only from approved text, with source references, a no-answer route, human approval and a measured comparison against the manual baseline. No AI model, API or claimed productivity gain is built here.
To clean up, remove only your copied broken files and generated reports after saving evidence you want to keep. Delete the local test folder if finished. There are no cloud resources, charges or credentials to revoke. Never run a broad delete command in the Thinkbox repository.
