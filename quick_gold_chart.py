import pandas as pd
import matplotlib.pyplot as plt

# قراءة البيانات
f = pd.read_csv("data/gold/futures_1h.csv", index_col=0, parse_dates=True).tail(300)
s = pd.read_csv("data/gold/spot_1h.csv", index_col=0, parse_dates=True).tail(300)

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.plot(f.index, f['close'], label="Gold Futures", color="gold")
plt.title("Gold Futures (GC=F)")
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(s.index, s['close'], label="Gold Spot", color="orange")
plt.title("Gold Spot (XAUUSD=X)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
