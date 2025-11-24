cat << 'EOF' > MarketAI/core/mx/utils/calc.py
def calc_range(high, low):
    return high - low

def percent_diff(a, b):
    return ((a - b) / b) * 100 if b != 0 else 0
EOF
