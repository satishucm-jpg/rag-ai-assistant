from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ingestion import load_documents, split_documents
from app.services.retrieval import create_vectorstore
from app.services.github_ingestion import clone_repo, load_repo_files

router = APIRouter()


# Request model for GitHub ingestion
class RepoRequest(BaseModel):
    repo_url: str


# Local ingestion (data folder)
@router.post("/ingest")
def ingest():
    try:
        docs = load_documents()

        if not docs:
            return {"error": "No documents found in data folder"}

        chunks = split_documents(docs)

        if not chunks:
            return {"error": "No chunks created"}

        create_vectorstore(chunks)

        return {"message": "Local documents ingested successfully"}

    except Exception as e:
        return {"error": str(e)}


# GitHub ingestion
@router.post("/ingest/github")
def ingest_github(req: RepoRequest):
    try:
        repo_path = clone_repo(req.repo_url)

        docs = load_repo_files(repo_path)

        if not docs:
            return {"error": "No files loaded from repo"}

        chunks = split_documents(docs)

        if not chunks:
            return {"error": "No chunks created"}

        create_vectorstore(chunks)

        return {"message": "GitHub repo ingested successfully"}

    except Exception as e:
        return {"error": str(e)}