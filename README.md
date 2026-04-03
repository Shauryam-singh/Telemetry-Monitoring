# ⚡ Smart Telemetry Monitoring System

## 🧩 Problem Definition

Municipal energy providers manage hundreds of sub-stations that continuously generate telemetry data such as voltage, load, and temperature.

Currently, engineers:

* Manually inspect raw logs
* Struggle to detect anomalies quickly
* Spend more time managing data than understanding it

### 🎯 Goal

Build a system that:

* Simplifies monitoring of multiple sub-stations
* Provides intuitive visualization of telemetry data
* Automatically detects anomalies
* Reduces cognitive load for engineers

---

## 🚀 Solution Overview

I built a **Smart Telemetry Monitoring Dashboard** using Streamlit that enables:

* 📊 Interactive visualization of telemetry data
* 🗺️ Geospatial monitoring via map view
* 🚨 Intelligent anomaly detection
* 🧠 Automated system insights
* ⚡ Real-time-like analysis from uploaded datasets

---

## ✨ Key Features

### 📊 Interactive Dashboard

* Built with Plotly for:

  * Zooming
  * Hover tooltips
  * Smooth exploration of trends

### 🗺️ Map Visualization

* Displays all sub-stations geographically
* Color-coded status:

  * 🟢 Normal
  * 🟠 Warning
  * 🔴 Critical

### 🚨 Hybrid Anomaly Detection

A robust system combining:

* Statistical detection (Z-score)
* Domain thresholds (real-world limits)
* Sudden spike detection

### 🧠 Smart Insights

* Detects:

  * Rising temperature trends
  * Load nearing capacity
  * Voltage instability

### 💡 Health Score

* Each station is assigned a score (0–100)
* Based on system conditions and risks

---

## 🏗️ Technical Architecture

The project follows a clean, modular architecture:

```
app.py                → UI (Streamlit frontend)

services/
  parser.py           → Data loading & validation
  anomaly.py          → Anomaly detection logic
  analytics.py        → Insights & health scoring

utils/
  helpers.py          → Utility functions
```

### 🔑 Design Decisions

* **Separation of concerns**

  * UI, business logic, and utilities are isolated
* **Scalability**

  * Easy to extend with ML models or real-time streaming
* **Performance**

  * Streamlit caching used for fast reloads

---

## 📊 Data Model

Each telemetry record includes:

* `timestamp`
* `station_id`
* `voltage`
* `load`
* `temperature`
* `latitude (lat)`
* `longitude (lon)`

---

## 🛠️ Setup & Deployment

### 1. Clone the repository

```bash
git clone https://github.com/Shauryam-singh/Telemetry-Monitoring.git
cd telemetry-monitoring
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📂 Sample Data

A realistic dataset is included in:

```
data/sample_data.csv
```

It simulates:

* Multiple substations
* Realistic telemetry trends
* Failure scenarios (overload, overheating, voltage drops)

---

## 🧪 Testing Strategy

* Manual validation using synthetic datasets
* Edge cases tested:

  * Missing columns
  * Extreme values
  * Sudden spikes

Future improvements:

* Unit tests for anomaly detection
* Performance benchmarking on large datasets

---

## ⚖️ Critical Reflection

One key design decision was choosing a **hybrid anomaly detection approach**.

### Trade-offs:

* ✅ More accurate than simple threshold or Z-score alone
* ❌ Still rule-based (not adaptive to all scenarios)

### Future Improvements:

* Implement machine learning models (e.g., Isolation Forest)
* Add real-time streaming data support
* Improve anomaly explainability

---

## 🚀 Future Enhancements

* 🔴 Real-time telemetry streaming
* 🔔 Alert/notification system
* 🧠 ML-based anomaly detection
* 🌐 Cloud deployment (public dashboard)
* 📊 Historical trend comparison

---

## 💬 Conclusion

This project focuses on **reducing cognitive load for engineers** by transforming raw telemetry data into:

* Actionable insights
* Visual patterns
* Immediate alerts

The goal was not to over-engineer, but to deliver a **high-impact, user-focused MVP** that can scale into a production system.

---
