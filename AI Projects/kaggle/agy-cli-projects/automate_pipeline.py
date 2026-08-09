import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import requests

# Feed URL for Google BigQuery Release Notes
FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
ATOM_NS = "http://www.w3.org/2005/Atom"

def fetch_and_parse_feed():
    """Fetches BigQuery release notes Atom feed and generates a structured summary."""
    print(" Fetching latest BigQuery Release Notes feed...")
    try:
        response = requests.get(FEED_URL, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch feed: {e}")
        return None

    try:
        root = ET.fromstring(response.text)
    except ET.ParseError as e:
        print(f"❌ XML Parsing Error: {e}")
        return None

    feed_title = root.findtext(f"{{{ATOM_NS}}}title", "BigQuery Release Notes")
    feed_updated = root.findtext(f"{{{ATOM_NS}}}updated", "")
    
    entries = []
    for entry in root.findall(f"{{{ATOM_NS}}}entry"):
        title = entry.findtext(f"{{{ATOM_NS}}}title", "")
        updated = entry.findtext(f"{{{ATOM_NS}}}updated", "")
        link_el = entry.find(f"{{{ATOM_NS}}}link[@rel='alternate']")
        link = link_el.get("href", "#") if link_el is not None else "#"
        
        entries.append({
            "title": title,
            "updated": updated,
            "link": link
        })
        
    return {
        "title": feed_title,
        "updated": feed_updated,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "entries": entries[:5] # Top 5 latest updates
    }

def generate_summary_file(data, output_file="latest_release_summary.txt"):
    """Saves structured release summary to a local text file."""
    if not data:
        return None

    content = []
    content.append("============================================================")
    content.append(f" {data['title'].upper()}")
    content.append("============================================================")
    content.append(f"Feed Last Updated: {data['updated']}")
    content.append(f"Digest Generated : {data['fetched_at']}\n")
    content.append("TOP LATEST UPDATES:")
    content.append("------------------------------------------------------------")

    for idx, entry in enumerate(data['entries'], 1):
        content.append(f"{idx}. {entry['title']} ({entry['updated'][:10]})")
        content.append(f"   Link: {entry['link']}\n")

    content.append("------------------------------------------------------------")
    content.append("Generated automatically by AGY CLI Automation Engine.")

    summary_text = "\n".join(content)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(f"✅ Summary report generated successfully: '{output_file}'")
    return output_file

def sync_to_google_drive(file_path):
    """Attempts to upload the summary report to Google Drive using upload_to_drive.py."""
    if not os.path.exists("upload_to_drive.py"):
        print("ℹ️ upload_to_drive.py not found. Skipping Google Drive upload.")
        return

    if not (os.path.exists("token.json") or os.path.exists("credentials.json")):
        print("ℹ️ Google Drive API credentials (token.json/credentials.json) not configured.")
        print("   Skipping automatic Drive upload. (Local summary saved).")
        return

    try:
        from upload_to_drive import authenticate_drive, upload_file
        print("\n Authenticaten with Google Drive API...")
        drive_service = authenticate_drive()
        file_id = upload_file(drive_service, file_path, f"BigQuery_Release_Summary_{datetime.now().strftime('%Y%m%d')}.txt")
        if file_id:
            print(f" Google Drive Sync Complete! File ID: {file_id}")
    except Exception as e:
        print(f"⚠️ Drive upload skipped or encountered error: {e}")

def run_pipeline():
    print("============================================================")
    print("STARTING: AGY CLI AUTOMATION PIPELINE")
    print("============================================================")
    
    data = fetch_and_parse_feed()
    if data:
        summary_file = generate_summary_file(data)
        sync_to_google_drive(summary_file)
        
    print("\n============================================================")
    print("SUCCESS: Automation pipeline execution complete.")
    print("============================================================")

if __name__ == "__main__":
    run_pipeline()
