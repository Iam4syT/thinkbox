import pandas as pd

class TenantGovernanceAuditor:
    """
    Simulates an automated auditor for Microsoft 365 Tenant architecture,
    scanning SharePoint site paths, identifying data security tags, and mapping RBAC configurations.
    """
    def __init__(self):
        # Simulated enterprise file repository metadata representing M365 enclaves
        self.mock_metadata = [
            {"item_id": 101, "source": "SharePoint/Finance", "file_name": "Q2_Profit_Ledger.xlsx", "classification": "Highly Confidential", "group_access": "Finance-Execs"},
            {"item_id": 102, "source": "SharePoint/HR", "file_name": "Executive_Comp_2026.docx", "classification": "Highly Confidential", "group_access": "HR-Managers"},
            {"item_id": 103, "source": "SharePoint/R&D", "file_name": "Copilot_Agent_Blueprint.md", "classification": "Internal Only", "group_access": "All-Employees"},
            {"item_id": 104, "source": "SharePoint/Public", "file_name": "Product_Catalog.pdf", "classification": "Public", "group_access": "All-Employees"},
            {"item_id": 105, "source": "SharePoint/Operations", "file_name": "Standard_SLA_Template.docx", "classification": "Internal Only", "group_access": "All-Employees"}
        ]
        
    def execute_audit_scan(self):
        """
        Processes raw tenant configurations and applies logic to flag over-sharing security risks.
        """
        # Convert raw JSON-style metadata into a high-performance Dataframe
        df = pd.DataFrame(self.mock_metadata)
        
        # Calculate a risk score based on sensitivity matching
        df['ATS_Risk_Score'] = df.apply(
            lambda row: 95 if row['classification'] == 'Highly Confidential' and 'All-Employees' in row['group_access'] else 10, 
            axis=1
        )
        
        # Injection Scenario: Artificially inject an active permission leak 
        # Simulating an executive file that inherited loose "All-Employees" access permissions
        df.loc[1, 'group_access'] = "All-Employees (Exposed Risk)"
        df.loc[1, 'ATS_Risk_Score'] = 98
        
        return df
