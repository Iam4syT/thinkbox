import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
ATOM_NS = "http://www.w3.org/2005/Atom"


def strip_html(html: str) -> str:
    """Very lightweight HTML-to-plain-text stripper for tweet text."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_feed(xml_text: str) -> dict:
    root = ET.fromstring(xml_text)
    feed_title = root.findtext(f"{{{ATOM_NS}}}title", "BigQuery Release Notes")
    feed_updated = root.findtext(f"{{{ATOM_NS}}}updated", "")

    entries = []
    for entry in root.findall(f"{{{ATOM_NS}}}entry"):
        title = entry.findtext(f"{{{ATOM_NS}}}title", "")
        updated = entry.findtext(f"{{{ATOM_NS}}}updated", "")
        link_el = entry.find(f"{{{ATOM_NS}}}link[@rel='alternate']")
        link = link_el.get("href", "#") if link_el is not None else "#"
        content_el = entry.find(f"{{{ATOM_NS}}}content")
        content_html = content_el.text if content_el is not None else ""

        # Extract category tags (h3 headings inside the HTML content)
        categories = re.findall(r"<h3>(.*?)</h3>", content_html or "", re.IGNORECASE)
        plain_text = strip_html(content_html or "")

        entries.append(
            {
                "title": title,
                "updated": updated,
                "link": link,
                "content_html": content_html,
                "plain_text": plain_text,
                "categories": list(dict.fromkeys(categories)),  # deduplicated, ordered
            }
        )

    return {
        "feed_title": feed_title,
        "feed_updated": feed_updated,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "entries": entries,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/releases")
def releases():
    try:
        resp = requests.get(FEED_URL, timeout=15)
        resp.raise_for_status()
        data = parse_feed(resp.text)
        return jsonify({"ok": True, "data": data})
    except requests.RequestException as exc:
        return jsonify({"ok": False, "error": str(exc)}), 502
    except ET.ParseError as exc:
        return jsonify({"ok": False, "error": f"XML parse error: {exc}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
