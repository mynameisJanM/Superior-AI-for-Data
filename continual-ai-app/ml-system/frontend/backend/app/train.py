from pydantic import BaseModel
from typing import Optional, Dict

class TrainRequest(BaseModel):
    # params if any

class TrainStatus(BaseModel):
    status: str
    metrics: Optional[Dict]