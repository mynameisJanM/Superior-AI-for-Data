from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    text: str
    top_k: int = 10

class QueryMatch(BaseModel):
    id: str
    score: float
    metadata: dict

class QueryResponse(BaseModel):
    matches: List[QueryMatch]