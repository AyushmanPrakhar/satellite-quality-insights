import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Satellite Signal Dashboard", layout="wide")

# Title
st.title("🛰️ Satellite Signal Performance Analysis Dashboard")

st.markdown("Analyze and predict satellite signal strength using elevation angle and ML-based insights.")

# Sidebar Inputs
st.sidebar.header("Input Parameters")

elevation = st.sidebar.slider("Elevation Angle (°)", 0, 90, 45)
satellite_type = st.sidebar.selectbox(
    "Satellite Type",
    ["NOAA", "ISS", "CubeSat", "INSAT/GSAT"]
)

# Simulated ML Logic
base_signal = {
    "NOAA": -45,
    "ISS": -50,
    "CubeSat": -55,
    "INSAT/GSAT": -43
}

signal_strength = base_signal[satellite_type] + (elevation * 0.1)

# Output Section
st.subheader("📊 Predicted Signal Strength")
st.metric(label="Signal Strength (dBm)", value=f"{signal_strength:.2f} dBm")

# Graph Section
st.subheader("📈 Elevation vs Signal Strength")

angles = np.linspace(0, 90, 100)
signals = base_signal[satellite_type] + (angles * 0.1)

fig, ax = plt.subplots()
ax.plot(angles, signals)
ax.set_xlabel("Elevation Angle (°)")
ax.set_ylabel("Signal Strength (dBm)")
ax.set_title(f"{satellite_type} Signal Behavior")

st.pyplot(fig)

# Insights Section
st.subheader("🔍 Insights")

if elevation > 60:
    st.success("High elevation → Strong signal expected")
elif elevation > 20:
    st.warning("Moderate elevation → Stable signal")
else:
    st.error("Low elevation → Weak signal likely")

# Footer
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | ML-Based Satellite Analysis")
