import plotly.graph_objects as go
import pandas as pd
import csv

# Read the CSV file
with open('data/wind.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract the header and data
header = data[0]
data = data[1:]

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=header)
df['wind_direction'] = df['wdir'].astype(float)
df['time'] = pd.to_datetime(df['date'])


# Create a line plot with arrows
fig = go.Figure()

# Plot wind direction
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['wind_direction'],
    mode='lines+markers',
    name='Wind Direction',
    fill='tozeroy',  # Fill under the line
    marker=dict(size=5, color='#87CEEB')
))

fig.show()

#save as html file
fig.write_html("wind_direction.html")
