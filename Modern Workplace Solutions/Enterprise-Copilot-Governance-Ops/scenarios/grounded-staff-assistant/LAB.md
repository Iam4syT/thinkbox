# Permission-aware staff knowledge assistant

## A. Outcome and status
Find an answer in a tiny approved knowledge set, include its source, and return no answer when the user lacks access or evidence is missing. The built component is an offline extractive baseline. It does not call a language model, Microsoft Graph, SharePoint or Copilot Studio. Tenant integration and AI answer evaluation remain unrun.

## B. Research and employer context
DWP's January 2026 Copilot evaluation reports frequent information-search use and a need for targeted guidance. Its August 2026 hackathon article describes onboarding prototypes, with implementation still a next step at publication. These are public facts; the particular mentor-helpdesk workflow here is an independent teaching scenario, not a DWP requirement or commissioned system.

## C. Role requirements exercised
Practise E3 access boundaries and E4 grounding, plus R1 testing and R2 context handling. The optional tenant route addresses E1 Microsoft 365 integration and E5 agent delivery. Completing only local mode does not satisfy those tenant delivery requirements.

## D. Candidate gap
Professional support and Graph queries provide useful starting knowledge. The missing proof is a complete grounded-agent build with real user authentication, permission checks and evaluation. This project creates a small bridge; it does not upgrade professional capability by itself.

## E. Recurring use and baseline
An employee or service-desk colleague needs approved instructions whenever a new starter asks for help. Compare manual keyword search and an extractive response with an AI answer for the same questions. Use AI only if it improves answer completeness or understanding without weaker evidence or access protection. Do not assume that a more fluent answer is more correct.

## F. Architecture
Local flow: simulated role and question → filter approved notes by explicit allowed role → rank visible text → return text plus citation or unknown. Permission filtering occurs before answer construction. The caller supplies the role, so this is a policy simulation, not authentication or a secure web service. Only a real identity provider can establish the caller in a hosted system.
Tenant target: signed-in test employee → Copilot Studio → SharePoint knowledge with the end user's access → response and citation. Use the SharePoint knowledge-source route described in Microsoft's documentation; uploading a copy to a different store can change the access boundary. Never rely on instructions in a prompt to enforce permissions.

## G. Prerequisites, budget and boundaries
Local mode needs Python 3.11 or later and a terminal. It uses only the standard library, costs £0 in API usage and requires no credentials. A code editor is helpful. Allow 60–90 minutes for local practice and one to three weekends for the optional tenant work, as a planning estimate rather than measured completion time.
The Microsoft extension needs your own isolated test tenant, test accounts, a maker environment, suitable Microsoft 365/Power Platform entitlements and an administrator-approved licensing check. Trials have limits and may need billing details. Check your tenant's displayed price and capacity before enabling anything paid. This guide does not authorise purchases, tenant changes or access grants. If access is unavailable, stop at the local boundary and record the tenant steps as unrun.
Use fabricated staff information only. Do not use claimant, customer, pupil, health or production records. No benefit entitlement or other decision about a person is made by either project.

## K. Evidence to retain
Keep README, LAB, code, test output, a simple architecture note, one normal run and one failure run. Add a short screen recording when personally reproduced. Record the source version, Python version, date, exact command, result and who performed it. Keep tokens and real account identifiers out of screenshots, logs and commits.

## L. Interview explanation
Explain the recurring user problem, the boundary you chose and why. Show the baseline, one design decision, a failure you diagnosed, the test that proved the local fix and what remains untested. Distinguish your own changes from an assisted implementation. Explain that synthetic test results do not establish real user impact or production readiness.

