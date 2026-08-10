# Climate Intelligence System – Task 003

## Technical Documentation

---

# 1. Project Overview

The **Climate Intelligence System – Task 003** is an end-to-end climate monitoring and temperature forecasting system developed using Python, Prophet, Pandas, Plotly and Streamlit.

The system analyzes historical climate data, identifies climate patterns, detects basic climate risks and generates maximum temperature forecasts.

The final Task 003 implementation uses an **11-year historical climate dataset from 2014 to 2024** and a **Prophet Time Series Model with Climate Regressors**.

The system also provides an interactive Streamlit dashboard for visualizing climate trends, forecasts, confidence intervals and climate risk alerts.

---

# 2. Project Objectives

The main objectives of Task 003 are:

1. Collect and analyze historical climate data.
2. Expand the historical dataset to a reliable long-term period.
3. Analyze maximum and minimum temperature patterns.
4. Analyze rainfall and wind-speed patterns.
5. Detect basic climate risks such as heatwaves and heavy rainfall.
6. Build a temperature forecasting model using Prophet.
7. Improve forecasting using meaningful climate regressors.
8. Evaluate the forecasting model using MAE, RMSE, MAPE and R².
9. Compare actual and predicted maximum temperature.
10. Generate future temperature forecasts.
11. Build an interactive Climate Intelligence Dashboard.

---

# 3. System Architecture

The final Task 003 pipeline follows the architecture:

```text
Open-Meteo Historical Climate Data
                ↓
        Data Ingestion
                ↓
        Data Validation
                ↓
      Historical Dataset
                ↓
       Data Preparation
                ↓
      Train/Test Split
                ↓
 Prophet + Climate Regressors
                ↓
       Model Training
                ↓
          Prediction
                ↓
        Model Evaluation
                ↓
      Forecast Generation
                ↓
       Climate Risk Engine
                ↓
      Streamlit Dashboard
```

---

# 4. Data Source

The historical climate dataset was generated using **Open-Meteo historical weather data**.

The selected location is:

```text
City      : Pune
Latitude  : 18.5204
Longitude : 73.8567
```

The system uses daily historical climate variables.

---

# 5. Historical Dataset

## 5.1 Dataset Period

The final historical dataset covers:

```text
Start Date : 2014-01-01
End Date   : 2024-12-31
```

This provides approximately **11 years of historical daily climate observations**.

---

## 5.2 Dataset Size

The final dataset contains:

```text
Rows          : 4018
Missing Values: 0
```

The dataset was validated before model training.

---

## 5.3 Dataset Location

The final dataset is stored at:

```text
data/climate_data.csv
```

---

# 6. Dataset Variables

The final dataset contains the following columns:

| Column    | Description         | Unit |
| --------- | ------------------- | ---- |
| Date      | Date of observation | Date |
| Temp_Max  | Maximum temperature | °C   |
| Temp_Min  | Minimum temperature | °C   |
| Rainfall  | Daily rainfall      | mm   |
| WindSpeed | Maximum wind speed  | km/h |

---

# 7. Dataset Validation

The final dataset was checked for:

* Correct date range
* Missing values
* Required columns
* Numeric climate variables
* Valid daily observations

Final validation result:

```text
Rows       : 4018
Start Date : 2014-01-01
End Date   : 2024-12-31
Missing    : 0
```

The dataset therefore provides a clean historical input for the forecasting pipeline.

---

# 8. Data Preparation

Before model training, the climate dataset is prepared for time-series forecasting.

The following operations are performed:

1. Load the CSV dataset.
2. Convert the `Date` column into datetime format.
3. Sort observations chronologically.
4. Validate the required climate columns.
5. Prepare the target variable.
6. Prepare climate regressors.
7. Split the dataset chronologically into training and testing sets.

The target variable is:

```text
Temp_Max
```

---

# 9. Forecasting Model

The final forecasting model uses:

## Prophet + Climate Regressors

Prophet is used as the main time-series forecasting model.

Climate variables are incorporated as external regressors to provide additional information for maximum temperature prediction.

---

# 10. Target Variable

The target variable is:

```text
Temp_Max
```

This represents the **daily maximum temperature in °C**.

The model therefore predicts future maximum temperature.

