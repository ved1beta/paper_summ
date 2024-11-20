import PyPDF2
import re

class PaperProcessor:
    def __init__(self):
        self.text = ""
    
    def extract_from_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                self.text += page.extract_text()
        return self.clean_text()
    
    def clean_text(self):
        # Remove special characters and normalize
        cleaned = re.sub(r'\s+', ' ', self.text)
        cleaned = re.sub(r'[^\w\s.,?!]', '', cleaned)
        return cleaned.strip() 