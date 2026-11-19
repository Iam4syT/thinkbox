# Lab 2 · Measure repeat use of an approved tool
## Purpose and design
A service owner wants to know how many invited people came back. Count unique eligible users with activity in a stated period. Repeat use means activity on at least two different days. This weekly measure can guide follow-up with a champion. It cannot tell you why someone returned or whether a task improved.
## Build and run · about 20 minutes
1. Open the project folder containing demo.py and sample.json. Use Python 3.9 or later, offline. Four fictional user IDs protect privacy. No installation, account or paid service is needed.
2. Read the roster, the inclusive start and end dates, and the five events. On paper, list the days each eligible user was active within the period. Count each user-day once. Keep people with no events in the denominator.
3. Run python3 demo.py sample.json. Expect eligible 4, active 2, repeat 1 and active_pct 50.0. A has two different days. B has one. C’s event falls outside the period. D has none. Repeated events on the same day do not increase the count.
4. Copy sample.json to trial.json. Add a second event for B on 2026-11-07. Run python3 demo.py trial.json. Expect active 2, repeat 2 and 50.0%. This distinguishes more frequent use from reaching more people.
5. Change the new event’s user to X. Run again. Expect an invalid-input message. Reconcile the roster before issuing the report. Restore B, replace the events list with [] and rerun. Expect zero active and zero repeat with four eligible.
6. Compare the results with the hand tally. Record the period, definition, input revision and counts. Delete the trial file. Share only aggregate results in a real dashboard and agree small-group reporting rules with the data owner first.
## Evaluate, demonstrate and extend
A spreadsheet tally is the baseline. The script makes the denominator and repeat rule reproducible. An AI summary could later draft commentary from approved aggregates. It adds no value to the count itself. User feedback or task timing would be needed to interpret adoption.
Demo the extra day for B and explain why reach stays at 50%. Ask a champion what prevented the unused workflow from fitting their day. Extension: test an eligible roster that changes mid-period. Describe this as hands-on practice only after reproducing it yourself.
