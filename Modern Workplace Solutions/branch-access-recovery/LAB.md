# Lab 2 — Branch access: DNS, permissions and recovery

Status: offline triage checker implemented/tested on synthetic data. Windows Server, Hyper-V, domain, file-share and restore steps below are unrun. No live tenant or company network is involved. Host compatibility and licences still need checking.

## A. Outcome

Build a small isolated Windows test domain, diagnose a deliberately broken name lookup, restore access, and prove that permitted users can read a test share while another user is denied. The offline part teaches the check order; it does not connect to a server.

## B. Company context

BCN supports varied customer environments and advertises Windows Server, virtualisation, networking and storage alongside M365. Its support-services, Copilot and Microsoft partnership announcements make dependable underlying access a plausible recurring need. A branch unable to open a file is an invented learning scenario, not an observed BCN incident. Cloud/AI direction does not make this an AI role.

## C. Job mapping

ownership/escalation; reusable notes; Windows Server; a basic Hyper-V VM workflow; basic network/DNS reasoning; identity dependency; a basic SMB share, not SAN/NAS or SQL Server administration. These foundations do not prove the advert's advanced skills.

## D. Learning-gap mapping

Previous support experience can provide context. Advanced server/virtualisation/firewall/storage delivery remains unestablished. The physical device gap is not solved by a VM. Keep professional support, this planned lab and any later supervised workplace experience separate.

## E. Recurring value and baseline

At each access incident, distinguish link, naming, service path, authorised access and denied unauthorised access. Baseline: five manual observations and a handover. Rules add consistency, not an assumed speed gain. No AI is required; a generated diagnosis would not replace a measured check or administrator approval.

## F. Architecture

Offline: synthetic JSON → strict Python → suggested next check, all failures and unknowns. The tool never declares a root cause or changes settings. Optional lab: compatible x64 Windows Hyper-V host → private switch LAB-ACCESS → SRV-LAB at 192.168.240.10/24 and CLIENT-LAB at 192.168.240.20/24. New forest lab.test; DNS hosted by SRV-LAB; one fictitious group, two users and a dummy SMB share. No default gateway on the private network. The domain controller also hosts the tiny share only to keep this isolated teaching setup small; separate roles in a real design. These addresses/names are examples inside the isolated lab, not customer infrastructure.

## G. Prerequisites, cost and checkpoints

Python 3.10+ standard library for offline work. For the VM part, confirm a compatible x64 PC, firmware virtualisation, a Hyper-V-capable Windows Pro/Enterprise host and administrator permission. Do not assume Mac/Apple Silicon or Windows Home compatibility. Plan roughly 16 GB host RAM and 120 GB spare storage for a small lab; verify actual OS requirements before allocating. Use a Windows Server 2025 evaluation ISO with Desktop Experience and an appropriately licensed Windows 11 Pro test client. Microsoft's evaluation lasts 180 days and needs internet activation within ten days. Obtain/update/activate guest images on an approved temporary internet connection before building the new domain, then disconnect that adapter and attach only LAB-ACCESS. Do not connect a promoted test domain controller to a shared external network. No Azure resources or paid account required. Existing hardware/client-licence costs are unknown; arrange access before buying. Budget one or two focused weekends, not an achieved duration. Checkpoints help recover a disposable lab, but are not production backups.

## H. Implementation — offline first; all VM steps unrun

### 1. Predict offline results

Start: terminal in this public project folder. Open templates/sample.json. Record the five manual outcomes before using the tool: link check, DNS check, identity/permission check, access-exposure review and missing evidence. Verify each against the fields rather than a narrative guess. If a check is unmeasured, retain null. No network probe is performed by this Python tool.

### 2. Run and inspect

Run `python3 -m unittest discover -s tests -v`, then `python3 scripts/check.py templates/sample.json outputs/result.json`. Windows may use `py -3` instead of python3. Expected: all tests pass and five results. Verify a failed unauthorised_denied check takes priority even when another check fails, and root_cause_confirmed stays false. Recovery: preserve a failed test, compare actual rules/fixture and fix the cause. A suggested next check is not a verified outage diagnosis.

### 3. Reject unsafe inputs

Copy the fixture to outputs/bad.json. Replace dns_ok with the string "false"; run against a new output path. Expected: error and no report. Next use the same input/output path; expect rejection without altering the input. Repeat with duplicate IDs and empty input. Restore the supplied fixture before continuing. Verify earlier valid output survives invalid input; never treat missing output as a successful check.

### 4. Prepare the host — unrun

Start: compatible authorised spare host and backed-up personal work. In Windows, check Settings → System → About for edition/processor/RAM, then Task Manager → Performance → CPU for virtualisation. If the host is unsupported, stop this section and retain the offline result. If approved and needed, enable Hyper-V through “Turn Windows features on or off”, select Hyper-V, accept and restart when prompted. Expected: Hyper-V Manager opens. Verify no other required virtualisation workload is disrupted. If unavailable or conflicting, follow the linked Microsoft requirements and resolve with an experienced reviewer; do not alter firmware blindly. This guide has not been exercised on your machine.

