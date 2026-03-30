from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import query, ingest

app = FastAPI(title="AI Software Engineer Assistant")

# ✅ ADD THIS (CORS FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router)
app.include_router(ingest.router)