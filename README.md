WhatsApp Review API

A simple backend API built using FastAPI that simulates receiving WhatsApp messages (in Twilio webhook format) and stores them as product reviews in memory.

 Features

POST /webhook – Receives WhatsApp-style data (From & Body) as form-data
GET /api/reviews – Returns all saved reviews as JSON
In-memory storage (no database required)
Swagger UI for easy testing Simple structure suitable for webhook-based systems like Twilio

Tech Stack

Python 3.13
FastAPI
Uvicorn
python-multipart

Installation and Running Locally

# Clone the repository
git clone https://github.com/Mudi-Srilakshmi/whatsapp-review-api.git
cd whatsapp-review-api

# Install dependencies
pip install fastapi uvicorn python-multipart

# Start the FastAPI server
uvicorn main:app --reload

API Documentation:

Once the server is running, open:

Swagger UI:
 http://127.0.0.1:8000/docs

 API Endpoints
1️ POST /webhook

Receives WhatsApp message data via form-data.

Request Fields
Field	Description
From	Sender phone number
Body	WhatsApp message text
Example Response
{
  "reply": "Thank you! Your review was received."
}

2️ GET /api/reviews

Returns all stored reviews.

Example Response
[
  {
    "from": "+919876543210",
    "message": "Awesome product!"
  }
]

 API Testing Screenshots
 
 1. POST /webhook

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6ea0a023-0d0f-49c7-a9ad-6889ad2489d4" />

2. GET /api/reviews

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/00cd3709-8378-4c2d-92f3-65fa78a3a769" />

Future Enhancements:

Add database (SQLite/MongoDB)
Add authentication (JWT)
Add Docker support
Deploy on cloud (Render/AWS/Heroku)

Author:

Srilakshmi Mudi
Python & API Development
FastAPI | Django | SQL

GitHub:

https://github.com/Mudi-Srilakshmi

License:
 
This project is created for educational and assignment purposes.






