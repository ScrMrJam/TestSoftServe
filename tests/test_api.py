from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_safe_url():
    url = "/urlinfo/1/google.com/search"
    response = client.get(url)
    print(f"Analizando URL segura: {url}")
    print(f"Respuesta: {response.json()}")
    assert response.status_code == 200
    assert response.json()["malicious"] is False

def test_malicious_url():
    url = "/urlinfo/1/bad.com/malware"
    response = client.get(url)
    print(f"Analizando URL maliciosa: {url}")
    print(f"Respuesta: {response.json()}")
    assert response.status_code == 200
    assert response.json()["malicious"] is True

def test_malicious_url_evil():
    url = "/urlinfo/1/evil.com/phishing"
    response = client.get(url)
    print(f"Analizando URL maliciosa: {url}")
    print(f"Respuesta: {response.json()}")
    assert response.status_code == 200
    assert response.json()["malicious"] is True
