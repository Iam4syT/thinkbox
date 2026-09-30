# Lab: M365 service review

Independent portfolio learning demonstration, 30 September 2026. Codex-assisted synthetic local slice tested; personal independent operation and every tenant/API/tool/AI step remain unestablished. This is not commissioned work or an enterprise production system.

## A. Outcome

Give an M365 support team a small, repeatable review that turns service-health, activity, capacity and audit observations into an owner-led action list without changing the tenant. The useful outcome is a clearer review and handover. Saved time, better uptime or fewer incidents are targets requiring a workplace baseline, not measured results here.

## B. Public operating context

Microsoft provides service health and usage reporting interfaces. An independent workplace scenario uses those interfaces as orientation for an owner-led recurring review. The need for a standard handover is a design hypothesis, not a measured customer problem. Official sources are listed below. No particular employer, tenant architecture or incident is assumed.

## C. Workflow mapping

The workflow exercises service observation, escalation, activity/capacity interpretation, a bounded audit checklist, adoption discussion and documentation. It does not establish production monitoring, enterprise architecture or commercial impact.

## D. Learning scope

The goal is to understand the quality of a repeatable operational review and its unknown-data boundaries. Codex implemented and tested the local code under Bunamin's authorised brief. Personal independent explanation, live access and operational ownership require their own evidence.

## E. Toothbrush test

Intended user: service desk lead or M365 administrator. Cadence: daily service-health check and weekly activity/capacity review, plus each service incident. Repeated friction: incomplete observations, unclear owners and provider incidents being mistaken for local faults. A completed review should record the source window, unknowns, severity, owner, next action and recheck point. Adoption means useful work completed; a low activity count alone does not prove poor adoption.

## F. Architecture, baseline and boundaries

Data flow: permitted snapshot → strict local checks → deterministic JSON findings → human review → private action/knowledge record. Four expected workloads, a 48-hour freshness limit, a 90% declared storage threshold and a 20% synthetic activity ratio make the demo easy to inspect. These are lab choices, not employer policy. The program reads one JSON file and writes only its standard output; it has no credentials, network client or remediation path. Its audit observations are synthetic labels, not live detection.

Simpler baseline: read the four official health statuses, then a checklist for capacity, activity, audit completeness and ownership. Keep that baseline if it is adequate. The program standardises missing-data and threshold checks; it does not replace platform expertise. AI is planned only for a grounded explanation of an already-reviewed incident. It must never set health status, prescribe unapproved tenant changes or invent an incident cause.

## G. Prerequisites, licences, cost and time

Local path: `solutions/01-service-review/public/`, or the public repository's `Modern Workplace Solutions/m365-service-review`. Python 3.11 or newer; only the standard library; no installation beyond Python and no API key. Local run cost: no chargeable service. Allocate 45–90 minutes for understanding, rerunning and explaining the synthetic slice; this is a planning estimate, not a recorded duration.

Optional live route: a separately authorised isolated Microsoft 365 test tenant with the needed services; a work/school identity; delegated `ServiceHealth.Read.All` for health and `Reports.Read.All` for usage, tenant consent and an appropriate reporting role. Purview audit visibility requires the appropriate audit role and licence. Confirm current tenant entitlement/retention; do not assume a free Developer Program tenant or instant activity reports. No paid account is created in this run. A 2–4 hour live learning session plus reporting latency is an estimate. The offline fixtures remain the zero-service-cost route.

## H. Granular procedure

Every live step below is **UNRUN**. Stop at the local boundary if there is no authorised test tenant; that is still a valid synthetic demonstration.

### 1. Confirm the safe starting state

Start: a copy of this package, without employer data. Action: read README.md, CONTRIBUTIONS.md and EVALUATION.md; open templates/healthy.json in a text editor. Check the sample domain is `example.test`, all records are synthetic, and no token exists. Expected: four named services and a deliberately declared audit window. Verification: explain implemented, simulated and planned components aloud. Recovery: remove any accidental private export from your copy and use the supplied fixtures; never commit the export.

### 2. Verify the runtime and folder

Start: a terminal in the package root containing scripts/, templates/ and tests/. Action: run `python3 --version`, then `python3 -m unittest discover -s tests -v`. Windows: use `py -3` for the same command arguments. Expected: the recorded run passed 14 behavioural tests; your run should pass the current test suite. Verification: read the final `OK` and test count, rather than assuming a quiet command worked. Recovery: if Python is missing, install an approved Python runtime; if imports fail, confirm you are in the package root. Retain the error before retrying.

### 3. Establish the manual baseline

Start: healthy.json unmodified. Action: manually check all four statuses, capture time against 09:00 UTC on 30 September, activity 60/100, storage 40/100, owner presence, and the synthetic audit completeness flag. Expected: no checklist finding. Verification: write the six observations into a private note; do not time the exercise unless actually measured. Recovery: an unknown or blank value stays unknown. Do not repair the input by guessing a favourable number.

