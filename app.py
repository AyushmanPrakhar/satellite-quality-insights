import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Satellite Dashboard", layout="wide")

st.title("🛰️ Satellite Signal Performance Analysis Dashboard")

st.markdown("### 🚀 ML-Based Satellite Communication Monitoring System")

# Input
elevation = st.slider("Elevation Angle (°)", 0, 90, 45)

# ML Prediction
prediction = model.predict([[elevation]])[0]

# Display
st.metric("Predicted Signal Strength", f"{prediction:.2f} dBm")

# Graph
angles = np.linspace(0, 90, 100)
predictions = model.predict(angles.reshape(-1, 1))

fig, ax = plt.subplots()
ax.plot(angles, predictions)
ax.set_xlabel("Elevation Angle")
ax.set_ylabel("Signal Strength (dBm)")
ax.set_title("ML-Based Signal Behavior")

st.pyplot(fig)

st.markdown("---")
st.markdown("Built by Ayushman Prakhar | ML-Based Satellite Analysis")
