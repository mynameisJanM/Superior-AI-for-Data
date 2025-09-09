from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from uuid import uuid4
from ..database import Base
import datetime

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    action = Column(String)
    target_type = Column(String)
    target_id = Column(String)
    details = Column(JSON)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)