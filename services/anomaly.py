import numpy as np

def zscore(series):
    return (series - series.mean()) / (series.std() + 1e-9)

def detect_anomalies(df):
    df = df.copy()

    anomalies = []

    # Z-score
    df["voltage_z"] = zscore(df["voltage"])
    df["temp_z"] = zscore(df["temperature"])
    df["load_z"] = zscore(df["load"])

    for i in range(len(df)):
        row = df.iloc[i]

        reasons = []

        # ---------- 1. HARD THRESHOLDS ----------
        if row["voltage"] > 250:
            reasons.append("High voltage")

        if row["voltage"] < 170:
            reasons.append("Low voltage")

        if row["temperature"] > 80:
            reasons.append("Overheating")

        if row["load"] > 95:
            reasons.append("Overload")

        # ---------- 2. Z-SCORE ----------
        if abs(row["voltage_z"]) > 2.5:
            reasons.append("Voltage anomaly (z-score)")

        if abs(row["temp_z"]) > 2.5:
            reasons.append("Temperature anomaly (z-score)")

        if abs(row["load_z"]) > 2.5:
            reasons.append("Load anomaly (z-score)")

        # ---------- 3. SUDDEN SPIKE ----------
        if i > 0:
            prev = df.iloc[i - 1]

            if abs(row["voltage"] - prev["voltage"]) > 30:
                reasons.append("Voltage spike")

            if abs(row["temperature"] - prev["temperature"]) > 15:
                reasons.append("Temperature spike")

        # ---------- SAVE ----------
        if reasons:
            anomalies.append({
                "timestamp": row["timestamp"],
                "station_id": row["station_id"],
                "voltage": row["voltage"],
                "load": row["load"],
                "temperature": row["temperature"],
                "issues": ", ".join(reasons)
            })

    return anomalies