### 4. Run the complete normal path

Start: baseline recorded. Action: `python3 scripts/review.py templates/healthy.json --as-of 2026-09-30T09:00:00Z`. Expected: `NO_RULE_FINDINGS`, service_count 4 and an empty findings list; exit 0. Verification: compare with evidence/normal-report.json. Read its limitation: no rule findings does not prove a healthy or secure tenant. Recovery: exit 2 means incomplete/invalid input; check the reported field and the supplied schema before retrying.

### 5. Run the review path

Start: original fixtures preserved. Action: `python3 scripts/review.py templates/review.json --as-of 2026-09-30T09:00:00Z`. Expected: `REVIEW`, exit 1, with SERVICE_REVIEW, ADOPTION_REVIEW, CAPACITY_REVIEW, OWNER_REVIEW and AUDIT_REVIEW findings. Verification: compare evidence/review-report.json and identify which observation caused each finding. Recovery: exit 1 is an expected operator review, not a crashed script. Do not suppress findings to obtain exit 0.

### 6. Introduce a stale snapshot and recover

Start: normal fixture. Action: copy it to `scratch.json` in a text editor and change captured_at to `2026-09-20T08:00:00Z`; run the step 4 command using scratch.json. Expected: `INCOMPLETE`, exit 2 and STALE_SNAPSHOT. Verification: explain why stale observations cannot support a current-health statement. Recovery: restore the original timestamp from the fixture and rerun; the state returns to NO_RULE_FINDINGS. Stale real reports must be recollected, not timestamp-edited.

### 7. Exercise missing data and bad input

Start: another scratch copy. Action: remove OneDrive's service row, then run the same command. Expected: MISSING_SERVICE and INCOMPLETE. Next, set licensed_users to 0 while active_users is 60. Expected: a validation error, exit 2. Verification: run the tests for missing workload, impossible usage, unknown provider status, future capture and duplicate services. Recovery: restore the original row and values; do not reinterpret invalid input as zero issues. The command must remain read-only.

### 8. Produce a useful operator handover

Start: review fixture output. Action: use docs/handover.md to record the capture window, finding, source, provisional owner, next check and disposition. Write a plain sentence such as: “Exchange has a declared provider degradation; check the current advisory and affected users before treating this as a local fault.” Expected: each action is grounded in a finding and an unknown is visible. Verification: a second reader can identify who decides and what observation would close it. Recovery: no named owner means owner assignment is the next action; do not invent a client's team structure.

### 9. Confirm a live tenant boundary — UNRUN

Start: only after obtaining applicable authorisation for the named disposable tenant. Action: open `https://admin.microsoft.com`, select the account menu, and verify the approved tenant name/domain privately; open Health → Service health and Reports → Usage. Expected: access to the relevant subscribed services/reporting window. Verification: record tenant identity and allowed scope privately, then sign out if the tenant differs. Recovery: access denied means request the limited role/consent through the tenant owner; never use production access to bypass the exercise. Do not publish account/tenant screenshots.

### 10. Read service health through the official interface — UNRUN

Start: approved identity and scoped access. Action: open each listed health incident/advisory and record service, current status, impact, update time and official reference. For API orientation, open Graph Explorer at `https://developer.microsoft.com/graph/graph-explorer`, sign in to the same authorised test tenant, choose GET and v1.0, and request `https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews?$expand=issues`. Consent only the documented permission if approved. Expected: a 200 response with subscribed services and, where present, issues. Verification: compare one service against Service health; follow any returned nextLink rather than discarding later pages. Recovery: 403 requires role/consent review; 429 requires the supplied Retry-After; empty/unknown data stays incomplete. No API command is run here.

### 11. Obtain an approved usage report — UNRUN

Start: same test tenant and appropriate reporting access. Action: in Reports → Usage choose SharePoint → Site usage, set an available window, note Report refresh date, and export to a private folder. API orientation: GET `https://graph.microsoft.com/v1.0/reports/getSharePointSiteUsageDetail(period='D7')`. Expected: the documented report download/CSV rather than a JSON service-health shape. Verification: confirm refresh date, storage byte units and that identifiers may be concealed; do not infer missing owners from a privacy setting. Recovery: the report endpoint can return a short-lived preauthenticated redirect; follow it only in the approved context and do not publish its URL. Wait for an available report; do not fabricate activity.

### 12. Review audit context and roadmap impact — UNRUN

Start: authorised audit access and a chosen test window. Action: open `https://purview.microsoft.com`, Audit → Search; select the window and a specific test activity, start the search and read the actual result/detail. Separately open the Microsoft 365 Roadmap and record one announced change's service, status/date and possible support/training impact. Expected: actual results or an explicitly empty/unavailable window plus a source-grounded change note. Verification: distinguish no matching audit event from a missing/unlicensed collection; roadmap status is an announcement, not this client's deployment date. Recovery: missing audit access/retention stays incomplete; ask the tenant owner to validate licence and role. No remediation or rollout is performed.

