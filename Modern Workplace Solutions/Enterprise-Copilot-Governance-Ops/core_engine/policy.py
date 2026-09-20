"""Small, explicit fixture policy. No tenant operations or semantic query evaluation."""
KNOWN_GROUPS = {"All-Employees", "Finance-Execs", "HR-Managers", "Research-Team", "Anonymous"}
KNOWN_CLASSES = {"Public", "Internal Only", "Confidential", "Highly Confidential"}

def assess_record(record):
    classification = record.get("classification")
    groups = record.get("access_groups")
    if groups is None and isinstance(record.get("group_access"), str):
        # Compatibility with the original fixture labels; annotations are not policy inputs.
        groups = [record["group_access"].split(" (")[0].strip()]
    if not isinstance(classification, str) or classification not in KNOWN_CLASSES or not isinstance(groups, list) or not groups:
        return {"decision": "review", "reason": "Missing or unsupported sensitivity/access metadata"}
    if any(not isinstance(g, str) or g not in KNOWN_GROUPS for g in groups):
        return {"decision": "review", "reason": "Unknown access group; membership needs verification"}
    if classification != "Public" and "Anonymous" in groups:
        return {"decision": "exposed", "reason": "Non-public data has anonymous access"}
    if classification in {"Confidential", "Highly Confidential"} and "All-Employees" in groups:
        return {"decision": "exposed", "reason": "Sensitive data has organisation-wide access"}
    return {"decision": "allowed", "reason": "No exposure under this limited metadata policy"}
