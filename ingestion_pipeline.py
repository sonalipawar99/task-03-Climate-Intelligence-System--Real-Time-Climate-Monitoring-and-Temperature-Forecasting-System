import pandas as pd

from validators import validate_data

def run_ingestion():

    df = pd.read_csv(
        "data/climate_data.csv"
    )

    validate_data(df)

    print(
        "Ingestion Pipeline Completed"
    )

    return df