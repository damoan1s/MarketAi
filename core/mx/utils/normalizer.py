cat << 'EOF' > MarketAI/core/mx/utils/normalizer.py
def normalize_value(val, scale=1):
    return val / scale if scale != 0 else val
EOF
