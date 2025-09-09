from sqlalchemy import Column, String, Enum, JSON, DateTime, ForeignKey
from uuid import uuid4
from ..database import Base
import datetime

class TrainJob(Base):
    __tablename__ = "train_jobs"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    requestor_id = Column(String, ForeignKey("users.id"))
    status = Column(Enum("pending", "preparing", "ready_for_approval", "approved", "running", "completed", "failed", name="status_enum"))
    artifact_path = Column(String)
    metrics = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    approved_by = Column(String, ForeignKey("users.id"))
    approved_at = Column(DateTime)