# Micro Agent
- Purpose: Microstructure analysis (CVD, wick timing, absorption)
- Inputs: OHLCV CSV (and optional buy/sell volumes)
- Outputs: micro.json (cvd_last, wick stats, micro flags)
- Run: python3 agents/micro_agent.py src/data/example_ohlcv.csv agents/runtime/micro.json
