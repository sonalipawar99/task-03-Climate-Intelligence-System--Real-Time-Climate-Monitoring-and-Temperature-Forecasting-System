import pandas as pd

def split_data(df):

    split_index = int(
        len(df) * 0.8
    )

    train_df = df.iloc[
        :split_index
    ]

    test_df = df.iloc[
        split_index:
    ]

    return (
        train_df,
        test_df
    )