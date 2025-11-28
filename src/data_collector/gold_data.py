#!/usr/bin/env python3
import yfinance as yf
import pandas as pd
from pathlib import Path

print("جاري تحميل بيانات الذهب... (اصبر 20-40 ثانية فقط)")

# الصحيح 100%
futures = yf.download("GC=F", period="1y", interval="1h", progress=False)
spot    = yf.download("XAUUSD=X", period="1y", interval="1h", progress=False)

# نطابق التواريخ بالضبط
common = futures.index.intersection(spot.index)
futures = futures.loc[common]
spot    = spot.loc[common]

# نعمل مجلد ونحفظ البيانات عشان ما ننزّلش تاني أبدًا
Path("data/gold").mkdir(parents=True, exist_ok=True)
futures.to_csv("data/gold/futures_1h.csv")
spot.to_csv("data/gold/spot_1h.csv")

print("تم بنجاح!")
print(f"عدد الشموع: {len(futures)}")
print("البيانات محفوظة في data/gold/ ومش هنحمل تاني")
