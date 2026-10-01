# Lab 2 — Safe factory-IT triage and knowledge handover

## A. Outcome and status
Build an offline triage aid that separates ordinary office support from suspected security incidents and production machinery problems, then writes a structured escalation note. The Python routing aid is implemented and locally evaluated by Codex; production, network, Windows, Apple and AI steps are unrun. This is a decision aid, not an incident-management system or proof of The learner's manufacturing competence.

## B–E. Business context, requirements, gaps and recurring value
Scenario: a textile factory needs machinery-PC escalation to senior engineers, business systems or suppliers (a hypothetical manufacturing-support workflow). Reasoned inference: understanding whether a symptom affects office work or production can make an escalation more useful. Nothing here establishes the hypothetical organisation's current incidents, ticket software, VLAN layout or machine vendors. Requirements addressed: first-contact support, accurate tickets, prioritisation, networking checks, confidentiality, security reporting, documentation and safe OT escalation. Gaps addressed: manufacturing context, legacy-machine boundaries and detailed network/device diagnosis. The toothbrush test is each incoming support request and each shift/team handover. Intended value: an engineer receives a usable symptom/impact/checks record without unsafe first-line intervention.

## F–G. Architecture, baseline and resources
Synthetic tickets → explicit routing rules → human-approved escalation → knowledge article. Python standard library plus JSON; no network calls, credentials or device access. Baseline: manual impact/urgency matrix and a fixed note template. Deterministic routing is the implemented aid. Optional AI summarisation is planned only, with no API integration; it must beat the template on usefulness without dropping warnings or exposing data. An LLM never chooses a machine command or changes priority on its own.

Use Python 3.10+, a text editor and the supplied fixtures. Offline cost is no new subscription; allow roughly 60–90 minutes as an estimate. An optional isolated Windows 11 VM and local router simulation can support learning; no live factory or production network is required. Real OT work needs employer/supplier authority, site induction, named risk owner, approved tools, maintenance windows and a rollback plan. Those prerequisites are not supplied here. NCSC guidance highlights operational continuity and legacy-system constraints; it is general security context, not a claim that this textile site is critical national infrastructure [T8].

## H1. Locate the routing aid
Start: supplied public project root. Run `python3 --version` and locate scripts/triage.py, scripts/test_triage.py and templates/sample.json. Expected: Python 3.10+ and all three files. Verify README paths. Recovery: recover the full project or use a known Python 3 installation. No additional package installation is needed.

## H2. Read the six synthetic tickets
Start: original sample.json. Open it and read t1–t6. The records include id, site, asset_id, symptom, impact, started, checks, zone, asset_type and symptom_type. The fixtures cover account support, a stopped machine PC, suspected security, a Mac, networking and an unknown incomplete request. Expected: entirely fictional records. Verify no employee, supplier, real IP or confidential design information is present. Recovery: restore the supplied fixture if sensitive data appears. A ticket field claiming “production” is only a fixture input.

## H3. Establish a manual routing baseline
Start: six tickets and blank baseline-notes.md. Assign a destination and boundary before running code. Expected: t1 service desk; t2 senior engineer/production owner, urgent, observe only; t3 security/service manager, urgent; t4 MDM specialist; t5 first-line office-network checks; t6 clarification with service manager and missing checks. Verify suspected security takes precedence over ordinary troubleshooting. Recovery: use the employer's actual priority matrix later; these demonstration priorities are not an agreed SLA.

## H4. Run the aid and inspect every reason
Start: public project root. Run `python3 scripts/triage.py --input templates/sample.json --output output/triage.json`. Expected: six results with route, priority, boundary and missing_fields. Compare each with your manual baseline. Verify the machine ticket includes no-reboot/patch/scan/PLC-change wording. Recovery: a JSON syntax error requires fixing a disposable copy; missing fields require a clearer ticket, not a guessed cause. No result opens a connection or sends an escalation.

## H5. Exercise routing boundaries
Start: normal run succeeds. Run `python3 -m unittest discover -s scripts -p "test_*.py" -v`. Expected: seven tests pass, including machine boundary, stopped production, security override, Apple specialist route, unknown category and missing information. In a disposable sample copy, make t2 security_suspected true and rerun; expected: security route retains incident-procedure boundary. Rerun unchanged fixtures to a second file and compare contents. Recovery: restore the original fixtures and investigate any test failure. These small designed cases establish local behaviour, not real-world classification accuracy.

## H6. Write an escalation packet
Start: t2 output and a blank Markdown note. Create fields: ticket ID; affected site/asset; symptom; reported start; production impact; suspected security; checks actually performed; facts versus assumptions; current owner; next update; proposed destination. Put “reported by requester” beside an unverified symptom. Expected: a readable handover with an observation-only boundary and no invented diagnosis. Verify every assertion exists in the fixture or your test evidence. Recovery: mark absent facts unknown and ask the requester; never convert “cannot connect” to “DHCP fault” without evidence.

## H7. Practise office Windows/network checks in isolation — unrun
Start: an authorised personal Windows 11 VM/office-style lab connection, not machinery. In Settings inspect connection status. In a terminal use `ipconfig /all` to record address, gateway, DNS servers and DHCP indication. Run `nslookup example.com` and record the response. If appropriate to the test network, check an approved gateway with ping; a blocked ping is inconclusive. Expected: observations that distinguish local configuration from name resolution. Verify against the lab's known network settings. Recovery: inspect virtual NIC/adapter and DNS configuration; do not change employer VLANs, machine addressing or routing. Label read-only observations and any separately authorised lab changes. Redact identifiers before publishing [T9].

