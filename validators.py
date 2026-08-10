import logging


def validate_data(df):

    if df.empty:
        logging.error("Dataset is empty.")
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

            logging.error(
                f"Missing Column: {column}"
            )

            raise ValueError(
                f"Missing Column: {column}"
            )

    logging.info(
        "Data Validation Successful."
    )

    return True