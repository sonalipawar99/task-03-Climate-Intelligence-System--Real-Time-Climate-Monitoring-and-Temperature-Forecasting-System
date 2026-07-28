# 🌍 Climate Intelligence System

## Project Overview

The Climate Intelligence System is an AI-powered climate monitoring and forecasting application developed using Python, Streamlit, and Facebook Prophet.

The system collects climate data, analyzes historical weather patterns, predicts future temperatures, and identifies climate risks through an interactive dashboard.

---

## Features

- Climate Data Analysis
- Temperature Trend Visualization
- Rainfall Trend Analysis
- Temperature Forecasting using Prophet
- Forecast Confidence Interval
- Climate Risk Monitoring
- Interactive Streamlit Dashboard
- Forecast Data Table

---

## Technology Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Prophet
- Scikit-learn

---

## Project Structure

Climate Intelligence System/
│
├── configs/
│   └── settings.py
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── alerts.py
│   └── metrics.py
│
├── data/
│   ├── climate_data.csv
│   └── temperature_forecast.csv
│
├── forecasting/
│   ├── prophet_engine.py
│   ├── forecasting_pipeline.py
│   ├── evaluation.py
│   └── train_test_validation.py
│
├── ingestion/
│   ├── weather_api.py
│   ├── ingestion_pipeline.py
│   └── validators.py
│
├── risk_engine/
│   ├── heatwave.py
│   ├── rainfall.py
│   └── anomaly_detection.py
│
├── tests/
│   ├── test_heatwave.py
│   └── test_rainfall.py
│
├── notebooks/
│   └── Climate_Intelligence_System.ipynb
│
├── outputs/
│
├── logs/
│   └── logger.py
│
├── requirements.txt
└── README.md

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Forecasting Workflow

1. Collect climate data
2. Data preprocessing
3. Prophet model training
4. Forecast generation
5. Dashboard visualization
6. Climate risk analysis

---

## Author

**Sonali Vishal Pawar**

Data Science & AI Intern