from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from ..database import Base
import datetime

class EmbeddingMeta(Base):
    __tablename__ = "embeddings_meta"
    id = Column(String, primary_key=True, ForeignKey("data_items.id"))
    norm = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)