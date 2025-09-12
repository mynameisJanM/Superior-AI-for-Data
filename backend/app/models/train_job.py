from sqlalchemy import Column, String, Enum, JSON, DateTime
from uuid import uuid4
from ..database import Base
import datetime

class TrainJob(Base):
    __tablename__ = "train_jobs"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    status = Column(Enum("pending", "approved", "completed", name="status_enum"), default="pending")
    metrics = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)