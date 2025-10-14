# AI Agent App

![JavaScript](https://img.shields.io/badge/Frontend-React-orange?logo=react)  
![Python](https://img.shields.io/badge/Backend-Flask-blue?logo=python)  
![OpenAI](https://img.shields.io/badge/AI-OpenAI-black?logo=openai)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Status-Active-success)

---
# 🤖 AI Agent App

A portfolio website that exposes multiple specialized AI agents powered by OpenAI LLMs. Each agent helps visitors learn about projects, skills, services, and research topics via a modern chat interface. The project is split into a React frontend (chat UI) and a Flask backend (API + OpenAI integration).

![AI Agent App](/img/ai-agent-app-home.png "AI Agent App")

---

## 💡 Backstory
For a while now, I have been thinking of creating a website portfolio for the numerous saved labs on my PC, and then I chanced upon an ai agent portfolio app article by Andrew Baisden. 
His solution was better because it makes a developer's portfolio more interactive and useful than a static site. Instead of only listing projects and skills, the idea was to create conversational agents that can:
- welcome visitors,
- explain projects in context,
- discuss career history and skills,
- describe services for potential clients,
- and answer research/tech questions.

The result is a portfolio that feels like a knowledgeable, approachable guide — useful for recruiters, clients, and curious peers.

---

## 🚀 Features

- Multiple specialized AI agents:
  - Welcome Agent — quick orientation and navigation help
  - Project Agent — details and deep-dive about projects
  - Career Agent — experience, skills, and career timeline
  - Client Agent — services, engagement model, pricing overview
  - Research Agent — technology explanations, trends, references
- Modern React-based chat UI (conversational interface)
- Flask backend exposing an API that forwards to OpenAI
- Configurable system/persona prompts per agent
- Local development friendly (separate frontend/backend)
- Extensible: add new agents or integrate a knowledge store

---

## 🛠️ Tech Stack

- Frontend: React (Vite) — chat UI and agent selector  
- Backend: Flask — API endpoints to interact with OpenAI  
- AI: OpenAI LLMs (chat/completion)  
- Optional: vector DB / embedding store for longer-term memory or project documents

---

## ⚙️ Prerequisites

- Node.js v16+ (frontend)
- Python 3.8+ (backend)
- npm or yarn
- An OpenAI API key

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/andrewbaisden/ai-agent-app.git
cd ai-agent-app
```

### 2. Set environment variables (backend)

Create a `.env` file in the `backend` directory with your OpenAI API key:

```env
OPENAI_API_KEY="your_api_key_here"
# Optionally set other config such as model, temperature, port, etc.
```

### 3. Set up the backend

```bash
# from project root
cd backend

# create virtual env (recommended)
python3 -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# start the Flask server
python main.py
```

Default backend URL: http://127.0.0.1:5001 (confirm in backend logs/config)

### 4. Set up the frontend

Open a new terminal:

```bash
cd frontend

# install node deps
npm install

# start development server
npm run dev
```

Default frontend URL: http://localhost:5173

---

## ▶️ Usage

1. Start both backend and frontend (see Installation).
2. Open http://localhost:5173 in your browser.
3. You'll be greeted by the Welcome Agent.
4. Choose an agent to talk to based on what you need:
   - Welcome Agent — overview and guidance
   - Project Agent — ask about individual projects or demos
   - Career Agent — inquire about experience, roles, and skills
   - Client Agent — learn about services and how to work together
   - Research Agent — ask technical questions, trends, or get references

Agents are driven by configurable prompts; you can tune personality and behavior in the backend.

---

## 🔍 Example

User: "Tell me about the demo chat app project. What tech did you use and what problems did it solve?"  
Agent (Project Agent): "The demo chat app uses React on the frontend and Flask for the API. It integrates OpenAI to power conversational features and solves the problem of making static project pages interactive by answering visitor questions in natural language..."

---

## 📈 Roadmap

- [ ] Add per-agent conversation history persistence (optionally with a vector store)  
- [ ] Improve prompt management UI for non-developers to edit agent personas  
- [ ] Add authentication for protected admin features (deploy/edit agents)  
- [ ] Unit & integration tests for backend and frontend  
- [ ] Deploy templates / Docker compose for one-command deployment  
- [ ] Add analytics to track agent usage and common queries

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Please:
1. Fork the repo
2. Create a branch for your change
3. Open a PR with a clear description and screenshots if UI changes are included

---

## 📜 License

This project is distributed under the MIT License.

---

## 👨‍💻 Author

Originally developed by Andrew Baisden  
(Repository: https://github.com/andrewbaisden/ai-agent-app)

Currently maintained by Bunamin Adams (4syT Labs)

🔗 LinkedIn | GitHub
🌐 think4syt.com
✉️ bunamin@think4syt.com

---
