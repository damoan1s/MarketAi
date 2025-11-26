import csv
from datetime import datetime
import turtle

# قراءة آخر 100 نقطة بس من الـ Spot (أخف حاجة)
prices = []
dates = []
with open("data/gold/spot_1h.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) < 5: continue
        try:
            price = float(row[4])  # Close column
            prices.append(price)
        except:
            continue
    prices = prices[-100:]  # آخر 100 نقطة فقط

if not prices:
    print("ما لقيتش بيانات… تأكد إن data/gold/spot_1h.csv موجود")
    exit()

# رسم بسيط جدًا
min_p = min(prices)
max_p = max(prices)
scale_y = 400 / (max_p - min_p)
scale_x = 800 / len(prices)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-400, -200 + (prices[0]-min_p)*scale_y)
t.pendown()
t.color("gold")
t.width(3)

for i in range(1, len(prices)):
    y = -200 + (prices[i]-min_p)*scale_y
    t.goto(-400 + i*scale_x, y)

turtle.done()
print("الشارت فتح قدامك دلوقتي يا ملك!")
