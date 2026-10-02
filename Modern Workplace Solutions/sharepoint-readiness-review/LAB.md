# Lab: SharePoint readiness review

Independent portfolio learning demonstration, 30 September 2026. Codex-assisted synthetic local slice tested; personal independent operation and every tenant/API/tool/AI step remain unestablished. This is not commissioned work or an enterprise production system.

## A. Outcome

Help a site owner and M365 administrator review who can access content, whether storage needs attention, and what must be checked before accepting a content move. The end-to-end workflow finishes with a permission test, reconciled content and a short adoption handover. The implemented slice checks synthetic declarations; its workplace benefits remain targets.

## B. Public operating context

Microsoft documents site creation, sharing/access, storage and Multi-Geo. Migration vendors document scoped pre-checks and content-migration limitations. This independent scenario uses an owner-led review as a hypothesis for a recurring workplace problem; no particular customer's architecture or migration is assumed. Official sources are listed below.

## C. Workflow mapping

The workflow exercises site/library/list orientation, declared permissions/capacity, before-and-after content checks, tool orientation, a permission test and an owner handover. No enterprise scale, tool migration or Multi-Geo administration is established by the local slice.

## D. Learning scope

The goal is to understand permissions and content acceptance rather than equating a completion screen with success. Codex implemented and tested the local code under Bunamin's authorised brief. Independent explanation, live identity tests and tool operation need separate evidence.

## E. Toothbrush test

Users: site owner, collaboration administrator and service desk. Cadence: monthly ownership/access/capacity review; each joiner/mover/leaver; each content move or permission change. Friction: unmanaged access, owner ambiguity and an apparently successful copy that loses content or metadata. Success target: a review with explicit owners and acceptance evidence. No saved hours, reduced risk percentage or adoption uplift is measured.

## F. Architecture and simpler baseline

Approved source manifest + destination manifest → schema validation → deterministic differences → human decision and owner handover. Each file declares relative path, bytes, SHA-256, principals, unique-permission status and metadata. Site fields declare owner, storage and geography. The program cannot query Microsoft, follow sharing links, discover nested-group effective access or change anything. Synthetic `geo_verified` means the fixture explicitly declares a location; it does not verify real residency.

Manual baseline: owner/access matrix plus a before/after content list; compare counts, hashes, group mapping and metadata, then test real identities. Deterministic comparisons are sufficient here. AI is not needed to decide permissions or validate content. An optional handover explanation may later use a grounded approved template, but no AI component is implemented. A matching manifest can miss versions, lists, workflows, sensitivity/retention controls and unexported objects; those require separate scoped tests.

## G. Prerequisites, cost and time

Local: Python 3.11+, standard library only; package root `solutions/02-sharepoint-readiness/public/` or `Modern Workplace Solutions/sharepoint-readiness-review` in thinkbox. No cloud subscription/API key. Cost: no chargeable service for the local route. Estimate 60–120 minutes to inspect, run and explain the synthetic workflow.

Optional tenant route, **UNRUN**: separately authorised disposable M365 test tenant with SharePoint Online; a permitted SharePoint administrator/site owner and licensed test editor/reader/outsider accounts. Confirm licences before creating users; use isolated existing test identities where possible. Tool-specific migration work may need paid licences and broader approved permissions. Do not assume free trials or buy anything for this exercise. Multi-Geo is a separately licensed enterprise feature; keep it as a documentation/tabletop exercise if unavailable. Allocate a further 3–6 hours plus service/report latency for the basic tenant route, as an estimate.

## H. Granular procedure

All tenant/tool actions are **UNRUN** and require their own applicable authorisation for the named disposable tenant. The local route needs no tenant. Do not use an employer environment as a substitute.

### 1. Establish scope and safe data

Start: a fresh package copy. Action: read README, CONTRIBUTIONS, EVALUATION and templates/source.json. Check there are two synthetic files, generic Lab- groups and only `example.test` identities. Expected: no tenant/customer records or credentials. Verification: explain that owner, geo and permissions are declarations. Recovery: replace accidental private data with the original fixtures before proceeding; retain necessary real evidence privately.

### 2. Verify runtime and behaviour tests

Start: terminal in the folder containing scripts/, templates/ and tests/. Action: run `python3 --version`, then `python3 -m unittest discover -s tests -v`; Windows may use `py -3`. Expected: the recorded run passed 16 tests; your fresh run should pass the current suite. Verification: final OK and count, with meaningful cases including missing content, hash mismatch, altered permissions, metadata loss, empty inventory and unsafe paths. Recovery: confirm folder/runtime if imports fail; retain the error, fix the cause and rerun.

