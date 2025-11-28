#!/usr/bin/env python3
# intent_agent.py

import argparse
import json
import math
from pathlib import Path

import pandas as pd
import numpy as np


def read_csv(path):
    df = pd.read_csv(path, parse_dates=True, index_col=0)
    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = np.nan
    return df


def swing_highs(series, L=2, R=2):
    highs = []
    N = len(series)
    for i in range(L, N - R):
        left = series.iloc[i - L:i].max()
        right = series.iloc[i + 1:i + 1 + R].max()
        if series.iloc[i] > left and series.iloc[i] >= right:
            highs.append(i)
    return highs


def swing_lows(series, L=2, R=2):
    lows = []
    N = len(series)
    for i in range(L, N - R):
        left = series.iloc[i - L:i].min()
        right = series.iloc[i + 1:i + 1 + R].min()
        if series.iloc[i] < left and series.iloc[i] <= right:
            lows.append(i)
    return lows


def angle_degrees(price1, price2, bars):
    if bars == 0:
        return 0.0
    slope = (price2 - price1) / bars
    return math.degrees(math.atan(slope))


def get_last_two_points(series, idx_list):
    if len(idx_list) < 2:
        return None
    i1, i2 = idx_list[-2], idx_list[-1]
    return (series.iloc[i1], i1), (series.iloc[i2], i2)


def lower_wick_ratio(row):
    rng = row["High"] - row["Low"]
    if rng == 0:
        return 0
    return (row["Close"] - row["Low"]) / rng


def detect_cases(spot_df, fut_df):
    out = {"cases": [], "scores": {}}

    spot_close = spot_df["Close"].dropna()
    fut_close = fut_df["Close"].dropna()

    s_highs = swing_highs(spot_df["High"])
    f_highs = swing_highs(fut_df["High"])
    s_lows = swing_lows(spot_df["Low"])
    f_lows = swing_lows(fut_df["Low"])

    if f_highs and (not s_highs or f_highs[-1] > s_highs[-1]):
        out["cases"].append("FUTURES_BREAK_HIGH_SPOT_NOT")

    if s_highs and (not f_highs or s_highs[-1] > f_highs[-1]):
        out["cases"].append("SPOT_BREAK_HIGH_FUTURES_NOT")

    f_pts = get_last_two_points(fut_close, f_highs)
    s_pts = get_last_two_points(spot_close, s_highs)

    if f_pts and s_pts:
        (fp1, fi1), (fp2, fi2) = f_pts
        (sp1, si1), (sp2, si2) = s_pts

        f_ang = angle_degrees(fp1, fp2, fi2 - fi1)
        s_ang = angle_degrees(sp1, sp2, si2 - si1)

        diff = abs(f_ang - s_ang)

        out["scores"]["futures_angle"] = float(round(f_ang, 2))
        out["scores"]["spot_angle"] = float(round(s_ang, 2))

        if diff > 5:
            out["cases"].append("ANGLE_DISCREPANCY")

    common = spot_df.index.intersection(fut_df.index)
    if len(common) > 0:
        s_last = spot_df.loc[common].iloc[-1]
        f_last = fut_df.loc[common].iloc[-1]

        s_wick = lower_wick_ratio(s_last)
        f_wick = lower_wick_ratio(f_last)

        out["scores"]["spot_wick"] = float(round(s_wick, 3))
        out["scores"]["futures_wick"] = float(round(f_wick, 3))

        if s_wick - f_wick > 0.20:
            out["cases"].append("SPOT_LARGE_LOWER_WICK_ONLY")

        if f_wick - s_wick > 0.20:
            out["cases"].append("FUTURES_LARGE_LOWER_WICK_ONLY")

    if "Volume" in spot_df.columns and "Volume" in fut_df.columns:
        s_vol = spot_df["Volume"].iloc[-1]
        f_vol = fut_df["Volume"].iloc[-1]

        out["scores"]["spot_volume"] = int(s_vol)
        out["scores"]["futures_volume"] = int(f_vol)

        if s_vol > f_vol * 1.5:
            out["cases"].append("SPOT_VOLUME_SPIKE_ONLY")

        if f_vol > s_vol * 1.5:
            out["cases"].append("FUTURES_VOLUME_SPIKE_ONLY")

    if "FUTURES_BREAK_HIGH_SPOT_NOT" in out["cases"]:
        out["scores"]["intent_hint"] = "STRONG_LONG"
    elif "SPOT_BREAK_HIGH_FUTURES_NOT" in out["cases"]:
        out["scores"]["intent_hint"] = "FAKE_LONG"
    elif "ANGLE_DISCREPANCY" in out["cases"]:
        out["scores"]["intent_hint"] = "STRUCTURAL_DISCREPANCY"
    else:
        out["scores"]["intent_hint"] = "NO_CLEAR_INTENT"

    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spot", required=True)
    parser.add_argument("--fut", required=True)
    parser.add_argument("--out", default="agents/runtime/intent.json")
    args = parser.parse_args()

    spot = read_csv(args.spot)
    fut = read_csv(args.fut)

    result = detect_cases(spot, fut)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)

    with open(args.out, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("Saved:", args.out)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if name == "main":
    main()
