from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    text: str

class QueryResponse(BaseModel):
    matches: List[dict]
    