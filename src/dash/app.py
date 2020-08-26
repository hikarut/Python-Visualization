# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

b1_data = pd.read_csv('src/data/b1_2019.csv')

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig = px.bar(b1_data, x="home_team", y="attendance", color="home_victory", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash B-league'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Dropdown(
        id = 'dropdown-for-example',
        options = [{'label': i, 'value': i} for i in b1_data.arena.unique()],
        # value = 'arena'
        value = b1_data.arena.min()
    ),
    dcc.Graph(
        id='example-graph',
        # figure=fig
    )
])

@app.callback(
    Output('example-graph', 'figure'),
    [Input('dropdown-for-example', 'value')])

def update_figure(selected):
    filtered_df = b1_data[b1_data.arena == selected]

    fig = px.bar(filtered_df, x="home_team", y="attendance", color="home_victory", barmode="group")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8001, debug=True)