from pydantic import BaseModel

class DataItemCreate(BaseModel):
    content: str