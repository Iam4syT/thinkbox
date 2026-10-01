# Lab 1 — Joiner, leaver and device readiness

## A. Outcome and status
Build a reviewable starter/leaver checklist that links approval, identity, licence, MFA and equipment readiness. The offline Python checker is implemented and locally evaluated by Codex with synthetic data. Microsoft 365, Entra and device steps below are unrun. The learner has not yet independently reproduced either part. This is a learning workbench, not a live provisioning system.

## B–E. Business context, requirements, gaps and recurring value
Scenario: a manufacturing-support team needs account/licence/MFA setup, equipment preparation, onboarding/offboarding and accurate asset records (a hypothetical manufacturing-support workflow). Hypothesis: a joined-up readiness checklist could help the service desk catch incomplete handovers before colleagues start work. It does not establish that the hypothetical organisation has a broken onboarding process. Requirements addressed: Microsoft 365 administration, Entra, MFA, managed devices, asset issue/return and documentation. Gaps addressed: complete lifecycle ownership, managed Windows 11 setup and unfamiliar Apple management. The toothbrush test is every joiner, mover, leaver and redeployment, rather than a one-off dashboard. Intended outcomes are clear ownership and fewer missed checks; no time or cost saving is measured.

## F–G. Architecture and prerequisites
Synthetic request JSON → deterministic checklist checks → evidence JSON → human review. The tool writes only local files and makes no network calls. Microsoft 365/Entra/Intune remain a separate optional learning stage. Intune is a chosen lab stack, not a verified the hypothetical organisation MDM product. A manual checklist is the simpler baseline; automation helps consistent checking, not access approval. AI is unnecessary here and is not implemented.

Use Python 3.10+ and a text editor. No packages, subscription or tenant are needed for offline mode. Estimate 60–90 minutes for the offline walkthrough; tenant/device learning may take several separate sessions. These are planning estimates, not measured time. For the optional stage, use a disposable Microsoft 365 test tenant with Exchange/Teams/SharePoint and Intune entitlement, suitable roles, test accounts, Entra ID P1/P2 if automatic Windows enrolment is selected, and a supported test Windows 11 Pro/Enterprise device plus a personally authorised test Mac and iPad/iPhone. Hardware access and eligible trials are not guaranteed. Check actual licence charges before purchasing; no paid resource is provisioned by this run. Use synthetic names, no employer data. Never use production machines or personal primary devices for destructive exercises.

## H1. Locate the project and check the runtime
Start: the supplied reusable folder or published project has been copied to a local working folder. Open a terminal in its public folder. Run `python3 --version`, then list `scripts`, `templates` and `evidence`. Expected: Python 3.10+ and readiness.py/test_readiness.py/sample.json are present. Verify filenames against README. Recovery: if the command is missing, use your known Python 3 installation; if a file is missing, recover the complete project before continuing.

## H2. Inspect the request before running it
Start: unchanged templates/sample.json. Open it in a text editor. Read j1 through j5 and l1. Each joiner has id, approval, action, licence, mfa_registered, asset_id, mdm_state and groups. The leaver has retention_review and asset_returned. Expected: six fictional records. Verify there are no real names, emails or device identifiers. Recovery: restore the original sample if edits or private data have been added. The status fields are assertions in sample data, not evidence retrieved from a tenant.

## H3. Establish the manual baseline
Start: the six sample requests are visible. On paper or in baseline-notes.md, mark which requests have approval, access, licence, MFA, managed-device and asset evidence. A valid request still needs human approval for actual work. Expected: j1 passes the sample checks; j2 lacks approval, j3 requests an unexpected privileged group, j4 lacks MFA, j5 lacks confirmed MDM state; l1 lacks retention review and equipment return. Verify your reasoning before seeing the checker output. Recovery: reread the field definitions if your answer differs; do not change the sample to make it pass.

## H4. Run and compare the checker
Start: public project root and original sample. Run `python3 scripts/readiness.py --input templates/sample.json --output output/readiness.json`. Expected: six results; j1 is ready-for-human-review and five requests are review. Open output/readiness.json and compare every reason with the manual baseline. Verify input bytes remain unchanged. Recovery: JSON errors require correcting syntax in a copy; wrong path requires returning to the project root. No output status executes a tenant change.

## H5. Test failure and idempotency
Start: normal run succeeds. Run `python3 -m unittest discover -s scripts -p "test_*.py" -v`. Expected: seven behavioural tests pass, including missing approval, elevated group, unmanaged device, duplicate ID, leaver retention and empty input. Rerun the checker to a second file and compare outputs; unchanged inputs should produce identical content. In a disposable copy, duplicate j1's ID and run again. Expected: missing-or-duplicate-id. Recovery: restore the fixture and rerun tests. Passing these checks does not establish completeness against a real HR or access policy.

## H6. Prepare an approved test-tenant request — unrun
Start: you have explicit authority over a disposable test tenant and have checked licences and spend. In a local checklist record LAB-JOIN-01, the account to create, approved staff group, licence, device and reviewer. Record the existing MFA/security policy and which limited admin role is appropriate. Expected: one clear test request with a cleanup plan. Verify no real colleague or production group is selected. Recovery: if you lack authority/licences, stop at offline mode and mark tenant evidence unrun. Do not disable tenant security to get a test working.

