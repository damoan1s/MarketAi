import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Day 5 — Library Test Started")

# اختبار pandas
df = pd.DataFrame({
    "num": [1, 2, 3],
    "value": [10, 20, 30]
})
print("Pandas OK — DataFrame created:")
print(df)

# اختبار numpy
arr = np.array([5, 10, 15])
print("NumPy OK — array:", arr)

# اختبار matplotlib (رسم بسيط)
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Day 5 Test Plot")
plt.show()

print("Day 5 — Test Completed Successfully")
