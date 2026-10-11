# Lab 2 — Approved access and device handover checks

## A. Purpose and present status
Check whether a fictional access/device request is ready for human review. The local checker and twelve tests were run by Codex on 11 October 2026. Windows, physical peripherals and Bunamin’s own completion are unrun. A review_ready result never grants access or confirms a real device works.

## B. Fictional learning context
A fictional office team needs clear support handover and permitted access/device checks. This additional scenario is independent learning, not a report of an employer’s incidents or systems.

## C. Job requirements exercised
investigation/escalation, application setup, peripheral/device development, access control and accurate checks. The offline part records approval and functional checks; the Windows extension practises permitted group inspection and printing. It does not simulate complete enterprise management or access-control operations.

## D. Gap and learning boundary
Bunamin reports FirstBank Active Directory/account support and Tek Outlook installation. He explicitly reports no physical laptop/server/network hardware practice. A+ knowledge is a foundation, not practical repair evidence. The optional Windows VM supports software practice; only authorised physical-device work can supply physical setup evidence. Arrange initial review before claiming independent performance.

## E. Repeated-use value
A support analyst could repeat the checklist for each authorised access request, device issue or handover. Intended value: an incomplete or privileged request stays visible instead of being mistaken for a completed handover. No faster provisioning, fewer incidents or real service benefit has been measured. Baseline is a manual five-request checklist.

## F. Architecture and demonstration rules
Fictional user/asset request JSON → strict field/type checks → findings → dry-run result → human evidence review. Missing approval, a disabled account, a privilege request or any missing sign-in/application/peripheral test causes hold. Otherwise status is review_ready. The script cannot validate an approval’s authenticity or inspect a real machine. It never contacts a tenant, creates users or changes permissions. A Windows local group is a teaching substitute, not the fictional office’s access model. AI is unnecessary for these explicit checks.

## G. Prerequisites, licences, cost and plan
Offline: Python 3.10+, terminal, text editor and this public folder; no extra packages or service charge. Plan 60–90 minutes; time is unmeasured. Optional Windows stage: your authorised spare supported Windows 11 computer or licensed disposable VM, a normal test-user session, a permitted reviewer/admin, a snapshot or recovery plan and an empty lab folder. Use existing licences; no trial or free hardware is promised. Physical extension needs an authorised spare printer or USB peripheral and its manufacturer’s approved driver. Check actual cost before obtaining anything. No Microsoft 365, Entra or Intune subscription is needed for this local lab. Windows/local-group work requires a suitable 64-bit PowerShell environment; current vendor guidance is listed in Sources.

## H. Granular implementation steps
### H1. Locate the offline project
Start with public containing solution.py, test_solution.py, sample.json and evidence. Open a terminal there and run python3 --version (Windows: py -3 --version). List files with ls or dir. Expect Python 3.10+ and the named files. If not, recover the complete package or use a known authorised Python installation; do not install on a work device without permission.

### H2. Record the manual decision
Open sample.json without editing it. Write READY-01 review_ready; READY-02 hold for approval; READY-03 hold for disabled account; READY-04 hold for privilege review; READY-05 hold for missing peripheral check. Verify each Boolean against section F. These five fictional requests have different faults. If a flag is unclear, leave the decision pending rather than treating an unknown as a pass.

### H3. Run the behaviour checks
Run python3 -m unittest -v. Expect twelve methods and final OK. Check the missing approval, privilege, invalid type, duplicate ID and input-preservation cases. Save the actual learner log. On failure retain the error and compare your changes with the supplied version. Do not weaken a guard to make the suite pass.

### H4. Generate the readiness report
Run python3 solution.py sample.json learner-result.json. Open it. Expect five results: one review_ready and four hold. Verify the asset, user, reviewer, findings and dry_run mode remain visible. Compare all five with your manual note. If output is absent, check folder/filename and JSON format. A result generated from false declarations can still be wrong; source evidence must be checked separately.

### H5. Repair only the fictional request
Copy sample.json to practice.json. Change READY-02 approved to true only for this fiction and add a note in your separate checklist explaining the pretend approval. Rerun to practice-result.json. Expect READY-02 review_ready; verify the other four decisions are unchanged. Then remove a required asset and retry to rejected.json: expect Missing asset and no new output. Restore the fixture. In real work, a checkbox never substitutes for an authorised manager’s approval.

### H6. Prepare the optional Windows stage — unrun
Start on the authorised spare device/VM. Ask the reviewer to confirm the test user, permitted non-privileged group and recovery plan. Record the device/VM label, OS version from Settings → System → About, expected app and printer. Create a folder named SupportLab in Documents. Expect one identifiable lab machine and a reviewed scope. Verify no employer account, real shared group or important data is selected. If access, licence or permission is missing, stop here and record unrun.

