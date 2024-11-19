from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import logging


class SectionClassifier:
    def __init__(self, model_name: str="bert-base-uncased" , lables:list=None):
        self.logger = logging.getLogger(__name__)
        
        self.lables = lables or[
            "Abstract",
            "Introduction",
            "Methods",
            "Results",
            "Discussion",
            "Conclusion"
        ]
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name,num_labels=len(self.lables))

            self.logger.info(f"Section Classifier loaded successfully with model: {model_name}")

        except Exception as e:
            self.logger.error(f"Error loading model: {e}")
            raise e
        
    def predict(self,text:str, confidence_threshold:float=0.5):
        try:
            inputs = self.tokenizer(text,return_tensors="pt",truncation=True,padding=True)

            with torch.no_grad():
                outputs = self.model(**inputs)
                probabilities = torch.nn.functional.softmax(outputs.logits,dim=1)
                confidence , predicted_class = torch.max(probabilities,dim=1)
            result = {
                "section":self.lables[predicted_class.item()],
                "confidence":confidence.item(),
                "is_confident":confidence.item() > confidence_threshold
            }
            return result
        except Exception as e:
            self.logger.error(f"Error predicting section: {e}")
            raise e
