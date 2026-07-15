import os
import streamlit as st
import pandas as pd
import plotly.express as px


def show_analytics():

    st.title("📊 Smart Grid Analytics Dashboard")

    # -----------------------------------------
    # Load Dataset
    # -----------------------------------------
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_path = os.path.join(
        BASE_DIR,
        "data",
        "smart_grid_dataset.csv"
    )

    df = pd.read_csv(csv_path)

    # -----------------------------------------
    # Dataset Preview
    # -----------------------------------------
    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------------
    # Charts
    # -----------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            df,
            x="Fault Type",
            color="Fault Type",
            title="Fault Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.scatter(
            df,
            x="Voltage(V)",
            y="Current(A)",
            color="Fault Type",
            title="Voltage vs Current"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        fig = px.box(
            df,
            x="Fault Type",
            y="Temperature(C)",
            color="Fault Type",
            title="Temperature Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col4:

        fig = px.scatter(
            df,
            x="Power(kW)",
            y="Power Factor",
            color="Fault Type",
            title="Power vs Power Factor"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("Dataset Statistics")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )