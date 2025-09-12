from pydantic import BaseModel
from typing import List

class AuditResponse(BaseModel):
    logs: List[dict]