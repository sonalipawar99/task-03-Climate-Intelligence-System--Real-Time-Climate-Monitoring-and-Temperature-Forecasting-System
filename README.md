# Climate Intelligence System – Task 003

An end-to-end **Climate Intelligence and Temperature Forecasting System** built using Python, Prophet, Streamlit, Pandas and Plotly.

The system analyzes historical climate data, monitors climate risks, forecasts maximum temperature and provides an interactive dashboard for climate intelligence.

---

## Project Overview

The Climate Intelligence System is designed to analyze historical climate conditions and generate maximum temperature forecasts using a **Prophet Time Series Forecasting Model with Climate Regressors**.

The final system uses **11 years of historical daily climate data from 2014 to 2024** for Pune.

The climate parameters used by the system are:

* Maximum Temperature
* Minimum Temperature
* Rainfall
* Wind Speed

The project performs:

* Historical climate data analysis
* Temperature trend analysis
* Rainfall analysis
* Climate risk detection
* Maximum temperature forecasting
* Actual vs Predicted temperature comparison
* Forecast confidence interval visualization
* Climate risk monitoring
* Interactive Streamlit dashboard

---

## Objectives

The main objectives of this project are:

1. Analyze long-term historical climate data.
2. Identify temperature and rainfall patterns.
3. Detect potential climate risks such as heatwaves and heavy rainfall.
4. Build a temperature forecasting model using Prophet.
5. Improve forecasting using meaningful climate regressors.
6. Evaluate the forecasting model using standard machine learning metrics.
7. Compare actual and predicted maximum temperature.
8. Develop an interactive climate intelligence dashboard.

---

## Dataset

The final system uses reliable historical daily climate data obtained from **Open-Meteo**.

### Location

**Pune, Maharashtra, India**

### Historical Period

**1 January 2014 – 31 December 2024**

### Dataset Size

* **Rows:** 4,018
* **Missing Values:** 0
* **Frequency:** Daily

### Dataset Columns

| Column    | Description                |
| --------- | -------------------------- |
| Date      | Date of observation        |
| Temp_Max  | Maximum temperature in °C  |
| Temp_Min  | Minimum temperature in °C  |
| Rainfall  | Daily rainfall in mm       |
| WindSpeed | Maximum wind speed in km/h |

### Dataset Validation

The final dataset was validated before model training.

```text
Rows       : 4018
Start Date : 2014-01-01
End Date   : 2024-12-31
Missing    : 0
```

The final dataset is stored at:

```text
data/climate_data.csv
```

---

## Forecasting Model

The project uses **Prophet** for time-series forecasting.

The final forecasting system combines Prophet's time-series components with external climate regressors.

### Final Model

**Prophet + Climate Regressors**

### Target Variable

```text
Temp_Max
```

The model forecasts **Maximum Temperature**.

### Climate Regressors

The following climate variables are added to the Prophet model:

1. **Temp_Min** – Minimum Temperature
2. **Rainfall** – Daily Rainfall
3. **WindSpeed** – Maximum Wind Speed

These regressors are incorporated using Prophet's `add_regressor()` functionality and are used during model training and prediction.

The model therefore combines:

```text
Time-Series Components
        +
Minimum Temperature
        +
Rainfall
        +
Wind Speed
        ↓
Maximum Temperature Forecast
```

---

## Training and Testing

The final dataset is divided chronologically into training and testing periods.

### Training Dataset

```text
Training Samples : 3214
Training Period  : 2014-01-01 to 2022-10-19
```

### Testing Dataset

```text
Testing Samples : 804
Testing Period  : 2022-10-20 to 2024-12-31
```

The chronological split prevents future observations from being used during model training.

---

## Model Evaluation

The final Prophet + Climate Regressors model was evaluated on **804 testing samples**.

### Final Results

| Metric |        Result |
| ------ | ------------: |
| MAE    | **1.2007 °C** |
| RMSE   | **1.5521 °C** |
| MAPE   |   **3.8291%** |
| R²     |    **0.8269** |

### Interpretation

#### MAE = 1.2007 °C

