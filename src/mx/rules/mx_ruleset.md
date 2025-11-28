# MX Ruleset — القواعد المركزية لطبقة Market eXplainability (MX)

## 1. مبادئ عامة
- كل تحليل MX يجب أن يُجرى على نوافذ متساوية زمنياً لكل مصدر (Futures vs Spot).
- التزام بالمزامنة الزمنية (timestamps alignment) شرط أساسي.
- إشارة MX يجب أن تصنف برتبة ثقة: {low, medium, high}.
- إذا حجم البيانات أو حجم التداول ناقص → إشارة = low_confidence.

---

## 2. DWAM — قواعد تشغيل (Delta Wick Asymmetry Model)
- حسابات:
  - Wick_F_avg = mean(upper_wick_length) على نافذة W.
  - Wick_S_avg = mean(upper_wick_length) لـ Spot.
  - Delta_wick = Wick_F_avg - Wick_S_avg.
  - Range_F = HH_F - LL_F ; Range_S = HH_S - LL_S.
  - Delta_range = Range_F - Range_S.
  - DWAM_score = alpha_w * normalize(Delta_wick) + alpha_r * normalize(Delta_range).

- قواعد اتخاذ القرار:
  1. إذا DWAM_score >= +T_high و Delta_wick متزايد على K شموع متتالية → FLAG = LEADING_FUTURES (High confidence).
  2. إذا DWAM_score بين +T_low و +T_high → FLAG = WEAK_LEADING_FUTURES (Medium).
  3. إذا DWAM_score <= -T_high → FLAG = LEADING_SPOT (High confidence).
  4. إذا |DWAM_score| < T_low → FLAG = NEUTRAL (Low confidence).

- مراجعات زمنية:
  - تحقق من slope change في Futures قبل إصدار إشارة نهائية (إذا slope_Futures_down بدأ قبل slope_Spot_down → رفع الثقة).

---

## 3. LSA — قواعد تشغيل (Liquidity Sweep Asymmetry)
- تعريف كسر ذيل:
  - wick_break_F(level) = عدد الشموع في Futures التي كسرت wick فوق level خلال window_sweep.
  - wick_break_S(level) = نفس القياس في Spot.

- قواعد:
  1. FULL_SWEEP إذا wick_break_F(level) >= k_full (مثلاً 2) و wick_break_S(level) <= k_partial (مثلاً 0 أو 1).
  2. PARTIAL_SWEEP إذا 1 <= wick_break_F(level) < k_full و wick_break_S(level) <= k_partial.
  3. NO_SWEEP إذا wick_break_F(level) == 0.

- دمج مع DWAM:
  - إذا DWAM.FLAG == LEADING_FUTURES و LSA == FULL_SWEEP → إشارة توزيع (Distribution Reversal) بثقة HIGH.
  - إذا DWAM.FLAG == LEADING_FUTURES و LSA == PARTIAL_SWEEP → إشارة تحذير (Watch) بثقة MEDIUM.

---

## 4. Futures–Spot Differential Engine — قواعد تشغيل
- cross-correlation:
  - حساب cross_corr(lag)؛ إيجاد lag_max.
  - إذا lag_max > 0 (positive) → Futures يقود بالـlag_max شمعة/وحدة.
  - قوة القيادة تتناسب مع قيمة cross_corr(lag_max).

- قيادة القرار:
  - إذا normalized_delta_range > R_threshold و cross_corr_peak at positive lag و DWAM_FLAG positive → dominant_market = FUTURES.
  - إذا العكس → dominant_market = SPOT.

---

## 5. Microstructure rules
- تعريف الشمعة الامتصاصية:
  - شمعة تحمل tail طويل + حجم أعلى من avg_volume*V_mult → tag 'absorption'.
- تعريف Exhaustion:
  - تتابع من 2-3 شموع ذات wicks متزايدة مع انخفاض body_size → tag 'exhaustion'.
- Stop Hunt detection:
  - cluster of wick breaks above level without follow-through in Spot → tag 'stop_hunt'.

---

## 6. مستوى الثقة وفلترة الإشارات
- Confidence scoring:
  - start = base_score from DWAM (0..1)
  - +0.3 إذا LSA == FULL_SWEEP
  - +0.2 إذا cross_corr supports leader
  - -0.3 إذا volume data missing
- Decision thresholds:
  - score >= 0.75 → TRADE_SIGNAL (High confidence) — يمر إلى Decision Engine مع قواعد حجم محافظ.
  - 0.5 <= score < 0.75 → WATCHLIST (Medium) — راجع يدوياً أو دمجه في استراتيجيات احترازية.
  - score < 0.5 → IGNORE.

---

## 7. الملاحظات الفنية
- دوماً استخدم نافذة اختبار out-of-sample للتحقق من thresholds.
- احتفظ بسجل لكل إشارة: raw_metrics + normalized_metrics + final_score.
- اعمل logging مفصل لأي حالة استثنائية (data gaps, unusual volume spikes, market holidays).

---

## 8. أمثلة عملية
- مثال: إذا DWAM_score = 0.9 و LSA == FULL_SWEEP و cross_corr lag=+2 → HIGH probability reversal → إخراج: SELL ALERT with confidence=0.9.
- مثال: DWAM_score = 0.3 و LSA == PARTIAL_SWEEP → MEDIUM watch.