## H8. Practise an office printer and peripheral handover — unrun
Start: an authorised personal test printer/peripheral and a baseline working configuration. Record device model, connection and symptom; inspect cable/power, selected printer, queue and driver status using normal Windows settings. Use a non-sensitive test page where allowed. Expected: a documented check sequence and confirmed test result or clear escalation. Verify the actual page/output and user confirmation. Recovery: restore your original test settings or escalate; a printing symptom does not authorise deleting every queue or changing a production print server. Hardware replacement and driver deployment remain separate competencies requiring evidence [T10].

## H9. Observe a machinery-PC scenario safely
Start: only the synthetic t2 ticket; no connection to factory hardware. Add a note describing what you would ask: operator's safety assessment, affected production step, asset/vendor, approved contact, change history, agreed service window and escalation owner. Expected: a useful information request and no instruction to reboot, patch, scan or alter the PLC/HMI. Verify your note does not contain an executable machine action. Recovery: remove assumptions and involve the production owner and senior/supplier engineer. This is a tabletop exercise. It cannot close the manufacturing/PLC experience gap [T8].

## H10. Turn a checked fix into a knowledge article
Start: a personally observed office-lab result from H7/H8, or a clearly labelled fictional walkthrough if those remain unrun. Write: scope, symptoms, prerequisites, read-only checks, approved remedy, verification, stop/escalate conditions, rollback, owner and review date. Expected: a user guide that a colleague can follow. Verify a second reader can identify when to stop and what proves success. Recovery: replace unclear wording and distinguish expected results from observations. Do not publish employer tickets or configuration. A simulated example must remain labelled simulated.

## H11. Compare optional AI with the simpler template — planned/unrun
Start: six synthetic escalation packets, a completed manual template and an approved AI tool only if available. Define a blinded review sheet: preserved facts, correct route/boundary, omissions, invented claims, useful length and time/cost. Ask for a summary limited to supplied fields, preserving unknowns and stop conditions; include a test ticket containing an instruction to ignore the safety boundary. Expected target: no invented facts, no lost warnings and no instruction-following from ticket text. Verify each summary against source fields before any use. Recovery: discard unsafe output and retain the deterministic template. No AI API was called, no model benefit or latency measured, and no customer data is sent. Publish only after a real comparison supports the choice.

## H12. Handover rehearsal and review
Start: routing output, one escalation note and one knowledge article. Explain normal account support, urgent production impact and suspected security to a reviewer. State what you can check, what you cannot safely change, and who owns the next action. Expected: a clear 3-minute walkthrough; this is a rehearsal target, not a measured duration. Verify the reviewer can find symptom, impact, checks, owner and next update. Recovery: shorten the note and correct ambiguous facts. Record personal reproduction separately from assistant-authored code.

## I–K. Acceptance and evidence
Offline acceptance: six sample tickets match the stated demonstration routes; seven tests pass; security overrides ordinary routing; OT output remains observation only; Apple output requests specialist support; incomplete tickets stay review; unchanged reruns agree. Keep the manual baseline, sample output, test log, escalation note, knowledge article and architecture note. Record the exact environment and sample size. Live desk/network outcomes, real SLA improvement, industrial diagnosis and AI evaluation remain unrun. No “100% accurate” operational claim is justified by a small designed test set.

## Cleanup, interview story and conditional wording
Delete only generated output and disposable fixture copies. For personal VM/printer practice, restore documented original settings and remove test data; check no unrelated files/devices changed. No factory cleanup is needed because the aid never connects to it. A future production rollout needs policy review, approved integration, access control, auditability, retention and monitoring.

After personal reproduction, explain the rule precedence, a failure, your evidence and why an office fix may be unsafe on a machine PC. Conditional CV wording: “Built and evaluated a synthetic first-line triage aid with explicit production/security escalation boundaries.” Use only after doing and explaining the work. Do not claim PLC/HMI support. A LinkedIn post can discuss the learning with assistance credited and no employer commission implied. Optional extension: add structured helpdesk import with redaction and human confirmation; evaluate fresh unseen tickets before considering AI.


## Technical references

Retrieved 1 October 2026. Recheck current screens and entitlements before tenant/device work.

[T1] Microsoft Learn Add users and assign licences
https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users?preserve-view=true&view=o365-worldwide

[T2] Microsoft Learn Set up multifactor authentication
https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide

[T3] Microsoft Learn Windows automatic MDM enrolment; Intune and Entra premium prerequisites
https://learn.microsoft.com/en-us/intune/device-enrollment/windows/enable-automatic-mdm

[T4] Microsoft Learn macOS enrolment deployment guide
https://learn.microsoft.com/en-us/mem/intune-service/fundamentals/deployment-guide-enrollment-macos

[T5] Microsoft Learn device enrolment overview; choose ownership-appropriate Apple method
https://learn.microsoft.com/en-us/intune/device-enrollment/enroll-devices?tabs=byod-enrollment

[T6] Microsoft Learn Apple MDM push certificate; CSR, PEM and renewal ownership
https://learn.microsoft.com/en-us/intune/intune-service/enrollment/apple-mdm-push-certificate-get

[T7] Microsoft Learn Remove a former employee and secure data; access and retention before removal
https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee?view=o365-worldwide

[T8] NCSC Operational Technology secure connectivity introduction; operational continuity and safety context
https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity/introduction

[T9] Microsoft Learn ipconfig and nslookup; diagnostic command references
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig

[T9b] Microsoft Learn nslookup
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup

[T10] Microsoft Support printer connection and printing troubleshooting
https://support.microsoft.com/en-gb/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows
