# Demo — why matching counts are insufficient

1. State the boundary: “This Codex-assisted local demonstration compares synthetic declarations; it does not access SharePoint or perform a migration.”
2. Open source.json and destination.json. Run the normal README command and show two matching declared files. Explain what MANIFESTS_MATCH does not establish.
3. Run the problematic pair. Show the missing file, changed hash/permissions/metadata, owner/capacity/geo gaps and broad link. Map findings to input rows.
4. Copy destination.json to scratch-destination.json and change a hash while leaving its file count unchanged. Rerun and show CONTENT_MISMATCH. Restore the fixture; run the tests.
5. Open the owner handover and planned identity-test lab. Explain why a real reader/editor/outsider matrix and computed source/destination hashes are still required. Delete only the scratch copy.

Lesson: acceptance needs explicit scope, evidence and ownership. No migration, live permission change or video was produced in this evaluation.
