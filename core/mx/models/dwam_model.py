# Delta Wick Asymmetry Model (DWAM)

## وصف عام
DWAM هو نموذج يقوم بقياس عدم التماثل في الذيول (wicks) والامتداد بين أسعار العقود المستقبلية (Futures) وسعر السوق الفوري (Spot) عبر فترات زمنية متعددة. الهدف: كشف إشارات النية المؤسسية (leading intent) خاصة عند القمم/القيعان لتحديد احتمالات الانعكاس أو استمرار الاتجاه.

## مدخلات
- سلسلة أسعار Futures (OHLCV) على نفس الإطار الزمني (نفس فترة/نفس عدد الشموع).
- سلسلة أسعار Spot (OHLCV) على نفس الإطار الزمني.
- نافذة (window) للتحليل: عدد الشموع (مثلاً 50-200).
- إعدادات حساسية: wick_threshold (نسبة/نقطة)، delta_threshold (% أو نقاط).
- معلومات فريم أعلى (context_f): حالة الاتجاه على فريم 4H/5H/1D إن وُجدت.

## مخرجات
- DWAM_score: رقم يتراوح موجبا/سالبا أو نسبة تشير لدرجة عدم التماثل.
- DWAM_flag: [NEUTRAL | LEADING_FUTURES | LEADING_SPOT | WEAK_SIGNAL]
- تفاصيل حدث: {wick_diff, hhll_diff, last_wick_timestamp, comment}

## ملخص المنطق
1. لِكل نافذة زمنية:
   - احسب wick_length لكل شمعة = max(high - max(open,close), min(open,close) - low) حسب النوع.
   - احسب مجموع/متوسط الذيول العلوية UpperWick_Futures و UpperWick_Spot.
2. احسب Delta_wick = UpperWick_Futures - UpperWick_Spot (نقطة أو نسبة).
3. احسب حركة القمة HH-LL لكل سوق داخل النافذة: Range_Futures, Range_Spot.
4. احسب Delta_range = Range_Futures - Range_Spot.
5. وزن النتائج بمعاملات حساسية (alpha_w, alpha_r) لإنتاج DWAM_score.
6. قواعد قرار مبسطة:
   - إذا DWAM_score > X و Delta_wick متزايد خلال N شموع ⇒ LEADING_FUTURES (نية شراء/بيع مبكرة).
   - إذا DWAM_score < -X ⇒ LEADING_SPOT.
   - إذا |DWAM_score| < Y ⇒ NEUTRAL.

## حالات استثنائية
- إذا كانت السيولة منخفضة أو حجم غير متوفر: علّم الإشارة كـ "low_confidence".
- عند وجود فجوات سعرية كبرى (gaps) ارفع العتبات (thresholds).

## ملاحظات تنفيذية
- تم التصميم للعمل مع أي زوج/أصل بشرط تطابق تردد البيانات.
- الرجاء توثيق حالة الفريم الأعلى لأنها تؤثر كبيرًا على معاني الإشارة.
