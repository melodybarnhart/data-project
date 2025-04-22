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
df['wind_speed'] = df['wspd'].astype(float)
df['wind_direction'] = df['wdir'].astype(float)
df['time'] = pd.to_datetime(df['date'])

# Create a line plot with arrows
fig = go.Figure()

# Plot wind speed
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['wind_speed'],
    mode='lines+markers',
    name='Wind Speed',
    fill='tozeroy',  # Fill under the line
    marker=dict(size=5, color='#87CEEB')
))

# Add a horizontal line for average wind speed
average_wind_speed = df['wind_speed'].mean()
fig.add_trace(go.Scatter(
    x=df['time'],
    y=[average_wind_speed] * len(df),  # Constant y-value for the average
    mode='lines',
    name='Average Wind Speed',
    line=dict(color='red', dash='dash')  # Red dashed line
))

# Add annotation for peak wind speed
max_idx = df['wind_speed'].idxmax()
max_time = df['time'][max_idx]
max_speed = df['wind_speed'][max_idx]

fig.update_layout(
    title='Wind Speed Over Time',
    xaxis_title='Time',
    yaxis_title='Wind Speed (m/s)',
    annotations=[
        dict(
            x=max_time, y=max_speed,
            xref="x", yref="y",
            text="Peak Wind",
            showarrow=True,
            arrowhead=4,
            ax=0, ay=-50,
            arrowcolor="#4682B4",  # Arrow color
            font=dict(color="#4682B4", size=12)  # Font color for annotation
        )
    ]
)

fig.show()

# save to html file
fig.write_html('wind_speed_plot.html')
