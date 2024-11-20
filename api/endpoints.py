# api/endpoints/classifier.py
from fastapi import APIRouter, HTTPException
from src.paper_summarizer.models.section_classifier import SectionClassifier
from src.paper_summarizer.schemas.classification_schema import (
    ClassificationRequest, 
    ClassificationResponse
)

router = APIRouter()
classifier = SectionClassifier()

@router.post("/classify", response_model=ClassificationResponse)
async def classify_section(request: ClassificationRequest):
    try:
        result = classifier.predict(
            request.text, 
            request.confidence_threshold
        )
        return ClassificationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))