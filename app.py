import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Satellite Signal Dashboard", layout="wide")

# Title
st.title("🛰️ Satellite Signal Performance Analysis Dashboard")

st.markdown("### 🚀 ML-Based Satellite Communication Monitoring System")

# Sidebar
st.sidebar.header("🔧 Input Parameters")

satellite = st.sidebar.selectbox(
    "Satellite Type",
    ["NOAA", "ISS", "CubeSat", "INSAT/GSAT"]
)

elevation = st.sidebar.slider("Elevation Angle (°)", 0, 90, 45)

# Base signal logic
base_signal = {
    "NOAA": -45,
    "ISS": -50,
    "CubeSat": -55,
    "INSAT/GSAT": -43
}

signal = base_signal[satellite] + (elevation * 0.12)

# KPI Section
col1, col2, col3 = st.columns(3)

col1.metric("Signal Strength", f"{signal:.2f} dBm")
col2.metric("Elevation", f"{elevation}°")
col3.metric("Satellite", satellite)

# Graph
st.markdown("## 📈 Signal Analysis")

angles = np.linspace(0, 90, 100)
signals = base_signal[satellite] + (angles * 0.12)

fig, ax = plt.subplots()
ax.plot(angles, signals)
ax.set_xlabel("Elevation Angle")
ax.set_ylabel("Signal Strength (dBm)")
ax.set_title(f"{satellite} Signal Behavior")

st.pyplot(fig)

# Insights
st.markdown("## 🔍 Insights")

if elevation > 60:
    st.success("High elevation → Optimal signal performance")
elif elevation > 20:
    st.warning("Moderate elevation → Stable signal range")
else:
    st.error("Low elevation → Weak signal expected")

# Footer
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | ML-Based Satellite Analysis")
