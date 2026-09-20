"""Local matplotlib chart of fixture decisions; no Power BI connection."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def generate_policy_chart(df, output=None):
    output = Path(output or Path(__file__).resolve().parents[1] / "evidence" / "policy-decisions.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    labels = ["allowed", "exposed", "review"]
    counts = [int((df["decision"] == label).sum()) if "decision" in df else 0 for label in labels]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(labels, counts, color=["#267d65", "#c23b3b", "#b7791f"])
    ax.set(title="Synthetic metadata policy decisions", ylabel="Fixture records")
    ax.set_yticks(range(max(counts, default=0) + 1))
    fig.text(.5, .01, "Simulation only — no tenant scan or permission changes", ha="center", fontsize=9)
    fig.tight_layout(rect=(0, .05, 1, 1))
    fig.savefig(output, dpi=150)
    plt.close(fig)
    return output
