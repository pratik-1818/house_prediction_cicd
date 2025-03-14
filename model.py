# train_house_price_model.py

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# ---------------------------
# Step 1: Load California Housing Dataset
# ---------------------------
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='Price')

# ---------------------------
# Step 2: Split into train/test
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# Step 3: Train Linear Regression Model
# ---------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------------------------
# Step 4: Save Model to Pickle File
# ---------------------------
with open('house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained using California Housing dataset and saved as 'house_price_model.pkl'")
