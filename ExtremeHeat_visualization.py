import pandas as pd
import plotly.express as px
import plotly.io as pio

file_path = '../data/extreme_heat.csv'
df = pd.read_csv(file_path)

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])

df['Year'] = df['date'].dt.year
df['Day'] = df['date'].dt.strftime('%m-%d')

fig = px.bar(
    df, x='Year', y='temp', color='Day',
    title="Extreme Heat Over the Years",
    labels={'Year': 'Year', 'temp': 'Temperature (°F)', 'Day': 'Date'},
    hover_data={'Day': True}
)

fig.update_layout(barmode='group')

pio.write_html(fig, file="extreme_heat_plot.html", auto_open=False)

# fig.show()