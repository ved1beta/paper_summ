from fastapi import FastAPI, File, UploadFile
from .model import SummarizerModel
from .data_processor import PaperProcessor

app = FastAPI()
model = SummarizerModel()
processor = PaperProcessor()

@app.post("/summarize")
async def summarize_paper(file: UploadFile):
    # Save uploaded file temporarily
    content = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(content)
    
    # Process and summarize
    text = processor.extract_from_pdf("temp.pdf")
    summary = model.summarize(text)
    
    return {"summary": summary} 