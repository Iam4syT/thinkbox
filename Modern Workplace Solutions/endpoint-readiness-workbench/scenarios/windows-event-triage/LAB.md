# Lab two Windows event triage and handover

## Outcome and role connection
Turn a small set of Windows events into a reviewed incident handover with clear ownership. This scenario practises monitoring, triage, investigation and resolution of events alongside user-focused troubleshooting. Hypothesis: repeated endpoint alerts can hide the few events needing immediate attention. No internal employer alerts, architecture or incidents are assumed.

The toothbrush test: use at each service-desk review or daily lab check. Baseline: manually classify five synthetic events. Intended measure: repeated errors grouped, stale/informational events excluded from action queue and unknown critical event escalated. No measured response-time or employment result.

## Scope prerequisites and architecture
The offline Python router and 9 tests were built with AI assistance. Native PowerShell collection, Windows event generation and Bunamin's own reproduction are unrun. Python 3.11+ uses no external packages or cloud account. Native practice needs a disposable Windows 11 VM or device with snapshot and authority to create a uniquely named lab event source. Windows licensing/VM capacity must already be available; no paid services started. Budget estimate two focused sessions. Do not collect employer logs or personal messages; only synthetic WorkplaceLab events.

Dataflow: synthetic events → timezone/window/schema checks → grouping → proposed owner/action → human review. No automatic remediation. PowerShell collection is read-only; generating lab events changes only the authorised sandbox log. Python triage is not full Windows monitoring or an Intune integration. Rules beat a language model for these few explicit conditions; any future AI explanation would remain reviewed text, not change authority.

## Manual baseline and native practice

### 1 Set the baseline
Start: project README and templates/events.json available. Action: inspect five records before running code; predict which should be actionable, grouped or excluded. Write predictions in a private run log using reference time 2026-01-01T10:00:00+00:00. Expected: two current repeated errors, one unknown critical, one information and one old record. Verify actual time zones and IDs. Recovery: do not tune expected answers after seeing output; label any changed prediction.

### 2 Run the router
Start: terminal in project root with Python 3.11+. Action: run `python3 scripts/triage.py templates/events.json --now 2026-01-01T10:00:00+00:00` and `python3 -m unittest discover -s tests -v`. Expected: two groups, two excluded records, repeated count 2, unknown critical owner specialist review, remediation_performed false; 9 tests pass. Verify against manual baseline. Recovery: correct runtime/path/JSON; retain failures.

### 3 Check rejection behaviour
Start: source fixture preserved. Action: make a temporary copy and duplicate its first record. Run router. Expected: duplicate-record ValueError. Then test a copied record without a time zone or with a future time. Expected: explicit error rather than an empty healthy result. Verify original hash/content unchanged. Recovery: remove temporary files and restore source; no silent dropping of malformed records.

### 4 Prepare Windows and a run folder
Start: disposable licensed Windows VM with snapshot and authority for sandbox log writes. Action: create C:\WorkplaceLab\events and copy collect-lab-events.ps1 there. Record Windows edition, time/timezone and LAB-WIN01 alias. Expected: no real employer events/data included. Verify script limits provider WorkplaceLab and last one hour. Recovery: stop if this is a managed daily-use or employer device.

### 5 Register a synthetic source
Start: snapshot saved, Windows PowerShell 5.1 opened as administrator on sandbox. Action: run `New-EventLog -LogName Application -Source WorkplaceLab` only if that source does not already exist. Expected: the source is registered; there is no actual fault. Verify in Event Viewer after writing an event. Recovery: if source exists, inspect ownership/use; reuse only if it is your lab source, otherwise choose a unique name and update collector filter. Do not overwrite other sources.

### 6 Write known lab events
Start: authorised synthetic source. Action: run `Write-EventLog -LogName Application -Source WorkplaceLab -EntryType Error -EventId 1001 -Message "Synthetic missing note test"` twice. Add `Write-EventLog -LogName Application -Source WorkplaceLab -EntryType Information -EventId 1000 -Message "Synthetic normal check"`. Expected: three lab events, no real device failure. Verify Event Viewer Windows Logs Application, filter source WorkplaceLab and inspect ID and time. Recovery: fix source or log permissions; never fabricate a native success if commands fail.

