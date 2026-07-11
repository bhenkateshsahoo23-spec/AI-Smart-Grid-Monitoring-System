import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

from simulator import get_live_data
from streamlit_autorefresh import st_autorefresh


# -----------------------------
# Load CSS
# -----------------------------

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


# -----------------------------
# Home Page
# -----------------------------

def show_home():

    # Auto Refresh Every 5 Seconds
    st_autorefresh(
        interval=5000,
        key="home_refresh"
    )

    # Live Sensor Data
    live = get_live_data()

    voltage = live["voltage"]
    current = live["current"]
    frequency = live["frequency"]
    power = live["power"]
    power_factor = live["power_factor"]
    temperature = live["temperature"]

    st.title("⚡ AI Smart Grid Monitoring Platform")

    st.caption(
        "Industry 4.0 | Machine Learning | Predictive Analytics"
    )

    # -----------------------------
    # Read Database
    # -----------------------------

    connection = sqlite3.connect("smart_grid.db")

    try:

        df = pd.read_sql_query(
            "SELECT * FROM prediction_history",
            connection
        )

    except:

        df = pd.DataFrame()

    connection.close()

    total_predictions = len(df)

    if total_predictions > 0:

        total_faults = len(
            df[df["fault"] != "Normal"]
        )

        average_confidence = round(
            df["confidence"].mean(),
            2
        )

        grid_health = round(
            100 - (total_faults / total_predictions) * 100,
            2
        )

    else:

        total_faults = 0
        average_confidence = 100
        grid_health = 100

    # -----------------------------
    # KPI Cards
    # -----------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Predictions",
        total_predictions
    )

    c2.metric(
        "Faults",
        total_faults
    )

    c3.metric(
        "Grid Health",
        f"{grid_health}%"
    )

    c4.metric(
        "AI Confidence",
        f"{average_confidence}%"
    )

    st.divider()

    # -----------------------------
    # Charts
    # -----------------------------

    if total_predictions > 0:

        left, right = st.columns([2, 1])

        with left:

            fig = px.histogram(
                df,
                x="fault",
                color="fault",
                title="Fault Distribution"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

        with right:

            st.subheader("⚡ Live Grid Status")

            st.success(f"Voltage : {voltage} V")

            st.success(f"Current : {current} A")

            st.success(f"Frequency : {frequency} Hz")

            st.info(f"Power : {power} kW")

            st.success(f"Power Factor : {power_factor}")

            st.warning(f"Temperature : {temperature} °C")

        st.divider()

        fig = px.line(
            df,
            y="confidence",
            title="Prediction Confidence Trend"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    else:

        st.info("No Prediction History Available")

    st.divider()

    st.subheader("📋 Project Overview")

    st.write("""
This platform provides:

- 🤖 AI-Based Fault Detection
- ⚡ Smart Grid Monitoring
- 📊 Interactive Analytics
- 🗄 SQLite Database
- 📜 Prediction History
- 📄 Report Generation
- 📈 Machine Learning Dashboard
""")