from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class ReviewCreate(BaseModel):
    phone: str = Field(..., min_length=10, max_length=15, example="+919876543210")
    message: str = Field(..., min_length=1, max_length=255, example="Great product!")


class ReviewResponse(BaseModel):
    id: int
    phone: str
    message: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