### 5. Create isolated infrastructure — unrun

Open Hyper-V Manager → Virtual Switch Manager → New virtual network switch → Private → Create. Name it LAB-ACCESS and apply. Expected: a private VM-only switch; verify it is not External or Default Switch. Create two Generation 2 VMs through New → Virtual Machine: SRV-LAB (4 GB RAM, 60 GB virtual disk) and CLIENT-LAB (4 GB RAM, 64 GB disk). These are lab allocations to check against guest requirements, not universal minimums. Use the prepared installation media; select Desktop Experience for Server and a licensed Pro client. Complete only lab-local accounts with new passwords kept in a private password manager. Attach each solely to LAB-ACCESS after installation/update/activation preparation. Expected: both guest consoles start. Recovery: if media/Secure Boot settings prevent boot, consult OS/Hyper-V guidance and correct that VM, preserving the host. Do not disable security on unrelated machines.

### 6. Set lab names and addresses — unrun

In SRV-LAB, use Server Manager → Local Server → Computer name → Change; rename and restart. In each guest, open Network Connections, choose its lab Ethernet adapter → Properties → Internet Protocol Version 4. Set server 192.168.240.10, client 192.168.240.20, subnet mask 255.255.255.0; leave gateway blank. Set each DNS server to 192.168.240.10. Expected: `ipconfig /all` in each guest shows those settings on the one lab adapter. Verify the host has no physical adapter bridged to this private switch. Recovery: wrong adapter/name/address means correct only the disposable guest and retest. A blank gateway is intentional; there is no internet route on this switch.

### 7. Install a new forest — unrun

Sign in as the local lab administrator on SRV-LAB. Server Manager → Manage → Add Roles and Features → Role-based installation → select SRV-LAB → Active Directory Domain Services → Add Features → Next → Install. Expected: role installs. Select the notification flag → Promote this server to a domain controller → Add a new forest → root domain lab.test. Keep DNS selected, set a new private Directory Services Restore Mode password, review paths/options and run prerequisite checks. Expected: checks pass or warnings are understood in this single-server isolated lab. The missing parent DNS delegation warning may be expected for this new private forest; unresolved errors require review. Install and allow restart, then sign in with the lab domain administrator. Verify Server Manager reports AD DS/DNS and open Active Directory Users and Computers. Recovery: if promotion fails, preserve the error and rebuild this disposable VM from the pre-domain baseline after review; never join an existing real forest.

### 8. Create least-privilege test identities — unrun

Open Active Directory Users and Computers → lab.test → create an OU named Practice. Within it create users reader1 and outsider1, with new lab-only passwords, and a global security group LabReaders. Add reader1 to LabReaders; leave outsider1 outside it. Do not add either user to administrator groups. Expected: two ordinary users and one group. Verify membership in each user's Member Of tab and the group's Members tab. Recovery: remove an unintended membership and recheck before testing access. Keep the lab administrator account solely for setup.

### 9. Join the client — unrun

On CLIENT-LAB verify DNS is 192.168.240.10, then run `nslookup lab.test`. Expected: the lab DNS server resolves the new domain. Open Settings → System → About → Domain or workgroup/advanced system settings → Computer Name → Change; select Domain and enter lab.test. Supply lab administrator credentials at the secure prompt and restart. Expected: welcome to the lab domain and successful restart. Verify computer membership in system properties. Recovery: if the domain is not found, check private switch, addresses and DNS first; do not point at public DNS or use workplace credentials. Time differences can affect sign-in; compare the guest clocks before escalating.

### 10. Publish a tiny test share — unrun

On SRV-LAB create C:\LabShare and a file readme.txt containing only “lab access test”. Right-click folder → Properties → Sharing → Advanced Sharing → Share this folder, name LabShare. Set share permissions so LabReaders has Read and lab Administrators retain Full Control; remove an unwanted Everyone grant. In Security, keep SYSTEM/Administrators, give LabReaders Read & execute, and remove inherited broad ordinary-user access if present by disabling inheritance and converting entries, then reviewing them. Do not remove administrator recovery access. Expected: both share and file permissions allow only the intended group at ordinary-user scope. Verify both tabs; they combine, so share permission alone is insufficient. Recovery: if uncertain, stop and have the reviewer check the ACLs before exposing any real data. Use only this dummy file and private switch.

### 11. Prove allowed and denied access — unrun

Sign into CLIENT-LAB as LAB\reader1. Open \\SRV-LAB\LabShare, read the file and try to create a new file. Expected: read succeeds, write is denied. Sign out fully, then sign in as LAB\outsider1 and open the same path. Expected: access denied. Separate sign-ins avoid reusing cached administrator credentials. Record each outcome and identity privately. From an approved client session run `Test-NetConnection SRV-LAB -Port 445`; expected TCP check recorded separately from share authorisation. Recovery: if TCP fails, inspect service/network profile and the built-in File and Printer Sharing rules on the isolated guest; do not disable Windows Firewall wholesale. If outsider access succeeds, treat it as failed acceptance, inspect both permission layers and group membership, correct the lab ACLs and repeat all three access tests.

