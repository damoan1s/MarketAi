# PROJECT CONFIG — MarketAI

PAIR: GOLD  
SPOT: "XAUUSD=X"  
FUTURES: "GC=F"

TIMEFRAMES:
- 1m
- 5m
- 15m
- 1h
- 4h
- 1D

ANGLE FORMULA:
theta = atan(ΔPrice / ΔBars) * (180/pi)

PEAKS RULE:
Swing High = 2 left + 2 right

LATE WICK RULE:
Spot wick after Futures peak = ignored

MAIN PIPELINE:
All blocks share same gold data loaded by SHARED_DATA_PIPELINE.py
