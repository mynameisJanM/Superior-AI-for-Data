from sentence_transformers import SentenceTransformer
from ..config import settings

model = SentenceTransformer(settings.EMBEDDING_MODEL)

def compute_embedding(text: str):
    return model.encode(text)