### 12. Break DNS, diagnose and restore — unrun

Record the client's working DNS setting. Change only CLIENT-LAB DNS to unused 192.168.240.99. In an administrator prompt on that guest run `ipconfig /flushdns`, then `nslookup SRV-LAB.lab.test`. Expected: lookup timeout/failure. Cached credentials or sessions may still permit some actions; do not infer all access must fail. Record lookup, IP configuration and any task result separately. Restore DNS to 192.168.240.10, flush the client cache and retry the same lookup and reader task. Expected: name resolves and authorised reading works again. Recovery: if not, compare private-switch membership, guest addresses and DNS service before changing anything else. Do not change server/firewall settings to mask a client DNS fault.

### 13. Practise a file restore — unrun

On the server, copy only C:\LabShare\readme.txt to a new private lab backup folder and verify its content. Modify the test file, record the change, then restore from the copy and reopen it as reader1. Expected: original text restored, reader still read-only and outsider still denied. This is a tiny file-copy recovery exercise, not a system-state or domain-controller backup. Recovery: if the copy is missing or permissions differ, stop and recreate only the dummy content under reviewed ACLs; do not claim restoration success. Keep checkpoints separate from this backup exercise.

### 14. Make the handover and record the boundary — unrun

Start: observed before/fault/after results. Write a ticket with symptom, impact, own checks, original DNS, change, outcome, original-task retest, permissions checks, rollback, escalation owner and next update. In a private fixture set fields from actual observations, not assumptions; run the offline checker and compare it with the manual note. Expected: every unmeasured field remains null. Produce a two-minute explanation and have someone introduce an unseen lab-only fault. Recovery: unclear evidence means repeat the test and keep the claim pending. Deploy this only as a disposable local lab; no remote management endpoint or tenant integration is published.

## I. Break/fix exercises

Offline: link and DNS both false must show both failures; access exposure must take priority; null must request evidence; injected text must reject. VM, unrun: restore wrong client DNS from step 12; remove reader1 from LabReaders and sign out/in to retest, then restore membership and retest; grant outsider access only to the dummy share as a deliberate reviewed fault, remove it and repeat denied-access testing. Change one thing at a time and preserve the starting settings.

## J. Acceptance and cleanup

Offline acceptance: five manual states agree, malformed input rejects without output damage, missing observations stay unknown, no mutation/root-cause claim. VM acceptance separately: domain membership checked, DNS fault observed/restored, reader reads/cannot write, outsider denied, file restored and original task repeated. Not achieved in this run. Save sanitised evidence first; shut down/remove only the two lab VMs and their virtual disks when no longer needed. Remove LAB-ACCESS only if unused. Remove temporary installation media according to your licence terms, retain private records securely and delete scratch outputs. Do not remove another VM, switch, domain or personal file. No cloud spend exists to cancel.

## K. Evidence package

Keep source, tests, fixtures, evaluation, architecture, lab and demo together. Later add permitted screenshots of lab-only addresses, domain/group configuration and before/after tests with date/environment/own contribution. Do not show passwords, product keys or real account names. Record source revision and failed as well as successful checks. A working VM lab supports Practised/Project scope, not independent advanced customer operations.

## L. Interview story

Problem: an access symptom can come from different layers. Constraints: isolated dummy systems and unknown existing hardware access. Design: test naming, service path and authorisation separately. Build: strict offline checker; real VM build still pending. Failure: synthetic evidence can show unauthorised access even alongside a network fault, so it gets priority. Verification: tests and manual baseline, later a real original-task retest. Intended value: a handover another engineer can follow. Improvement: repeat unseen faults and obtain reviewed real-world practice before expanding claims.

## M. Conditional CV wording — not usable yet

After independently completing and evidencing the VM section: “Built an isolated Windows Server test domain and read-only file share; reproduced a client DNS fault, restored access and verified allowed and denied user paths.” If only Python checks are completed, describe an offline synthetic triage checker instead. Do not claim SAN/NAS, production Hyper-V, advanced firewall or customer deployment.

## N. Optional extension and sources

Add a second member file server and reviewed DHCP scopes only after the first lab is repeatable. Later compare a read-only PowerShell evidence collector against manual results. No AI, SQL Server or paid Azure extension is required.

Sources checked 27 October 2026: BCN advert https://bcngroup.recruitee.com/o/2nd-line-support-consultant-5 ; three announcements as in Lab 1; evaluation https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2025 ; Hyper-V https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V (the lower-case URL first timed out; capitalised page successfully read); private switch https://learn.microsoft.com/en-us/powershell/module/hyper-v/new-vmswitch?view=windowsserver2025-ps ; AD DS https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100- ; SMB overview https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview ; DNS and TCP references in Lab 1. UI labels can vary by guest edition; verify the intended setting before applying it.
