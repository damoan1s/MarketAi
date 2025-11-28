# Structure Agent
- Purpose: Build market structure (peaks, swings, angles, DWAM helpers)
- Inputs: OHLCV CSV (indexed by datetime)
- Outputs: structure.json (peaks, angles, summary)
- Run: python3 agents/structure_agent.py src/data/example_ohlcv.csv agents/runtime/structure.json
