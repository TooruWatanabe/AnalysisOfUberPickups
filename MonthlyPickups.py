import pandas as pd
import matplotlib.pyplot as plt

# Combined_data.csvファイルを読み込む
combined_data = pd.read_csv('Combined_data.csv')

# 'Date/Time' 列を日付型に変換
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# 月ごとの行数を計算
monthly_counts = combined_data.resample('M', on='Date/Time').size()

# 棒グラフで月毎の行数を表示
plt.figure(figsize=(10, 6))
ax = monthly_counts.plot(kind='bar', color='skyblue')
plt.title('Monthly Counts of Data')
plt.xlabel('Month')
plt.ylabel('Number of Rows')
plt.xticks(rotation=0)  # X軸のラベルの回転角度を0度に設定

# 値を棒グラフに表示
for i, v in enumerate(monthly_counts):
    ax.text(i, v + 10, str(v), ha='center', va='bottom')

# X軸のラベルを設定
plt.xticks(range(len(monthly_counts)), ["Apr", "May", "Jun", "Jul", "Aug", "Sep"])

plt.tight_layout()
plt.show()
