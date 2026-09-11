from fastapi import FastAPI, HTTPException

from models import (
    SentimentRequest,
    SentimentResponse,
    BatchSentimentRequest,
    BatchSentimentResponse
)

from sentiment import analyze_sentiment


app = FastAPI(
    title="Sentiment Analysis API",
    description="AI-powered sentiment analysis API",
    version="1.0.0"
)


def validate_word_count(text: str):
    word_count = len(text.split())

    if word_count < 1:
        raise HTTPException(
            status_code=400,
            detail="Text must contain at least 1 word."
        )

    if word_count > 500:
        raise HTTPException(
            status_code=400,
            detail="Text must not exceed 500 words."
        )


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Sentiment Analysis API is running"
    }


@app.post("/api/analyze", response_model=SentimentResponse)
def analyze(request: SentimentRequest):

    validate_word_count(request.text)

    result = analyze_sentiment(request.text)

    return {
        "text": request.text,
        "sentiment": result["sentiment"],
        "confidence": result["confidence"]
    }


@app.post(
    "/api/analyze/batch",
    response_model=BatchSentimentResponse
)
def analyze_batch(request: BatchSentimentRequest):

    results = []

    for text in request.texts:

        validate_word_count(text)

        result = analyze_sentiment(text)

        results.append({
            "text": text,
            "sentiment": result["sentiment"],
            "confidence": result["confidence"]
        })

    return {
        "results": results
    }