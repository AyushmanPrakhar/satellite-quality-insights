import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Satellite Dashboard", layout="wide")

# ---- Load Data ----
df1 = pd.read_csv("signal-strength.csv")
df2 = pd.read_csv("elevation-analysis.csv")
data = pd.concat([df1, df2], ignore_index=True)

# ---- Sidebar ----
st.sidebar.title("⚙️ Filters")

satellite = st.sidebar.selectbox(
    "Satellite",
    ["All"] + list(data["name"].unique())
)

status = st.sidebar.selectbox(
    "Status",
    ["All", "strong", "moderate", "weak"]
)

filtered = data.copy()

if satellite != "All":
    filtered = filtered[filtered["name"] == satellite]

if status != "All":
    filtered = filtered[filtered["status"] == status]

# ---- Title ----
st.title("🛰️ Satellite Signal Performance Dashboard")
st.markdown("### 📡 Interactive Monitoring System")

# ---- KPI CARDS ----
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Signal", f"{filtered['signalStrength'].mean():.2f}")
col2.metric("Best Signal", f"{filtered['signalStrength'].max():.2f}")
col3.metric("Worst Signal", f"{filtered['signalStrength'].min():.2f}")
col4.metric("Satellites", len(filtered))

# ---- TABS ----
tab1, tab2 = st.tabs(["📊 Overview", "📈 Analysis"])

# ================= TAB 1 =================
with tab1:

    st.markdown("## 📊 Signal Strength Overview")

    fig_bar = px.bar(
        filtered,
        x="name",
        y="signalStrength",
        color="status",
        hover_data=["elevation", "successRate"],
        color_discrete_map={
            "strong": "green",
            "moderate": "orange",
            "weak": "red"
        }
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("## 📈 Success Rate")

    fig_line = px.line(
        filtered,
        x="name",
        y="successRate",
        markers=True
    )

    st.plotly_chart(fig_line, use_container_width=True)

# ================= TAB 2 =================
with tab2:

    st.markdown("## 🔍 Elevation vs Signal")

    fig_scatter = px.scatter(
        filtered,
        x="elevation",
        y="signalStrength",
        color="status",
        size="successRate",
        hover_data=["name"],
        color_discrete_map={
            "strong": "green",
            "moderate": "orange",
            "weak": "red"
        }
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

    # Insights
    st.markdown("## 📌 Insights")

    strong = filtered[filtered["status"] == "strong"]
    weak = filtered[filtered["status"] == "weak"]

    st.write(f"🟢 Top Performers: {', '.join(strong['name'].head(3))}")
    st.write(f"🔴 Weak Signals: {', '.join(weak['name'].head(3))}")

# Footer
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | Interactive Satellite Dashboard")
