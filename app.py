import streamlit as st

st.set_page_config(page_title="Satellite Signal Dashboard", layout="wide")

# Title
st.title("🛰️ Satellite Signal Performance Analysis Dashboard")

st.markdown("### 🚀 Live ML-Based Satellite Communication Monitoring System")

# Live App Section
st.markdown("## 🌐 Live Application")

# Button (always works)
st.link_button(
    "🚀 Open Full App",
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/"
)

# Try embedding (may or may not work)
st.markdown("### 📺 App Preview")

st.components.v1.iframe(
    "https://satellite-quality-insights--ayushmanprakhar.replit.app/",
    height=700,
    scrolling=True
)

# Footer
st.markdown("---")
st.markdown("Built by Ayushman Prakhar | ML-Based Satellite Analysis")
