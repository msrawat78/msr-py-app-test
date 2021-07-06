import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


#df = pd.read_csv('https://github.com/msrawat78/msr-py-app-test/stocks.csv')
df = pd.read_csv('stocks.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        date, GOOG = 'date', 'GOOG'
    else:
        GOOG, date = 'GOOG', 'date'

    fig = px.line(df, x=date, y=GOOG)    
    return fig

app.run_server(debug=True)

