import pandas as pd
import matplotlib.pyplot as plt

# Combined_data.csvファイルを読み込む
combined_data = pd.read_csv('Combined_data.csv')

# 'Date/Time' 列を日付型に変換
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# 'Date/Time' 列をインデックスに設定
combined_data.set_index('Date/Time', inplace=True)

# 1時間毎のデータを集計
hourly_counts = combined_data.resample('H').size()

# 24時間ごとに集計
hourly_counts_24h = hourly_counts.groupby(hourly_counts.index.hour).sum()

# 棒グラフで1時間毎のデータを表示
plt.figure(figsize=(10, 6))
hourly_counts_24h.plot(kind='bar', color='skyblue')
plt.title('Hourly Counts of Data')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rows')
plt.xticks(range(24), [f"{i:02}:00" for i in range(24)], rotation=45)
plt.tight_layout()
plt.show()
