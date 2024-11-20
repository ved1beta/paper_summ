# src/paper_summarizer/schemas/classification_schema.py
from pydantic import BaseModel, Field
from typing import Optional

class ClassificationRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=5000)
    confidence_threshold: Optional[float] = Field(0.5, ge=0.0, le=1.0)

class ClassificationResponse(BaseModel):
    section: str
    confidence: float
    is_confident: bool