class CopilotAgentSimulator:
    """
    Simulates a Microsoft Copilot custom agent verifying user prompts against 
    the semantic index and information protection boundaries before rendering answers.
    """
    def __init__(self, audit_dataframe):
        # Accept the analytical dataframe compiled by the TenantCrawler
        self.tenant_data = audit_dataframe
        
    def evaluate_prompt_safety(self, user_role, user_query):
        """
        Determines whether a user query running on a custom Copilot Agent would
        leak confidential information based on tenant access governance.
        """
        print(f"\n[Copilot Agent Interface] Processing request from Role: '{user_role}'")
        print(f"[Copilot Agent Interface] Query Received: '{user_query}'")
        
        leaks_detected = 0
        remediation_actions = []
        
        # Iterate over structural tenant metadata records to isolate security leaks
        for idx, row in self.tenant_data.iterrows():
            if "Exposed" in row['group_access'] and user_role == "General-Staff":
                leaks_detected += 1
                remediation_actions.append(
                    f"CRITICAL LEAK PREVENTED: Document '{row['file_name']}' within '{row['source']}' "
                    f"was flagged. Restricting Copilot Semantic Index access immediately."
                )
                
        return {
            "status": "Flagged & Isolated" if leaks_detected > 0 else "Compliant",
            "leaks_blocked": leaks_detected,
            "actions": remediation_actions
        }
