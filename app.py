import streamlit as st

st.set_page_config(page_title="Satellite Dashboard", layout="wide")

st.title("🛰️ Satellite Signal Performance Analysis Dashboard")
st.markdown("### 🚀 Live Satellite Monitoring System")

# Button
st.link_button(
    "🚀 Open Full Interactive Dashboard",
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/"
)

# Embedded view (like preview)
st.markdown("## 📊 Live Dashboard Preview")

st.components.v1.iframe(
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/",
    height=800,
    scrolling=True
)

st.markdown("---")
st.markdown("Built by Ayushman Prakhar | Real-Time Satellite Dashboard")
