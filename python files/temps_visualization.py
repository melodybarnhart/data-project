import pandas as pd
import plotly.graph_objects as go


# Load the CSV
df = pd.read_csv('data/Precipitaton_and_temps.csv', parse_dates=['DATE'])


# Filter for July 18 to July 22
df_filtered = df[(df['DATE'].dt.month == 7) & (df['DATE'].dt.day >= 18) & (df['DATE'].dt.day <= 22)]
df_filtered['Year'] = df_filtered['DATE'].dt.year


# Group and calculate temperature values
grouped = df_filtered.groupby('Year').agg({
    'TMIN': 'min',
    'TMAX': 'max'
}).reset_index()
grouped['TAVG'] = (grouped['TMIN'] + grouped['TMAX']) / 2


# Plot temperature bar chart
fig_temp = go.Figure()
fig_temp.add_trace(go.Bar(x=grouped['Year'], y=grouped['TMIN'], name='Min Temp'))
fig_temp.add_trace(go.Bar(x=grouped['Year'], y=grouped['TMAX'], name='Max Temp'))
fig_temp.add_trace(go.Bar(x=grouped['Year'], y=grouped['TAVG'], name='Avg Temp'))


fig_temp.update_layout(
    title='Min, Max, and Avg Temperatures (July 18–22, 2015–2025)',
    xaxis=dict(
        title='Year',
        tickmode='linear',
        tick0=grouped['Year'].min(),
        dtick=1
    ),
    yaxis_title='Temperature (°F)',
    barmode='group'
)


fig_temp.show()
fig_temp.write_html("temps_visualization.html")
