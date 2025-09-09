from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey, JSON
from uuid import uuid4
from ..database import Base
import datetime

class DataItem(Base):
    __tablename__ = "data_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    owner_id = Column(String, ForeignKey("users.id"))
    source = Column(String)
    content = Column(String)
    summary = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_accessed_at = Column(DateTime)
    ttl_days = Column(Integer, default=90)
    soft_deleted = Column(Boolean, default=False)
    metadata = Column(JSON)