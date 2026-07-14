"""
Service layer for Brent Oil Price Dashboard.

Handles:
- Loading Brent oil prices
- Loading historical events
- Loading Bayesian change point results
- Computing dashboard KPIs
"""

from pathlib import Path
import json

import pandas as pd


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "Data"

ANALYSIS_DIR = BASE_DIR / "analysis"

PRICE_FILE = "../Data/BrentOilPrices.csv"

EVENT_FILE = "../Data/oil_market_events.csv"

CHANGE_POINT_FILE = ANALYSIS_DIR / "change_points.json"


# ---------------------------------------------------------------------
# Load Data
# ---------------------------------------------------------------------

def load_prices():
    """
    Load Brent oil prices.
    """

    df = pd.read_csv(PRICE_FILE)

    df["Date"] = pd.to_datetime(df["Date"])

    return df.sort_values("Date")


def load_events():
    """
    Load oil market events.
    """

    events = pd.read_csv(EVENT_FILE)

    events["start_date"] = pd.to_datetime(events["start_date"])
    events["end_date"] = pd.to_datetime(events["end_date"])

    return events.sort_values("start_date")


# ---------------------------------------------------------------------
# API Responses
# ---------------------------------------------------------------------

def get_price_data():
    """
    Return all historical prices.
    """

    prices = load_prices()

    return prices.assign(
        Date=prices["Date"].dt.strftime("%Y-%m-%d")
    ).to_dict(orient="records")


def get_events():
    """
    Return historical events.
    """

    events = load_events()

    events["start_date"] = events["start_date"].dt.strftime("%Y-%m-%d")
    events["end_date"] = events["end_date"].dt.strftime("%Y-%m-%d")

    return events.to_dict(orient="records")


# ---------------------------------------------------------------------
# Date Filtering
# ---------------------------------------------------------------------

def get_prices_between(start, end):
    """
    Filter prices by date.
    """

    prices = load_prices()

    mask = (
        (prices["Date"] >= pd.to_datetime(start))
        &
        (prices["Date"] <= pd.to_datetime(end))
    )

    prices = prices.loc[mask]

    prices["Date"] = prices["Date"].dt.strftime("%Y-%m-%d")

    return prices.to_dict(orient="records")


# ---------------------------------------------------------------------
# Bayesian Results
# ---------------------------------------------------------------------

def get_change_points():
    """
    Load Bayesian model output.
    """

    if CHANGE_POINT_FILE.exists():

        with open(CHANGE_POINT_FILE, "r") as file:
            return json.load(file)

    return {
        "change_point": None,
        "message": "No Bayesian results found."
    }


# ---------------------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------------------

def get_dashboard_metrics(start=None, end=None):
    prices = load_prices()

    if start and end:
        prices = prices[
            (prices["Date"] >= pd.to_datetime(start))
            &
            (prices["Date"] <= pd.to_datetime(end))
        ]

    return {
        "average_price": round(prices["Price"].mean(), 2),
        "maximum_price": round(prices["Price"].max(), 2),
        "minimum_price": round(prices["Price"].min(), 2),
        "volatility": round(prices["Price"].std(), 2),
        "observations": len(prices)
    }

# ---------------------------------------------------------------------
# Event Details
# ---------------------------------------------------------------------

def get_event(event_id):
    """
    Retrieve a single historical event.
    """

    events = load_events()

    result = events.loc[
        events["event_id"] == event_id
    ]

    if result.empty:
        return None

    event = result.iloc[0].copy()

    event["start_date"] = event["start_date"].strftime("%Y-%m-%d")
    event["end_date"] = event["end_date"].strftime("%Y-%m-%d")
  
    return event.to_dict()