The model's average absolute prediction error is approximately **1.20 °C**.

#### RMSE = 1.5521 °C

The RMSE measures prediction error while giving greater importance to larger errors.

#### MAPE = 3.8291%

The average percentage error is approximately **3.83%**, indicating relatively low forecasting error on the evaluation dataset.

#### R² = 0.8269

The positive R² indicates that the model explains approximately **82.69% of the variation in maximum temperature** in the evaluation dataset.

This represents a substantial improvement compared with the earlier model trained on the smaller historical dataset.

---

## Final Model Output

The model generates an Actual vs Predicted comparison file:

```text
outputs/actual_vs_predicted_regressors.csv
```

The file contains:

* Date
* Actual Temperature
* Predicted Temperature
* Prediction Error

Example structure:

```text
Date
Actual_Temp
Predicted_Temp
Error
```

The Streamlit dashboard uses this output to display the **Actual vs Predicted Maximum Temperature** visualization.

---

## Forecast Output

The final temperature forecast is saved to:

```text
data/temperature_forecast.csv
```

The system is configured to generate a **30-day temperature forecast**.

---

## Climate Risk Intelligence

The dashboard provides basic climate risk monitoring based on configured thresholds.

### Heatwave Detection

The system identifies days where maximum temperature crosses the configured heatwave threshold.

Configured threshold:

```text
Heatwave Threshold = 40 °C
Severe Heatwave Threshold = 45 °C
```

### Heavy Rainfall Detection

The system identifies days with rainfall above the configured rainfall thresholds.

Configured thresholds:

```text
Heavy Rainfall Threshold   = 50 mm
Extreme Rainfall Threshold = 100 mm
```

The dashboard displays climate risk alerts based on these thresholds.

---

## Dashboard

The project includes an interactive **Streamlit Climate Intelligence Dashboard**.

The dashboard provides:

###  Temperature Trend

Displays historical maximum temperature trends.

###  Rainfall Trend

Displays rainfall variation over the historical period.

###  Temperature Forecast

Displays the generated future temperature forecast.

###  Forecast Confidence Interval

Displays the uncertainty range associated with the forecast.

###  Actual vs Predicted Maximum Temperature

Compares actual maximum temperature with the model's predicted temperature using the final evaluation output.

###  Forecast Data

Displays generated forecast data in tabular form.

###  Climate Risk Alerts

Displays heatwave and heavy rainfall alerts.

---

## Dashboard Summary

The final dashboard provides a high-level climate intelligence view including:

* Average Temperature
* Total Rainfall
* Average Wind Speed
* Heatwave Days
* Predicted Temperature
* Climate Risk Alerts
* Historical Temperature Trend
* Rainfall Trend
* Temperature Forecast
* Forecast Confidence Interval
* Actual vs Predicted Temperature
* Forecast Data

---

## Project Structure

```text
Climate Intelligence System Task 003/
│
├── configs/
│   ├── __init__.py
│   └── settings.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── climate_data.csv
│   └── temperature_forecast.csv
│
├── forecasting/
│   ├── evaluation.py
│   ├── forecasting_pipeline.py
│   ├── prophet_engine.py
│   └── train_test_validation.py
│
├── ingestion/
│
├── logs/
│
├── notebooks/
│
├── outputs/
│   └── actual_vs_predicted_regressors.csv
│
├── risk_engine/
│
├── tests/
│
├── generate_climate_data.py
├── README.md
├── requirements.txt
├── run_dashboard.py
└── Task_003_Documentation.md
```

---

## Installation

### Step 1 – Open the project

Open the project folder in VS Code.

### Step 2 – Create a virtual environment

```bash
python -m venv venv
```

### Step 3 – Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4 – Install dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Historical Climate Dataset

The project includes a climate data generation script using Open-Meteo historical data.

```bash
python generate_climate_data.py
```

The final dataset is stored as:

```text
data/climate_data.csv
```

The final dataset covers:

```text
2014-01-01 → 2024-12-31
```

---

## Run Forecasting Model

From the project root directory:

