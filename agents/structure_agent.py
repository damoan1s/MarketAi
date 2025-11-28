"""
structure_agent.py
Responsible for ROOT 1 — Market Structure Engine
- Detect peaks/valleys (HH/LL)
- Compute angles / DWAM
- Export structure.json (trend / angles / peaks)
"""

from dataclasses import dataclass, asdict
import pandas as pd
import numpy as np
import json
from typing import Dict, Any, List, Tuple

@dataclass
class Peak:
    idx: int
    time: str
    price: float
    type: str  # "HH" or "LL"

class StructureAgent:
    def init(self):
        self.name = "structure_agent"

    # I/O ------------------------------------------------
    def load_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path, parse_dates=['datetime']).set_index('datetime')

    def save_structure(self, out: Dict[str, Any], path: str):
        with open(path, "w") as f:
            json.dump(out, f, indent=2, default=str)

    # Core utils -----------------------------------------
    def find_peaks(self, series: pd.Series, L:int=2, R:int=2) -> List[Peak]:
        peaks = []
        highs = series.values
        for i in range(L, len(highs)-R):
            left_max = highs[i-L:i].max()
            right_max = highs[i+1:i+R+1].max()
            if highs[i] > left_max and highs[i] >= right_max:
                peaks.append(Peak(i, str(series.index[i]), float(highs[i]), "HH"))
        return peaks

    def angle_between(self, p1: Tuple[int,float], p2: Tuple[int,float]) -> float:
        # p = (index, price)
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return 0.0
        rad = np.arctan2(dy, dx)
        deg = np.degrees(rad)
        return float(deg)

    # High-level -----------------------------------------
    def run(self, csv_path: str, out_path: str):
        df = self.load_csv(csv_path)  # expects column "high"
        highs = df['high']
        peaks = self.find_peaks(highs)
        angles = []
        for i in range(len(peaks)-1):
            p1 = (peaks[i].idx, peaks[i].price)
            p2 = (peaks[i+1].idx, peaks[i+1].price)
            angles.append(self.angle_between(p1, p2))
        out = {
            "peaks": [asdict(p) for p in peaks],
            "angles": angles,
            "summary": {
                "n_peaks": len(peaks),
                "angle_mean": float(np.mean(angles)) if angles else None
            }
        }
        self.save_structure(out, out_path)

if name == "main":
    import sys
    sa = StructureAgent()
    csv_in = sys.argv[1] if len(sys.argv)>1 else "src/data/example_ohlcv.csv"
    out = sys.argv[2] if len(sys.argv)>2 else "agents/runtime/structure.json"
    sa.run(csv_in, out)
    print("StructureAgent done ->", out)
