import streamlit as st
from graphviz import Digraph

from simulator import get_live_data
from ai_engine import predict_live_fault
from streamlit_autorefresh import st_autorefresh


def show_sld():

    # Refresh every 5 seconds
    st_autorefresh(interval=5000, key="sld_refresh")

    # Live Sensor Data
    live = get_live_data()

    # AI Prediction
    fault, confidence = predict_live_fault(live)

    st.title("⚡ Smart Grid Single Line Diagram")

    st.caption("Industry 4.0 | AI Based Electrical Monitoring")

    st.divider()

    graph = Digraph()

    graph.attr(rankdir="TB")

    graph.attr(
        "node",
        shape="box",
        style="filled",
        fontsize="12"
    )

    green = "#00C853"
    yellow = "#FFC107"
    red = "#F44336"

    generator = green
    transformer = green
    line = green
    breaker = green
    bus = green
    load = green

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

    graph.node("G", "Generator", fillcolor=generator)

    graph.node(
        "T",
        "Step-Up Transformer",
        fillcolor=transformer
    )

    graph.node(
        "L",
        "Transmission Line",
        fillcolor=line
    )

    graph.node(
        "CB",
        "Circuit Breaker",
        fillcolor=breaker
    )

    graph.node(
        "B",
        "Distribution Bus",
        fillcolor=bus
    )

    graph.node(
        "LOAD",
        "Industrial Load",
        fillcolor=load
    )

    graph.edge("G", "T")
    graph.edge("T", "L")
    graph.edge("L", "CB")
    graph.edge("CB", "B")
    graph.edge("B", "LOAD")

    st.graphviz_chart(graph)

    st.divider()

    st.subheader("🤖 AI Prediction")

    c1, c2, c3 = st.columns(3)

    c1.metric("Fault", fault)
    c2.metric("Confidence", f"{confidence:.2f}%")

    if fault == "Normal":
        c3.success("🟢 HEALTHY")
    else:
        c3.error("🔴 FAULT")

    st.divider()

    recommendation = {

        "Normal": "No Action Required",

        "LG Fault": "Inspect Ground Insulation",

        "LL Fault": "Inspect Phase Conductors",

        "LLG Fault": "Check Protection Relay",

        "LLL Fault": "Emergency Shutdown Required"

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

        st.success("Grid Operating Normally")

    else:

        st.error(f"Fault Detected : {fault}")

    st.warning(f"Recommendation : {recommendation[fault]}")

    st.info(f"Severity : {severity[fault]}")

    st.divider()

    st.subheader("⚡ Live Electrical Parameters")

    p1, p2, p3 = st.columns(3)

    p1.metric("Voltage", f"{live['voltage']} V")
    p2.metric("Current", f"{live['current']} A")
    p3.metric("Frequency", f"{live['frequency']} Hz")

    p4, p5, p6 = st.columns(3)

    p4.metric("Power", f"{live['power']} kW")
    p5.metric("Power Factor", live["power_factor"])
    p6.metric("Temperature", f"{live['temperature']} °C")