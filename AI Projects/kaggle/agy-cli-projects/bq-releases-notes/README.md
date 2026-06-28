# 📦 BigQuery Release Notes Viewer

A lightweight **Python Flask** web application that fetches, displays, and lets you share the latest [Google BigQuery Release Notes](https://cloud.google.com/bigquery/docs/release-notes) directly from the official Atom feed.

---

## ✨ Features

- 🔄 **Live feed** — Pulls directly from Google Cloud's official Atom XML feed
- 🔃 **Refresh button with spinner** — Reload the latest notes on demand
- 🏷️ **Category filter chips** — Filter entries by type: `Feature`, `Change`, `Deprecated`, etc.
- 📖 **Expandable cards** — Click any entry to reveal the full release details
- 🔗 **Docs link** — Jump straight to the official Google Cloud documentation page for each entry
- 🐦 **Tweet any update** — Pre-fills a 280-character tweet with a summary and link, opens X (Twitter) intent
- 🎨 **Dark glassmorphism UI** — Clean, modern dark theme with Google Cloud colour accents

---

## 🗂️ Project Structure

```
bq-releases-notes/
├── app.py               # Flask backend — proxies & parses the Atom XML feed
├── requirements.txt     # Python dependencies
├── .gitignore           # Standard Python / Flask ignores
├── README.md            # This file
├── templates/
│   └── index.html       # Jinja2 HTML template
└── static/
    ├── style.css        # Dark UI styles (vanilla CSS)
    └── main.js          # Frontend logic (vanilla JavaScript)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- `pip`

### 1. Clone / navigate to the project

```bash
cd bq-releases-notes
```

### 2. Create and activate a virtual environment *(recommended)*

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoint

The Flask backend exposes a single JSON endpoint used by the frontend:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/releases` | Fetches and parses the BigQuery Atom feed, returns JSON |

**Example response:**

```json
{
  "ok": true,
  "data": {
    "feed_title": "BigQuery - Release notes",
    "feed_updated": "2026-06-25T00:00:00-07:00",
    "fetched_at": "2026-06-28 14:00:00 UTC",
    "entries": [
      {
        "title": "June 25, 2026",
        "updated": "2026-06-25T00:00:00-07:00",
        "link": "https://cloud.google.com/bigquery/docs/release-notes#June_25_2026",
        "content_html": "<h3>Feature</h3><p>...</p>",
        "plain_text": "Feature ...",
        "categories": ["Feature"]
      }
    ]
  }
}
```

---

## 🐦 Tweeting an Update

1. Expand any release entry card
2. Click **"Tweet this"**
3. Edit the pre-filled tweet text in the modal (280-character limit enforced)
4. Click **"Post to X"** — this opens a Twitter/X intent window, no API key required

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework |
| `flask-cors` | Cross-Origin Resource Sharing headers |
| `requests` | HTTP client for fetching the XML feed |

---

## 🌐 Data Source

Feed URL:
```
https://docs.cloud.google.com/feeds/bigquery-release-notes.xml
```

Official docs page:
```
https://cloud.google.com/bigquery/docs/release-notes
```

---

## 📄 License

This project is for personal / educational use. Release note content is © Google LLC.
