from fastapi import FastAPI, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, Base
from models import Review
from schemas import ReviewResponse

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/webhook")
def webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Simulate WhatsApp webhook
    """

    # Validation
    if not Body.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        new_review = Review(
            phone=From,
            message=Body.strip()
        )

        db.add(new_review)
        db.commit()
        db.refresh(new_review)

        return {
            "reply": "Thank you! Your review was received successfully."
        }

    except Exception:
        raise HTTPException(status_code=500, detail="Server error")


@app.get("/api/reviews", response_model=List[ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    try:
        reviews = db.query(Review).all()
        return reviews
    except Exception:
        raise HTTPException(status_code=500, detail="Server error")
