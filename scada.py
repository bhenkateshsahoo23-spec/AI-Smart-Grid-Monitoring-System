import streamlit as st

from simulator import get_live_data
from ai_engine import predict_live_fault
from streamlit_autorefresh import st_autorefresh


def show_scada():

    # Refresh every 5 seconds
    st_autorefresh(interval=5000, key="scada_refresh")

    # Live Data
    live = get_live_data()

    # AI Prediction
    fault, confidence = predict_live_fault(live)

    st.title("⚡ Smart Grid SCADA Mimic Panel")

    st.caption("Industry 4.0 | AI Based Live Monitoring")

    st.divider()

    # Live Parameters
    c1, c2, c3 = st.columns(3)

    c1.metric("Voltage", f"{live['voltage']} V")
    c2.metric("Current", f"{live['current']} A")
    c3.metric("Frequency", f"{live['frequency']} Hz")

    c4, c5, c6 = st.columns(3)

    c4.metric("Power", f"{live['power']} kW")
    c5.metric("Power Factor", live["power_factor"])
    c6.metric("Temperature", f"{live['temperature']} °C")

    st.divider()

    green = "🟢"
    yellow = "🟡"
    red = "🔴"

    generator = green
    transformer = green
    line = green
    breaker = green
    bus = green
    load = green

    # AI Controlled SCADA

    if fault == "LG Fault":

        line = red
        breaker = red

    elif fault == "LL Fault":

        line = yellow
        breaker = yellow

    elif fault == "LLG Fault":

        transformer = yellow
        line = red
        breaker = red

    elif fault == "LLL Fault":

        generator = red
        transformer = red
        line = red
        breaker = red
        bus = red
        load = red

    st.subheader("⚡ Live SCADA Mimic")

    st.markdown(f"""

## {generator} Generator

⬇

## {transformer} Step-Up Transformer

⬇

## {line} Transmission Line

⬇

## {breaker} Circuit Breaker

⬇

## {bus} Distribution Bus

⬇

## {load} Industrial Load

""")

    st.divider()

    st.subheader("🤖 AI Prediction")

    a1, a2, a3 = st.columns(3)

    a1.metric("Fault", fault)
    a2.metric("Confidence", f"{confidence:.2f}%")

    if fault == "Normal":
        a3.success("🟢 HEALTHY")
    else:
        a3.error("🔴 FAULT")

    st.divider()

    recommendation = {

        "Normal": "No Action Required",

        "LG Fault": "Inspect Ground Insulation",

        "LL Fault": "Inspect Phase Conductors",

        "LLG Fault": "Check Protection Relay",

        "LLL Fault": "Emergency Shutdown"

    }

    severity = {

        "Normal": "LOW",

        "LG Fault": "MEDIUM",

        "LL Fault": "MEDIUM",

        "LLG Fault": "HIGH",

        "LLL Fault": "CRITICAL"

    }

    st.subheader("🚨 Alarm Panel")

    if fault == "Normal":

        st.success("✅ Grid Operating Normally")

    else:

        st.error(f"⚠ Fault Detected : {fault}")

    st.warning(f"Recommendation : {recommendation[fault]}")

    st.info(f"Severity : {severity[fault]}")