### 7 Collect only the lab events
Start: events in last one hour. Action: in C:\WorkplaceLab\events run reviewed collector with approved script policy/signature. Expected: lab-events.json with IDs, synthetic host alias, provider, UTC time and level; no event messages or usernames. Verify read JSON in Notepad and count at least three newly written events. Recovery: if no events, check time or source filter; record error, do not widen to all production logs. A script policy block remains blocked; no bypass.

### 8 Compare native and synthetic inputs
Start: saved collection. Action: copy only this permitted JSON to the Python project. Inspect IDs/severity then run router with current explicit UTC ISO time, not the fixed January fixture time. Expected: Error 1001 count 2 for a clean new run; Information excluded. Verify source, time window and group count against Event Viewer. Recovery: repeated prior lab runs add records; filter the intended period or record actual count instead of forcing 2. Future clock error requires correcting clocks/reference, not deleting evidence.

### 9 Investigate within scope
Start: error group visible. Action: create a local note C:\WorkplaceLab\events\status.txt with text "ready" and document it as a simulated healthy setting. Rename only that file to status.bad; observe missing expected path via Test-Path. Expected: reproducible file-state difference. Verify this is your injected condition, not a proven cause of every Windows 1001 event. Recovery: rename back and reread; if the path differs stop. No production service restart or registry changes.

### 10 Close a known test condition
Start: deliberately renamed lab file. Action: restore status.txt, run `Get-Content C:\WorkplaceLab\events\status.txt`, then write an Information WorkplaceLab event 1002 with message "Synthetic recovery checked". Expected: expected file and content and fresh recovery marker. Verify actual application or device function separately if testing a real app; an event alone is not proof of recovery. Recovery: keep ticket open if the file or content check fails; do not infer repair from the log message.

### 11 Practise unknown escalation
Start: router fixture copy. Action: set a test record provider to UnknownLabProvider and level Critical with current timestamp and unique ID; run router. Expected: urgent true, specialist review owner and no automatic fix. Verify no command executed. Recovery: if output hides it, preserve failing fixture and fix rules before relying on routing. Native collector deliberately collects only WorkplaceLab; this scenario is an offline unknown-case test, not a claim of collecting all providers.

### 12 Write and review handover
Start: known and unknown outputs available. Action: write ticket alias, users affected (if known), source and time window, symptom, evidence, injected fault, checks and result, next owner and next check date. Separate observation from suspected cause; mark unknown impact as unknown. Expected: another person can reproduce the lab condition and see who owns the next action. Verify against logs and fixtures; no unsupported SLA or severity claims. Recovery: return ambiguous handover for clarification; do not close native incidents from a script recommendation.

### 13 Retest and clean up
Start: evidence preserved. Action: rerun 9 tests, record source commit, runtime and actual result, restore status.txt and remove only files created for your lab when finished. Remove-EventLog -Source WorkplaceLab is optional only if you created that source and it serves nothing else; removal does not erase historical Application entries. Never clear the Application log. Expected: no remaining active lab objects. Verify ownership and snapshot before VM disposal. Recovery: keep uncertain objects and record pending cleanup rather than bulk deleting logs.

## Acceptance portfolio and next step
Offline: 9 tests pass for repeated grouping, unknown critical escalation, stale/information exclusion, no remediation, duplicate/future/timezone/severity/schema failures. Native steps remain unrun. Native completion requires source and event evidence, correctly scoped export, current time window, observed file fault and recovery and reviewed handover. A generated failure event is not an actual Windows outage, and a working router is not full monitoring experience.

Save source, predictions, synthetic/native-permitted evidence, errors, restored file check and handover. Explain what you observed, what you controlled, why you escalated and what remains unknown. After Bunamin's own completed reproduction only: Built a Windows lab event-triage workflow and verified grouping, escalation and handover using synthetic events. Claim PowerShell collection and native checks separately only when performed. Optional extension: approved scheduled read-only collection and an ITSM sandbox connector; retention, permissions and rate-limit review needed before integration.

Sources checked 17 October 2026: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.5 . Windows PowerShell event-write cmdlets differ from PowerShell 7; use 5.1 for the listed New-EventLog and Write-EventLog commands. No production or live operations performed.
