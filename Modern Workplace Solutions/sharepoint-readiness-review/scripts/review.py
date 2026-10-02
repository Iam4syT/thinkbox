"""Synthetic SharePoint inventory and migration-manifest review, without network I/O."""
import argparse
import hashlib
import json
import math
import re
from pathlib import Path, PurePosixPath


def manifest(value):
    if value.get("schema_version") != 1:
        raise ValueError("unsupported schema_version")
    site = value["site"]
    for field in ("name", "owner", "geo", "geo_verified", "allocated_bytes", "used_bytes"):
        if field not in site:
            raise ValueError(f"missing site {field}")
    if type(site["geo_verified"]) is not bool:
        raise ValueError("geo_verified must be boolean")
    for field in ("allocated_bytes", "used_bytes"):
        n = site[field]
        if type(n) not in (int, float) or not math.isfinite(n) or n < 0:
            raise ValueError(f"invalid {field}")
    files = value["files"]
    if not isinstance(files, list):
        raise ValueError("files must be a list")
    paths = set()
    for f in files:
        path = f["path"]
        if not path or "\\" in path or PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
            raise ValueError("path must be a safe relative inventory key")
        if path in paths:
            raise ValueError("duplicate inventory path")
        paths.add(path)
        if type(f["size_bytes"]) is not int or f["size_bytes"] < 0:
            raise ValueError("invalid size_bytes")
        if not re.fullmatch(r"[0-9a-f]{64}", f["sha256"]):
            raise ValueError("missing or malformed sha256; no content integrity conclusion")
        if type(f["unique_permissions"]) is not bool:
            raise ValueError("unique_permissions must be boolean")
        if not isinstance(f["principals"], list) or not f["principals"] or any(not isinstance(p, str) or not p for p in f["principals"]):
            raise ValueError("principals need a non-empty explicit list")
        if not isinstance(f["metadata"], dict):
            raise ValueError("metadata must be an explicit dictionary")
    return value


def evaluate(source, destination):
    source, destination = manifest(source), manifest(destination)
    findings = []

    def add(code, subject, detail):
        findings.append({"code": code, "subject": subject, "detail": detail})

    for label, m in (("source", source), ("destination", destination)):
        site = m["site"]
        if not site["owner"]:
            add("MISSING_OWNER", label, "Obtain owner sign-off before moving or changing content.")
        if not site["geo"] or not site["geo_verified"]:
            add("GEO_UNVERIFIED", label, "Declared geography is not evidence of Multi-Geo or residency compliance.")
        if site["allocated_bytes"] <= 0:
            add("CAPACITY_UNKNOWN", label, "Confirm the storage model and available capacity.")
        elif site["used_bytes"] / site["allocated_bytes"] >= 0.9:
            add("CAPACITY_REVIEW", label, "Declared usage is at least 90% of allocation.")
        if not m["files"]:
            add("EMPTY_INVENTORY", label, "Empty export does not prove there is no content.")
        for f in m["files"]:
            if "Anyone" in f["principals"]:
                add("PUBLIC_LINK_REVIEW", f"{label}:{f['path']}", "Confirm whether the broad link is intended; do not change it automatically.")
            if f["unique_permissions"]:
                add("UNIQUE_PERMISSION_REVIEW", f"{label}:{f['path']}", "Document broken inheritance and the intended access boundary.")
    source_by_path = {f["path"]: f for f in source["files"]}
    destination_by_path = {f["path"]: f for f in destination["files"]}
    if source["site"]["geo"] != destination["site"]["geo"]:
        add("GEO_DIFFERENCE", "site", "Approve the intended location separately; this program does not validate data residency.")
    for p in sorted(source_by_path.keys() - destination_by_path.keys()):
        add("MISSING_CONTENT", p, "Destination is missing a declared source item.")
    for p in sorted(destination_by_path.keys() - source_by_path.keys()):
        add("UNEXPECTED_CONTENT", p, "Reconcile this destination-only item with the approved scope.")
    for p in sorted(source_by_path.keys() & destination_by_path.keys()):
        before, after = source_by_path[p], destination_by_path[p]
        if before["size_bytes"] != after["size_bytes"] or before["sha256"] != after["sha256"]:
            add("CONTENT_MISMATCH", p, "Size/hash differs; investigate before accepting the copy.")
        if set(before["principals"]) != set(after["principals"]) or before["unique_permissions"] != after["unique_permissions"]:
            add("PERMISSION_DIFFERENCE", p, "Review intended group mapping and inheritance before acceptance.")
        if before["metadata"] != after["metadata"]:
            add("METADATA_DIFFERENCE", p, "Declared metadata differs; investigate with the content owner.")
    findings.sort(key=lambda x: (x["code"], x["subject"]))
    return {"scope": "synthetic-manifest-only", "state": "REVIEW_REQUIRED" if findings else "MANIFESTS_MATCH",
            "source_count": len(source_by_path), "destination_count": len(destination_by_path),
            "findings": findings, "interpretation": "Matching declarations do not prove a successful migration, effective access, version history, list fidelity or residency compliance."}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("destination", type=Path)
    a = p.parse_args()
    try:
        report = evaluate(json.loads(a.source.read_text()), json.loads(a.destination.read_text()))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({"state": "INCOMPLETE", "error": str(error)}, indent=2))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
