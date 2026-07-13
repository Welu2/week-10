"""
Utility functions for Brent Oil Bayesian Change Point Analysis

Author: Your Name
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================================
# DATA LOADING
# ==========================================================

def load_price_data(filepath):
    """
    Load Brent oil prices.

    Parameters
    ----------
    filepath : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    filepath = Path(filepath)

    df = pd.read_csv(filepath)

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values("Date")

    df.reset_index(drop=True, inplace=True)

    return df


def load_event_data(filepath):
    """
    Load historical oil market events.

    Parameters
    ----------
    filepath : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    filepath = Path(filepath)

    events = pd.read_csv(filepath)

    events["start_date"] = pd.to_datetime(events["start_date"])
    events["end_date"] = pd.to_datetime(events["end_date"])

    events = events.sort_values("start_date")

    return events


# ==========================================================
# LOG RETURNS
# ==========================================================

def calculate_log_returns(df):
    """
    Compute daily log returns.

    Formula:
        log(P_t / P_t-1)
    """

    data = df.copy()

    data["Log_Return"] = np.log(
        data["Price"] / data["Price"].shift(1)
    )

    data.dropna(inplace=True)

    return data


# ==========================================================
# VISUALIZATION
# ==========================================================

def plot_price_series(df):
    """
    Plot Brent oil prices.
    """

    plt.figure(figsize=(15, 6))

    plt.plot(
        df["Date"],
        df["Price"],
        color="steelblue",
        linewidth=2
    )

    plt.title("Brent Oil Prices")

    plt.xlabel("Date")
    plt.ylabel("Price (USD/Barrel)")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_log_returns(df):
    """
    Plot log returns.
    """

    plt.figure(figsize=(15, 5))

    plt.plot(
        df["Date"],
        df["Log_Return"],
        color="darkred"
    )

    plt.title("Daily Log Returns")

    plt.xlabel("Date")

    plt.ylabel("Log Return")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_change_point(df, change_index):
    """
    Plot detected change point.
    """

    plt.figure(figsize=(16, 6))

    plt.plot(
        df["Date"],
        df["Price"],
        label="Brent Price",
        linewidth=2
    )

    plt.axvline(
        df.iloc[change_index]["Date"],
        color="red",
        linestyle="--",
        linewidth=2,
        label="Detected Change Point"
    )

    plt.legend()

    plt.title("Detected Bayesian Change Point")

    plt.tight_layout()

    plt.show()


# ==========================================================
# EVENT MATCHING
# ==========================================================

def nearest_event(change_date, events):
    """
    Find nearest historical event.

    Parameters
    ----------
    change_date : datetime
    events : DataFrame

    Returns
    -------
    pandas.Series
    """

    idx = (
        events["start_date"] - change_date
    ).abs().idxmin()

    return events.loc[idx]


def summarize_change(change_date, events):
    """
    Return dictionary describing
    nearest historical event.
    """

    event = nearest_event(change_date, events)

    return {
        "Change Date": change_date.date(),
        "Nearest Event": event["event_name"],
        "Category": event["category"],
        "Event Start": event["start_date"].date(),
        "Expected Direction": event["expected_direction"]
    }


# ==========================================================
# IMPACT
# ==========================================================

def calculate_percentage_change(before, after):
    """
    Percentage change between two values.
    """

    return ((after - before) / before) * 100


# ==========================================================
# REPORT
# ==========================================================

def generate_report(change_date,
                    mu_before,
                    mu_after,
                    events):
    """
    Generate interpretation dictionary.
    """

    info = summarize_change(change_date, events)

    pct = calculate_percentage_change(
        mu_before,
        mu_after
    )

    return {
        "Detected Change Point":
            change_date.date(),

        "Nearest Event":
            info["Nearest Event"],

        "Category":
            info["Category"],

        "Average Before":
            round(mu_before, 2),

        "Average After":
            round(mu_after, 2),

        "Percentage Change":
            round(pct, 2),

        "Expected Direction":
            info["Expected Direction"]
    }


# ==========================================================
# CONVERGENCE CHECK
# ==========================================================

def check_convergence(summary):
    """
    Check R-hat values.

    Parameters
    ----------
    summary : arviz.summary()

    Returns
    -------
    bool
    """

    return (summary["r_hat"] < 1.01).all()