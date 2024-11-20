from transformers import AutoTokenizer, AutoModelForSeq2SeqGeneration

class SummarizerModel:
    def __init__(self):
        # Start with a pre-trained model like t5-small or BART
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")
        self.model = AutoModelForSeq2SeqGeneration.from_pretrained("t5-small")
    
    def summarize(self, text):
        inputs = self.tokenizer("summarize: " + text, 
                              return_tensors="pt", 
                              max_length=512, 
                              truncation=True)
        
        summary_ids = self.model.generate(inputs["input_ids"],
                                        max_length=150,
                                        min_length=40,
                                        length_penalty=2.0,
                                        num_beams=4)
        
        return self.tokenizer.decode(summary_ids[0], 
                                   skip_special_tokens=True) 