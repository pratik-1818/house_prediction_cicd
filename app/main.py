from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the trained model
with open(r"house_price_model.pkl", "rb") as f:
    model = pickle.load(f)
print("✅ Model loaded successfully")  # Add this line


# Initialize FastAPI app
app = FastAPI(title="House Price Prediction API", version="1.0")

# Request body schema using Pydantic
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"message": "Welcome to House Price Prediction API"}

# Prediction endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                            features.AveBedrms, features.Population,
                            features.AveOccup, features.Latitude, features.Longitude]])
    prediction = model.predict(input_data)[0]
    return {"predicted_price (in 100,000s USD)": round(prediction, 2)}
