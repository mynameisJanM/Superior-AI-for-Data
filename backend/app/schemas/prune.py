from pydantic import BaseModel
from typing import List

class PruneRequest(BaseModel):
    dry_run: bool = True

class PruneResponse(BaseModel):
    candidates: List[str]