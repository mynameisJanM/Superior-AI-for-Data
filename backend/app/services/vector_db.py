import faiss
import numpy as np
from .embedding import compute_embedding
from sqlalchemy import create_engine, Column, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings

engine = create_engine('sqlite:///embeddings.db')
Base = declarative_base()
class Embedding(Base):
    __tablename__ = 'embeddings'
    id = Column(String, primary_key=True)
    vector = Column(LargeBinary)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

index = faiss.IndexFlatL2(384)

def insert_vector(id: str, vector: np.ndarray):
    index.add(np.array([vector]))
    db = Session()
    emb = Embedding(id=id, vector=vector.tobytes())
    db.add(emb)
    db.commit()

def search_vectors(query_text: str, top_k: int):
    vector = compute_embedding(query_text)
    D, I = index.search(np.array([vector]), top_k)
    return [{"id": str(I[0][i]), "score": D[0][i]} for i in range(len(I[0])) if I[0][i] >= 0]

def delete_vector(id: str):
    pass  # Simplified, no delete for demo