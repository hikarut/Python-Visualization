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

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
b1_data = pd.read_csv('src/data/b1_2019.csv')
# b1_data.head()

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

    # fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
    #                  size="pop", color="continent", hover_name="country",
    #                  log_x=True, size_max=55)
    fig = px.bar(filtered_df, x="home_team", y="attendance", color="home_victory", barmode="group")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8001, debug=True)