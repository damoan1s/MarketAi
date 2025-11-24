cat << 'EOF' > MarketAI/progress/100_days_plan.md
# MarketAI – 100 Day Master Plan (Rebuilt Version)
*Institutional-Level Market Intelligence System*

---

# 🔵 Phase 1 — Foundation (Days 1–20)
## الهدف: بناء الأساس + أدوات بسيطة + قراءة البيانات + الرسم

### Day 1–5: Setup & Basics
- إنشاء هيكل المشروع
- ضبط Python environment
- تثبيت المكتبات الضرورية
- بناء ملفات README الأساسية
- تنظيم المجلدات Core / Data / MX / Engine

### Day 6–10: Data Handling
- قراءة CSV
- تنظيف البيانات
- التطبيع (Normalization)
- استخراج الشموع، الذيل، المدى HH–LL
- بناء أول مكتبة DataLoader

### Day 11–20: Visualization Layer
- بناء أول أدوات Plotting
- رسم Candles
- رسم فريمات متعددة
- رسم Futures vs Spot على نفس الشارت
- استخراج الزوايا البسيطة
- حفظ الصور للتحليل اليدوي

---

# 🟣 Phase 2 — Market Structure Intelligence (Days 21–40)
## الهدف: بناء Root 1 (Market Structure Engine)

### Day 21–30: Swing & Structure
- كود استخراج القمم والقيعان
- مزامنة الفيوتشر والفوري
- استخراج HH/HL/LH/LL
- زاوية الحركة (Slope Engine)

### Day 31–40: Intent Preparation
- حسـاب ranges
- حساب wick asymmetry
- حساب microstructure noise
- بناء ملف microstructure_engine.py
- ربطه مع Data Loader

---

# 🔴 Phase 3 — MX Intelligence Layer (Days 41–60)
## الهدف: بناء DWAM – LSA – M5 – Futures/Spot Intelligence

### Day 41–48: DWAM Model
- كشف عدم تناسق الذيول
- قراءة نمط السيولة
- بناء DWAM Model
- إضافة Readme

### Day 49–54: LSA Model
- Liquطات Sweep Algorithm
- اكتشاف الامتصاص
- بناء LSA Model
- توثيق النموذج

### Day 55–58: Futures–Spot Engine
- استخراج الفروقات
- تحليل السبق الزمني
- تحليل القوة
- تقييم الانعكاس

### Day 59–60: M5 Engine
- دمج كل هذه العوامل
- بناء m5_engine.py
- إضافة m5_readme.md
- اختبار يدوي على الشارت

---

# 🟢 Phase 4 — DNA Engine (Days 61–75)
## الهدف: تحويل التحليل إلى “قواعد نية سوق” (Market Intent Ruleset)

### Day 61–68: DNA Phases
- Absorption
- Discrepancy
- Exhaustion
- Release
- Expansion

### Day 69–75: DNA Engine
- ربط MX داخل DNA
- بناء Ruleset
- إخراج intent النهائي:
  - BUY  
  - SELL  
  - NEUTRAL  
  - REVERSE_SOON  
  - ABSORBING  
  - EXPANDING  

---

# 🟡 Phase 5 — Backtesting Engine (Days 76–85)
## الهدف: اختبار كل شيء

- بناء backtester بسيط
- استدعاء DNA Engine
- تجربة 3 نماذج:
  - Swing Trading
  - Day Trading
  - Scalping (خفيف)
- نتائج أولية
- حفظ تقارير في ui/reports

---

# 🟠 Phase 6 — Execution Layer (Days 86–95)
## الهدف: بناء نظام تداول حقيقي

- بناء Executor
- Simulation Mode فقط
- إدارة المخاطر Risk Manager
- Position Manager
- لا يوجد API حقيقي بعد

---

# 🟤 Phase 7 — Automation & v1 Release (Days 96–100)
## الهدف: أول نسخة MarketAI v1 جاهزة للعمل

- دمج كل شيء
- تحسين الكود
- إنشاء ملف config
- نظام Logs
- واجهة Dashboard بسيطة (HTML + Python)
- اختبار سيناريوهات متعددة
- إنتاج النسخة v1.0

---

# 🟩 Output at Day 100

- MarketAI v1.0  
- DNA Engine جاهز  
- MX Intelligence جاهز  
- Backtesting جاهز  
- Trading Simulator جاهز  
- توقعات مؤسسية راقية  
- مشروع يمكنك الاعتماد عليه في التداول الآلي  
- بدون أي خسائر مالية — جميع الاختبارات محلية  

EOF