---

# 11. Climate Regressors

Three climate regressors are currently used in the final model:

### 1. Temp_Min

Minimum daily temperature.

### 2. Rainfall

Daily rainfall amount.

### 3. WindSpeed

Maximum daily wind speed.

These regressors are added to Prophet using its `add_regressor()` functionality.

The model therefore combines:

```text
Prophet Time-Series Components
            +
        Temp_Min
            +
        Rainfall
            +
        WindSpeed
            ↓
       Temp_Max Forecast
```

---

# 12. Why Climate Regressors Were Added

The initial model used a smaller historical dataset and produced a negative R² value.

The model was then improved by:

1. Expanding the historical dataset.
2. Adding meaningful climate variables as regressors.
3. Retraining and evaluating the forecasting model.

The expanded historical dataset provides more information about seasonal and long-term temperature patterns.

The climate regressors provide additional information related to daily maximum temperature.

---

# 13. Training and Testing Strategy

A chronological train/test split is used.

Future observations are not used during training.

## Training Dataset

```text
Training Samples : 3214

Training Period:
2014-01-01 to 2022-10-19
```

## Testing Dataset

```text
Testing Samples : 804

Testing Period:
2022-10-20 to 2024-12-31
```

The testing dataset is kept separate from model training and is used to evaluate forecasting performance.

---

# 14. Model Training

The forecasting pipeline performs the following steps:

```text
Load Dataset
     ↓
Validate Dataset
     ↓
Prepare Time-Series Data
     ↓
Create Training Dataset
     ↓
Add Climate Regressors
     ↓
Train Prophet Model
     ↓
Generate Test Predictions
     ↓
Evaluate Predictions
     ↓
Generate Future Forecast
```

The main forecasting implementation is located in:

```text
forecasting/prophet_engine.py
```

---

# 15. Model Evaluation Metrics

The final model is evaluated using:

* MAE
* RMSE
* MAPE
* R²

These metrics provide different views of forecasting performance.

---

# 16. Final Model Performance

The final Prophet + Climate Regressors model produced the following results:

| Metric |  Final Result |
| ------ | ------------: |
| MAE    | **1.2007 °C** |
| RMSE   | **1.5521 °C** |
| MAPE   |   **3.8291%** |
| R²     |    **0.8269** |

---

# 17. Metric Interpretation

## MAE – 1.2007 °C

Mean Absolute Error indicates the average absolute difference between actual and predicted maximum temperature.

The final model has an average prediction error of approximately:

```text
1.20 °C
```

---

## RMSE – 1.5521 °C

Root Mean Squared Error gives greater importance to larger prediction errors.

The final RMSE is:

```text
1.55 °C
```

---

## MAPE – 3.8291%

Mean Absolute Percentage Error represents the average percentage error between actual and predicted values.

The final MAPE is:

```text
3.83%
```

---

## R² – 0.8269

The final R² value is:

```text
0.8269
```

This means the model explains approximately:

```text
82.69%
```

of the variation in maximum temperature on the evaluation dataset.

This is a significant improvement compared with the earlier negative R² result obtained using the smaller historical dataset.

For the current MVP climate forecasting system, the positive R² represents an important improvement in model performance.

---

# 18. Mean Prediction Error

The final evaluation produced:

```text
Mean Prediction Error:
0.29 °C
```

This represents the average signed difference between actual and predicted temperature according to the final evaluation output.

---

# 19. Actual vs Predicted Output

The model generates an Actual vs Predicted comparison file.

Output location:

```text
outputs/actual_vs_predicted_regressors.csv
```

The file contains:

```text
Date
Actual_Temp
Predicted_Temp
Error
```

Example:

```text
Date        Actual_Temp    Predicted_Temp    Error
2022-10-20     27.5          29.710427       -2.210427
2022-10-21     26.7          29.374980       -2.674980
2022-10-22     27.5          29.418398       -1.918398
```

This output is used by the dashboard for actual versus predicted temperature visualization.

---

# 20. Future Temperature Forecast

The system is configured to generate:

```text
Forecast Horizon : 30 Days
```

The generated forecast is stored at:

```text
data/temperature_forecast.csv
```

The forecast contains future dates and predicted temperature values.

