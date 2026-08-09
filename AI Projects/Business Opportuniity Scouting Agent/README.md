# Business Opportunity Scouting Agent

[![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT--4o--mini-412991?style=flat-square&logo=openai)](https://platform.openai.com/)
[![Pandas](https://img.shields.io/badge/Data-Pandas%20%7C%20OpenPyXL-150458?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **An autonomous RAG-style (Retrieval-Augmented Generation) AI agent that ingests unstructured web documentation links from an Excel spreadsheet, evaluates content alignment against company strategic goals, scouts business opportunities, generates concrete OKRs, and automatically updates the spreadsheet.**

---

## 1. Business Value & Problem Statement

Strategic alignment across enterprise initiatives and scouting new business opportunities is frequently hindered by manual overhead and fragmented documentation. Strategic planning and business development teams often spend hundreds of hours reading project proposals, mapping them to strategic objectives, and writing Objectives & Key Results (OKRs).

This project automates that workflow using the **Business Opportunity Scouting Agent**:
1. **Automated Ingestion:** Extracts live textual content from project documentation URLs.
2. **Contextual Grounding:** Evaluates project alignment and scouts business opportunities against explicit corporate Vision, Mission, and Strategic Goals using GPT-4o-mini.
3. **Automated Write-Back:** Directly updates the source Excel spreadsheet (`initiatives.xlsx`) with structured Strategic Benefits, actionable OKRs, and execution status.

---

## 2. Technical Architecture & Workflow

```
┌────────────────────────┐
│  initiatives.xlsx      │  Reads: Initiative Name & Documentation Link
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  Scraper Module        │  Fetches URL text via BeautifulSoup & Requests
│  (scraper.py)          │  (cleans scripts, styles, nav, footer)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  Strategic Analyzer    │  Injects Company Vision & Mission context
│  (analyzer.py)         │  Generates Strategic Benefits & OKRs via OpenAI
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  Excel Write-Back      │  Updates Strategic Benefits, Actionable OKR,
│  (main.py)             │  and Status columns in initiatives.xlsx
└────────────────────────┘
```

### Input & Output Schema

| Column | Initial State | Agent Processing Action |
| --- | --- | --- |
| **Initiative Name** | Pre-filled | Identifies target project |
| **Documentation Link** | Pre-filled | Scrapes webpage text from URL |
| **Strategic Benefits** | *Empty* | Populates 2 concrete alignment benefits |
| **Actionable OKR** | *Empty* | Populates 1 Objective and 2 Key Results (KR1, KR2) |
| **Status** | *Empty / Pending* | Marks as `Completed`, `Completed (Unstructured)`, or `Error` |

---

## 3. Project Structure

```
Business Opportuniity Scouting Agent/
├── setup_excel.py    # Generates initial sample initiatives.xlsx workbook
├── scraper.py        # Web scraping module for URL text extraction
├── analyzer.py       # OpenAI RAG analyzer for strategic benefit & OKR extraction
├── main.py           # End-to-end orchestration and Excel write-back loop
├── requirements.txt  # Project dependencies
├── .env.example      # Environment variable template
├── .gitignore        # Git exclusion rules
└── README.md         # Detailed technical documentation
```

---

## 4. Setup and Installation

### Prerequisites
- Python 3.10 or higher
- OpenAI API Key

### Quickstart

1. **Clone or navigate to the project directory:**
   ```bash
   cd "/Users/4syt/Documents/thinkbox/AI Projects/Business Opportuniity Scouting Agent"
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and set your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
   Or set environment variables directly:
   ```bash
   export OPENAI_API_KEY="your-actual-api-key"
   ```

---

## 5. Usage Guide

### Step 1: Generate the Sample Spreadsheet
Create the initial input workbook (`initiatives.xlsx`):
```bash
python setup_excel.py
```

### Step 2: Run the Agent Orchestrator
Execute the complete workflow:
```bash
python main.py
```

### Step 3: Inspect Output
Open `initiatives.xlsx` using Excel, Numbers, or any spreadsheet viewer. Columns C (`Strategic Benefits`), D (`Actionable OKR`), and E (`Status`) will be populated with AI-generated strategic insights.

---

## 6. Development Best Practices Included

- **Environment Isolation:** Clean Virtualenv and modular imports.
- **Secret Management:** Automatic configuration via `.env` / `python-dotenv`.
- **Robust Error Handling:** Scraper catches network timeouts, invalid URLs, and HTTP errors gracefully.
- **Model Fallbacks:** Structured output parsing with fallback handling for unstructured LLM outputs.
- **Extensibility:** Easily adjust `COMPANY_CONTEXT` in `analyzer.py` to match any organization's strategic goals.

---

## 7. License

MIT License. Developed as part of the Thinkbox AI Projects lab series.