## H7. Create a test identity and record its licence — unrun
Start: approved disposable tenant and suitable user/licence admin access. In Microsoft 365 admin centre, use Users > Active users > Add a user. Create a unique LAB-JOIN-01 test account in your tenant domain and assign only an available approved test licence. In Entra, find that exact user and add it to the approved non-privileged lab group. Expected: the correct user, licence and group appear. Verify the object/account identity and licence assignment in the portals, not only in local JSON. Recovery: missing licences stop provisioning; correct only the test request or remove the mistaken test membership. Record a before/after screenshot privately. These are learning actions you perform later, not actions executed by this assessment [T1].

## H8. Verify access and MFA — unrun
Start: the test user exists. Follow the tenant's existing MFA policy and register a permitted test authentication method through the user's security-information flow. Sign in as the test user and check approved Outlook, Teams and SharePoint access; send a harmless test mail and confirm receipt. Expected: successful authorised sign-in and app access, with MFA evidence. Verify actual sign-in/authentication records and the destination mailbox. Recovery: use the shown error and sign-in details to distinguish missing licence, propagation, wrong account or authentication policy; escalate beyond your test permissions. Do not broadly turn off MFA or claim that one successful login proves all protection [T2].

## H9. Windows 11 device handover — unrun
Start: a disposable supported Windows 11 test device/VM and approved enrolment method. Record asset tag, serial/VM ID, owner, OS version and intended management state. Use the organisation's permitted enrolment flow, then confirm the device record and applicable compliance status in Intune. Test sign-in and only the approved apps. Expected: a traceable device record and working test-user session. Verify the local device matches the portal record before setting mdm_state to managed. Recovery: identify enrolment restrictions, licence and identity mismatches; keep the handover pending rather than marking ready. No corporate Autopilot provisioning capability is inferred [T3].

## H10. Learn managed Apple enrolment — unrun
Start: authorised disposable Apple devices and an Apple MDM push certificate in the test tenant. First read the current macOS and iOS/iPadOS enrolment choices [T4–T6]. Choose a supported method for your test device's ownership; do not treat personal enrolment as supervised corporate enrolment. For a supported personal macOS Company Portal scenario, install the official Company Portal app, sign in as the lab user, choose the offered enrolment, install the downloaded management profile in System Settings when prompted, and return to Company Portal to confirm status. For an iPad/iPhone personal-enrolment scenario, use Company Portal and its supported Safari flow to obtain the profile, install it in Settings > General > VPN & Device Management, then return to Company Portal for status checks. Follow the current vendor prompts if screens differ; stop if your ownership/enrolment method is unsupported. Expected: a device record in Intune and visible management profile on the exact device. Verify app access, management state and serial/device identifier. Recovery: inspect certificate validity, enrolment restrictions and profile installation; ask for experienced supervision instead of erasing the device. Record Mac and iPad/iPhone evidence separately; one platform does not demonstrate all three. Without real hardware, mark this stage unrun, not simulated Apple proficiency.

## H11. Certificate prerequisite if the test tenant has none — unrun
Start: a tenant you own, authorised Apple account and no existing Apple MDM certificate. In Intune: Devices > Device onboarding > Enrollment > Apple > Apple MDM Push Certificate. Download the CSR, create the matching certificate in Apple's portal using your lab account, then upload the downloaded .pem and record the account used and expiry. Expected: active certificate status. Verify the exact certificate identity before enrolment. Recovery: if permission, ownership or terms are unclear, pause for the tenant owner; never replace a production certificate. Renew with the same Apple account when due; expiry can affect management. This prerequisite is separate from the offline checker and was not performed [T6].

## H12. Leaver and asset return exercise — unrun
Start: the same test user/device with no valuable data. Record a leaver approval, exact account and asset, retention decision and change reviewer. Following your test tenant's approved procedure, block the test sign-in and revoke test sessions; review mailbox/OneDrive retention needs before licence removal. Confirm group removal and asset return in a handover record. Expected: the retained test data decision is documented and the test user cannot regain access once controls take effect. Verify portal state and a controlled sign-in attempt; account for token propagation. Recovery: reverse only changes authorised for the lab user when testing rollback. Do not delete data or wipe devices as a shortcut. The local JSON checker does not execute these operations [T7].

## I–K. Acceptance, failure recovery and artefacts
Offline acceptance: six records processed; j1 has no findings; all five adverse examples are caught; seven behaviour tests pass; input unchanged; two runs agree. Record actual outputs rather than only “works”. Tenant acceptance, still unrun: approved identity/licence/group, observed MFA and app access, Windows and Apple device records, leaver access check, asset return and reviewed retention/cleanup. Failures to practise include duplicate ID, absent approval, privilege request, expired MDM certificate observation and wrong-device mapping. Keep screenshots, baseline notes, output JSON, test log, architecture note and a brief personal explanation. A certificate problem is inspected in the test tenant; do not break an employer's certificate.

## Cleanup, interview story and conditional wording
Offline: remove only your generated output folder and disposable edited copies; preserve supplied evidence. Tenant: after retention review remove test-only groups/licences/accounts created by this exercise, retire the test profile using a suitable authorised method, and confirm that unrelated accounts/devices remain untouched. Do not assume deletion is reversible. Keep the Apple certificate if other test devices depend on it; coordinate tenant shutdown and recurring costs with its owner.

Interview story after personal reproduction: explain why an apparently complete request can still lack approval, MFA or an asset link; show the failure and corrected result. Conditional CV wording, only after completion: “Built and tested a synthetic lifecycle-readiness checker, then documented supervised Microsoft 365/device onboarding practice.” Name only the tenant/device stages actually performed. LinkedIn wording must say independent lab and credit assistance. Optional extension: add read-only Graph inventory after learning permissions, then compare portal evidence with local declarations. Do not let AI authorise account changes.


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
