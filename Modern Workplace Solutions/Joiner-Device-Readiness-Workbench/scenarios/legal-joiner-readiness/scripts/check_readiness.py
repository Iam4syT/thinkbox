"""Check a synthetic joiner record. Never connect to or change a tenant."""
import argparse, csv, json
from pathlib import Path
REQUIRED = ("approved", "account", "license", "mfa", "device_enrolled", "compliant", "app_test", "asset_record", "handover")
def assess(row):
    missing = [key for key in REQUIRED if row.get(key, "").strip().lower() != "yes"]
    return {"id": row.get("id", "unknown"), "status": "HOLD" if missing else "READY", "missing": missing}
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path); args = parser.parse_args()
    with args.input.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not {"id", *REQUIRED}.issubset(reader.fieldnames or []):
            parser.error("Missing required column; no readiness decision made")
        print(json.dumps([assess(row) for row in reader], indent=2))
if __name__ == "__main__": main()
