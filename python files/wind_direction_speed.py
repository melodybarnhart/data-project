import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('wind.csv')
#reads the date as a real date
df['date'] = pd.to_datetime(df['date'])
#find the year in the date
df['year'] = df['date'].dt.year
#find the day
df['day_of_year'] = df['date'].dt.dayofyear

#create the figure
fig = go.Figure()
#add wind direction and wind speed
fig.add_trace(go.Scatter(x=df['date'], y=df['wspd'], mode='lines', name='Wind Speed (m/s)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=df['date'], y=df['wdir'], mode='lines', name='Wind Direction (°)', line=dict(color='red')))
#find the averages
avg_wspd = df['wspd'].mean()
avg_wdir = df['wdir'].mean()
#avg wind speed line
fig.add_trace(go.Scatter(x=df['date'], y=[avg_wspd] * len(df),
                         mode='lines', name=f'Average Wind Speed ({avg_wspd:.2f} m/s)',
                         line=dict(color='blue', dash='dash')))
#avg wind direction line
fig.add_trace(go.Scatter(x=df['date'], y=[avg_wdir] * len(df),
                         mode='lines', name=f'Average Wind Direction ({avg_wdir:.2f}°)',
                         line=dict(color='red', dash='dash')))

fig.update_layout(
    title='Wind Speed and Direction',
    xaxis_title='Date',
    yaxis_title='Wind Speed (m/s)',
    yaxis2=dict(title='Wind Direction (°)', overlaying='y', side='right'),
    template='plotly_dark'
)

fig.show()
#write the html file
fig.write_html("wind_speed_direction.html")
