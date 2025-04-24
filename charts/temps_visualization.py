import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data/Precipitaton_and_temps.csv', parse_dates=['DATE'])


# Filter for July 18 to July 22
df_filtered = df[(df['DATE'].dt.month == 7) & (df['DATE'].dt.day >= 18) & (df['DATE'].dt.day <= 22)]
df_filtered['Year'] = df_filtered['DATE'].dt.year


# Group and summarize precipitation
grouped = df_filtered.groupby('Year').agg({
    'PRCP': 'sum'
}).reset_index()


# Plot precipitation bar chart
fig_precip = go.Figure()
fig_precip.add_trace(go.Bar(x=grouped['Year'], y=grouped['PRCP'], name='Total Precipitation'))


fig_precip.update_layout(
    title='Total Precipitation (July 18–22, 2015–2025)',
    xaxis=dict(
        title='Year',
        tickmode='linear',
        tick0=grouped['Year'].min(),
        dtick=1
    ),
    yaxis_title='Precipitation (inches)'
)


fig_precip.show()
fig_precip.write_html()