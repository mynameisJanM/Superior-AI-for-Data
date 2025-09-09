from sqlalchemy import Column, Enum, String, DateTime
from uuid import uuid4
from ..database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, index=True)
    role = Column(Enum("user", "approver", "admin", name="role_enum"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)