### 13. Normalise permitted data locally — UNRUN

Start: private exports and a reviewer-approved schema mapping. Action: make a separate snapshot in a private folder; map provider service names/statuses exactly, convert storage to bytes, preserve capture/report dates and mark audit completeness only for an established collection. Reuse the schema in the supplied fixture; re-run the evaluator. Expected: reproducible findings and explicit gaps. Verification: manually reconcile one normal and one review finding to the original source; compare every required workload and every page. Recovery: unsupported fields/statuses need a documented mapping and test before interpreting them. This package does not contain or verify an adapter; live results must be labelled unestablished until independently checked.

### 14. Capture evidence and clean up

Start: local rerun complete, any optional access recorded. Action: retain only synthetic output, runtime version, exact command and source hash in a new evidence record. Delete scratch.json if no longer needed. For any separately run live session, sign out of Graph Explorer; have the tenant owner revoke the temporary consent/role and confirm it is absent; remove private exports according to the approved retention rule. Expected: reusable public evidence without tokens, private names or tenant exports. Verification: reread the file list before sharing. Recovery: preserve needed troubleshooting evidence privately; never delete business resources as lab cleanup.

## I. Break/fix exercises

Required local faults: service missing, stale capture, unknown status, zero/impossible activity denominator, invalid numeric data, duplicate service and incomplete audit window. Tests explicitly prevent a falsely clean result. Optional live faults: denied reporting permission, report delay and throttling. Diagnose the actual condition, restore approved access/input, and rerun; never make extra tenant changes to manufacture success.

## J. Acceptance and outcome rules

Observed on 30 September: 14 tests passed; one normal fixture produced NO_RULE_FINDINGS/0 and one review fixture produced REVIEW/1. No measured labour saving, uptime change, AI benefit or live platform connection. Acceptance for the local slice: deterministic findings, unchanged input, expected exits and no credential/network path. Acceptance for a future live adapter additionally requires complete/paginated collection, age/units/identifier handling, manual source reconciliation and a denied-access test. Three categories remain separate: guide authored; Codex-assisted synthetic slice tested; Bunamin independent/live evidence pending.

## K. Artefacts

The public folder holds README, this sanitised lab, source, fixtures, 14 tests, EVALUATION, DEMO SCRIPT, CONTRIBUTIONS, CHANGELOG, architecture/adapter/handover notes and synthetic evidence. No demo video or live screenshot has been produced; they are optional later evidence. Keep authentic live evidence private and publish only a checked derivative.

## L. Interview story

Problem: repeatable operational review. Constraint: no disclosed client or authorised live tenant. Design: readable rules and human ownership before AI. Build: Codex-assisted standard-library snapshot evaluator. Failure: missing/stale data could have looked healthy; tests require INCOMPLETE. Verification: two supplied scenarios and 14 tests. Business value: a proposed clearer handover, still unmeasured. Improvement: independently run it, then validate a permitted read-only adapter. Say who wrote the code and what you can personally explain.

## M. Conditional wording

Use only after Bunamin independently runs, explains and verifies the stated scope: “Built and tested a small Microsoft 365 review lab using synthetic service-health and usage data, with checks for missing information and a clear handover for human review.” Do not say enterprise monitoring deployed, availability improved, AI incidents solved or customer time saved. Current description: “Prepared a Codex-assisted synthetic demonstration; independent and live validation pending.”

## N. Optional AI extension and baseline decision

Planned only: pass a sanitised, already-reviewed incident note and source ID to an approved model; ask for a brief explanation using only that note, returning “insufficient information” for cause/impact not supplied. Run 10 held-out synthetic notes against a fixed rules/template baseline, including missing source, conflicting timestamps and prompt-like text. A human scores factual support, useful next check, leakage and unsupported cause; record latency/cost only when measured. Accept AI only if it improves explanation while making no unsupported claim and preserving the baseline fallback. Otherwise keep the deterministic handover. No AI account, API call or comparative result exists in this run.

## Official references

Checked 30 September 2026. These sources support technical orientation, not proof of a client implementation.

- Health API and permission: https://learn.microsoft.com/en-us/graph/api/serviceannouncement-list-healthoverviews?view=graph-rest-1.0 (page updated 23 July 2025).
- Site usage schema/permission/redirect: https://learn.microsoft.com/en-us/graph/api/reportroot-getsharepointsiteusagedetail?view=graph-rest-1.0.
- Service-health overview: https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health?view=o365-worldwide.
- Audit search and role/licence prerequisites: https://learn.microsoft.com/en-us/purview/audit-search.
- Public release announcements: https://www.microsoft.com/en-us/microsoft-365/roadmap.
