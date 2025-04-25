import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('Water Temperatures.csv', parse_dates=['DATE'])
df_filtered = df[(df['DATE'].dt.month == 7) & (df['DATE'].dt.day >= 18) & (df['DATE'].dt.day <= 22)].copy()
df_filtered['Year'] = df_filtered['DATE'].dt.year


df_avg = df_filtered.groupby('Year')['TEMP'].mean().reset_index()


colorscale = 'RdYlBu_r'

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_avg['Year'],
    y=df_avg['TEMP'],
    marker=dict(
        color=df_avg['TEMP'],
        colorscale='RdYlBu_r',
        colorbar=dict(
            title=dict(text='Avg Temp (°F)', font=dict(color='white')),
            tickfont=dict(color='white')
        ),
    ),
    name='5-Day Avg Temp'
))


start_year = df_avg['Year'].min()
end_year = df_avg['Year'].max()

fig.update_layout(
    title=f'Average Water Temperatures (July 18–22, {start_year}–{end_year})',
    title_font=dict(color='white'),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Year', tickmode='linear', dtick=1, color='white'),
    yaxis=dict(title='Temperature (°F)', color='white')
)

fig.show()
fig.write_html("water_temperatures.html")
