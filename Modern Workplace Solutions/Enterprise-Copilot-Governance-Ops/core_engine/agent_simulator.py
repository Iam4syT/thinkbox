"""Metadata policy demonstration, not a Copilot enforcement layer."""
from .policy import assess_record

class CopilotAgentSimulator:
    def __init__(self, audit_dataframe):
        self.tenant_data = audit_dataframe

    def evaluate_prompt_safety(self, user_role, user_query):
        results = []
        for row in self.tenant_data.to_dict(orient="records"):
            results.append({"item_id": row.get("item_id"), "file_name": row.get("file_name"), **assess_record(row)})
        exposed = sum(r["decision"] == "exposed" for r in results)
        review = sum(r["decision"] == "review" for r in results)
        if not results:
            status = "Manual review required: no metadata supplied"
        elif exposed:
            status = "Exposure identified"
        elif review:
            status = "Manual review required"
        else:
            status = "No exposure in checked metadata"
        return {"mode": "simulation", "status": status, "exposures_identified": exposed,
                "manual_review_count": review, "records": results,
                "proposed_actions": [f"Review access for {r['file_name']}" for r in results if r['decision'] != 'allowed'],
                "performed_actions": [], "query_evaluated": False,
                "limitations": "User role/query are context only. No live membership resolution, semantic evaluation or tenant mutation."}
