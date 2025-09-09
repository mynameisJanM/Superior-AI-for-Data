from sqlalchemy import Column, String, DateTime, JSON, Boolean, ForeignKey
from uuid import uuid4
from ..database import Base
import datetime

class PruneLog(Base):
    __tablename__ = "prune_logs"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    dry_run = Column(Boolean)
    details = Column(JSON)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)