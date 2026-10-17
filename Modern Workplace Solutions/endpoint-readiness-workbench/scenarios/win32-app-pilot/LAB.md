# Lab one Win32 application pilot

## Outcome and role connection
Build a harmless SupportNote package, test detection and removal, and plan a limited Intune pilot. This scenario practises device management and software packaging for a hypothetical workplace support team. The recurring problem here is a hypothesis: an engineer needs a repeatable way to verify a small app before rollout. This is an independent learning exercise, not an employer infrastructure replica or commissioned work.

The toothbrush test: use the checklist at each app release or onboarding wave, rather than a one-off screenshot. Baseline: manually check installation, version and removal on a test device. Intended measure: all acceptance checks recorded for a known good package and deliberately bad detection. No time saving or business benefit measured.

## Scope tools and prerequisites
Offline contract checker and 7 Python tests are implemented and evaluated by Codex. CMD installation/removal, PowerShell detection, Windows VM and Intune operations are supplied but unrun. Bunamin has not yet reproduced the lab. A VM builds Windows workflow knowledge; it does not establish physical laptop repair experience.

Use Python 3.11+, a disposable Windows 11 Pro, Enterprise or Education device or licensed VM, a snapshot/backup and a test-only local administrator. For optional Intune phase: licensed test tenant, permitted app/device administration, test user/licence and one enrolled personally controlled device. Never enrol an employer or current personal daily-use device for this exercise. Confirm licence/trial eligibility and billing first; no subscriptions/resources created by Codex. Offline cost zero beyond existing computer; Windows/virtualisation/Intune may cost money. Budget estimate two or three focused sessions, not a measured duration. If no tenant/licence is available, complete local steps and leave Intune unrun.

Stack: Windows, CMD, PowerShell, Intune, Entra registration/enrolment. Python provides only an offline package-contract check. AI is unnecessary: a deterministic checklist and human approval are simpler and more transparent. No broad assignment, security bypass or automatic production action.

## Set up the local baseline

### 1 Read and prepare the source
Start: this project folder and README are available. Action: read CONTRIBUTIONS and EVALUATION; create a private run log with date, runtime, source commit and device alias LAB-WIN01. Expected: implemented versus unrun components listed. Verify: explain that Python does not install anything. Recovery: stop if provenance or source scope is unclear.

### 2 Run the offline contract
Start: terminal in this public project folder, Python 3.11+. Action: run `python3 scripts/pilot.py templates/package.json` and `python3 -m unittest discover -s tests -v` (Windows: replace python3 with py -3). Expected: one LAB-WIN01 pilot, native_validated false, 7 tests pass. Verify exact output, not just exit status. Recovery: check working folder/runtime and retain failed output.

### 3 Exercise a bad plan
Start: source template unchanged. Action: copy templates/package.json to a temporary file; change pilot to ["ALL-DEVICES"] and run checker on that copy. Expected: ValueError, no installation or assignment. Verify the original template is unchanged and bad scope is refused. Recovery: remove only your temporary copy, restore fixture and rerun tests. This validates the local checker, not tenant RBAC.

### 4 Prepare a Windows sandbox
Start: authorised disposable Windows 11 device or VM with correct licence and snapshot. Action: open Settings then System then About; note edition and system type. Create C:\WorkplaceLab\src and C:\WorkplaceLab\out in File Explorer. Expected: supported Windows architecture and empty staging folders. Verify you are using a test device with no real work data. Recovery: restore snapshot or stop if unsupported. Do not change organisation security settings.

### 5 Stage the dummy package
Start: Windows staging folder exists. Action: copy scripts/install.cmd, uninstall.cmd and detect.ps1 plus templates/note.txt and version.txt into C:\WorkplaceLab\src. Open note/version in Notepad; version must be 1.0.0. Expected: exactly five reviewed files, no credentials. Verify with `Get-ChildItem C:\WorkplaceLab\src` in PowerShell. Recovery: fix missing filenames/content before packaging. No system changes yet.

### 6 Install locally and inspect
Start: snapshot saved and scripts reviewed. Action: open Command Prompt as administrator on this test VM; run `cd /d C:\WorkplaceLab\src`, then `install.cmd`, then `echo %ERRORLEVEL%`. Expected: exit 0 and note/version under %ProgramData%\WorkplaceLab\SupportNote. Verify open both files in Notepad and compare content. Recovery: read any error, check write permission/source paths; never disable security controls to force a pass.

### 7 Verify detection and removal
Start: dummy files installed. Action: in authorised PowerShell run `& C:\WorkplaceLab\src\detect.ps1`; inspect `$LASTEXITCODE`. Expected: output SupportNote 1.0.0 detected and exit 0. If script policy blocks execution, record blocked; use approved signing/policy or stop, do not bypass it. Next run uninstall.cmd from staging Command Prompt. Expected: only dummy note/version removed; detection returns 1. Verify both installed and absent states. Recovery: use snapshot if cleanup differs.