---

# 21. Forecast Confidence Interval

Prophet provides uncertainty estimates around the forecast.

The dashboard visualizes the forecast confidence interval to show the expected range around the predicted temperature.

This helps users understand that a forecast is an estimate rather than an exact future temperature value.

---

# 22. Climate Risk Intelligence

The system includes basic climate risk monitoring.

The current risk engine focuses on:

* Heatwave detection
* Heavy rainfall detection

---

# 23. Heatwave Detection

The configured heatwave thresholds are:

```text
Heatwave Threshold        : 40 °C
Severe Heatwave Threshold : 45 °C
```

The system identifies observations crossing the configured threshold.

The dashboard displays the detected heatwave days as a climate risk indicator.

---

# 24. Rainfall Risk Detection

The configured rainfall thresholds are:

```text
Heavy Rainfall Threshold   : 50 mm
Extreme Rainfall Threshold : 100 mm
```

The system identifies heavy rainfall conditions according to these configured thresholds.

The dashboard displays the detected rainfall risk as an alert.

---

# 25. Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

The dashboard provides:

### Temperature Monitoring

Displays historical maximum temperature information.

### Rainfall Monitoring

Displays historical rainfall patterns.

### Wind Speed Monitoring

Displays wind-speed information.

### Temperature Forecast

Displays future temperature predictions.

### Forecast Confidence Interval

Displays forecast uncertainty.

### Actual vs Predicted Temperature

Displays model evaluation results visually.

### Climate Risk Alerts

Displays heatwave and heavy rainfall alerts.

### Forecast Data

Displays generated forecast records in tabular format.

---

# 26. Dashboard Metrics

The dashboard provides high-level climate indicators such as:

```text
Average Temperature
Total Rainfall
Average Wind Speed
Heatwave Days
Predicted Temperature
```

The values are calculated from the climate dataset and forecast output.

---

# 27. Dashboard Technology

The dashboard is built using:

```text
Streamlit
Pandas
Plotly
Python
```

The main dashboard file is:

```text
dashboard/app.py
```

---

# 28. Project Structure

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

# 29. Configuration

The project configuration is maintained in:

```text
configs/settings.py
```

Final configuration:

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

# 30. Installation

## Step 1 – Open Project

Open the project folder in VS Code.

## Step 2 – Create Virtual Environment

```bash
python -m venv venv
```

## Step 3 – Activate Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## Step 4 – Install Requirements

```bash
pip install -r requirements.txt
```

---

# 31. Generate Historical Climate Data

The project contains:

```text
generate_climate_data.py
```

This script can be used to generate the historical climate dataset from Open-Meteo.

Run:

```bash
python generate_climate_data.py
```

The final dataset is stored as:

```text
data/climate_data.csv
```

---

# 32. Run Forecasting Model

From the project root directory:

```bash
python -m forecasting.prophet_engine
```

The command performs:

1. Dataset loading.
2. Data validation.
3. Time-series preparation.
4. Train/test split.
5. Prophet model creation.
6. Climate regressor integration.
7. Model training.
8. Test prediction.
9. Metric calculation.
10. Actual vs Predicted output generation.
11. Future forecast generation.

---

# 33. Run Dashboard

From the project root directory:

```bash
streamlit run dashboard/app.py
```

The dashboard is normally available at:

```text
http://localhost:8501
```

---

# 34. Requirements

The project dependencies are:

```text
pandas
numpy
prophet
streamlit
plotly
scikit-learn
```

These are listed in:

```text
requirements.txt
```

---

# 35. Final Outputs

The final Task 003 system produces the following important outputs:

### Historical Dataset

```text
data/climate_data.csv
```

### Future Forecast

```text
data/temperature_forecast.csv
```

### Model Evaluation Output

```text
outputs/actual_vs_predicted_regressors.csv
```

### System Logs

```text
logs/system.log
```

---

# 36. Final Task 003 Results

The final Task 003 implementation successfully achieved:

```text
Historical Period : 2014–2024
Dataset Rows      : 4018
Missing Values    : 0

Training Samples  : 3214
Testing Samples   : 804

MAE               : 1.2007 °C
RMSE              : 1.5521 °C
MAPE              : 3.8291%
R²                : 0.8269
```

