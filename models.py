from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, index=True)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
