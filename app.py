import streamlit as st
import pandas as pd

from charts import (
    temperature_chart,
    rainfall_chart,
    forecast_chart,
    confidence_interval_chart
)

from metrics import (
    display_metrics
)

from alerts import (
    show_alerts
)

# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Climate Intelligence Dashboard",
    layout="wide"
)

# --------------------------------
# Load Data
# --------------------------------

climate_df = pd.read_csv(
    "data/climate_data.csv"
)

forecast_df = pd.read_csv(
    "data/temperature_forecast.csv"
)

# --------------------------------
# Title
# --------------------------------

st.title("🌍 Climate Intelligence Dashboard")

st.write(
    "Real-Time Climate Monitoring and Temperature Forecasting System"
)

# --------------------------------
# Metrics
# --------------------------------

display_metrics(
    climate_df,
    forecast_df
)

# --------------------------------
# Alerts
# --------------------------------

show_alerts()

# --------------------------------
# Temperature Trend
# --------------------------------

st.subheader("🌡 Temperature Trend")

st.plotly_chart(
    temperature_chart(climate_df),
    use_container_width=True
)

# --------------------------------
# Rainfall Trend
# --------------------------------

st.subheader("🌧 Rainfall Trend")

st.plotly_chart(
    rainfall_chart(climate_df),
    use_container_width=True
)

# --------------------------------
# Forecast
# --------------------------------

st.subheader("📈 Temperature Forecast")

st.plotly_chart(
    forecast_chart(forecast_df),
    use_container_width=True
)

# --------------------------------
# Confidence Interval
# --------------------------------

st.subheader("📊 Forecast Confidence Interval")

st.plotly_chart(
    confidence_interval_chart(forecast_df),
    use_container_width=True
)

# --------------------------------
# Forecast Table
# --------------------------------

st.subheader("Forecast Data")

st.dataframe(
    forecast_df.tail(15)
)

# --------------------------------
# Summary
# --------------------------------

st.subheader(" Project Summary")

st.info("""
### Climate Intelligence System

This dashboard provides an end-to-end climate monitoring and temperature forecasting solution.

**Key Features:**

✅ Climate Data Analysis

✅ Temperature Trend Visualization

✅ Rainfall Trend Analysis

✅ Prophet-based Temperature Forecasting

✅ Forecast Confidence Interval

✅ Climate Risk Monitoring

✅ Interactive Forecast Dashboard

**Technology Stack**

• Python

• Streamlit

• Prophet

• Pandas

• Plotly

• Scikit-learn
""")