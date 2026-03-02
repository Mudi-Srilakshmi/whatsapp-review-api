from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String(15), nullable=False, index=True)

    message = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return f"<Review id={self.id} phone={self.phone}>"