### 8 Break and repair the version check
Start: dummy app installed again using step 6. Action: edit only installed version.txt to 0.9.0. Run detection. Expected: exit 1, despite file presence. Verify this catches version mismatch. Repair by rerunning reviewed install.cmd; expect exit 0 and version 1.0.0. Recovery: check copy errors and source version; retain before/after outputs. This tests rollback logic locally, not Intune status.

### 9 Prepare the Intune file
Start: local install, detect and uninstall states verified; optional test tenant/licence/access confirmed. Action: download Win32 Content Prep Tool only from Microsoft official GitHub, linked in Microsoft Learn; review release and extract IntuneWinAppUtil.exe. Run tool, provide source C:\WorkplaceLab\src, setup install.cmd and output C:\WorkplaceLab\out; do not specify a catalogue folder. Expected: install.intunewin. Verify tool version, output filename and file hash with Get-FileHash. Recovery: correct paths and review all source files; never include secrets or unrelated files.

### 10 Create a bounded pilot
Start: test Entra/Intune tenant and only disposable test device enrolled. Action: open the Entra admin centre, Identity, Groups, All groups, New group. Select Security and Assigned membership, name it LAB-Win32-Pilot, then Members and add only your test device. Review and Create. Compare member device ID against your recorded alias. Expected: one test member, no dynamic/all-device group. Verify membership explicitly in Entra before continuing. Recovery: remove mistaken membership and stop; no assignment until scope is correct. A dummy group name is not a security boundary by itself.

### 11 Configure the Win32 app
Start: package and pilot ready. Action: Intune admin centre, Apps then Windows then Create/Add then Windows app (Win32). Upload install.intunewin. Name SupportNote Lab 1.0.0; publisher IndependentLab. Program: install `install.cmd`, uninstall `uninstall.cmd`, install behaviour System. Requirements: actual test architecture and supported minimum Windows version. Expected: reviewed metadata, no production assignment. Microsoft Learn documents the Intune Management Extension (IME), the Windows agent that processes Win32 apps; inspect its logs when needed. Verify every command against local tested files. Recovery: correct metadata before Create; portal labels may change, use current Learn workflow.

### 12 Add detection and assignment
Start: app draft open. Action: use custom detection script and upload detect.ps1; use 64-bit script context for x64 device and approved signature settings. No dependencies/supersedence for this first version. Assign Required only to LAB-Win32-Pilot. Review group ID, membership and scope before Create. Expected: one test-target deployment. Verify in assignment screen; retain sanitised screenshots. Recovery: remove assignment immediately if unexpected scope; do not continue with All users/All devices.

### 13 Observe installation
Start: pilot app assigned. Action: on test Windows Settings, Accounts, Access work or school, select test connection, Info, Sync where available. In Intune inspect app/device install status; also check local note/version and detection. Expected: native status and actual local files agree. Verify both sides and record timestamps; assignment processing may be delayed. Recovery: check enrolment, architecture, source files and IME logs using Microsoft troubleshooting guide; do not claim success from assignment alone.

### 14 Practise native removal
Start: native install confirmed. Action: remove Required pilot assignment and allow processing; configure Uninstall for the same test group using current portal. Expected: dummy note/version absent and native uninstall status. Verify local detection returns 1 and no Required or Available assignments conflict. Recovery: wait/check statuses and review logs; do not delete application record before the removal test completes. Stop if any non-lab device appears.

### 15 Record evidence and clean up
Start: both native states recorded or clearly unrun. Action: save private run log, hashes, commands, expected/actual result, one failed version check and recovery. Remove only lab assignments, group and app after evidence review; unregister disposable device only if no other work relies on it. Delete staging folders/test VM only after confirming they contain your lab data. Expected: no remaining lab policy or dummy app. Verify tenant and device state, then restore snapshot if required. Recovery: preserve failures and unresolved objects; no bulk cleanup.

## Acceptance and interview explanation
Offline acceptance: good contract passes; broad scope, duplicate targets, missing uninstall and unsupported architecture fail; absent/wrong-version detection model is false. 7 tests passed by Codex. Native acceptance remains unrun: installation exit 0, correct file content, detection exit 0, wrong version detection 1, corrected version detection 0, uninstallation exit 0, final detection 1; tenant status and local state must agree. Physical hardware support remains a separate supervised practice need.

Keep run log, package manifest/hash, source, approved screenshots, error/recovery notes and a short demo. Explain problem → constraints → small pilot → failure → verification → operational limit. No video recorded. After Bunamin personally reproduces and evidences it only: Built a test-only Win32 app package and verified install, detection and removal on a disposable device. State Intune assignment separately only if performed. Optional extension: version 1.1.0 and a supervised supersedence pilot with rollback; do not change the detection contract without retesting.

Sources checked 17 October 2026: https://learn.microsoft.com/en-us/intune/app-management/deployment/win32 and https://learn.microsoft.com/en-us/intune/app-management/deployment/add-win32 . Live licence/portal paths may vary; no production claim.
