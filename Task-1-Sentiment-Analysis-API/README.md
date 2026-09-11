# Sentiment Analysis API

## Description

An AI-powered REST API that analyzes English text and classifies its sentiment as positive, negative, or neutral with a confidence score between 0 and 1.

## Features

- Sentiment classification
- Confidence score
- Single text analysis
- Batch text analysis (up to 10 texts)
- Health check endpoint
- English text support

## API Endpoints

- `POST /api/analyze` — Analyze the sentiment of a single text
- `POST /api/analyze/batch` — Analyze multiple texts
- `GET /api/health` — Check API status

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt2. Start the API
python -m uvicorn app.main:app --reload
*****3. Open the API**
http://127.0.0.1:8000
**API Documentation**
http://127.0.0.1:8000/docs
**Technologies Used**
Python
FastAPI
Pydantic
Uvicorn
Sentiment Analysis
**Project Structure**    
Task-1-Sentiment-Analysis-API/
│
├── app/
│   ├── main.py
│   └── models.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
└── README.md
**Author**

**Tanzeela Nawaz**
