from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_analyze_positive():
    response = client.post(
        "/api/analyze",
        json={
            "text": "I love this amazing product!"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["sentiment"] in [
        "positive",
        "negative",
        "neutral"
    ]

    assert 0 <= data["confidence"] <= 1


def test_analyze_negative():
    response = client.post(
        "/api/analyze",
        json={
            "text": "This is a terrible experience."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["sentiment"] in [
        "positive",
        "negative",
        "neutral"
    ]


def test_analyze_neutral():
    response = client.post(
        "/api/analyze",
        json={
            "text": "The meeting is scheduled for Monday."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["sentiment"] in [
        "positive",
        "negative",
        "neutral"
    ]


def test_batch_analyze():
    response = client.post(
        "/api/analyze/batch",
        json={
            "texts": [
                "I love this!",
                "This is terrible.",
                "The weather is okay."
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert "count" in data
    assert data["count"] == 3


def test_batch_limit():
    response = client.post(
        "/api/analyze/batch",
        json={
            "texts": [
                "Test text"
            ] * 11
        }
    )

    assert response.status_code == 400
    