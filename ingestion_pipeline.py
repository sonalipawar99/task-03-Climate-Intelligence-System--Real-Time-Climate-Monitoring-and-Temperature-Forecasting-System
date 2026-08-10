import logging
import pandas as pd

from configs.settings import DATA_PATH

from ingestion.validators import validate_data


logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO
)


def run_ingestion():

    try:

        df = pd.read_csv(DATA_PATH)

        validate_data(df)

        logging.info(
            "Ingestion Pipeline Completed Successfully."
        )

        return df

    except FileNotFoundError:

        logging.error(
            "Climate Data File Not Found."
        )

        print(
            "Climate Data File Not Found."
        )

    except Exception as e:

        logging.error(str(e))

        print(e)