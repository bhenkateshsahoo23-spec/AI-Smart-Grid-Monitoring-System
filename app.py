import streamlit as st
from datetime import datetime
import os
# ==========================================================
# IMPORT PAGES
# ==========================================================

from home import show_home
from dashboard import show_dashboard
from scada import show_scada
from sld import show_sld
from analytics import show_analytics
from predictor import predict_fault
from history import show_history
from report import show_report
from alarm import show_alarm


from database import (
    create_database,
    save_prediction
)

# ==========================================================
# DATABASE
# ==========================================================

create_database()

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
 
    page_title="⚡ AI Smart Grid Control Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    css_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "style.css"
    )

    if os.path.exists(css_path):

        with open(css_path) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()



# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("⚡ AI SMART GRID")
st.sidebar.caption("Control Center")

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "📡 Control Center",

        "🏭 SCADA Panel",

        "⚡ Single Line Diagram",

        "🤖 AI Prediction",

        "📊 Analytics",

        "📜 Prediction History",

        "📄 Reports",

        "🚨 Alarm Center"

    ]

)

st.sidebar.markdown("---")

st.sidebar.success("🟢 SYSTEM ONLINE")

st.sidebar.info("🤖 AI MODEL\n\nRandom Forest v1.0")

st.sidebar.info("🗄 DATABASE\n\nSQLite Connected")

st.sidebar.info("⏱ REFRESH RATE\n\nEvery 5 Seconds")

st.sidebar.info(
    f"🕒 LAST UPDATE\n\n{datetime.now().strftime('%H:%M:%S')}"
)

st.sidebar.markdown("---")

st.sidebar.markdown("## 👨‍💻 Developer")

st.sidebar.info("""
**Name:** Bhenkateswar Sahoo

**Department:** Electrical Engineering

**College:** IGIT Sarang

**Project:** AI Smart Grid Monitoring & Fault Analysis

**Email:** Bhenkateshsahoo23@gmail.com

**Phone Number:** 7735232196

**Technology:** Python | Streamlit | Random Forest | SQLite

**Year:** 2026
""")




# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    show_home()

# ==========================================================
# CONTROL CENTER
# ==========================================================

elif page == "📡 Control Center":

    show_dashboard()

# ==========================================================
# SCADA PANEL
# ==========================================================

elif page == "🏭 SCADA Panel":

    show_scada()

# ==========================================================
# SINGLE LINE DIAGRAM
# ==========================================================

elif page == "⚡ Single Line Diagram":

    show_sld()

# ==========================================================
# AI PREDICTION
# ==========================================================

elif page == "🤖 AI Prediction":

    st.title("🤖 AI Smart Grid Fault Prediction")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        voltage = st.number_input(
            "Voltage (V)",
            min_value=0.0,
            value=230.0
        )

        current = st.number_input(
            "Current (A)",
            min_value=0.0,
            value=5.0
        )

        frequency = st.number_input(
            "Frequency (Hz)",
            min_value=0.0,
            value=50.0
        )

    with col2:

        power = st.number_input(
            "Power (kW)",
            min_value=0.0,
            value=1.20
        )

        power_factor = st.number_input(
            "Power Factor",
            min_value=0.0,
            max_value=1.0,
            value=0.98
        )

        temperature = st.number_input(
            "Temperature (°C)",
            value=30.0
        )

    st.markdown("---")

    if st.button("⚡ Predict Fault"):

        fault, confidence = predict_fault(
            voltage,
            current,
            frequency,
            power,
            power_factor,
            temperature
        )

        current_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        save_prediction(
            current_time,
            voltage,
            current,
            frequency,
            power,
            power_factor,
            temperature,
            fault,
            confidence
        )

        st.success(f"⚡ Fault Type : {fault}")

        st.info(
            f"🎯 Confidence : {confidence:.2f}%"
        )

        recommendation = {

            "Normal": "✅ No Action Required",

            "LG Fault": "⚠ Inspect Ground Insulation",

            "LL Fault": "⚠ Inspect Phase Conductors",

            "LLG Fault": "⚠ Check Relay Coordination",

            "LLL Fault": "🚨 Emergency Shutdown Required"

        }

        severity = {

            "Normal": "Low",

            "LG Fault": "Medium",

            "LL Fault": "Medium",

            "LLG Fault": "High",

            "LLL Fault": "Critical"

        }

        st.subheader("AI Recommendation")

        st.warning(
            recommendation.get(
                fault,
                "Contact Maintenance Team"
            )
        )

        st.metric(
            "Severity",
            severity[fault]
        )

        st.success(
            "Prediction Saved Successfully"
        )

# ==========================================================
# ANALYTICS
# ==========================================================

elif page == "📊 Analytics":

    show_analytics()

# ==========================================================
# HISTORY
# ==========================================================

elif page == "📜 Prediction History":

    show_history()

# ==========================================================
# REPORTS
# ==========================================================

elif page == "📄 Reports":

    show_report()

# ==========================================================
# ALARM CENTER
# ==========================================================

elif page == "🚨 Alarm Center":

    show_alarm()

# =======================================
# FOOTER
# =======================================

st.markdown("---")

st.caption("""
© 2026 AI Smart Grid Monitoring Platform

Developed by Bhenkateswar Sahoo

Electrical Engineering | IGIT Sarang

Powered by Python • Streamlit • Random Forest • SQLite
""")