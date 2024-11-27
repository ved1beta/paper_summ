import PyPDF2
import re
 
import fitz
from tqdm.auto import tqdm 

def text_formatter(text : str )->str:
    """
    This function is used to format the text extracted from the pdf files.
    """
    text_clean = text.replace("\n"," ").strip()
    return text_clean
def open_read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages_text = []
    for page_num in tqdm(range(len(doc))):
        page = doc[page_num]
        text = page.get_text()
        text = text_formatter(text=text)

        pages_text.append({
            "page_num": page_num,
            "text": text,
            "pages_token_count": len(text)/4
        }) 
    return pages_text
pages_text = open_read_pdf("Assignment 3 material.pdf")
print(pages_text[:10])


