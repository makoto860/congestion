data = {
    2020: 75000,
    2021: 50000,
    2022: 90000,
    2023: 250000,
    2024: 300000,
    2025: 150000,
}

years = sorted(data.keys())

# 増減を計算
changes = []

for i in range(1, len(years)):
    prev = data[years[i - 1]]
    current = data[years[i]]
    changes.append(current - prev)

# 平均増減
avg_change = sum(changes) / len(changes)

# 2025年から予測
prediction = data[2025] + avg_change

print("平均増減数:", avg_change)
print("2026年予測人数:", int(prediction))

# 時間別
from datetime import datetime

hour = datetime.now().hour

if 8 <= hour <= 10:
    level = "激混み"
elif 11 < hour <= 14:
    level = "混雑"
else:
    level = "通常"

print("現在時刻:", hour)
print("混雑状況:", level)
