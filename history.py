import streamlit as st
import sqlite3
import pandas as pd


def show_history():

    st.title("📜 Prediction History")

    connection = sqlite3.connect("smart_grid.db")

    df = pd.read_sql_query(
        "SELECT * FROM prediction_history ORDER BY id DESC",
        connection
    )

    connection.close()

    if df.empty:

        st.warning("No prediction history available.")

    else:

        st.success(f"Total Predictions : {len(df)}")

        st.dataframe(
            df,
            width="stretch"
        )