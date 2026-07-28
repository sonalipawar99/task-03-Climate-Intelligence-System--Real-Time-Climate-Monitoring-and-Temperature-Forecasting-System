import pandas as pd

from prophet_engine import run_forecast

def run_forecasting_pipeline():

    forecast = run_forecast()

    print(
        "Forecasting Pipeline Completed"
    )

    return forecast


if __name__ == "__main__":
    run_forecasting_pipeline()