"""Explain a synthetic ticket route. Human review remains necessary."""
import argparse, csv, json
from pathlib import Path
REQUIRED=("id","kind","suspected_exposure","service_wide","urgent_event","minutes_open","target_minutes","user_retested")
def triage(row):
    def yes(key): return row.get(key,"").strip().lower()=="yes"
    try:
        elapsed=int(row.get("minutes_open","")); target=int(row.get("target_minutes",""))
        if elapsed<0 or target<=0: raise ValueError()
    except (TypeError,ValueError): return {"id":row.get("id"),"route":"REVIEW","reason":"Invalid time or target; do not guess"}
    if yes("suspected_exposure"): route,reason="SECURITY","Suspected data exposure; approved security process first"
    elif yes("service_wide"): route,reason="INCIDENT","Possible shared outage; check service health and incident lead"
    elif elapsed>=target: route,reason="ESCALATE","Target reached; specialist handoff needed"
    elif yes("urgent_event"): route,reason="URGENT REVIEW","Time-sensitive event; agree priority and fallback with owner"
    elif row.get("kind","").lower() not in ("document","meeting","vpn","print"): route,reason="REVIEW","Unknown category"
    else: route,reason="FIRST LINE","Use approved checks for this category"
    return {"id":row.get("id"),"route":route,"reason":reason,"closure":"CONFIRM" if yes("user_retested") else "KEEP OPEN"}
def main():
    parser=argparse.ArgumentParser();parser.add_argument("input",type=Path);args=parser.parse_args()
    with args.input.open(newline="",encoding="utf-8-sig") as stream:
        reader=csv.DictReader(stream)
        if not set(REQUIRED).issubset(reader.fieldnames or []): parser.error("Missing required column; no routing decision made")
        print(json.dumps([triage(row) for row in reader],indent=2))
if __name__=="__main__":main()
