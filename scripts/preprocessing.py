import pandas as pd

def clean_data(df):

    df = df.copy()

    df = df.sort_values("Date")

    df = df.drop_duplicates()

    df = df.dropna()

    return df