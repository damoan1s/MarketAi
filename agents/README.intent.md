# Intent Agent (agents/intent_agent.py)
هذا الـ Agent يحول قوانين حالة Spot/Futures إلى كشف قواعدي بسيط.
- مدخلات: ملف CSV للسبوت و ملف CSV للفيوتشر (index datetime في العمود الأول).
- مخرجات: agents/runtime/intent.json
- تشغيل: python3 agents/intent_agent.py --spot src/data/spot.csv --fut src/data/fut.csv
