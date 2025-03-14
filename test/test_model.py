from fastapi.testclient import TestClient
from app import main # If your app is inside 'app/main.py', change this to from app.main import app

client = TestClient(main)

# ✅ Test for the root/home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to House Price Prediction API"

# ✅ Test for the prediction endpoint
def test_predict():
    sample_input = {
        "MedInc": 8.3252,
        "HouseAge": 41,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert "predicted_price (in 100,000s USD)" in response.json()
