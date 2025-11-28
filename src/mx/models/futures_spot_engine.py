# Futures–Spot Differential Engine

## وصف عام
هذا المحرك يحسب مؤشرات الاختلاف العددية والزمنية بين سلاسل الأسعار (Futures vs Spot). يوفر مؤشرات مثل: HH-LL ranges, % change over window, normalized delta, time-lag cross-correlation، ومصفوفة اختلافات متعددة الفريمات.

## مدخلات
- OHLCV Futures، OHLCV Spot (مزامنة زمنية مطابقة).
- windows: قائمة نوافذ (e.g., [20,50,100,200]).
- normalization method: [zscore, minmax, none].
- correlation_lag_max: أقصى تأخر زمني للاختبار.

## مخرجات
- df_metrics: جدول بالـmetrics لكل نافذة: {range_fut, range_spot, delta_range, pct_fut, pct_spot, delta_pct, cross_corr, lag_of_max_corr}
- signal_summary: تجميع مبسط: {dominant_market: FUTURES|SPOT|NEUTRAL, strength_score}

## منطق التشغيل
1. مزامنة السلاسل زمنياً (align timestamps).
2. للكل نافذة:
   - range = max(high)-min(low) أو HH-LL
   - pct_change = (last - first)/first *100
   - delta_range = range_fut - range_spot
   - normalized_delta = normalize(delta_range)
3. حساب cross-correlation عند lags من -L..+L لمعرفة أي سوق يسبق الآخر.
4. قرار قيادة السوق:
   - إذا cross_corr_peak occurs at positive lag (futures leads) و normalized_delta > threshold ⇒ futures leading.
   - عكس ذلك لspot.
5. إنتاج تقارير زمنية ومخططات للـheatmap.

## ملاحظات
- هذا المحرك هو الأساس الكمي الذي تغذي به نماذج DWAM/LSA.
- يجب أن يكون دقيقًا في محاذاة timestamps لأن تأخير 1 شمعة يمكنه قلب الاستنتاج.
