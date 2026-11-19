"""Summarise unique users and repeat use in one reporting period."""
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


def summarise(data):
    roster, events = data["eligible"], data["events"]
    if not isinstance(roster, list) or not roster or not all(isinstance(x, str) and x.strip() for x in roster):
        raise ValueError("Supply a non-empty roster of eligible user IDs.")
    if len(set(roster)) != len(roster) or not isinstance(events, list):
        raise ValueError("Use unique roster IDs and a list of events.")
    start, end = map(date.fromisoformat, (data["start"], data["end"]))
    if end < start:
        raise ValueError("End date precedes start.")
    days = defaultdict(set)
    for event in events:
        user, day = event["user"], date.fromisoformat(event["day"])
        if user not in roster:
            raise ValueError("Unknown user in event file.")
        if start <= day <= end:
            days[user].add(day)
    repeat = sum(len(used) >= 2 for used in days.values())
    return {"eligible": len(roster), "active": len(days), "repeat": repeat,
            "active_pct": round(100 * len(days) / len(roster), 1)}


if __name__ == "__main__":
    try:
        report = summarise(json.loads(Path(sys.argv[1]).read_text()))
    except (IndexError, KeyError, OSError, TypeError, ValueError) as exc:
        sys.exit(f"Invalid input: {exc}")
    print(json.dumps(report, indent=2))
