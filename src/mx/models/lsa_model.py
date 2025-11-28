# Liquidity Sweep Asymmetry (LSA) Model

## وصف عام
LSA يكشف عمليات "sweep" أو "stop-hunt" المنظمة التي تنفذها المؤسسات لجمع سيولة فوق/تحت مستويات معينة. يركز على مقارنة كسر التيول (wicks) عبر Futures و Spot وتحديد حالات كسر شامل (full sweep) مقابل كسر جزئي.

## مدخلات
- سلسلة OHLCV لـ Futures و Spot.
- قائمة مستويات مهمة (local highs/lows, prior swing highs/lows).
- window_sweep: عدد الشموع حول المستوى للننظر إليها.
- حجم عصري (volume) إن توفر: يُستخدم لتمييز sweep حقيقي من حركة سعرية بسيطة.

## مخرجات
- LSA_event: {type: FULL_SWEEP | PARTIAL_SWEEP | NO_SWEEP, confidence}
- swept_levels: قائمة المستويات التي تم فيها عملية المسح
- notes: توضيح إذا ما كانت العملية متزامنة مع DWAM أو منفصلة.

## ملخص المنطق
1. تعرّف local swing highs/lows في النافذة.
2. فحص كل swing: هل توجد شموع في Futures تكسر أعلى الذيل (wick) فوق المستوى عدد مرات >= k؟ (مثلاً 2-3)
3. فحص نفس المستوى في Spot: هل كُسرت الـwicks بنفس الشدة أو أقل؟
4. تعريف FULL_SWEEP إذا: Futures يقضي على كل الذيول/مستويات الستوب (k>=2) وSpot يكسر ذيل واحد أو لا يكسره.
5. حساب confidence بناءً على حجم (volume spike) وDelta_range ووجود تجمع شمعي.
6. دمجها مع DWAM: إذا DWAM يشير لعدم تماثل وLSA=FULL_SWEEP ⇒ احتمال توزيع عالي.

## ملاحظات
- LSA يحذر من سيناريو "take profit run" أو "liquidity grab" قبل الانعكاس.
- يستخدم لتمييز "جمع السيولة" عن "حركة سعرية صحية".
