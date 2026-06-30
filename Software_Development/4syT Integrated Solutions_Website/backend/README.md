# ⚙️ 4syT Website API Backend

This is a lightweight **Python Flask** API backend that powers the interactive AI features of the **4syT Integrated Solutions Website**.

It is inspired by the modular multi-agent structure of the `ai-agent-app` and provides the endpoints required by the frontend's RAG Assistant and forms:

- 🤖 **`/api/rag`** — Contextual corporate RAG assistant using OpenAI or Groq LLMs.
- ✉️ **`/api/contact`** — Receives and logs client contact form submissions.
- 📰 **`/api/newsletter`** — Receives and logs newsletter subscriptions.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- An API key for **Groq** (`GROQ_API_KEY`) or **OpenAI** (`OPENAI_API_KEY`).

### 1. Installation

Navigate to the `backend/` directory:
```bash
cd backend
```

Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the `backend/` directory:
```env
PORT=5002
# Configure either Groq or OpenAI
GROQ_API_KEY="your_groq_api_key_here"
# OR
OPENAI_API_KEY="your_openai_api_key_here"
```

### 3. Run the Backend

Launch the development server:
```bash
python main.py
```

The server will start on `http://127.0.0.1:5002`.

---

## 🎨 Frontend Integration

In `4syT-Website/js/main.js`, the chat widget is programmed to automatically attempt fetching this backend (`/api/rag`). 
- If the backend is running, the assistant leverages the live LLM agent.
- If the backend is offline or the site is hosted statically (e.g. on Netlify/Vercel) without a server, the frontend transparently falls back to a **client-side local RAG engine** that uses keyword-matching to answer queries, ensuring the assistant is *always* functional.