### 3. Create the manual comparison baseline

Start: source.json and destination.json unchanged. Action: compare site owners/geo/capacity and the two file records in a text editor. Match each path, byte count, hash, principals, inheritance and metadata. Expected: the file declarations match; destination site name differs intentionally. Verification: a private checklist records each compared field and marks actual effective access unknown. Recovery: a blank value is an open question, not permission to assume equality.

### 4. Run the normal complete path

Start: manual baseline complete. Action: `python3 scripts/review.py templates/source.json templates/destination.json`. Expected: MANIFESTS_MATCH, source_count 2, destination_count 2, no findings, exit 0. Verification: compare evidence/normal-report.json and read its scope limitation. Recovery: exit 2 means invalid/incomplete declarations; fix the schema from verified source data, never by inventing a hash or owner.

### 5. Run the realistic review path

Start: original fixtures preserved. Action: `python3 scripts/review.py templates/source-review.json templates/destination-review.json`. Expected: REVIEW_REQUIRED, exit 1; findings include missing owner, unverified geography, high capacity, broad link, unique permissions, missing content, hash difference, permission difference and metadata difference. Verification: locate each differing record and compare evidence/review-report.json. Recovery: keep the review finding until its real source is resolved; an expected exit 1 is not a broken evaluator.

### 6. Diagnose a corrupt or missing copy

Start: duplicate destination.json as scratch-destination.json. Action: replace the first sha256 with 64 zeros, run step 4 using the scratch file, then remove its second file row and rerun. Expected: CONTENT_MISMATCH, then MISSING_CONTENT as well. Verification: describe how equal counts alone could miss corruption or substitutions. Recovery: restore the fixture and verify MANIFESTS_MATCH; a real copy must be rechecked/retransferred from the permitted source, not have its manifest edited to hide the issue.

### 7. Diagnose unsafe or incomplete inventory

Start: another scratch source copy. Action: change a path to `../Private.txt` and run the comparator. Expected: INCOMPLETE/2. Next, restore the path and set sha256 to `unknown`; expected INCOMPLETE/2. Finally compare two files with empty files arrays; expected EMPTY_INVENTORY findings, not success. Verification: tests preserve these failure boundaries. Recovery: restore verified paths and computed hashes; collect a complete inventory before acceptance.

### 8. Prepare the operational review

Start: review output. Action: fill docs/handover.md with scope/window, accountable owner, source/destination, approved group mapping, findings and acceptance evidence. Separate an intended permission difference from accidental broadening. Expected: explicit review decisions with unresolved gaps visible. Verification: a reader can tell what is being moved, who approves and which observations allow acceptance. Recovery: unknown owner/mapping or location means stop acceptance and obtain the named decision; the script cannot approve it.

### 9. Verify tenant and test identities — UNRUN

Start: authorisation for a named disposable tenant and a cost/licence boundary. Action: sign in to `https://admin.microsoft.com`, verify the account/tenant privately, open Users → Active users and confirm a test owner plus editor, reader and outsider identities with SharePoint entitlement. If approved new users are needed: Add a user, enter a Lab- name, choose the test domain, assign the approved licence and require password change; store credentials only in the approved secret method. Expected: four identifiable test roles, no business users. Verification: use separate private-browser profiles to sign in; confirm the outsider belongs to no lab group. Recovery: stop if the tenant/account/licence differs. Record an unavailable route rather than buying a subscription.

### 10. Create two bounded test sites — UNRUN

Start: approved SharePoint administrator identity. Action: Admin centres → SharePoint → Active sites → Create → Communication site; choose an available standard template, name the first `Lab-Source`, assign the test owner and language, then create. Repeat as `Lab-Destination`. Record the actual resulting URLs privately. Expected: two new disposable sites, not a duplicate production URL. Verification: both are listed in Active sites and the owner opens each. Recovery: if the name exists, choose a new clearly disposable name; never delete a business site or redirect to reuse a name.

### 11. Build a tiny library and list — UNRUN

