import csv
import pandas as pd
import matplotlib.pyplot as plt

file_path = '../data/humidity.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
data = data[1:]

df = pd.DataFrame(data, columns=header)

df['time'] = pd.to_datetime(df['time'])
df['rhum'] = df['rhum'].astype(float)

df = df[(df['time'].dt.month == 7) & (df['time'].dt.day.isin(range(18, 23)))]

df['year'] = df['time'].dt.year

df['day_offset'] = df['time'].dt.day - 18

df['x_position'] = df['year'] + (df['day_offset'] * 0.2)

plt.figure(figsize=(12, 6)) 
plt.scatter(df['x_position'], df['rhum'], color='black', alpha=0.7, s=30, label='Humidity')
plt.xlabel('Year')
plt.ylabel('Humidity')
plt.title('Humidity Levels (July 18–22 Only)')
plt.legend()
plt.xticks(df['year'].unique())
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.savefig('humidity_plot.png') 

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Humidity Levels Report</title>
</head>
<body>
    <h1>Humidity Levels (July 18–22 Only)</h1>
    <img src="humidity_plot.png" alt="Humidity Plot">
</body>
</html>
"""

with open('humidity_report.html', 'w') as html_file:
    html_file.write(html_content)

print("Report generated: Open 'humidity_report.html' in your browser.")
