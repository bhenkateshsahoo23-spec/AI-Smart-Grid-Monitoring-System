import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📊 Smart Grid Analytics Dashboard")

    df = pd.read_csv("data/raw/smart_grid_dataset.csv")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            df,
            x="Fault Type",
            color="Fault Type",
            title="Fault Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            df,
            x="Voltage(V)",
            y="Current(A)",
            color="Fault Type",
            title="Voltage vs Current"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    fig = px.line(
        df.head(200),
        y="Voltage(V)",
        title="Voltage Trend"
    )

    st.plotly_chart(fig, use_container_width=True)