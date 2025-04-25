import pandas as pd
import plotly.express as px

df = pd.read_csv("data/wind.csv")

def deg_to_compass(deg):
    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    ix = int((deg + 22.5) % 360 / 45)
    return dirs[ix]


df['dir_compass'] = df['wdir'].apply(deg_to_compass)


fig = px.bar_polar(df, r="wspd", theta="dir_compass", direction="clockwise",
                   color="wspd", color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(title="Wind Rose with Compass Directions")
fig.show()
fig.write_html("wind_rose.html")
