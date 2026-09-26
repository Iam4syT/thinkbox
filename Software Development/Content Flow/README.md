# ContentFlow — AI-Powered Cross-Platform Content Repurposing Engine

[![Node.js](https://img.shields.io/badge/Runtime-Node.js%20v18+-339933?style=flat-square&logo=nodedotjs)](https://nodejs.org/)
[![Vite](https://img.shields.io/badge/Frontend-Vite%20%7C%20Vanilla%20JS-646CFF?style=flat-square&logo=vite)](https://vitejs.dev/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20%7C%20Gemini-412991?style=flat-square&logo=openai)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **An automated 4-stage AI content pipeline that transforms raw brain dumps into refined drafts, tailors content across social platforms (LinkedIn, Instagram, YouTube), schedules optimal posting sequences, and tracks performance against OKRs.**

---

## 1. Core Problem & Product Vision

Content creators produce long-form content and manually rewrite, resize, and reformat it for every platform. **ContentFlow** automates this lifecycle through an intelligent multi-provider AI pipeline.

### The 4-Stage Content Pipeline

```
┌───────────────┐     AI Refines     ┌────────────────┐
│  🧠 Brain     ├───────────────────►│  ✍️ Refined     │
│  Dump Input   │                    │  Draft         │
└───────────────┘                    └───────┬────────┘
                                             │ AI Tailors
                                             ▼
┌───────────────┐   Automated Post   ┌────────────────┐
│  📤 Scheduled ◄────────────────────┤  🎯 Platform   │
│  Queue        │   & Journey Sync   │  Adaptations   │
└───────────────┘                    └────────────────┘
```

---

## 2. Project Structure

```
Content Flow/
├── implementation_plan.md    # Detailed architecture & feature specification
├── content-flow/
│   ├── server/               # Express backend, SQLite DB, AI providers & routes
│   │   ├── ai/               # Gemini & OpenAI provider adapters & prompt engineering
│   │   ├── automation/       # Timing optimizer, journey planner, & queue engine
│   │   ├── db/               # SQLite database & repository patterns
│   │   └── routes/           # REST API endpoints
│   ├── src/                  # Frontend Vite UI components & dashboards
│   ├── package.json          # Dependencies & npm scripts
│   ├── .env.example          # Environment variable template
│   └── vite.config.js        # Vite bundler configuration
└── README.md                 # Primary project documentation
```

---

## 3. Quickstart Guide

1. **Navigate to the application folder:**
   ```bash
   cd "/Users/4syt/Documents/thinkbox/Software Development/Content Flow/content-flow"
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure Environment:**
   Copy `.env.example` to `.env` and set your API keys:
   ```bash
   cp .env.example .env
   ```

4. **Launch Development Servers:**
   ```bash
   npm run dev
   ```

---

## 4. License

Distributed under the **MIT License**. Part of the Thinkbox Software Development portfolio.
