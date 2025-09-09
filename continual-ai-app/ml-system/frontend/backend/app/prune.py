from pydantic import BaseModel
from typing import List, Dict

class PruneRequest(BaseModel):
    dry_run: bool = True
    target_size: Optional[float] = None  # reduction %

class PruneCandidate(BaseModel):
    id: str
    reason: str
    weight: float

class PruneResponse(BaseModel):
    candidates: List[PruneCandidate]
    committed: bool = False