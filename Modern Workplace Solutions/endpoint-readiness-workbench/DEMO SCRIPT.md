# Three-minute demonstration

1. Explain the recurring operator task and synthetic scope. State assistant provenance and unrun tenant boundaries.
2. Open `templates/readiness.json`. Point to LAB-05 stale evidence and LAB-04 separate application/connectivity faults.
3. Run `python3 scripts/readiness.py --output outputs/result.json`. Open the output and show the human next action. No mutation or message sending occurs.
4. Copy the fixture; change a sync timestamp to older than the fixed clock threshold. Rerun and show that readiness remains unknown.
5. Run `python3 -m unittest discover -s tests -v`; explain one meaningful failure boundary rather than reciting the count.
6. State the lesson: an observation is evidence for a test, not automatic proof of root cause. Explain the next tenant test and its licence/approval dependencies.

No video recorded. A future recording should show actual run output and exclude private identifiers. Do not narrate unrun steps as completed experience.
