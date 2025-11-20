import pandas as pd

print("🔍 Day 6 Test Started...")

# 1) تحديد مسار ملف CSV
csv_path = "/home/damoan1s/Desktop/MarketAi/data/example_data/ohlcv_sample.csv"

# 2) قراءة ملف CSV
df = pd.read_csv(csv_path)

print("\n📄 CSV Loaded Successfully!")
print(df)

# 3) طباعة آخر صف
print("\n🔚 Last Row:")
print(df.tail(1))

print("\n✅ Day 6 Completed Successfully!")
