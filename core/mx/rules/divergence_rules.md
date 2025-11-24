cat << 'EOF' > MarketAI/core/mx/rules/divergence_rules.md
# Divergence Rules – Futures vs Spot

1. إذا كان Range(Futures) > Range(Spot) بشكل ملحوظ → نية بيع.
2. إذا كان Range(Spot) > Range(Futures) → نية شراء.
3. إذا كانت الزاوية في Futures أعلى بمرتين من Spot → كسر مصطنع.
4. إذا كان الفيوتشر يكسر مستويات والسبوت يرفض → انعكاس قادم.
5. إذا تحرك السبوت قبل الفيوتشر → حركة حقيقية.
EOF
