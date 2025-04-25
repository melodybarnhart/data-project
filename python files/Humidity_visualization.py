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

#Create DataFrame(df)
df = pd.DataFrame(data, columns=header)

#Convert column types, converts the datetime strings into datetime objects,
#easier to filter and rhum converts it to floating numbers
df['time'] = pd.to_datetime(df['time'])
df['rhum'] = df['rhum'].astype(float)

#Filter DataFrame,
#where it helps manage the range of the graph (so it doesn't look as scrunched up),
#where it only shows data from july between the days 18-22
df = df[(df['time'].dt.month == 7) & (df['time'].dt.day.isin(range(18, 23)))]

#extracts the year from the time. calculates data offset from july 18th (created the offset due to otherwise they'd fall on the same vertical line,)
#subtracting the 18 seem to help center calculations around the middle of the month
#then line 30 combines the year and the scaled day offset,
#helps distinguish and helps show how the humidity changed between each day,
df['year'] = df['time'].dt.year
df['day_offset'] = df['time'].dt.day - 18
df['x_position'] = df['year'] + (df['day_offset'] * 0.2)

#finally we plot the scatter points, combining it all, just the bland stuff
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
