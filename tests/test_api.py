from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_safe_url():
    response = client.get("/urlinfo/1/google.com/search")
    assert response.status_code == 200
    assert response.json()["malicious"] is False

def test_malicious_url():
    response = client.get("/urlinfo/1/bad.com/malware")
    assert response.status_code == 200
    assert response.json()["malicious"] is True