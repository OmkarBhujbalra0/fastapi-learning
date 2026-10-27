from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get('/')

    assert response.status_code == 200

    assert response.json() == {"message":"Welcome to API"}

def test_add():
    response = client.get('/addition?a=4&b=3')

    assert response.status_code == 200

    assert response.json() == 7