# Lab 1 · Check a proposed quotation against a source
## Purpose and design
A reviewer needs to find the wording behind a draft before using it. On each new draft, identify the clause and check that the quotation occurs once. A successful match locates words for review. It does not establish their legal meaning, completeness or relevance.
## Build and run · about 20 minutes
1. Open the project folder containing demo.py and sample.json. Use Python 3.9 or later. The exercise runs offline with no account, credentials or charge. Use only the fictional clauses supplied.
2. Read C1 and C2 in sample.json. Before running the tool, classify each proposed quotation by hand. Write down the clause ID, the exact words and whether there is one match.
3. Run python3 demo.py sample.json from this folder. The input contains two clauses and four proposals. The script checks the cited clause, looks for the exact words and checks whether they occur more than once.
4. Read the four results in input order. Expect located for human review, ambiguous match, missing clause and no exact match. The mixed file should return exit code 2. The discrepancy stays with a reviewer.
5. Copy sample.json to trial.json. Retain the first proposal only. Run python3 demo.py trial.json. Expect one located result and exit code 0. Change Monday to Friday in its quotation. Rerun and expect no exact match and exit code 2.
6. Empty the quotation and run again. Expect an invalid-input message. Restore it and rerun. If a genuine quotation fails, inspect punctuation, case and spacing. Correct the proposal only after checking the source. Keep original wording.
## Evaluate, demonstrate and extend
Compare the four outputs with your hand labels. Record any disagreement and the input revision. A generative model could suggest quotations later. This baseline catches invented wording without sending any text to a model. It cannot catch a quotation that is accurate but misleading out of context.
Show a colleague the clean match and one failed proposal. Ask them to explain why a reviewer still reads the surrounding clause. Record their feedback separately. Delete trial.json afterwards. No remote resources need cleanup.
Interview prompt: How would you handle two versions of the same contract? Extension: add a source version or hash and test a stale draft. After running it yourself, describe the exact check and observed failure in a portfolio note.