Start: Lab-Source as the owner. Action: open Documents and upload two local UTF-8 text files: Guide.txt containing `Synthetic guide` plus one newline and Checklist.txt containing `Synthetic checklist` plus one newline. Open Site contents → New → List → Blank list; name it `Collaboration register`, add text column `Owner` and choice column `Status` with Draft/Approved; add one synthetic row. In Documents add a choice Status column with the same values and mark both files Approved. Expected: two readable documents and one list row. Verification: record path, bytes, actual SHA-256, metadata and a list screenshot privately. Recovery: filenames/line endings alter hashes; compute actual hashes instead of forcing equality. The local fixture illustrates only declared files; the list needs its own check.

### 12. Establish the access boundary — UNRUN

Start: only the test owner has assigned lab access. Action: site Settings → Site permissions → Advanced permissions settings; add the editor to the site's Members group and reader to Visitors. Keep the outsider unassigned. Open each document in separate signed-in test profiles; test editor can edit, reader can read without editing, outsider cannot open. Expected: three distinct effective-access results. Verification: retain a private role/object/allowed/denied table, checking both direct site URL and document link. Recovery: if outsider opens a file, inspect site membership and Manage access/sharing links; remove only the unintended lab assignment with the owner's approval and retest. Do not alter tenant-wide sharing to pass the test.

### 13. Break and restore inheritance — UNRUN

Start: normal inherited access and a baseline access table. Action: as owner select Guide.txt → Manage access → Advanced (if present) → Stop inheriting permissions. Preserve owner access; remove only the test Members permission from this file while retaining Visitors Read. Confirm the test editor loses access to Guide but can still edit Checklist; reader still reads Guide. Expected: a deliberate unique scope and a changed access matrix. Verification: inspect the item's advanced permissions and repeat identity tests. Recovery: use Delete unique permissions/restore inheritance for that test file, then rerun the original matrix; if controls differ, consult current SharePoint documentation before changing anything. Do not lock out the owner.

### 14. Inspect storage without changing the tenant model — UNRUN

Start: SharePoint admin centre and disposable site. Action: inspect Active sites → selected lab site → General → Storage limit, and Settings → Site storage limits to record automatic/manual mode. Expected: a storage model and usage observation with report age. Verification: distinguish pooled allocation from a real per-site quota; Microsoft notes storage display latency. If the approved test tenant already uses Manual and a quota change is expressly within scope, record the prior value, set an approved bounded value and owner alert, then restore it after observing. Recovery: if mode is Automatic, do not switch the whole tenant for this lab; retain the synthetic threshold exercise. Never fill a real site to force an outage.

### 15. Run a small manual pilot copy and validate — UNRUN

Start: normal permissions restored, source baseline recorded, destination owner access confirmed. Action: download the two source documents to a private local folder and upload copies to Lab-Destination/Documents; recreate the Status column and Approved values. Assign only the approved lab Members/Visitors mapping. Recreate the single list row separately. Expected: a deliberately manual pilot, not a tool-driven or fidelity-preserving migration. Verification: download destination files, compute SHA-256 with `python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('Guide.txt').read_bytes()).hexdigest())"` from their folder, compare both hashes/bytes and metadata, and repeat all three identity tests. Check the list separately. Recovery: quarantine/recopy a mismatched file and retest; stop if history, labels or permissions require preservation beyond this pilot. Do not describe manual copying as ShareGate/BitTitan migration experience.

### 16. Understand migration tools and multi-geo — UNRUN

Start: official guides and a documented pilot scope. Action: read the ShareGate pre-check guide and BitTitan's exact SharePoint Online document-library guide; record source/target types, permissions, licence, supported objects and exclusions. For a separately authorised licensed ShareGate trial: Copy → chosen type → connect only the test source → select source → Next → connect test destination → select destination/object → Run pre-check → Export. Expected: warnings/errors requiring review, without copied content. Verification: inspect mappings/unsupported features; a pre-check is not a migration and its later report may differ. Recovery: no trial/licence/approved permissions means documentation-only orientation. Do not configure BitTitan credentials or launch a migration here. For Multi-Geo, read the official architecture/licensing page and draft a primary/satellite/owner/residency table; no satellite is created and a geo string is not compliance evidence.

### 17. Hand over and verify learning — UNRUN for tenant adoption

Start: reconciled pilot, access matrix and open limitations. Action: explain to a test learner how to find a document, coauthor, share to a named permitted person, check Manage access and ask the owner for help. Ask them to locate Guide, identify their allowed action and describe who approves a new member. Expected: an observed task and a short help note. Verification: record actual completion/errors, not a satisfaction percentage. Recovery: revise the unclear instruction and repeat the task; no broad sharing link is needed. Owner acceptance includes content, access, metadata, list and unresolved-history limits.

