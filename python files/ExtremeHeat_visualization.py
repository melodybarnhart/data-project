import pandas as pd
import plotly.express as px


file_path = 'extreme heat.csv'
df = pd.read_csv(file_path)

df['date'] = pd.to_datetime(df['DATE'], errors='coerce')
df = df.dropna(subset=['date'])

df['Year'] = df['date'].dt.year
df['Day'] = df['date'].dt.strftime('%m-%d')

fig = px.bar(
    df, x='Year', y='TEMP', color='Day',
    title="Extreme Heat Over the Years",
    labels={'Year': 'Year', 'TEMP': 'Temperature (°F)', 'Day': 'Date'},
    hover_data={'Day': True}
)

fig.update_layout(barmode='group')

fig.write_html("extreme_heat.html")

#fig.show()
