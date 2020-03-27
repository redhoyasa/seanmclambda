import pandas as pd


def add_hour(df, column, hour):
    df = df.copy()
    df[column] += pd.to_timedelta(hour, unit='h')
    return df
