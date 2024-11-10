from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

app = Dash(__name__)

fig = px.scatter(df, x='V', y='S')

app.layout = html.Div([dcc.Graph(figure=fig)],
                     )

if __name__ == "__main__":
   app.run(debug=True)
