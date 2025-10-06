from fastapi.testclient import TestClient


from backend.app import app
import sys
import os

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "LangGraph backend" in response.json()["message"]
