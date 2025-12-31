# ⚖️ AI Debate Arena

AI Debate Arena is a web-based application that helps users prepare for professional debates using multi-agent AI.

Users can enter a debate topic and watch two AI agents argue **FOR** and **AGAINST** the motion, followed by a neutral summary. All debates are saved and can be revisited later.

---

## ✨ Features

- 🔐 Google Authentication (Firebase)
- 🤖 Multi-agent AI debate system
- 🧠 FOR vs AGAINST structured arguments
- 📚 Debate history per user
- 🧾 Individual debate detail pages
- 🎨 Clean single-page UI with animations
- ☁️ MongoDB Atlas for persistence

---

## 🛠️ Tech Stack

**Backend**
- FastAPI
- MongoDB Atlas
- Firebase Admin SDK

**Frontend**
- HTML + CSS
- Jinja2 Templates
- Firebase Auth (Google Login)

**AI**
- Agentic debate system (LLM-based)

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/ai-debate-arena.git
cd ai-debate-arena

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables
Create a .env file:
MONGO_URI=your_mongodb_atlas_uri

5️⃣ Run the app
uvicorn main:app --reload

open:
http://localhost:8000





🔒 Authentication Flow

Google login via Firebase (frontend)

Secure cookie-based sessions

Backend token verification

Automatic token refresh handling

📌 Future Improvements

Public shareable debate links

PDF export of debates

Debate analytics (winner analysis)

Deployment on Render / Railway