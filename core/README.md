# Core — MarketAI Logical Engine

The core/ directory contains the heart of the MarketAI system.  
It implements the logical engines that correspond to the four ROOT levels:

---

## ROOT 1 — Market Structure Engine
Located in:
- divergence/
- parts of intent_engine/microstructure_filters.py

Includes:
- Swing detection
- Angle deviation
- Differential slope analysis
- Structure compression/expansion

---

## ROOT 2 — Smart Indicators
Located in:
- absorption/

Includes:
- Absorption zone mapping
- Imbalance scanning
- Liquidity pressure modeling

---

## ROOT 3 — Multi-Market Intent Engine
Located in:
- data_collector/
- intent_engine/futures_spot_delta.py

Includes:
- Spot vs futures deviation analysis
- Multi-market data synchronization
- Normalization and compression filters

---

## ROOT 4 — Decision Engine
Located in:
- decision_engine/

Includes:
- Swing model strategies
- Day-trading model strategies
- Scalping strategies

---

## Note
No execution happens here.  
This layer only decides — it does not execute trades.

Execution is handled in /execution.

