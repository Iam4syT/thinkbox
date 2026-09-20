# Thinkbox portfolio assistant

Let a visitor find real project evidence without depending on an LLM conversation.

This is a portfolio learning project maintained by Bunamin Adams. Read [contribution and provenance](CONTRIBUTIONS.md), [the lab](LAB.md), [evaluation](EVALUATION.md) and [change record](CHANGELOG.md).

## What works and what it means

| Component | State | Evidence |
|---|---|---|
| React project/career pages and Flask catalogue backed by the same portfolio.json | Implemented at the scope described here | [Source](portfolio.json); [Verification record](EVALUATION.md) |
| Live/business outcome | Unestablished unless explicitly recorded | Optional chat needs provider access. The previous fictional employment/project examples have been removed from the portfolio routes; no template proficiency ratings are treated as facts. |

Adapted from Andrew Baisden’s ai-agent-app. Original attribution is retained in CONTRIBUTIONS.md. Static project evidence is the default route.

## Reproduce a small example

Commands below assume a new clone; if already inside thinkbox, navigate directly to the quoted project path. Python examples use Python 3.11. On Windows activate the environment using its Scripts/Activate.ps1 instead.

```sh
git clone https://github.com/Iam4syT/thinkbox.git
cd "thinkbox/AI Projects/ai-agent-app"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd backend
python -m unittest discover -s tests -v
# Optional backend server: python main.py
cd ../frontend
npm ci
npm run build
# Optional frontend server: npm run dev
```

Read [LAB.md](LAB.md) for expected results, troubleshooting and cleanup. Do not interpret an unrun live step as an integration test. Dependency downloads require internet access; offline fixtures do not need service credentials.

## Results, limits and next step

Optional chat needs provider access. The previous fictional employment/project examples have been removed from the portfolio routes; no template proficiency ratings are treated as facts. [Verification record](EVALUATION.md) describes method and observed results; a small synthetic evaluation is not proof of workplace impact. Source revision/environment are recorded in the repository verification report.

Use [DEMO SCRIPT.md](DEMO%20SCRIPT.md) for a short walkthrough. The next useful step is the smallest evaluation that could change a decision, using permitted data and a justified baseline.

## Layout and reuse

Keep the established source folders in place. Repository CI lives at root `.github/workflows`, with project working directories. Code licensing follows [the root licence](../../LICENSE) and any project-specific notice; third-party datasets, papers and adapted code retain their own terms.

## Last local verification

20 September 2026, macOS arm64. See the [verification report](../../docs/VERIFICATION.md) for the exact runtime, command, result and untested boundaries. The evidence is local or mocked at the stated scope.
