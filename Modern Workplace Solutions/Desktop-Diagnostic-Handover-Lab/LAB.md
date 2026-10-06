# Desktop observations and handover lab

Status: Codex-authored local learning asset. Fixture tests can be executed by Codex; Bunamin completion and Windows/live work remain unrun.

## Outcome and role relevance

Produce an evidence-led desktop diagnostic handover from explicit observations. the general first-line support workflow includes first-line hardware/software diagnosis; The learning objective makes physical device work a development gap. This lab connects user symptoms to safe checks and escalation; a simulated snapshot cannot demonstrate physical repair competence.

## Architecture and baseline

Synthetic observation JSON → Python validation → suggested next checks → human escalation note. Four scenarios: DNS/connectivity failure, low disk space, checks clear and observations unknown. Manual baseline: inspect the observations and write next check plus missing evidence. No remote access, automatic repair, patient data or AI.

## Prerequisites and cost

Offline section: Python 3.10+, text editor and public folder; no packages or bill. Optional Windows section: a personally controlled Windows 11 device or licensed VM, standard PowerShell and permission for network tests. Windows licence/hardware costs depend on what is already available; VM does not prove physical repair. Do not run on clinical equipment or a live employer environment.

## Step 1 Inspect fixtures

Starting state: diagnose.py, sample.json and test_solution.py in the public folder. Run python3 --version; open sample.json. Expected: four synthetic asset aliases and explicit booleans/nulls. Verify no personal identifiers, real hostnames or patient data. Recovery: replace any imported data with the supplied synthetic fixtures before proceeding.

## Step 2 Record the manual baseline

For DEMO-PC-01 note DNS/TCP/application observations failed; for 02 note disk space 5%; for 03 note checks clear but user task not yet verified; for 04 note five missing observations. Expected: four handovers that preserve uncertainty. Verify these notes against the JSON. Recovery: do not substitute false for an unknown null value.

## Step 3 Run checks and create the report

Run python3 -m unittest -v, then python3 diagnose.py sample.json output.json. Expected: seven test methods pass and four handovers. Verify 01 suggests network/app review, 02 warns against deleting user files, 03 requires user-task confirmation and 04 asks for missing observations. Recovery: malformed JSON rejects; restore the fixture and rerun.

## Step 4 Validate failure behaviour

Copy sample.json to broken.json and change DNS true/false to the string "false". Run diagnose.py broken.json broken-output.json. Expected: validation error and no new output. Restore the boolean, then set disk_free_percent to 101; expect rejection. Restore it to 30. Verify a failed run cannot overwrite a prior valid handover.

## Step 5 Write a useful escalation

Choose DEMO-PC-01 and create handover.txt: synthetic symptom; alias; impact still to confirm; DNS/TCP observations; checks already attempted; requested specialist review; current owner; next user update. Expected: observations distinct from a root-cause assertion. Verify no phrase claims a confirmed DNS outage or patient impact. Recovery: replace conclusions with measured observations and questions.

## Step 6 Optional Windows starting state

Unrun extension. Use only a personal Windows 11 lab with permission. Open ordinary PowerShell. Run Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption,Version. Expected: local operating-system details [the general first-line support workflow3]. Verify Windows environment. Recovery: if access is denied or command unavailable, record the error and stop; no elevation, remoting or execution-policy change is required.

## Step 7 Optional read only desktop checks

Unrun extension. Run Get-PSDrive -Name C | Select-Object Used,Free and Get-NetIPConfiguration. Expected: local disk and adapter/IP observations. Calculate free percent = Free divided by Used+Free times 100. Verify adapter/IP/gateway observations manually; local IP data stays private. Recovery: missing adapter/gateway is an observation, not permission to reconfigure networking. Do not delete files or change drivers.

## Step 8 Optional DNS and TCP checks

Unrun extension. With permitted outbound access, run Resolve-DnsName www.microsoft.com, then Test-NetConnection -ComputerName www.microsoft.com -Port 443. Expected: DNS answer and TcpTestSucceeded value [the general first-line support workflow1]. Verify exact command target and timestamp privately. Recovery: failure may reflect policy, connectivity or service state; record it, compare an approved known-good target and escalate rather than changing a firewall.

## Step 9 Optional snapshot and user retest

Unrun extension. In a local private copy of sample.json add a fictitious alias and the actual observed booleans/free percentage. Leave app_ok null until an approved test task has been attempted. Run diagnose.py on this private copy. Expected: handover asks for any unmeasured observations. Verify the original task with the user before closure. Recovery: successful TCP does not prove application, authentication or clinical workflow success.

## Step 10 Desktop hardware learning session

Planned separate physical practice. With a personal spare device, obtain manufacturer instructions and a supervised/approved learning scope. Record symptom, visible power/cable/peripheral checks, own actions and before/after test. Do not open powered equipment or make repairs beyond that scope. Expected evidence: actual device observations and a verified result or escalation. Recovery: stop at uncertainty. No physical practice happened in this run.

## Acceptance and break fix exercises

Accept the offline section when all four handovers match the manual baseline, missing data stays unknown, bad types/ranges reject, no auto-remediation occurs and checks_clear never closes a case. Break/fix: set adapter_up false and verify cable/Wi-Fi check; set app_ok false with network true and verify app-focused escalation; retain nulls to verify missing evidence is requested.

## Cleanup and evidence

Delete generated output/broken files only after saving sanitised evidence. Private Windows snapshots, IPs and screenshots stay outside public folders. Close a VM when finished; remove only a lab snapshot you created and no employer resources. Capture baseline comparison, test log and any new actual observation with environment/date and attribution.

## Toothbrush test and gap plan

Every support shift needs repeatable checks and an intelligible specialist handover. Start with the offline fixture reasoning, then approved personal Windows practice, then supervised physical equipment and local induction. Repeat faults on a second device before making broader claims. This is a plan, not a promise of rapid or unsupervised competence.

## Interview story and conditional wording

After personal completion, explain why DNS/TCP/disk observations are not root causes, how unknowns were preserved and how authority limits controlled action. Conditional wording: Tested a synthetic desktop diagnostic handover tool and documented read-only observations and escalation boundaries. Mention real Windows or physical tests only when performed and evidenced.

## AI alternative and extension

Keep the checklist as baseline. Optional AI could draft a handover from approved synthetic observations; measure factual omission, invented causes and unsafe remediation against a human note. It must abstain when evidence is incomplete and require review. No AI deployment, model evaluation or NHS approval is implied.
