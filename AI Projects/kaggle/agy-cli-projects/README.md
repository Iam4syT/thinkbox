# AGY CLI Automation Engine

[![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Google Cloud](https://img.shields.io/badge/Cloud-Google%20BigQuery-4285F4?style=flat-square&logo=googlecloud)](https://cloud.google.com/bigquery)
[![Google Drive API](https://img.shields.io/badge/API-Google%20Drive%20v3-34A853?style=flat-square&logo=googledrive)](https://developers.google.com/drive)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#6-license)

> **An automated cloud telemetry, news summarization, and Google Drive publishing workflow powered by the Antigravity CLI (agy) ecosystem.**

---

## 1. Project Overview

The **AGY CLI Automation Engine** brings together automated feed parsing, content summarization, local web dashboards, and cloud storage publishing. It automates monitoring critical cloud platform changes (e.g. Google BigQuery Release Notes) and syncing summarized operational intelligence directly to Google Drive.

### Core Components

1. **BigQuery Release Notes Viewer (`bq-releases-notes/`):**
   - Flask web application proxying Google Cloud's official Atom XML feed (`https://docs.cloud.google.com/feeds/bigquery-release-notes.xml`).
   - Features live filtering, expandable release cards, dark glassmorphism UI, and 1-click sharing.

2. **Google Drive Sync Engine (`upload_to_drive.py`):**
   - OAuth2 / Service Account enabled uploader pushing generated summary files (`news_summary.txt`, release logs) directly to Google Drive.

3. **News & Telemetry Summarizer (`news.txt` & `news_summary.txt`):**
   - Ingestion and summarization pipeline for daily news feeds and technical releases.

---

## 2. Technical Architecture & Workflow

```
┌────────────────────────────────┐
│  BigQuery Atom XML Feed        │  Live Feed: https://docs.cloud.google.com/
│  & News Telemetry              │  feeds/bigquery-release-notes.xml
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Flask Backend & Parser        │  Parses XML entries, strips HTML tags,
│  (bq-releases-notes/app.py)    │  categorizes updates (Feature, Deprecated)
└───────────────┬────────────────┘
                │
                ├──► [ Local Web Dashboard (http://localhost:5000) ]
                │
                ▼
┌────────────────────────────────┐
│  Automated Summarization       │  Generates structured digests (news_summary.txt)
│  & Drive Sync                  │  and uploads automatically to Google Drive
│  (upload_to_drive.py)          │  via Google Drive v3 API
└───────────────┬────────────────┘
```

---

## 3. Project Structure

```
agy-cli-projects/
├── bq-releases-notes/        # Flask Web Application for BigQuery Release Notes
│   ├── app.py                # Flask API backend & Atom feed parser
│   ├── templates/index.html  # Modern glassmorphism HTML interface
│   ├── static/               # CSS & JavaScript assets
│   ├── requirements.txt      # Flask app dependencies
│   └── README.md             # Sub-project documentation
├── upload_to_drive.py        # Google Drive API v3 upload script
├── automate_pipeline.py      # End-to-end automated fetch, summarize & sync orchestrator
├── news.txt                  # Raw news telemetry feed sample
├── news_summary.txt          # Processed news summary digest
├── latest_release_summary.txt# Generated latest BigQuery release notes summary
├── .env.example              # Secret & API configuration template
├── .gitignore                # Git ignore rules
└── README.md                 # Primary project documentation
```

---

## 4. Setup and Installation

### Prerequisites
- Python 3.10 or higher
- Google Cloud / Drive API credentials (`credentials.json` or `token.json`)

### Quickstart

1. **Navigate to the project directory:**
   ```bash
   cd "/Users/4syt/Documents/thinkbox/AI Projects/kaggle/agy-cli-projects"
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r bq-releases-notes/requirements.txt google-api-python-client google-auth-httplib2 google-auth-oauthlib python-dotenv
   ```

---

## 5. How to Automate the Project

### Option 1: Running the Automated Orchestrator Script
Execute `automate_pipeline.py` to pull the latest BigQuery release feed, parse entries, save `latest_summary.txt`, and automatically upload the digest to Google Drive:

```bash
python automate_pipeline.py
```

### Option 2: Scheduling via Cron / macOS Launchd
Set up a daily cron job to run the pipeline automatically at 08:00 AM every day:

```bash
0 8 * * * cd "/Users/4syt/Documents/thinkbox/AI Projects/kaggle/agy-cli-projects" && ./venv/bin/python automate_pipeline.py >> automation.log 2>&1
```

### Option 3: Scheduling via Antigravity `/schedule` Slash Command
You can trigger recurring background execution directly in Antigravity using:
```text
/schedule "Run automate_pipeline.py every day at 08:00 AM"
```

---

## 6. License

Distributed under the **MIT License**. Release note content is © Google LLC.
