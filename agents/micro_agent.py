"""
micro_agent.py
Responsible for ROOT 2 — Microstructure Engine
- Delta / CVD / Wick timing / Absorption detection
- Produces micro.json with micro-signals
"""

import pandas as pd
import numpy as np
import json
from typing import Dict, Any

class MicroAgent:
    def init(self):
        self.name = "micro_agent"

    def load_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path, parse_dates=['datetime']).set_index('datetime')

def compute_cvd(self, df: pd.DataFrame) -> pd.Series:
        # naive example: buy_volume - sell_volume (requires dataset with buy/sell)
        if 'buy_volume' in df.columns and 'sell_volume' in df.columns:
            return (df['buy_volume'] - df['sell_volume']).cumsum()
        else:
            # fallback: use close diff * volume as proxy
            return (df['close'].diff().fillna(0) * df['volume']).cumsum()

    def wick_timing(self, df: pd.DataFrame) -> Dict[str,Any]:
        # detect long lower/upper wicks per bar
        wick_info = {"lower_wicks": 0, "upper_wicks": 0}
        wick = (df['high'] - df['low']) - abs(df['close'] - df['open'])
        # simple thresholds
        wick_info['avg_wick'] = float(wick.mean())
        return wick_info

    def run(self, csv_path: str, out_path: str):
        df = self.load_csv(csv_path)
        cvd = self.compute_cvd(df)
        wick = self.wick_timing(df)
        out = {
            "cvd_last": float(cvd.iloc[-1]) if len(cvd)>0 else None,
            "wick": wick,
        }
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)
        print("MicroAgent done ->", out_path)

if name == "main":
    import sys
    ma = MicroAgent()
    csv_in = sys.argv[1] if len(sys.argv)>1 else "src/data/example_ohlcv.csv"
    out = sys.argv[2] if len(sys.argv)>2 else "agents/runtime/micro.json"
    ma.run(csv_in, out)
