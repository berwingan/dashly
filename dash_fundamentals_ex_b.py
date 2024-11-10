import micropip
await micropip.install("dash_ag_grid")
from dash import Dash, dcc, html
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
app = Dash(__name__)

grid = dag.AgGrid(
   id="my-table",
   rowData=df.to_dict("records"),
   columnDefs=[{"field": i} for i in df.columns],
   columnSize = "sizeToFit",
    dashGridOptions={"pagination":True,"paginationAutoPageSize":True}
)

app.layout = html.Div([grid])

if __name__ == "__main__":
   app.run(debug=True)

