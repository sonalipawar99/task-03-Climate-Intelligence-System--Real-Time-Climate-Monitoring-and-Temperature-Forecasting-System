import pandas as pd

def validate_data(df):

    if df.empty:
        raise ValueError(
            "Dataset is empty."
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
                f"Missing Column: {column}"
            )

    print(
        "Data Validation Successful"
    )

    return True