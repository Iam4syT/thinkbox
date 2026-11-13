import csv
import sys
from collections import Counter
from pathlib import Path


def reconcile(path):
    totals = Counter()
    ids = set()
    with Path(path).open(encoding="utf-8", newline="") as source:
        rows = csv.DictReader(source)
        if rows.fieldnames != ["id", "account", "pence"]:
            raise ValueError("expected id,account,pence")
        for row in rows:
            entry_id, account = row["id"], row["account"]
            if not entry_id or not account or entry_id in ids:
                raise ValueError("missing or duplicate entry")
            ids.add(entry_id)
            totals[account] += int(row["pence"])
    if not ids:
        raise ValueError("no entries")
    return {account: total for account, total in sorted(totals.items()) if total}


def main():
    try:
        imbalances = reconcile(sys.argv[1])
    except (IndexError, OSError, TypeError, ValueError) as exc:
        print(f"Invalid ledger: {exc}", file=sys.stderr)
        return 2
    if imbalances:
        print("Unbalanced:", imbalances)
        return 1
    print("Balanced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
