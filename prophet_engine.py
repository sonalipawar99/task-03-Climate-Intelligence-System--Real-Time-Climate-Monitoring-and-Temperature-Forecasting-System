import pandas as pd

from prophet import Prophet

def run_forecast():

    df = pd.read_csv(
        "data/climate_data.csv"
    )

    prophet_df = df[
        ["Date","Temp_Max"]
    ].copy()

    prophet_df.columns = [
        "ds",
        "y"
    ]

    prophet_df["ds"] = pd.to_datetime(
        prophet_df["ds"]
    )

    model = Prophet()

    model.fit(
        prophet_df
    )

    future = model.make_future_dataframe(
        periods=30
    )

    forecast = model.predict(
        future
    )

    forecast.to_csv(
    "data/temperature_forecast.csv",
    index=False
    )

    print(
        "Forecast Generated Successfully"
    )

    return forecast