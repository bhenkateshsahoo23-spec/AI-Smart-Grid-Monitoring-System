import streamlit as st
import sqlite3
import pandas as pd


def show_report():

    st.title("📄 Reports")

    connection = sqlite3.connect("smart_grid.db")

    df = pd.read_sql_query(
        "SELECT * FROM prediction_history",
        connection
    )

    connection.close()

    if df.empty:

        st.warning("No prediction history available.")

    else:

        st.success(f"Total Records : {len(df)}")

        st.dataframe(
            df,
            width="stretch"
        )

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv"
        )