### 18. Capture evidence and clean up

Start: local exercise finished; optional disposable objects listed. Action: retain synthetic outputs and source/runtime metadata; delete your scratch copies. If tenant steps were separately run, remove only the two recorded disposable sites through Active sites → Delete, remove only created test identities/licences/consents and verify the recorded objects are absent or in the expected recycle state. Do not permanently purge by default. Expected: no chargeable lab resource left active beyond the approved retention plan. Verification: check the final object list/cost boundary privately. Recovery: retention blocks need owner review; do not bypass compliance controls. Keep real credentials/exports and identity screenshots outside public evidence.

## I. Break/fix

Local faults: missing and unexpected content, same-sized hash corruption, size mismatch, altered groups/inheritance, lost metadata, missing owner, unverified/different geography, empty inventory, duplicate/unsafe paths and malformed hash. Planned tenant faults: one incorrect lab group, one unique item scope and one wrong file copy. Each needs a baseline, bounded correction and a repeated identity/content check. Never test leakage with confidential data.

## J. Acceptance and outcome rules

Observed: 16 behavioural tests passed on 30 September; matching two-file manifests returned MANIFESTS_MATCH/0; review fixtures returned REVIEW_REQUIRED/1. The evaluator is deterministic and input-preserving. Actual effective access, complete discovery, versions, workflows, list fidelity, migration performance, tool operation and residency remain unestablished. Future tenant acceptance requires all three identity tests, two independently computed content hashes, approved metadata/list checks, owner sign-off and cleanup. No labour saving, reduced incident rate or customer outcome is claimed.

## K. Artefacts

Public package: source, four synthetic manifests, 16 tests, recorded normal/review outputs and runtime/source hash; README, canonical lab's sanitised copy, EVALUATION, DEMO SCRIPT, CONTRIBUTIONS, CHANGELOG and architecture/handover notes. No live screenshots or demo video exist. Keep any actual tenant ledger private.

## L. Interview story

Problem: content changes need ownership and acceptance, not just a completion screen. Constraint: client unknown, no licensed test migration. Design: compare declarations and require human/identity evidence. Build: Codex-assisted local checker. Failure: equal counts can hide corruption or changed access; tests detect differences. Verification: two synthetic scenarios and 16 tests; live checks unrun. Business value: proposed safer handover, unmeasured. Improvement: personally validate the permissions lab before asking for a licensed pilot. Never present tool orientation as commercial migration delivery.

## M. Conditional wording

Use only after Bunamin personally runs and explains the evidenced scope: “Built and tested a SharePoint readiness lab using synthetic before-and-after manifests to flag missing content, changed permissions and metadata, with a documented owner handover.” Live wording needs separately recorded permission/content tests. Current description: “Prepared a Codex-assisted synthetic comparison demo; tenant, migration-tool and independent validation pending.” Do not claim multi-geo administration, enterprise migration delivery or automatic security enforcement.

## N. Optional extension

After independent local/tenant validation, add a permitted read-only inventory adapter with complete pagination, explicit object scope and owner-approved effective-access tests. Extend acceptance to versions, list columns/items and label/retention behaviour appropriate to the actual tool. Compare each change with the manual baseline. CI may run only synthetic tests; no migration or tenant mutation belongs in ordinary CI. Any AI summary must cite approved findings and leave the human decision unchanged.

## Official references

Checked 30 September 2026; guides describe vendor capabilities, not this client's configuration or completed candidate experience.

- Permissions: https://learn.microsoft.com/en-us/sharepoint/modern-experience-sharing-permissions.
- Site creation: https://learn.microsoft.com/en-us/sharepoint/create-site-collection (updated 24 June 2026).
- Capacity and mode: https://learn.microsoft.com/en-us/sharepoint/manage-site-collection-storage-limits (updated 30 July 2026).
- Multi-Geo: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-multi-geo?view=o365-worldwide (updated 26 August 2026).
- ShareGate pre-check: https://help.sharegate.com/en/articles/10236265-run-a-pre-check; report interpretation: https://help.sharegate.com/en/articles/10236266-pre-check-report-details (13 December 2024).
- BitTitan exact scenario and limits: https://help.bittitan.com/hc/en-us/articles/1260800116209-SharePoint-Online-to-SharePoint-Online-Document-Library-Migration-Guide-including-Microsoft-365-Groups (7 May 2026).
