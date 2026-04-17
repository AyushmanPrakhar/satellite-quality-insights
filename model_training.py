import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample dataset (you can expand later)
data = pd.DataFrame({
    "Elevation": [5, 10, 20, 30, 40, 50, 60, 70, 80, 90],
    "Signal": [-56, -54, -52, -50, -48, -46, -45, -44, -43, -42]
})

# Features & target
X = data[["Elevation"]]
y = data["Signal"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")
