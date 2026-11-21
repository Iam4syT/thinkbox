# Route a workplace prototype
## Purpose and boundary
A service owner needs a recorded decision each time someone proposes an automation. A spreadsheet is an adequate baseline. A repeatable rule makes missing evidence visible before the idea reaches a developer. Triage the idea. The person who owns the process still decides whether to accept it. This is an offline exercise using invented examples. Budget 20 minutes, Python 3, a text editor and a local folder. It needs no account, licence, network access or API credit.
## From a clean folder to a decision
1. Open a terminal in the project folder. Type python3 --version. Expect Python 3. If the command is missing on Windows, try py -3 and use that prefix below.
2. Open templates/sample.json. Read the two records. Each has a unique ID. Predict a route for each on paper and name the field that changes your decision. This is the manual baseline.
3. Run python3 scripts/review.py templates/sample.json. Expect P1: HANDOVER REVIEW and P2: GOVERNANCE REVIEW. Compare both lines with your predictions. If the file cannot be found, check that the terminal folder contains scripts and templates.
4. Save a copy of templates/sample.json as trial.json in the project folder. Change P1 tested from true to false. Run python3 scripts/review.py trial.json. Expect P1: IMPROVE. Read the changed row aloud to explain why the result moved.
5. Try the boundary case. Set needed to false with approved data and complete fields to route a redundant idea to RETIRE REVIEW. Restore the original values by copying the sample again. Reuse the same ID on both rows. Run the command. Expect an invalid-input message and no decision list. Restore unique IDs and rerun.
## Handover and acceptance
Show purpose, intended users, logic, data class, benefit, named owner, support route and test evidence. Ask the process owner to sign off the recommendation before any live move. Keep the input, the output and the reason for any human override together. Compare the two original decisions, the changed case, the duplicate and a wrongly typed flag with evidence/results.txt. Fix a wrong file path or JSON value and run again before accepting.
## What to practise next
A language model could draft a short explanation from approved information. The rule-based version is the baseline because the decision must be reproducible. No AI call, tenant write or business saving was measured. With an approved practice tenant, map the fields to a Microsoft List, restrict who can edit reviews and test access with two test identities. That extension has not been run. Remove trial.json when finished. Keep the original fixture for the next learner.
## Evidence and interview use
Describe the decision, the input you changed, the observed result and the effect of a missing check. Only after a personal rerun, use wording such as “I tested a synthetic review workflow and documented its failure cases.” Keep the results local until any real data and access rules are approved.
