import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
df = pd.read_csv('data/Water Temperatures.csv')

# Convert the DATE column to a datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Ensure TEMP is a float
df['Temp'] = df['TEMP'].astype(float)

# Filter the DataFrame for dates between July 18–22 in all years
start_date = '07-18'
end_date = '07-22'
df = df[df['DATE'].dt.strftime('%m-%d').between(start_date, end_date)]

# Extract year and day for visualization
df['Year'] = df['DATE'].dt.year
df['Day'] = df['DATE'].dt.strftime('%m-%d')

# Create the bar chart
fig = px.bar(
    df,
    x='Day',
    y='Temp',  # Corrected to reference 'Temp' instead of 'VALUE'
    color='Year',
    title='Water Temperature for July 18–22 Across Years',
    labels={'Day': 'Date (MM-DD)', 'Temp': 'Water Temperature (°F)'}
)

# Customize layout and hide the y-axis values
fig.update_layout(
    xaxis_title='Date (MM-DD)',
    yaxis_title='Water Temperature (°F)',
    bargap=0.2,
    yaxis=dict(
        showticklabels=False,  # Hides y-axis tick labels
        showgrid=False,        # Optionally hides the grid lines
    )
)

# Show the plot
fig.show()

fig.write_html("water_temp.html")