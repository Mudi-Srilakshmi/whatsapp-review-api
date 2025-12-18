## WhatsApp Review API

A FastAPI-based backend application that simulates receiving WhatsApp messages (in Twilio webhook format) and stores them as product reviews in a SQLite database using a clean REST API design.

## Project Overview

This project mimics how businesses collect customer feedback via WhatsApp.
Incoming messages are received through a webhook endpoint, processed, and
stored persistently using a database. The API is designed following
real-world backend practices.

## Features

POST /webhook – Receive WhatsApp-style messages (From, Body) via form-data
GET /api/reviews – Fetch all stored reviews in JSON format
Database-backed storage (SQLite using SQLAlchemy)
Pydantic schemas for clean API responses
Swagger UI for easy testing and exploration
Modular project structure (models, schemas, database)
Designed for webhook-based systems like Twilio WhatsApp API

## Tech Stack

Python 3.13
FastAPI
SQLAlchemy
Pydantic
Uvicorn
python-multipart
SQLite

## Project Structure

whatsapp-review-api/
├── main.py        # FastAPI routes
├── database.py    # Database configuration
├── models.py      # SQLAlchemy models
├── schemas.py     # Pydantic schemas
├── README.md
├── .gitignore


## Installation and Running Locally

### Clone the repository
git clone https://github.com/Mudi-Srilakshmi/whatsapp-review-api.git
cd whatsapp-review-api

### Install dependencies
pip install fastapi uvicorn sqlalchemy python-multipart

### Run the Server
uvicorn main:app --reload

## API Documentation

Once the server is running, open:

 ### Swagger UI
 http://127.0.0.1:8000/docs

## API Endpoints

 ### 1.POST /webhook
 Simulates a WhatsApp webhook request.

 ### Request (form-data):

 | Field | Description |
 |------|------------|
| From | Sender phone number |
| Body | WhatsApp message text |

 ### Example Response

 {
   "reply": "Thank you! Your review was received and stored successfully."
 }

 ### 2.GET /api/reviews
 Fetches all saved reviews.

 ### Example Response

 [
   {
     "id": 1,
     "phone": "+919876543210",
     "message": "Awesome product!",
     "created_at": "2025-01-17T10:30:00Z"
   }
 ]

## API Testing Screenshots
 
 ### 1.POST /webhook

 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6ea0a023-0d0f-49c7-a9ad-6889ad2489d4" />

 ### 2.GET /api/reviews

 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/00cd3709-8378-4c2d-92f3-65fa78a3a769" />

## Future Enhancements

JWT Authentication
Docker support
Cloud deployment (Render / AWS / Railway)
Pagination & filtering for reviews
Real Twilio WhatsApp integration

## Author

Srilakshmi Mudi
Python & Backend Developer
FastAPI | Django | SQL

 ### GitHub
 
 https://github.com/Mudi-Srilakshmi

