import pandas as pd

def detect_rainfall_risk(df):

    heavy_rainfall = df[
        df["Rainfall"] > 50
    ]

    extreme_rainfall = df[
        df["Rainfall"] > 100
    ]

    return {
        "Heavy Rainfall":
        len(heavy_rainfall),

        "Extreme Rainfall":
        len(extreme_rainfall)
    }