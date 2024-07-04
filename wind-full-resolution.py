import pandas as pd
import matplotlib.pyplot as plt
from os import walk
from pylab import *


mypatch = "weather_data" 
files = next(walk(mypatch), (None,None ,[]))[2]

file_path = mypatch + "\\" + files[-1]
df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')


df['DateTime'] = pd.to_datetime(df['Time'])

wind_stats = df['Wind(m/s)'].describe().round(2)

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
plt.plot(df['DateTime'], df['Wind(m/s)'], linestyle='-', color='b', label='Prędkość wiatru (m/s)')

plt.xlabel('Data i czas')
plt.ylabel('Prędkość wiatru (m/s)')
plt.title('Szczegółowa prędkość wiatru w czasie')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend([stat_text], loc='upper right')

plt.tight_layout()
plt.show()