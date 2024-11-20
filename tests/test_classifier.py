# tests/test_classifier.py
import pytest
from src.paper_summarizer.models.section_classifier import SectionClassifier

def test_classifier_initialization():
    classifier = SectionClassifier()
    assert classifier is not None

def test_section_classification():
    classifier = SectionClassifier()
    
    test_cases = [
        ("Introduction paragraph", "Introduction"),
        ("Methodology details", "Methodology"),
        ("Results analysis", "Results")
    ]
    
    for text, expected_section in test_cases:
        result = classifier.predict(text)
        assert result['section'] == expected_section
        assert result['is_confident']