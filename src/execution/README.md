# Execution Layer — Order, Risk & Webhook System

The execution/ directory handles everything related to trade execution.

It is separated into three main components:

---

## 1. API Layer
Located in:
- api/webhook_api.py

Purpose:
- Receive webhook signals (internal or external)
- Validate payloads
- Route execution requests to the engine

---

## 2. Execution Engine
Located in:
- engine/executor.py

Purpose:
- Build orders
- Send executions through API bridges (future)
- Confirm fills
- Store logs

---

## 3. Risk Management
Located in:
- risk/risk_manager.py

Purpose:
- Position sizing
- Daily drawdown limits
- Rule enforcement (no over-exposure / no revenge trading)
- Safety checks

---

## Note
Actual API integration (MT5, FIX, brokers) will be added later.  
Currently, the system is designed around Webhook-first architecture.
