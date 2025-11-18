from fastapi import FastAPI, Form
from datetime import datetime

app = FastAPI()

# temporary in-memory storage
reviews = []
user_state = {}


@app.post("/webhook")
async def webhook(From: str = Form(...), Body: str = Form(...)):
    """
    Simulate WhatsApp webhook.
    Twilio will send:
      From -> phone number
      Body -> message text
    """
    sender = From
    message = Body.strip()

    if sender not in user_state:
        user_state[sender] = {}
        return "Which product is this review for?"

    if "product_name" not in user_state[sender]:
        user_state[sender]["product_name"] = message
        return "What's your name?"

    if "user_name" not in user_state[sender]:
        user_state[sender]["user_name"] = message
        return f"Please send your review for {user_state[sender]['product_name']}."

    # this is the final message = review text
    user_state[sender]["product_review"] = message

    review = {
        "id": len(reviews) + 1,
        "contact_number": sender,
        "user_name": user_state[sender]["user_name"],
        "product_name": user_state[sender]["product_name"],
        "product_review": user_state[sender]["product_review"],
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    reviews.append(review)

    # clear state for this sender
    del user_state[sender]

    return f"Thanks {review['user_name']} -- your review for {review['product_name']} has been recorded."


@app.get("/api/reviews")
def get_reviews():
    return reviews