The final model uses:

```text
Prophet
+
Temp_Min
+
Rainfall
+
WindSpeed
```

to forecast:

```text
Temp_Max
```

---

# 37. Improvement from Earlier Model

The earlier version used approximately two years of historical data and produced a negative R² value.

The Task 003 improvement focused on two major changes:

## 1. Historical Dataset

The final historical climate dataset covers approximately **11 years**, from **2014-01-01 to 2024-12-31**, for Pune.

```text
Dataset Period : 2014-01-01 to 2024-12-31
Location       : Pune
Total Rows     : 4,018
Missing Values : 0
Data Source    : Open-Meteo Historical Weather Data
```

The dataset contains daily observations of maximum temperature, minimum temperature, rainfall, and wind speed.


### 2. Climate Regressors

Meaningful climate variables were added to Prophet:

```text
Temp_Min
Rainfall
WindSpeed
```

After retraining the model, the final R² improved to:

```text
R² = 0.8269
```

This indicates that the model now explains a substantial proportion of the variation in maximum temperature on the evaluation dataset.

---

# 38. Key Technical Achievements

Task 003 successfully demonstrates:

* Long-term historical climate data processing
* Open-Meteo data integration
* Data validation
* Time-series forecasting
* Prophet model implementation
* External climate regressor integration
* Chronological train/test validation
* Model evaluation
* Actual vs Predicted analysis
* Future temperature forecasting
* Forecast confidence intervals
* Heatwave detection
* Heavy rainfall detection
* Interactive Streamlit visualization
* End-to-end climate intelligence pipeline

---

# 39. Limitations

The current system has some limitations:

1. The model is trained for the selected Pune location.
2. Forecast quality depends on historical data quality.
3. Only three external climate regressors are currently used.
4. The system does not yet include humidity or atmospheric pressure.
5. Climate risk detection currently uses threshold-based rules.
6. Forecast uncertainty increases for longer forecast horizons.
7. The current system is an MVP-level climate intelligence implementation.

---

# 40. Future Improvements

Future versions can include:

* Humidity as an additional regressor
* Atmospheric pressure
* Solar radiation
* Cloud cover
* More advanced climate risk models
* Automated anomaly detection
* Comparison with XGBoost
* Comparison with Random Forest
* Comparison with other forecasting models
* Multi-location forecasting
* Real-time weather data integration
* Advanced flood-risk prediction
* Advanced heatwave prediction
* Automated model retraining
* Production deployment
* Cloud-based monitoring
* Multi-city Climate Intelligence

---

# 41. Conclusion

Task 003 successfully evolved the Climate Intelligence System from a small historical forecasting experiment into a more reliable MVP-level climate forecasting pipeline.

The historical dataset was expanded to approximately **11 years (2014–2024)** using Open-Meteo historical daily climate data.

The Prophet model was enhanced with three meaningful climate regressors:

```text
Temp_Min
Rainfall
WindSpeed
```

The final model achieved:

```text
MAE  : 1.2007 °C
RMSE : 1.5521 °C
MAPE : 3.8291%
R²   : 0.8269
```

The positive R² of **0.8269** indicates that the final model explains approximately **82.69% of the variation in maximum temperature** on the evaluation dataset.

The final system integrates:

```text
Data Collection
      ↓
Data Validation
      ↓
Climate Analysis
      ↓
Prophet + Climate Regressors
      ↓
Model Evaluation
      ↓
Temperature Forecasting
      ↓
Climate Risk Detection
      ↓
Interactive Dashboard
```

This completes the major objectives of **Climate Intelligence System – Task 003** and provides a strong foundation for the next stage of the Climate Intelligence roadmap.

---

# 42. Final Status

```text
Task 003 Status: Completed

Historical Dataset : 2014–2024
Dataset Rows       : 4018
Missing Values     : 0

Forecasting Model  : Prophet + Climate Regressors
Target             : Temp_Max
Regressors         : Temp_Min, Rainfall, WindSpeed

MAE                : 1.2007 °C
RMSE               : 1.5521 °C
MAPE               : 3.8291%
R²                 : 0.8269

Dashboard          : Streamlit
Forecast Horizon   : 30 Days
```

