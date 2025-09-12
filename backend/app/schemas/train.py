from pydantic import BaseModel

class TrainStatus(BaseModel):
    status: str