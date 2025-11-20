"""
📌 Day 5 — Library Quick Card
الغرض من هذا الملف:
- تلخيص ما تعلمناه اليوم عن المكتبات
- إنشاء مثال بسيط ونظيف (بدون تعقيد)
- الاستعداد لـ Repo 1C و Root 1

المكتبات الأساسية:
- pandas : معالجة البيانات والجداول
- numpy : العمليات الرقمية
- matplotlib : الرسم البياني
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=== Day 5 Quick Card ===")

# 1) pandas example
data = {
    "price": [10, 11, 13],
    "volume": [100, 120, 90]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# 2) numpy example
arr = np.array([1, 2, 3])
print("\nNumpy Array:", arr)

# 3) matplotlib simple plot
plt.plot(df["price"])
plt.title("Simple Price Plot (Day 5)")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()

print("\n=== Completed Successfully ===")
