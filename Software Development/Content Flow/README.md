# Content Flow — writing workflow application

Organise drafts, adaptations and review steps while preserving publication truth.

This is a portfolio learning project maintained by Bunamin Adams. Read [contribution and provenance](CONTRIBUTIONS.md), [the lab](LAB.md), [evaluation](EVALUATION.md) and [change record](CHANGELOG.md).

## What works and what it means

| Component | State | Evidence |
|---|---|---|
| Node application, SQLite storage, provider adapters and a queue that stops at manual review | Implemented at the scope described here | [Source](content-flow/server/automation/PostScheduler.js); [Verification record](EVALUATION.md) |
| Live/business outcome | Unestablished unless explicitly recorded | No social-platform publishing adapter is implemented. Mock provider outputs are demonstrations. A queue state or simulated engagement score does not prove a published post or audience result. |

A due item becomes ready_for_review. A published state requires a verified receipt with URL and time; no live post is created by the demo.

## Reproduce a small example

Commands below assume a new clone; if already inside thinkbox, navigate directly to the quoted project path. Python examples use Python 3.11. On Windows activate the environment using its Scripts/Activate.ps1 instead.

```sh
git clone https://github.com/Iam4syT/thinkbox.git
cd "thinkbox/Software Development/Content Flow/content-flow"
# Node.js 24 LTS and npm
npm ci
npm test
npm run build
```

Read [LAB.md](LAB.md) for expected results, troubleshooting and cleanup. Do not interpret an unrun live step as an integration test. Dependency downloads require internet access; offline fixtures do not need service credentials.

## Results, limits and next step

No social-platform publishing adapter is implemented. Mock provider outputs are demonstrations. A queue state or simulated engagement score does not prove a published post or audience result. [Verification record](EVALUATION.md) describes method and observed results; a small synthetic evaluation is not proof of workplace impact. Source revision/environment are recorded in the repository verification report.

Use [DEMO SCRIPT.md](DEMO%20SCRIPT.md) for a short walkthrough. The next useful step is the smallest evaluation that could change a decision, using permitted data and a justified baseline.

## Layout and reuse

Keep the established source folders in place. Repository CI lives at root `.github/workflows`, with project working directories. Code licensing follows [the root licence](../../LICENSE) and any project-specific notice; third-party datasets, papers and adapted code retain their own terms.

## Last local verification

20 September 2026, macOS arm64. See the [verification report](../../docs/VERIFICATION.md) for the exact runtime, command, result and untested boundaries. The evidence is local or mocked at the stated scope.
