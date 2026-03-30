from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retrieval import retrieve_docs
from app.services.llm import generate_answer

router = APIRouter()


# ✅ Request schema
class QueryRequest(BaseModel):
    question: str


# ✅ Query endpoint
@router.post("/query")
def query_rag(request: QueryRequest):
    try:
        # Step 1: Retrieve relevant documents
        docs = retrieve_docs(request.question)

        # Step 2: Generate answer using LLM
        answer = generate_answer(request.question, docs)

        # Step 3: Extract sources
        sources = list(set([
            doc.metadata.get("source", "unknown")
            for doc in docs
        ]))

        # 🔥 NEW: Add code snippets (top 300 chars)
        snippets = [doc.page_content[:300] for doc in docs]

        return {
            "answer": answer,
            "sources": sources,
            "snippets": snippets
        }

    except Exception as e:
        return {"error": str(e)}