### H7. Inspect group membership — unrun
Use the permitted PowerShell session. First run Get-LocalGroup to see the actual group names. Choose the reviewer-approved non-privileged group, then run Get-LocalGroupMember -Group "ACTUAL-APPROVED-GROUP" with that exact name. Expect its listed members, possibly none. Compare the exact test identity with the approved request; save permitted output privately. A missing group means the request or name must be checked, not that you should grant administrator membership. If the module is unavailable, confirm a 64-bit Windows PowerShell session with the reviewer. The lab performs read-only inspection; creation/addition/removal are outside this step. See Microsoft Learn source T1.

### H8. Check sign-in and a harmless application task — unrun
Sign in to the authorised test-user session through Windows’ normal sign-in flow. Open Notepad, type “SupportLab test”, and save lab-note.txt in SupportLab. Close and reopen it. Expect the same text under the test identity. Record what worked and the exact error if it did not. Verify the saved file, not only that the application opened. If permissions or identity differ, retain the failure and ask the reviewer; do not broaden access as a shortcut. This is local application verification, not an Outlook or cloud access test.

### H9. Verify software printing — unrun
From Notepad choose File → Print, select Microsoft Print to PDF if available and save lab-note.pdf into SupportLab. Open the PDF and compare its text with the note. Expect a readable one-page file. Verify the actual content. If the printer option is absent, record it and ask the reviewer for the approved setup; do not download an unknown driver. This checks a software print path and does not prove physical peripheral maintenance.

### H10. Add supervised physical peripheral practice — unrun
On an authorised spare machine, record the printer/peripheral model and approved connection method. With the reviewer, check power and cable, use the manufacturer-approved installation steps, then check Windows Settings → Bluetooth & devices → Printers & scanners for the exact printer. Print a harmless test page or the lab note. Expect the correct device and readable physical output. Compare device, queue and page; capture a sanitised photo/checklist. If it fails, record power/connection/queue status and the exact error, follow current Microsoft/manufacturer guidance and escalate outside your scope. Do not alter a corporate queue or open electrical equipment. VM/PDF output cannot substitute for this physical stage. See source T2.

### H11. Complete a human handover
Record requested access, reviewer, machine, observed sign-in/app/peripheral results, unresolved faults and next owner. Change any practice JSON flags only after the corresponding real lab check is observed. Expect a truthful distinction between offline flags, software checks and physical checks. Have the reviewer compare the evidence. If one check is missing, leave hold. A reviewer’s permitted confirmation is still separate from production readiness.

## I. Break and recover
Offline: set approved to the string "yes" in a copy; expect Invalid approved. Restore Boolean true, rerun and verify. Duplicate an ID; expect rejection; restore it. Windows: select a different available printer queue for a harmless task and notice the mismatch before printing; return to the approved queue and verify the correct output. For an approved spare USB peripheral, have the reviewer disconnect only its external cable, identify the unavailable device, reconnect and repeat the harmless functional check. Record what actually happened. Do not induce faults on work equipment, disable security or delete user data.

## J. Acceptance and security checks
Offline acceptance: twelve tests pass; all five manual decisions match; malformed/duplicate requests reject; input remains unchanged; the tool remains a dry run. Windows acceptance, still pending: correct identity/device, observed group membership, reopened application file, readable PDF and reviewer-confirmed record. Physical acceptance additionally needs the actual peripheral and functional output. No passwords, personal names, tenant exports or real serial numbers enter public files. The checker lacks authenticated approvals, expiry, concurrency, secure audit storage and live integration.

## K. Artefacts and cleanup
Keep the manual baseline, test log, result, architecture, observed faults and a short case study. Screenshots/photos and a demo video are optional and currently unrecorded. Remove only disposable practice/rejected output copies after retaining permitted evidence. For Windows, review SupportLab contents before deleting only those test files. Restore the reviewed snapshot only if it contains no unrelated work. This exercise creates no users/groups, so no permission removal is claimed. Unplug only your spare test peripheral; preserve approved drivers/settings unless the reviewer authorises removal.

## L. Interview story after personal completion
Explain the access/device request; constraints and approval boundary; why a checklist beat unnecessary AI; your own adaptation; the malformed approval or wrong queue you found; the functional test and reviewer evidence; the intended value of a truthful handover; and the next supervised physical practice. Name which stages you actually completed. Do not imply the fictional office’s systems or a live tenant were used.

## M. Conditional wording
Use only after personal completion: “Adapted and tested a Codex-assisted offline access/device checklist with fictional requests and explicit holds for missing approval or functional checks.” Add Windows or physical practice only after doing and documenting that specific stage. Today’s CV/letter exclude this new project as achieved experience. Any LinkedIn draft needs review and separate posting permission.

## N. Extension and comparison
After the local baseline, propose a read-only inventory connector in a separately authorised test tenant. Compare actual inventory with declared flags; use minimum permitted access and human approval. Do not let AI approve access. An optional summary assistant would need a manual comparison for omissions/invented checks. Neither connector nor AI extension was built or run here.

## Technical sources
Reviewed 11 October 2026.
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/get-localgroupmember
https://support.microsoft.com/en-us/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows
