from sqlalchemy import Column, String, DateTime, Integer, Boolean
from uuid import uuid4
from ..database import Base
import datetime

class DataItem(Base):
    __tablename__ = "data_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    content = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    ttl_days = Column(Integer, default=90)
    soft_deleted = Column(Boolean, default=False)