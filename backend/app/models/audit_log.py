from sqlalchemy import Column, String, DateTime, JSON
from uuid import uuid4
from ..database import Base
import datetime

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    action = Column(String)
    details = Column(JSON)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)