```bash
python -m forecasting.prophet_engine
```

The forecasting pipeline will:

1. Load the historical climate dataset.
2. Validate and prepare the data.
3. Create the time-series training dataset.
4. Split the data chronologically.
5. Configure the Prophet model.
6. Add climate regressors.
7. Train the forecasting model.
8. Generate predictions.
9. Calculate MAE, RMSE, MAPE and R².
10. Save Actual vs Predicted results.
11. Generate the future temperature forecast.

---

## Run Streamlit Dashboard

From the project root directory:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in the browser.

Usually:

```text
http://localhost:8501
```

---

## Configuration

The main project configuration is maintained in:

```text
configs/settings.py
```

### Final Configuration

```python
CITY = "Pune"

LATITUDE = 18.5204
LONGITUDE = 73.8567

START_DATE = "2014-01-01"
END_DATE = "2024-12-31"

FORECAST_DAYS = 30

HEATWAVE_THRESHOLD = 40
SEVERE_HEATWAVE_THRESHOLD = 45

HEAVY_RAINFALL_THRESHOLD = 50
EXTREME_RAINFALL_THRESHOLD = 100

DATA_PATH = "data/climate_data.csv"

FORECAST_PATH = "data/temperature_forecast.csv"

LOG_PATH = "logs/system.log"
```

---

## Technology Stack

* **Python**
* **Pandas**
* **Prophet**
* **Streamlit**
* **Plotly**
* **Scikit-learn**
* **Open-Meteo Historical Weather Data**

---

## Key Features

✅ 11-Year Historical Climate Dataset

✅ Open-Meteo Historical Climate Data

✅ Climate Data Validation

✅ Temperature Trend Analysis

✅ Rainfall Trend Analysis

✅ Prophet Time-Series Forecasting

✅ Climate Regressor Integration

✅ Minimum Temperature Regressor

✅ Rainfall Regressor

✅ Wind Speed Regressor

✅ Chronological Train/Test Evaluation

✅ MAE / RMSE / MAPE / R² Metrics

✅ Actual vs Predicted Temperature

✅ Forecast Confidence Interval

✅ 30-Day Temperature Forecast

✅ Heatwave Detection

✅ Heavy Rainfall Detection

✅ Climate Risk Monitoring

✅ Interactive Streamlit Dashboard

---

## Final Model Performance

The final model trained using the expanded 11-year historical dataset achieved:

```text
MAE  : 1.2007 °C
RMSE : 1.5521 °C
MAPE : 3.8291 %
R²   : 0.8269
```

The model explains approximately **82.69% of the variation in maximum temperature** on the evaluation dataset.

The improvement demonstrates the benefit of:

1. Increasing the historical dataset from approximately 2 years to 11 years.
2. Adding meaningful climate regressors to the Prophet model.

---

## Future Improvements

The system can be further improved by:

* Adding additional reliable climate variables
* Adding humidity and atmospheric pressure
* Comparing Prophet with XGBoost and Random Forest
* Comparing multiple forecasting approaches
* Adding automated anomaly detection
* Adding location-wise climate intelligence
* Improving climate risk prediction
* Adding real-time weather information
* Expanding the system to multiple locations
* Deploying the dashboard for wider access

---

## Project Summary

This project demonstrates an end-to-end approach to climate intelligence by combining:

```text
Historical Data Collection
        ↓
Data Validation
        ↓
Climate Data Analysis
        ↓
Feature / Regressor Preparation
        ↓
Prophet + Climate Regressors
        ↓
Model Evaluation
        ↓
Temperature Forecasting
        ↓
Climate Risk Detection
        ↓
Visualization
        ↓
Interactive Streamlit Dashboard
```

The final Task 003 system uses **11 years of historical climate data (2014–2024)** and a **Prophet model with Temp_Min, Rainfall and WindSpeed as climate regressors**.

The final evaluation achieved:

**MAE = 1.2007°C, RMSE = 1.5521°C, MAPE = 3.8291%, and R² = 0.8269.**

This provides a strong foundation for the next stage of the Climate Intelligence roadmap.
