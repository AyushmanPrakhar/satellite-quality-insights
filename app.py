import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Satellite Dashboard", layout="wide")

# -----------------------------
# 📊 DATA (Your 30 Satellites)
# -----------------------------
data = pd.DataFrame({
    "name": [
        "NOAA-18","NOAA-19","METEOR-M2","METEOR-M2-2","ISS","FUNCUBE-1",
        "LILACSAT-2","CAS-4A","CAS-4B","PEGASUS","NEXUS","VYSAT",
        "LUCKY-7","DELFIN-C3","UVSQ-SAT","ALTO-1","FOX-1B","FOX-1D",
        "GOMX-1","STRAND-1","DUCHIFAT-1","LAPAN-A2","NUSAT-1",
        "SPROUT","CUTE-1.7+APDII","SWISSCUBE","ATMCUBE-1","BEESAT-9",
        "TEVEL-2","PLANETUM-1"
    ],
    "signal": [
        -42,-44,-41,-43,-40,-45,
        -46,-48,-47,-49,-44,-42,
        -50,-41,-43,-45,-46,-47,
        -48,-49,-50,-42,-43,
        -55,-56,-54,-53,-57,
        -59,-52
    ],
    "successRate": [
        92,90,85,88,95,76,
        74,87,85,70,92,80,
        65,94,89,78,93,90,
        69,63,62,95,87,
        61,75,79,93,90,
        58,94
    ]
})

# Remove duplicates (safety)
data = data.drop_duplicates(subset=["name"])

# -----------------------------
# 🎯 STATUS CLASSIFICATION
# -----------------------------
def classify(signal):
    if signal >= -45:
        return "Strong"
    elif signal >= -50:
        return "Moderate"
    else:
        return "Weak"

data["status"] = data["signal"].apply(classify)

# -----------------------------
# 🎛 FILTERS
# -----------------------------
st.sidebar.header("🔧 Filters")

selected_status = st.sidebar.selectbox(
    "Filter by Status",
    ["All", "Strong", "Moderate", "Weak"]
)

if selected_status != "All":
    filtered = data[data["status"] == selected_status]
else:
    filtered = data.copy()

# -----------------------------
# 🧾 TITLE
# -----------------------------
st.title("🛰 Satellite Signal Performance Analysis Dashboard")
st.markdown("🚀 ML-Based Satellite Communication Monitoring System")

# -----------------------------
# 📊 KPIs
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Signal", round(filtered["signal"].mean(), 2))
col2.metric("Best Signal", filtered["signal"].max())
col3.metric("Worst Signal", filtered["signal"].min())
col4.metric("Satellites", filtered["name"].nunique())  # ✅ FIXED COUNT

# -----------------------------
# 📊 SIGNAL STRENGTH BAR CHART
# -----------------------------
st.markdown("## 📊 Signal Strength Overview")

color_map = {
    "Strong": "green",
    "Moderate": "orange",
    "Weak": "red"
}

fig_bar = px.bar(
    filtered,
    x="name",
    y="signal",
    color="status",
    color_discrete_map=color_map,
    title="Signal Strength by Satellite"
)

fig_bar.update_layout(template="plotly_dark")

st.plotly_chart(fig_bar, use_container_width=True)

# -----------------------------
# 📈 SUCCESS RATE GRAPH
# -----------------------------
st.markdown("## 📈 Success Rate Analysis")

# Remove duplicates again (safety)
unique_data = filtered.drop_duplicates(subset=["name"])

# Sort for better trend readability
unique_data = unique_data.sort_values(by="successRate")

x = unique_data["name"]
y = unique_data["successRate"]

# Trend line
z = np.polyfit(range(len(y)), y, 1)
trend = np.poly1d(z)
trend_y = trend(range(len(y)))

fig = go.Figure()

# Actual data
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines+markers",
    name="Success Rate",
    line=dict(color="#00BFFF", width=3),
    marker=dict(size=6)
))

# Trend line (CLEAR + LABELED)
fig.add_trace(go.Scatter(
    x=x,
    y=trend_y,
    mode="lines",
    name="Trend Line (Overall Direction)",
    line=dict(color="red", width=4, dash="dash")
))

fig.update_layout(
    xaxis_title="Satellites (Sorted by Performance)",
    yaxis_title="Success Rate (%)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 🧠 INSIGHTS SECTION
# -----------------------------
st.markdown("## 🧠 Insights")

best_sat = filtered.loc[filtered["successRate"].idxmax()]["name"]
worst_sat = filtered.loc[filtered["successRate"].idxmin()]["name"]

st.info(f"🏆 Best Performing Satellite: {best_sat}")
st.warning(f"⚠️ Worst Performing Satellite: {worst_sat}")

# -----------------------------
# 🧾 FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | Satellite Analytics Dashboard")
