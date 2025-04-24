import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio

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


fig = px.scatter(
    df, x='x_position', y='rhum',
    color='day_offset',
    title='Humidity Levels (July 18–22 Only)',
    labels={'x_position': 'Year', 'rhum': 'Humidity', 'day_offset': 'Day Offset'},
    opacity=0.7
)
fig.update_traces(marker=dict(size=10))


html_file_path = 'humidity_report.html'
pio.write_html(fig, file=html_file_path, auto_open=False)

print(f"Report generated: Open '{html_file_path}' in your browser.")
