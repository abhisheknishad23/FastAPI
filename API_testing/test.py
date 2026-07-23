from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    #chec status code 
    assert response.status_code == 200
    #check response data
    assert response.json()=={"message":"hello modi "}

def test_add():
    response = client.get("/add?a=3&b=4")

    assert response.status_code == 200
    assert response.json() == {"result":7}