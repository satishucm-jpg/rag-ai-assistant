AI Software Engineer Assistant

An AI-powered application that can analyze GitHub repositories and answer technical questions about the codebase.

## 🌍 Live Demo

- Backend API: https://rag-ai-assistant-81gg.onrender.com/docs
- Frontend UI: https://rag-ai-assistant-1-srx6.onrender.com/)

🧠 Features

- 🔍 GitHub Repository Ingestion  
- 💬 Ask Questions about Code  
- 📄 Source Attribution (shows files used)  
- 🧩 Code Snippet Extraction  
- ⚡ FastAPI Backend  
- 🌐 Deployed on Cloud (Render)

⚙️ Tech Stack

- **Backend:** FastAPI, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Data Processing:** Custom Retrieval (Lightweight RAG)  
- **Deployment:** Render  

🚀 How It Works

1. Enter a GitHub repository URL  
2. The system clones and reads the codebase  
3. Documents are stored in memory  
4. User asks a question  
5. System retrieves relevant content  
6. Returns answer with sources  


## 🧪 API Usage

### Ingest Repository

POST /ingest/github :
{
  "question": "What does this project do?"
}
📌 Example Response
{
  "answer": "This project is a Python library for making HTTP requests...",
  "sources": ["repo/README.md"],
  "snippets": ["# Requests", "..."]
}
💼 Why This Project Matters

This project demonstrates:
	•	Building AI-powered developer tools
	•	Designing retrieval-based systems (RAG)
	•	Working with real-world GitHub codebases
	•	Full-stack development (frontend + backend)
	•	Cloud deployment and debugging
🏗️ Architecture Overview
Frontend (UI)
    ↓
FastAPI Backend
    ↓
GitHub Repo Ingestion
    ↓
Document Processing
    ↓
Retrieval Engine
    ↓
Answer Generation

🔥 Future Improvements
	•	Add LLM-based summarization (OpenAI / local models)
	•	Improve search with embeddings (FAISS / vector DB)
	•	Chat-style UI (like ChatGPT)
	•	Persistent storage (database / vector store)
	•	Multi-repository support

👨‍💻 Author

Sai Venkata
