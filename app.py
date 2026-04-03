import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from services.parser import load_data
from services.anomaly import detect_anomalies
from services.analytics import moving_average, health_score, generate_insights
from utils.helpers import get_stations, filter_station

st.set_page_config(page_title="Telemetry Dashboard", layout="wide")

st.title("⚡ Smart Telemetry Monitoring System")

# Sidebar
st.sidebar.title("⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)

    stations = get_stations(df)
    selected_station = st.sidebar.selectbox("Select Station", stations)

    filtered_df = filter_station(df, selected_station)

    # Header
    st.header(f"📍 Station {selected_station}")

    latest = filtered_df.iloc[-1]
    prev = filtered_df.iloc[-2] if len(filtered_df) > 1 else latest

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Voltage", f"{latest['voltage']:.2f}", f"{latest['voltage'] - prev['voltage']:.2f}")
    col2.metric("Load", f"{latest['load']:.2f}", f"{latest['load'] - prev['load']:.2f}")
    col3.metric("Temperature", f"{latest['temperature']:.2f}", f"{latest['temperature'] - prev['temperature']:.2f}")

    score = health_score(filtered_df)
    col4.metric("Health Score", f"{score}/100")

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📊 Trends", "🚨 Anomalies", "🧠 Insights", "📄 Data", "🗺️ Map"]
    )

    # 📊 Trends (Plotly)
    with tab1:
        st.subheader("📊 Interactive Trends")

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=filtered_df["timestamp"],
            y=filtered_df["voltage"],
            mode='lines',
            name='Voltage'
        ))

        fig.add_trace(go.Scatter(
            x=filtered_df["timestamp"],
            y=moving_average(filtered_df, "voltage"),
            mode='lines',
            name='Voltage MA',
            line=dict(dash='dash')
        ))

        fig.add_trace(go.Scatter(
            x=filtered_df["timestamp"],
            y=filtered_df["temperature"],
            mode='lines',
            name='Temperature'
        ))

        fig.add_trace(go.Scatter(
            x=filtered_df["timestamp"],
            y=filtered_df["load"],
            mode='lines',
            name='Load'
        ))

        fig.update_layout(
            height=500,
            hovermode="x unified",
            xaxis_title="Time",
            yaxis_title="Values"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 🚨 Anomalies
    with tab2:
        anomalies = detect_anomalies(filtered_df)

        if anomalies:
            st.error(f"{len(anomalies)} anomalies detected")

            for a in anomalies:
                st.warning(
                    f"{a['timestamp']} → {a['issues']} "
                    f"(V:{a['voltage']}, L:{a['load']}, T:{a['temperature']})"
                )
        else:
            st.success("No anomalies detected")
            
    # 🧠 Insights
    with tab3:
        insights = generate_insights(filtered_df)

        if insights:
            for i in insights:
                st.warning(i)
        else:
            st.info("System stable")

    # 📄 Data
    with tab4:
        st.dataframe(filtered_df)

    # 🗺️ Map
    with tab5:
        st.subheader("🗺️ Smart Station Map")

        latest_points = df.sort_values("timestamp").groupby("station_id").tail(1)

        def get_status(row):
            if row["temperature"] > 80 or row["load"] > 90:
                return "Critical"
            elif row["voltage"] < 180 or row["voltage"] > 240:
                return "Warning"
            else:
                return "Normal"

        latest_points["status"] = latest_points.apply(get_status, axis=1)

        fig = px.scatter_mapbox(
            latest_points,
            lat="lat",
            lon="lon",
            color="status",
            hover_name="station_id",
            hover_data=["voltage", "load", "temperature"],
            zoom=10,
            height=500
        )

        fig.update_layout(mapbox_style="open-street-map")

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Upload a telemetry CSV file to begin.")