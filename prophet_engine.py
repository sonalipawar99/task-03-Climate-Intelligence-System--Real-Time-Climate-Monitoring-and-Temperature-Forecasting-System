import logging
from pathlib import Path

import numpy as np
import pandas as pd
from prophet import Prophet

from configs.settings import (
    DATA_PATH,
    FORECAST_PATH,
    FORECAST_DAYS,
    START_DATE,
    END_DATE,
    LOG_PATH
)

from forecasting.evaluation import (
    calculate_metrics,
    save_metrics
)

from forecasting.train_test_validation import (
    split_data
)


# ============================================================
# LOGGING
# ============================================================

Path(LOG_PATH).parent.mkdir(
    parents=True,
    exist_ok=True
)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# CREATE PROPHET MODEL
# ============================================================

def create_model():

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,

        seasonality_mode="additive",

        changepoint_prior_scale=0.01,

        seasonality_prior_scale=5
    )

    # Climate regressors
    model.add_regressor(
        "Temp_Min"
    )

    model.add_regressor(
        "Rainfall"
    )

    model.add_regressor(
        "WindSpeed"
    )

    return model


# ============================================================
# MAIN FORECAST FUNCTION
# ============================================================

def run_forecast():

    try:

        # ====================================================
        # 1. LOAD DATA
        # ====================================================

        df = pd.read_csv(
            DATA_PATH
        )

        if df.empty:

            raise ValueError(
                "Climate dataset is empty."
            )


        required_columns = [
            "Date",
            "Temp_Max",
            "Temp_Min",
            "Rainfall",
            "WindSpeed"
        ]

        for column in required_columns:

            if column not in df.columns:

                raise ValueError(
                    f"Missing required column: {column}"
                )


        # ====================================================
        # 2. PREPROCESSING
        # ====================================================

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        for column in [
            "Temp_Max",
            "Temp_Min",
            "Rainfall",
            "WindSpeed"
        ]:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )


        df = df.dropna(
            subset=required_columns
        )


        # ====================================================
        # 3. DATE RANGE
        # ====================================================

        start_date = pd.to_datetime(
            START_DATE
        )

        end_date = pd.to_datetime(
            END_DATE
        )

        df = df[
            (df["Date"] >= start_date)
            &
            (df["Date"] <= end_date)
        ].copy()


        if df.empty:

            raise ValueError(
                "No climate data available within configured date range."
            )


        # ====================================================
        # 4. SORT
        # ====================================================

        df = df.sort_values(
            "Date"
        ).reset_index(
            drop=True
        )


        # ====================================================
        # 5. PROPHET DATASET
        # ====================================================

        prophet_df = df[
            [
                "Date",
                "Temp_Max",
                "Temp_Min",
                "Rainfall",
                "WindSpeed"
            ]
        ].copy()


        prophet_df = prophet_df.rename(
            columns={
                "Date": "ds",
                "Temp_Max": "y"
            }
        )


        # ====================================================
        # 6. 80/20 CHRONOLOGICAL SPLIT
        # ====================================================

        train_df, test_df = split_data(
            prophet_df[
                [
                    "ds",
                    "y",
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ],
            train_ratio=0.8
        )


        print(
            f"\nTraining samples: {len(train_df)}"
        )

        print(
            f"Testing samples: {len(test_df)}"
        )

        print(
            "Training period: "
            f"{train_df['ds'].min().date()} "
            f"to "
            f"{train_df['ds'].max().date()}"
        )

        print(
            "Testing period: "
            f"{test_df['ds'].min().date()} "
            f"to "
            f"{test_df['ds'].max().date()}"
        )


        # ====================================================
        # 7. TRAIN MODEL
        # ====================================================

        model = create_model()

        model.fit(
            train_df[
                [
                    "ds",
                    "y",
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ]
        )


        # ====================================================
        # 8. TEST PERIOD PREDICTION
        # ====================================================

        test_forecast = model.predict(
            test_df[
                [
                    "ds",
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ]
        )


        # ====================================================
        # 9. ACTUAL / PREDICTED
        # ====================================================

        actual = test_df[
            "y"
        ].values

        predicted = test_forecast[
            "yhat"
        ].values


        # ====================================================
        # 10. DATE ALIGNMENT
        # ====================================================

        if not test_df[
            "ds"
        ].reset_index(
            drop=True
        ).equals(
            test_forecast[
                "ds"
            ].reset_index(
                drop=True
            )
        ):

            raise ValueError(
                "Actual and predicted dates are not aligned."
            )


        # ====================================================
        # 11. METRICS
        # ====================================================

        metrics = calculate_metrics(
            actual,
            predicted
        )


        print(
            "\nModel Evaluation - Prophet + Climate Regressors"
        )

        print(
            "-----------------------------------------------"
        )

        print(
            f"MAE  : {metrics['MAE']:.4f}"
        )

        print(
            f"RMSE : {metrics['RMSE']:.4f}"
        )

        print(
            f"MAPE : {metrics['MAPE']:.4f}%"
        )

        print(
            f"R2   : {metrics['R2']:.4f}"
        )


        # ====================================================
        # 12. SAVE METRICS
        # ====================================================

        save_metrics(
            metrics,
            output_path="logs/model_evaluation_regressors.txt"
        )


        # ====================================================
        # 13. COMPARISON DATAFRAME
        # ====================================================

        comparison_df = pd.DataFrame({

            "Date":
                test_df["ds"].values,

            "Actual_Temp":
                actual,

            "Predicted_Temp":
                predicted
        })


        comparison_df["Error"] = (
            comparison_df["Actual_Temp"]
            -
            comparison_df["Predicted_Temp"]
        )


        # ====================================================
        # 14. SAVE COMPARISON
        # ====================================================

        comparison_path = Path(
            "outputs/actual_vs_predicted_regressors.csv"
        )

        comparison_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        comparison_df.to_csv(
            comparison_path,
            index=False
        )


        print(
            "\nActual vs Predicted output saved to:"
        )

        print(
            comparison_path
        )


        # ====================================================
        # 15. SAMPLE OUTPUT
        # ====================================================

        print(
            "\nSample Actual vs Predicted Values:"
        )

        print(
            comparison_df.head(10).to_string(
                index=False
            )
        )


        # ====================================================
        # 16. ERROR
        # ====================================================

        mean_error = (
            comparison_df["Error"].mean()
        )

        print(
            "\nMean Prediction Error:"
        )

        print(
            f"{mean_error:.2f} °C"
        )


        # ====================================================
        # 17. FULL MODEL
        # ====================================================

        final_model = create_model()

        final_model.fit(
            prophet_df[
                [
                    "ds",
                    "y",
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ]
        )


        # ====================================================
        # 18. FUTURE REGRESSORS
        # ====================================================
        #
        # IMPORTANT:
        # Future climate variables are not actually known.
        #
        # For this experiment we use historical monthly
        # averages as proxy values.
        # ====================================================

        historical_monthly = (
            df
            .assign(
                Month=df["Date"].dt.month
            )
            .groupby("Month")[
                [
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ]
            .mean()
        )


        future_dates = pd.date_range(
            start=df["Date"].max()
            + pd.Timedelta(days=1),
            periods=FORECAST_DAYS,
            freq="D"
        )


        future_df = pd.DataFrame({
            "ds": future_dates
        })


        future_df["Month"] = (
            future_df["ds"].dt.month
        )


        future_df["Temp_Min"] = (
            future_df["Month"]
            .map(
                historical_monthly["Temp_Min"]
            )
        )


        future_df["Rainfall"] = (
            future_df["Month"]
            .map(
                historical_monthly["Rainfall"]
            )
        )


        future_df["WindSpeed"] = (
            future_df["Month"]
            .map(
                historical_monthly["WindSpeed"]
            )
        )


        # ====================================================
        # 19. FUTURE FORECAST
        # ====================================================

        forecast_future = final_model.predict(
            future_df[
                [
                    "ds",
                    "Temp_Min",
                    "Rainfall",
                    "WindSpeed"
                ]
            ]
        )


        # ====================================================
        # 20. SAVE FORECAST
        # ====================================================

        forecast_path = Path(
            FORECAST_PATH
        )

        forecast_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        # Keep full Prophet forecast format
        full_forecast = final_model.predict(
            pd.concat(
                [
                    prophet_df[
                        [
                            "ds",
                            "Temp_Min",
                            "Rainfall",
                            "WindSpeed"
                        ]
                    ],
                    future_df[
                        [
                            "ds",
                            "Temp_Min",
                            "Rainfall",
                            "WindSpeed"
                        ]
                    ]
                ],
                ignore_index=True
            )
        )


        full_forecast.to_csv(
            forecast_path,
            index=False
        )


        print(
            "\nForecast Generated Successfully."
        )

        return full_forecast


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except FileNotFoundError:

        logging.error(
            "Climate Data File Not Found."
        )

        print(
            "Climate Data File Not Found."
        )

        return None


    except ValueError as e:

        logging.error(
            "Validation Error: %s",
            e
        )

        print(
            f"Validation Error: {e}"
        )

        return None


    except Exception as e:

        logging.exception(
            "Forecasting Error"
        )

        print(
            f"Forecasting Error: {e}"
        )

        return None


# ============================================================
# MODULE EXECUTION
# ============================================================

if __name__ == "__main__":

    run_forecast()