## H. Granular build and practice
1. Start with this scenario folder open in your terminal. Run `python3 --version`. Expect 3.11 or later. If Python is missing, install it from the official Python distribution before continuing. On Windows, use `py -3` in place of `python3` where required.
2. Run `python3 -m unittest discover -s tests -v`. Expect 10 tests to pass. If an import fails, run from the directory containing main.py, not the parent governance project. Keep the real output in your own evidence log.
3. Open main.py. Read the three Note records. Identify the common onboarding record, the restricted payroll record and the unreviewed record. Explain why the last two should not appear to an ordinary staff user.
4. Run `python3 main.py --role staff --question mentor`. Expect status answer, citation onboarding and the mentor instruction. Check that the output uses the stored sentence rather than an invented answer.
5. Run `python3 main.py --role staff --question payroll`. Expect unknown, with no restricted title or content in the result. If payroll appears, stop and inspect the visibility filter before adding any generative model.
6. Run `python3 main.py --role hr --question payroll`. Expect an answer citing restricted-pay. This positive/negative pair tests the local rule. It does not validate an Entra identity or SharePoint permission.
7. Run `python3 main.py --role guest --question mentor`, then ask about asteroid as staff. Expect refuse for an unknown role and unknown for the unsupported topic. Verify that neither result fabricates an instruction.
8. Copy main.py to a temporary practice file before changing it. Change the allowed roles on the onboarding note to an empty set. Re-run the mentor test; expect unknown. Restore the file and rerun all tests. This demonstrates access revocation in the local rule model.
9. Add a fourth synthetic note and one test for it. Write down your own reason for its visibility and review state. Show one test failing before the fix and passing after it. This is the personal evidence step; do not claim it happened until you perform it.
10. Create docs/personal-run.md with your commands, one observed failure, the correction and limitations. Do not copy the existing evaluation as if you personally executed it.

### Optional tenant extension — not run
11. Confirm an isolated tenant, licences and two test users. Check that the agent maker's licence is not being mistaken for every end user's entitlement. Record actual displayed licence/capacity terms; if unavailable, keep this section planned.
12. In the test SharePoint site, create an ordinary library and a separate restricted library. Add two short, fabricated help articles. Remove broad inheritance from the restricted area only in your own lab and grant the second user the intended access. First prove each user can/cannot open each article directly in SharePoint. An agent cannot repair incorrect source permissions.
13. At copilotstudio.microsoft.com, choose the test environment and create a small agent. Under Settings → Security → Authentication, use the Microsoft authentication option appropriate to your test channel. If the current interface differs, follow the linked Microsoft page and record the actual setting; do not select unauthenticated access to make a failing test work.
14. In Knowledge → Add knowledge → SharePoint, enter the specific test site/library URL. Use the full SharePoint knowledge route, not the file-upload route. Confirm the knowledge status is ready. If no results appear, check source access, supported content, indexing and authentication; allow for indexing rather than widening permissions.
15. Add a short instruction: answer from approved knowledge, give a source, and say when there is not enough evidence. Treat this as answer guidance, not a security control. Keep web search and unrelated knowledge out of this bounded comparison.
16. Use the maker test panel for an initial check, then publish only to your authorised private test channel. Have both test users ask the same permitted, restricted and unsupported questions. Record the signed-in identity, direct source access, answer and citation separately. Maker-only success is insufficient.
17. Use a fixed set of 12 questions: four permitted, four restricted and four unsupported. Run the manual/extractive baseline and agent on the same set. Score answer correctness, citation support, inappropriate disclosure and honest unknowns. The release target is zero disclosures and every cited claim supported. Record latency/cost only if actually measured. Do not tune on every test question and then call the same set independent evaluation.
18. Stop on any leakage. Disable the test channel, fix source permissions/authentication, start a fresh conversation and rerun the full set. Preserve the failure record. Obtain peer review before adding a larger corpus or real data.

## I. Break and fix
Test a role with no visible notes, remove an allowed role, add an unreviewed note and ask an unsupported question. Expected local outcomes are refuse or unknown rather than a guessed answer. In tenant mode, test revoked source access and a stale URL with a fresh session. Diagnose source access separately from indexing and answer quality.

## J. Acceptance and cleanup
Local acceptance: all 10 tests pass; staff payroll produces neither private content nor citation; an allowed question has the exact stored source. This small fixed test set is not a penetration test or language-model evaluation.
Tenant acceptance is separate: both identities tested, no restricted-source disclosure, supported citations, unknowns handled and 12-case evidence saved. No tenant acceptance is claimed here.
Local cleanup: remove only your temporary practice file and personal outputs after retaining permitted evidence. No resource is created in Microsoft services by local mode. Tenant cleanup: unpublish the private test agent, remove test content/accounts and dispose of the test environment only after confirming it contains no unrelated work; check billing separately.

## M. Conditional portfolio wording
Use only after personally rebuilding and recording results: “Extended a synthetic knowledge-assistant lab with a permission-filtered retrieval baseline and tested allowed, denied and unsupported requests.” Add Copilot Studio/SharePoint integration only if actually built and validated. Do not claim DWP use.

## N. Next version and sources
Add a separately tested model-adapter layer with permitted context only; evaluate citation faithfulness against extraction before choosing AI. Add real identity only with appropriate isolation and review.
Microsoft technical source checked 7 November 2026: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-sharepoint
DWP research: https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial
