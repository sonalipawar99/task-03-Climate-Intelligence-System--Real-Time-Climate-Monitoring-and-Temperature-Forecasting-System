import pandas as pd

def detect_heatwaves(df):

    heatwave_days = df[
        df["Temp_Max"] > 40
    ]

    severe_heatwave_days = df[
        df["Temp_Max"] > 45
    ]

    return {
        "Heatwave Days":
        len(heatwave_days),

        "Severe Heatwave Days":
        len(severe_heatwave_days)
    }