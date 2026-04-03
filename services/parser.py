import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)

    df.columns = df.columns.str.strip()

    required = ["timestamp", "station_id", "voltage", "load", "temperature", "lat", "lon"]

    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df = df.sort_values("timestamp")

    return df