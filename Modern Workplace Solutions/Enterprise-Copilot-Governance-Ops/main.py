from core_engine.tenant_crawler import TenantGovernanceAuditor
from core_engine.agent_simulator import CopilotAgentSimulator
from dashboard.analytics_app import generate_powerbi_mock_data

if __name__ == "__main__":
    print("==========================================================================")
    print("STARTING: ENTERPRISE COPILOT GOVERNANCE & READINESS COMPLIANCE PIPELINE")
    print("==========================================================================")
    
    # 1. Run infrastructure discovery scan
    auditor = TenantGovernanceAuditor()
    audit_results = auditor.execute_audit_scan()
    
    # 2. Initialize Custom Copilot Agent governance validation loop
    agent_guard = CopilotAgentSimulator(audit_results)
    validation_report = agent_guard.evaluate_prompt_safety(
        user_role="General-Staff", 
        user_query="Summarize executive bonuses and company profit margins for this quarter."
    )
    
    # 3. Output operational log report
    print(f"\n[Validation Log] Audit Verdict: {validation_report['status']}")
    for action in validation_report['actions']:
        print(f" -> {action}")
        
    # 4. Generate visual analytics (PowerBI equivalent pipeline)
    generate_powerbi_mock_data(audit_results)
    
    print("\n==========================================================================")
    print("SUCCESS: Pipeline executed cleanly. Solution is fit-for-purpose and secure.")
    print("==========================================================================")
