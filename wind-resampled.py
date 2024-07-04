import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from os import walk


mypatch = "weather_data"
files = next(walk(mypatch), (None, None, []))[2]

file_path = mypatch + "\\" + files[-1]
df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')

df['DateTime'] = pd.to_datetime(df['Time'], format='%d-%m-%Y %H:%M', dayfirst=True)

df.set_index('DateTime', inplace=True)
df_hourly = df['Wind(m/s)'].resample('H').mean().reset_index()

wind_stats = df_hourly['Wind(m/s)'].describe().round(2)

stat_text = (
    f'Count: {wind_stats["count"]}\n'
    f'Mean: {wind_stats["mean"]}\n'
    f'Std: {wind_stats["std"]}\n'
    f'Min: {wind_stats["min"]}\n'
    f'25%: {wind_stats["25%"]}\n'
    f'50%: {wind_stats["50%"]}\n'
    f'75%: {wind_stats["75%"]}\n'
    f'Max: {wind_stats["max"]}'
)

plt.figure(figsize=(16, 8))
plt.plot(df_hourly['DateTime'], df_hourly['Wind(m/s)'], linestyle='-', color='b', label='Prędkość wiatru (m/s)')

plt.xlabel('Data i czas')
plt.ylabel('Prędkość wiatru (m/s)')
plt.title('Prędkość wiatru co godzinę')

plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

plt.xticks(rotation=45)
plt.grid(True)
plt.legend([stat_text], loc='upper right')

plt.tight_layout()
plt.show()
