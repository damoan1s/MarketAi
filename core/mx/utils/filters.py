cat << 'EOF' > MarketAI/core/mx/utils/filters.py
def smooth(values):
    # simple smoothing for microstructure signals
    return sum(values) / len(values) if values else 0
EOF
