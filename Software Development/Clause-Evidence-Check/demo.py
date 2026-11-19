"""Locate proposed source quotations in synthetic numbered clauses."""
import json
import sys
from pathlib import Path


def evaluate(data):
    clauses, proposals = data["clauses"], data["proposals"]
    if not isinstance(clauses, dict) or not clauses or not isinstance(proposals, list) or not proposals:
        raise ValueError("Supply clauses and at least one proposal.")
    if not all(isinstance(s, str) and s.strip() for s in clauses.values()):
        raise ValueError("Clause text must be non-empty.")
    results = []
    for proposal in proposals:
        clause, quote = proposal["clause"], proposal["quote"]
        if not isinstance(clause, str) or not isinstance(quote, str) or not quote.strip():
            raise ValueError("Supply a clause ID and non-empty quotation.")
        source = clauses.get(clause)
        if source is None:
            state = "missing clause"
        elif quote not in source:
            state = "no exact match"
        elif source.find(quote) != source.rfind(quote):
            state = "ambiguous match"
        else:
            state = "located for human review"
        results.append({"clause": clause, "status": state})
    return results


if __name__ == "__main__":
    try:
        result = evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except (IndexError, KeyError, OSError, TypeError, ValueError) as exc:
        sys.exit(f"Invalid input: {exc}")
    print(json.dumps(result, indent=2))
    sys.exit(0 if all(r["status"] == "located for human review" for r in result) else 2)
