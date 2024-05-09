import folium
import pandas as pd

# ファイルからデータ読み込み
df = pd.read_csv('Pick100Up.csv')

# NaN を含む行を取り除く
df = df.dropna(subset=['Lat', 'Lon'])

# 地図の作成
map = folium.Map(location=[df.iloc[0]['Lat'], df.iloc[0]['Lon']], zoom_start=10)

# マーカーの追加
for i, r in df.iterrows():
    folium.Marker(location=[r['Lat'], r['Lon']], popup=r['Date/Time']).add_to(map)

# 地図を保存
map.save("Pick100Up.html")
