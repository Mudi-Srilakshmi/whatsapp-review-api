from pydantic import BaseModel
from datetime import datetime


class ReviewCreate(BaseModel):
    phone: str
    message: str


class ReviewResponse(BaseModel):
    id: int
    phone: str
    message: str
    created_at: datetime

    class Config:
        orm_mode = True
