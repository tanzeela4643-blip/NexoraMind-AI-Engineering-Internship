from pydantic import BaseModel, Field
from typing import List


class SentimentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="English text between 1 and 500 words"
    )


class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float


class BatchSentimentRequest(BaseModel):
    texts: List[str] = Field(
        ...,
        min_length=1,
        max_length=10,
        description="List of up to 10 texts"
    )


class BatchSentimentResponse(BaseModel):
    results: List[SentimentResponse]