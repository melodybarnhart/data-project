import pandas as pd
import plotly.express as px


file_path = 'extreme heat.csv'
df = pd.read_csv(file_path)

#converts and cleans date columns,
#and removes any rows where there isn't a date/invalid values (just incase)
df['date'] = pd.to_datetime(df['DATE'], errors='coerce')
df = df.dropna(subset=['date'])

#creates columns for year and day/date
df['Year'] = df['date'].dt.year
df['Day'] = df['date'].dt.strftime('%m-%d')

#makes the bar for that (bland stuff again) 
fig = px.bar(
    df, x='Year', y='TEMP', color='Day',
    title="Extreme Heat Over the Years",
    labels={'Year': 'Year', 'TEMP': 'Temperature (°F)', 'Day': 'Date'},
    hover_data={'Day': True}
)

#used it for side by side comparision (looked nicer and neater along with more clarity)
fig.update_layout(barmode='group')

fig.write_html("extreme_heat.html")

#fig.show()
