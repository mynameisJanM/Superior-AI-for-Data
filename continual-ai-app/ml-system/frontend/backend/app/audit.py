from pydantic import BaseModel
from typing import List

class AuditEntry(BaseModel):
    action: str
    timestamp: str
    details: dict

class AuditResponse(BaseModel):
    logs: List[AuditEntry]
    page: int
    total: int