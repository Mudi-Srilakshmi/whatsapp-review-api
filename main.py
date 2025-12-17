from fastapi import FastAPI, Form
from datetime import datetime
from typing import List

from database import SessionLocal, engine, Base
from models import Review
from schemas import ReviewResponse

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


@app.post("/webhook")
async def webhook(From: str = Form(...), Body: str = Form(...)):
    """
    Simulate WhatsApp webhook.
    Twilio will send:
      From -> phone number
      Body -> message text
    """

    db = SessionLocal()

    new_review = Review(
        phone=From,
        message=Body.strip()
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    db.close()

    return {
        "reply": "Thank you! Your review was received and stored successfully."
    }


@app.get("/api/reviews", response_model=List[ReviewResponse])
def get_reviews():
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()

    return reviews
