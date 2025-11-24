# Microstructure Detection Utilities

## وصف عام
مجموعة دوال وخوارزميات صغيرة لالتقاط إشارات microstructure: wick detection, absorption detection (based on volume + body/wick ratio), footprint approximations، وmicro candle classification (e.g., long-wick, inside-bar, blunted bar).

## مدخلات
- OHLCV (Futures & Spot)
- params: wick_ratio_threshold, body_ratio_threshold, volume_spike_multiplier

## مخرجات
- per_candle_tags: لكل شمعة علامة (e.g., 'long_upper_wick', 'long_lower_wick', 'inside', 'engulfing', 'volume_spike')
- absorption_zones: نطاقات سعرية مقترنة بزمن ومؤشرات ثقة
- micro_events: لائحة بأحداث مفصلّة (timestamp, type, strength)

## وظائف رئيسية
- detect_wick(candle): return wick_length, wick_ratio, tag
- detect_absorption(window): uses cumulative volume & wicks to score absorption
- classify_candle_pattern(window): returns patterns like 'stop-hunt', 'exhaustion', 'breakout_confirm'

## ملاحظات تنفيذية
- صمّم هذه المكتبة بسيطة للتوسع، وتعمل كـ dependency مع DWAM/LSA/Futures–Spot Engine.
- عند غياب حجم موثوق، استخدم بدائل كمية (e.g., tick_count proxy).
