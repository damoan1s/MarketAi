import yfinance as yf
import pandas as pd

def load_data(interval="1h", period="2y"):
    spot = yf.download("XAUUSD=X", period=period, interval=interval)
    fut  = yf.download("GC=F",      period=period, interval=interval)

    # sync timestamps
    common = spot.index.intersection(fut.index)
    spot = spot.loc[common]
    fut  = fut.loc[common]

    # rename for consistency
    spot = spot.rename(columns=str.lower)
    fut  = fut.rename(columns=str.lower)

    return spot, fut


def normalize(spot, fut):
    """Ensure both dataframes have same structure."""
    cols = ["open", "high", "low", "close", "volume"]
    spot = spot[cols].copy()
    fut  = fut[cols].copy()
    return spot, fut
