#!/usr/bin/env bash
# Quick run of Block1 pipeline (structure -> micro -> intent)
python3 agents/structure_agent.py src/data/example_ohlcv.csv agents/runtime/structure.json
python3 agents/micro_agent.py src/data/example_ohlcv.csv agents/runtime/micro.json
python3 agents/intent_agent.py agents/runtime/structure.json agents/runtime/micro.json agents/runtime/intent.json
echo "Files created in agents/runtime:"
ls -la agents/runtime || true
