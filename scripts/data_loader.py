import pandas as pd

def load_price_data(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def load_events(path):
    events = pd.read_csv(path)
    events["Date"] = pd.to_datetime(events["Date"])
    return events