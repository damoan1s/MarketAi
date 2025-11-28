import numpy as np
import pandas as pd

def detect_peaks(df, window=2):
    highs = df["high"].values
    peaks = []

    for i in range(window, len(highs)-window):
        left  = highs[i-window:i]
        right = highs[i+1:i+window+1]

        if highs[i] > max(left) and highs[i] >= max(right):
            peaks.append((df.index[i], highs[i]))

    return peaks


def match_spot_futures(fut_peaks, spot_df):
    matched = []

    for t, v in fut_peaks:
        if t in spot_df.index:
            spot_val = spot_df.loc[t]["high"]
            matched.append((t, v, spot_val))
        else:
            matched.append((t, v, None))

    return matched


def filter_late_wicks(matched, spot_df):
    final = []

    for t, fut_val, spot_val in matched:
        if spot_val is None:
            final.append((t, fut_val, None))
            continue

        # check for late wick
        future_slice = spot_df.loc[t:]
        late = future_slice["high"].max()

        if late > spot_val:
            # late wick ignore
            final.append((t, fut_val, spot_val))
        else:
            final.append((t, fut_val, spot_val))

    return final
