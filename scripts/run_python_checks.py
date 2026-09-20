"""Run credential-free project checks in independent Python processes."""
from pathlib import Path
import os
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
CASES = [
 ("Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops", ["-m","unittest","discover","-s","tests","-v"]),
 ("Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops", ["evaluate.py"]),
 ("Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops", ["main.py"]),
 ("Modern Workplace Solutions/Enterprise-Ops-Telemetry-Engine", ["-m","unittest","discover","-s","tests","-v"]),
 ("Modern Workplace Solutions/Enterprise-Ops-Telemetry-Engine", ["main.py"]),
 ("AI Projects/Enterprise-AI-Prioritization-Engine", ["-m","unittest","discover","-s","tests","-v"]),
 ("AI Projects/SmartLifeCycle-Ops", ["app/models/train_model.py"]),
 ("AI Projects/SmartLifeCycle-Ops", ["app/scripts/validate_api.py"]),
 ("AI Projects/Agentic-Compliance-Auditor", ["-m","unittest","discover","-s","tests","-v"]),
 ("AI Projects/Business Opportuniity Scouting Agent", ["-m","unittest","discover","-s","tests","-v"]),
 ("AI Projects/ai-agent-app/backend", ["-m","unittest","discover","-s","tests","-v"]),
 ("AI Projects/MLOps/mlops-project", ["demo.py"]),
 ("AI Projects/kaggle/agy-cli-projects/bq-releases-notes", ["demo.py"]),
 ("Software Development/Smart Home Energy Manager", ["-m","unittest","discover","-s","tests","-v"]),
 ("Software Development/Smart Home Energy Manager", ["evaluate_solar.py"])
]

def main():
    env = dict(os.environ, MPLBACKEND="Agg")
    env.setdefault("MPLCONFIGDIR", "/tmp/thinkbox-matplotlib")
    for project, args in CASES:
        print(f"Checking {project}: {' '.join(args)}", flush=True)
        subprocess.run([sys.executable, *args], cwd=ROOT/project, env=env, check=True, timeout=120)
    print(f"PASS: {len(CASES)} isolated Python commands")

if __name__=="__main__":main()
