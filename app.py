import streamlit as st

# Page config
st.set_page_config(page_title="Satellite Signal Dashboard", layout="wide")

# Title
st.title("🛰️ Satellite Signal Performance Analysis Dashboard")

# 🔥 Show dashboard immediately (best UX)
st.components.v1.iframe(
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/",
    height=750,
    scrolling=True
)

# Description (after preview)
st.markdown("### 🚀 Live ML-Based Satellite Communication Monitoring System")

st.markdown(
    "This dashboard provides real-time insights into satellite signal performance, "
    "including signal strength, elevation impact, and communication quality analysis."
)

# Button (fallback + full view)
st.link_button(
    "🔗 Open Full App in New Tab",
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/"
)

# Footer
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | ML-Based Satellite Analysis")
