# Lab 2 • Can the restored file be trusted?
A recovery report can say a copy finished even when the bytes differ. After each restore drill, compare the recovered bytes with a trusted digest recorded before the incident. A fixed cryptographic check gives a repeatable answer without AI.
### Set up
Allow 15 minutes. Open a terminal in the exercise folder containing check.py and test_check.py. Run python3 --version. Use Python 3.8 or newer. The standard library is sufficient. No accounts, licence fees or network calls are required.
### Run and investigate
1. Open test_check.py. Identify the known-good bytes and their SHA-256 digest (a fingerprint of the contents). The original reference must come from a trusted copy made before recovery.
2. Run python3 -B -c "from test_check import RestoreTests as T; from check import verify_restore as v; print(v(T.reference,b'site inventory'),v(T.reference,b'site Inventory'))". Expect verified then mismatch. Only one letter changed.
3. Break/fix: in a disposable copy change the restored bytes in test_good from inventory to Inventory. The good-restore test should now fail. Keep the original reference, restore the known-good bytes and run all tests again.
### Check, explain and extend
Run python3 -B -m unittest -v test_check. Compare every named test with its expected decision. Save the console output with the date. If an import fails, check that both files are in the current folder. Work on a copy for experiments. Restore the supplied files and rerun the tests after changing a rule. No external resources need cleanup.
Five checks passed locally. This tests file contents in memory. Recovery time, application consistency, backup retention and a live disaster recovery exercise remain untested.
After personal replication, explain why rehashing the damaged copy as the reference would defeat the test. Conditional portfolio line: “Verified synthetic restored data against a known-good SHA-256 digest.” Extend the exercise to a temporary folder with a separate manifest.
