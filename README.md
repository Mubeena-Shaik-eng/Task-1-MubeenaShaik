# RuleBot 🤖 — Hybrid Rule-Based AI Chatbot

**DecodeLabs AI Internship 2026 — Project 1: Rule-Based AI Chatbot**

A chatbot combining deterministic rule-based logic with a generative AI fallback (Google Gemini). Built on the **Input → Process → Output (IPO)** model used by production AI guardrail systems.

---

## 🧠 How It Works

```
User Input
    │
    ▼
Sanitization (lowercase + strip whitespace)
    │
    ▼
Rule Match? ──Yes──▶ Instant Rule-Based Response (fast, traceable, zero hallucination)
    │
    No
    │
    ▼
Gemini AI Fallback ─▶ Generative Response (flexible, handles anything outside the rule set)
```

The bot checks every predefined rule against the cleaned input. If any keyword is found, it replies instantly. If nothing matches, the question is passed to Google's Gemini model for a generated answer.

---

## ✅ Features (Spec Compliance)

| Requirement | Implementation |
|---|---|
| Continuous input loop | `while True` loop with explicit `break` |
| Sanitization | `.lower().strip()` on every input |
| Knowledge base | Dictionary of predefined intents (`hi`, `hello`, `bye`, `your name`) |
| Fallback for unknowns | Gemini API call when no rule matches |
| Clean exit strategy | `exit` / `bye` commands |

---

## 📂 Project Structure

```
AI-Chatbot/
├── chatbot.py          # Main chatbot logic
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/<your-username>/AI-Chatbot.git
cd AI-Chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Gemini API key**

The script reads the key from an environment variable named `GEMINI_API_KEY`. Set it before running:

```bash
export GEMINI_API_KEY="your_real_key_here"      # macOS/Linux
set GEMINI_API_KEY=your_real_key_here           # Windows (cmd)
```

Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

> ⚠️ If no environment variable is set, the script falls back to the placeholder `"Api here"` in the code — replace this only for local testing, and **never commit a real key in this fallback string**.

**4. Run the chatbot**
```bash
python chatbot.py
```

---

## 💬 Sample Interaction

```
RuleBot: Hi! I'm RuleBot. Type 'exit' or 'bye' to end the chat.
You: hi
RuleBot: Hello! What can I do for you?
You: your name
RuleBot: I'm RuleBot, your friendly assistant.
You: what is artificial intelligence
RuleBot: Artificial intelligence (AI) is the field of computer science focused
on building systems that can perform tasks normally requiring human intelligence...
You: bye
RuleBot: Goodbye! Have a great day.
```
*(The first two replies are instant rule-based matches. The AI question is routed to Gemini.)*

---

## 🛠️ Tech Stack

- **Python 3** — core logic
- **`requests`** — lightweight HTTP calls to the Gemini REST API
- **Google Gemini 2.5 Flash** — generative fallback model

---

## 🔒 Security Note

This project reads its API key from the `GEMINI_API_KEY` environment variable. The hardcoded fallback in the code is a placeholder and must never contain a real, live key in any committed version.

---

## 🎓 Key Skills Demonstrated

- Control flow & decision-making logic
- Dictionary-based rule matching
- REST API integration with error handling
- Hybrid deterministic/generative system design

---

## 👤 Author

**Mubeena**
AI Intern, Batch 2026 — DecodeLabs
