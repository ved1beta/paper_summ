# api/main.py
from fastapi import FastAPI
from api.endpoints import classifier, summarizer

app = FastAPI(
    title="Research Paper Assistant",
    description="AI-powered tool for research paper analysis"
)

# Include routers
app.include_router(classifier.router, prefix="/classifier", tags=["Section Classification"])
app.include_router(summarizer.router, prefix="/summarizer", tags=["Paper Summarization"])