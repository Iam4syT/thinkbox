# SharePoint readiness review

An independent learning demo for owner-led content/access review before accepting a change. Status: evaluated synthetic local slice. SharePoint access, migration tools, Multi-Geo, personal independent operation and workplace outcomes remain unestablished.

## The recurring problem

A completion screen or matching file count can hide missing content, changed permissions or lost metadata. This small checker compares two declared manifests and keeps owner, capacity and geography questions visible. The scenario is generic; no customer defect, commissioned work or actual migration is claimed.

## Contribution and current scope

Bunamin authorised the learning brief. Codex wrote and ran the standard-library Python demonstration, fixtures, behaviour tests and docs. Read [CONTRIBUTIONS.md](CONTRIBUTIONS.md) before interpreting these results as independent personal mastery.

| Component | State | Evidence |
|---|---|---|
| Read-only comparison of file/hash/permission/metadata declarations | Implemented and tested | [Source](scripts/review.py), [tests](tests/test_review.py) |
| Site ownership, capacity and geo review conditions | Simulated declarations | [Source fixture](templates/source.json), [evaluation](EVALUATION.md) |
| Effective access, site/list/library operation and pilot copy | Planned, unrun | [Granular lab](LAB.md) |
| ShareGate/BitTitan and Multi-Geo | Documentation orientation, unrun | [Lab](LAB.md), [limits](docs/adapter.md) |

## Run a small example

Python 3.11 or newer; no package installation, tenant account or API key. From a thinkbox clone:

```sh
cd "Modern Workplace Solutions/sharepoint-readiness-review"
python3 -m unittest discover -s tests -v
python3 scripts/review.py templates/source.json templates/destination.json
python3 scripts/review.py templates/source-review.json templates/destination-review.json
```

Windows may replace python3 with py -3. Matching manifests return MANIFESTS_MATCH/0. The intentionally problematic pair returns REVIEW_REQUIRED/1 with nine findings. Malformed or unsafe input returns INCOMPLETE/2. This only compares declarations; it cannot establish a successful migration, effective access, version/list fidelity or data-residency compliance.

## Design and observed results

The baseline is a manual owner/access and before/after content checklist. Deterministic comparisons are sufficient; AI is not needed to approve access or content. On 30 September 2026, 16 behaviour tests passed and two synthetic CLI scenarios returned expected states. This is not a sampled customer dataset or business-impact experiment. Read [EVALUATION.md](EVALUATION.md), [architecture](docs/architecture.md) and [DEMO SCRIPT.md](DEMO%20SCRIPT.md).

## Learn, reuse and clean up

[LAB.md](LAB.md) explains each action, output, verification, recovery and cleanup. Tenant and vendor-tool actions remain unrun and require applicable permission, licences and an isolated tenant. Actual group membership, history, lists, metadata, labels and residency require independent tests. Keep real exports, identities and credentials private. The implemented program has no network or tenant-mutation path; delete only your scratch copies after a local demo.

Original code follows the [MIT licence](LICENSE); vendor documents retain their own terms. See [CHANGELOG.md](CHANGELOG.md) for actual scope.
