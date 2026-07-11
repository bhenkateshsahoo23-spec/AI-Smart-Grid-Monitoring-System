import streamlit as st

from simulator import get_live_data
from ai_engine import predict_live_fault
from streamlit_autorefresh import st_autorefresh


def show_alarm():

    st_autorefresh(interval=5000, key="alarm_refresh")

    live = get_live_data()

    fault, confidence = predict_live_fault(live)

    st.title("🚨 Smart Grid Alarm Center")

    st.caption("Industry 4.0 | Real-Time Alarm Monitoring")

    st.divider()

    voltage = live["voltage"]
    current = live["current"]
    frequency = live["frequency"]
    temperature = live["temperature"]

    severity = {
        "Normal": "LOW",
        "LG Fault": "MEDIUM",
        "LL Fault": "MEDIUM",
        "LLG Fault": "HIGH",
        "LLL Fault": "CRITICAL"
    }

    location = {
        "Normal": "Healthy Grid",
        "LG Fault": "Transmission Line",
        "LL Fault": "Distribution Line",
        "LLG Fault": "Transformer",
        "LLL Fault": "Main Bus"
    }

    recommendation = {
        "Normal": "No Action Required",
        "LG Fault": "Inspect Ground Insulation",
        "LL Fault": "Inspect Phase Conductors",
        "LLG Fault": "Check Protection Relay",
        "LLL Fault": "Emergency Shutdown Immediately"
    }

    c1, c2 = st.columns(2)

    if fault == "Normal":

        c1.success("🟢 GRID HEALTHY")

    elif severity[fault] == "MEDIUM":

        c1.warning("🟡 WARNING")

    else:

        c1.error("🔴 CRITICAL")

    c2.metric("Confidence", f"{confidence:.2f}%")

    st.divider()

    st.subheader("🚨 Current Alarm")

    st.error(f"Fault Type : {fault}")

    st.info(f"Severity : {severity[fault]}")

    st.info(f"Location : {location[fault]}")

    st.warning(f"Recommended Action : {recommendation[fault]}")

    st.divider()

    st.subheader("⚡ Live Electrical Parameters")

    a1, a2, a3 = st.columns(3)

    a1.metric("Voltage", f"{voltage} V")

    a2.metric("Current", f"{current} A")

    a3.metric("Frequency", f"{frequency} Hz")

    b1, b2 = st.columns(2)

    b1.metric("Temperature", f"{temperature} °C")

    b2.metric("Power Factor", live["power_factor"])

    st.divider()

    if fault == "Normal":

        st.success("✔ All equipment operating normally.")

    elif fault == "LG Fault":

        st.warning("Ground fault detected. Dispatch maintenance team.")

    elif fault == "LL Fault":

        st.warning("Phase-to-phase fault detected.")

    elif fault == "LLG Fault":

        st.error("High priority fault. Check transformer and relays.")

    else:

        st.error("Critical three-phase fault! Immediate shutdown required.")