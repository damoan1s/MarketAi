import yfinance as yf
import pandas as pd

def load_gold(interval="1h", period="2y"):
    spot = yf.download("XAUUSD=X", period=period, interval=interval)
    fut  = yf.download("GC=F",      period=period, interval=interval)

    # sync timestamps
    common = spot.index.intersection(fut.index)
    spot = spot.loc[common]
    fut  = fut.loc[common]

    return spot, fut

if name == "main":
    s, f = load_gold()
    print("Spot:", s.shape)
    print("Futures:", f.shape)
