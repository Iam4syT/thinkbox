"""Run the credential-free governance fixture and save its actual result."""
import json
from pathlib import Path
from core_engine.tenant_crawler import TenantGovernanceAuditor
from core_engine.agent_simulator import CopilotAgentSimulator
from dashboard.analytics_app import generate_policy_chart

def main():
    data = TenantGovernanceAuditor().execute_audit_scan()
    report = CopilotAgentSimulator(data).evaluate_prompt_safety("General-Staff", "Example request")
    target = Path(__file__).resolve().parent / "evidence"
    target.mkdir(exist_ok=True)
    (target / "simulation-result.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("Local chart:", generate_policy_chart(data))

if __name__ == "__main__":
    main()
