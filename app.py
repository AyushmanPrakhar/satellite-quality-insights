import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Satellite Dashboard", layout="wide")

# Title
st.title("🛰️ Satellite Communication Quality Dashboard")
st.markdown("Mission-control monitoring of satellite communication quality")

# Sidebar Filters
st.sidebar.header("🔧 Filters")

satellite = st.sidebar.selectbox(
    "Satellite Name",
    ["All Satellites", "NOAA", "ISS", "CubeSat", "INSAT/GSAT"]
)

status = st.sidebar.selectbox(
    "Status",
    ["All Statuses", "Strong", "Moderate", "Weak"]
)

# Simulated dataset (like your Replit app)
data = pd.DataFrame({
    "Satellite": ["NOAA", "ISS", "CubeSat", "INSAT/GSAT"],
    "Signal": [-45, -50, -55, -43],
    "Elevation": [70, 50, 20, 80]
})

# Filter logic
if satellite != "All Satellites":
    data = data[data["Satellite"] == satellite]

# Tabs
tab1, tab2 = st.tabs(["📊 Overview", "📈 Analysis"])

# ---------------- OVERVIEW ----------------
with tab1:

    st.subheader("Overview Metrics")

    avg_signal = data["Signal"].mean()
    best_signal = data["Signal"].max()
    worst_signal = data["Signal"].min()
    total_sat = len(data)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg Signal Strength", f"{avg_signal:.2f} dBm")
    col2.metric("Best Signal", f"{best_signal} dBm")
    col3.metric("Worst Signal", f"{worst_signal} dBm")
    col4.metric("Total Satellites", total_sat)

# ---------------- ANALYSIS ----------------
with tab2:

    st.subheader("Signal Analysis")

    fig, ax = plt.subplots()
    ax.scatter(data["Elevation"], data["Signal"])

    ax.set_xlabel("Elevation Angle")
    ax.set_ylabel("Signal Strength (dBm)")
    ax.set_title("Elevation vs Signal Strength")

    st.pyplot(fig)
