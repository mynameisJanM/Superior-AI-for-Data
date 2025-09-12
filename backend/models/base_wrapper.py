from transformers import AutoModelForMaskedLM, AutoTokenizer
from peft import get_peft_model, LoraConfig
from ..app.config import settings
import torch

class BaseModelWrapper:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(settings.EMBEDDING_MODEL)
        self.model = AutoModelForMaskedLM.from_pretrained(settings.EMBEDDING_MODEL)
        lora_config = LoraConfig(r=settings.LORA_R, target_modules=["query"])
        self.model = get_peft_model(self.model, lora_config)