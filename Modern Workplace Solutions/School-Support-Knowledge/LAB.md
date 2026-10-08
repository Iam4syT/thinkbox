# Recurring issue and knowledge review
## A. Outcome
A desk lead needs to find repeat software issues and check whether approved guidance exists. This lab groups resolved dummy tickets by service and symptom, then lists matching approved, unexpired article IDs. It asks for review when there is no usable article. It does not generate fixes or prove a root cause.
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
The input contains structured tickets and article metadata. There is no free-text notes field. Open tickets do not count as resolved. Sensitive tickets are excluded from groups. Two resolved tickets with the same service and symptom count as recurring. An article must be approved and valid on the chosen date. A blank article list means no supported answer was found. A person must check the original approved article before advising a user.
Inspect src/knowledge_check.py. Find the ticket field allow-list, then the sensitive exclusion and resolved-only rule. Find the article approval and valid_until test. Find needs_review: this is the no-answer route. The local write helper is reused from the queue example. The program cannot recognise sensitive content hidden in an allowed label. Synthetic structured input is a boundary, not a general data-loss prevention system.
## G. Before you start
Use Windows, macOS or Linux with Python 3.11 or later and a plain-text editor. Python means the program runner; no extra packages are needed. Use a personal test folder. No licence or tenant needed. Estimated direct software cost £0, excluding your existing computer and internet. Allow two focused sessions for reading, running and explaining; this is a plan, not measured time. If python3 is unavailable on Windows, try py -3 in the commands. Do not install software on an employer device without approval.
## H. Step-by-step lab
1. Get the source. Open the Thinkbox project URL below and choose Download ZIP from the repository Code menu, or use Git if already installed. Unzip it into a new test folder. Open the named project folder in your editor. Check that README.md, src, tests, data and LAB.md exist. The private public-folder copy is usable if publication is unavailable.
https://github.com/Iam4syT/thinkbox/tree/main/Modern%20Workplace%20Solutions/School-Support-Knowledge
2. Open a terminal in that project folder. On macOS, open Terminal, type cd followed by a space, drag the folder into the window, then press Return. On Windows, use your editor's Open in Terminal action. All following paths start here. Check Python:
python3 --version
3. Open data/history.json in your editor. Read the dummy labels. Do not replace them with school, pupil, staff or client records. Keep an untouched copy. Read the design rules above before running anything.
4. Run the tests. A test checks an expected behaviour automatically:
python3 -m unittest discover -s tests -v
Expected: all tests report OK. Any failure means stop and read that test's name and message before using a report. Tests must use only the local dummy fixtures.
5. Create the report. The program creates evidence if it is missing:
python3 src/knowledge_check.py data/history.json evidence/result.json --as-of 2026-10-08
6. Open evidence/result.json in the editor. It should be readable named values, not an empty file. Compare with this answer key:
Two groups should appear. Email/sign-in has resolved_count 2, recurring true, article_ids [KB1] and needs_review false. Teaching portal/access has count 1, recurring false, an empty article list and needs_review true. One sensitive ticket is excluded. T4 is open and does not count. KB2 expired on 7 October; KB3 is unapproved. Neither may be recommended.
7. Save evidence from your own run. Record your date, Python version, exact command, test result and one explanation of a flag. A screenshot may show the dummy report and terminal only. Do not include usernames, private folders or other windows. Keep a short screen recording only if you want one; no recording is claimed complete.
8. Follow the break/fix steps. Work on copies. Keep each error and corrected run in your notes. Do not publish a stale result as a successful new run.
## I. Break and fix
1. Run the command below. The Email article should disappear because KB1 expired after 8 October. Confirm needs_review becomes true.
python3 src/knowledge_check.py data/history.json evidence/later.json --as-of 2026-10-09
2. Copy data/history.json to data/broken.json. Open the copy in a plain-text editor. Change KB3 approved from false to true, leaving its future date unchanged. Run with --as-of 2026-10-08 using broken.json. KB3 should now appear for Teaching portal/access. This is a simulated review decision, not permission to approve real guidance.
3. Add a notes field to T1 in the copy. Keep valid JSON commas. Run again. Expect a Ticket fields invalid error. The last good output must remain unchanged. Remove notes and rerun to recover.
4. Duplicate T1, including its ID. Expect a duplicate-ticket error. Remove the duplicate and rerun. Never fix duplicate real records by deleting evidence without the owner's process.
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
