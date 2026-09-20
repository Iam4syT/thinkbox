"""Synthetic metadata source; this does not crawl a Microsoft tenant."""
import pandas as pd
from .policy import assess_record

class TenantGovernanceAuditor:
    def __init__(self):
        self.mock_metadata = [
            {"item_id": 101, "source": "Synthetic/Finance", "file_name": "ledger.xlsx", "classification": "Highly Confidential", "access_groups": ["Finance-Execs"]},
            {"item_id": 102, "source": "Synthetic/HR", "file_name": "compensation.docx", "classification": "Highly Confidential", "access_groups": ["All-Employees"]},
            {"item_id": 103, "source": "Synthetic/Research", "file_name": "design.md", "classification": "Internal Only", "access_groups": ["All-Employees"]},
            {"item_id": 104, "source": "Synthetic/Public", "file_name": "catalogue.pdf", "classification": "Public", "access_groups": ["Anonymous"]},
            {"item_id": 105, "source": "Synthetic/Operations", "file_name": "handover.docx", "classification": "Internal Only", "access_groups": ["All-Employees"]}
        ]

    def execute_audit_scan(self):
        rows = []
        for row in self.mock_metadata:
            result = assess_record(row)
            rows.append({**row, **result})
        return pd.DataFrame(rows)
