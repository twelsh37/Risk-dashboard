# -*- coding: utf-8 -*-
'''
Documentation: - Delete when complete
* Talk to 'Future You' readint the methods and classes 6/8 months from now.
* Future you has spent those months on 5/6 other projects and cant
remember any of this.
* Future you doesn't have time to spend a full day trying to 'get
into' the code in order to fix a bug / adapt a method.
* Be Generous to future you, that will be you some day.

DESCRIPTION:

Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 22/04/2023
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


import dash_table_experiments as dt



app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = \
dbc.Container\
([
    html.Br(),
    dbc.Row([
    dbc.Col([dbc.Button("row 1 col 1",style={"width":"100%"})],width=3),
    dbc.Col([dbc.Button("row 1 col 2", style={"width": "100%"})],width=3),
    dbc.Col([dbc.Button("row 1 col 3",style={"width":"100%"})],width=3),
    dbc.Col([dbc.Button("row 1 col 4",style={"width":"100%"})],width=3),
    ]),
    html.Br(),
    dbc.Row([
    dbc.Col([dbc.Button("row 2 col 1",style={"width":"100%"})],width=3),
    dbc.Col([dbc.Button("row 2 col 2", style={"width": "100%"})],width=3),
    dbc.Col([dbc.Button("row 2 col 3",style={"width":"100%"})],width=6),
    ]),
    html.Br(),
    dbc.Row([
    dbc.Col([dbc.Button("row 3 col 1",style={"width":"100%"})],width=9),
    dbc.Col([dbc.Button("row 3 col 2", style={"width": "100%"})],width=3),
    ])
])

if __name__ == "__main__":
    app.run_server(debug=False, port=8050, host='0.0.0.0')