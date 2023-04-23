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
import plotly.graph_objects as go

import dash_table_experiments as dt

from dataprep import sanity_check


# Run our sanity check function on each dataframe
b_process, b_risk, b_controls, b_actions, a_process, a_risk, a_controls, a_actions, ca, cb = sanity_check()

# get the data for our Control activity gauge
controla = ca.value_counts()
controlb = cb.value_counts()
cards = go.Figure()

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_process,
    delta={'reference': a_process},
    domain={'row': 1, 'column': 0},
    title={"text": "<b>Processes</b>", 'font': {'size': 24}},
    number={"font": {"size": 60}},
        )
    )

# cards.add_trace(go.Indicator(
#     mode="number+delta",
#     value=b_risk,
#     delta={'reference': a_risk},
#     domain={'row': 1, 'column': 2},
#     title={"text": "<b>Risks</b>", 'font': {'size': 24}},
#     number={"font": {"size": 60}},
#         )
#     )
#
# cards.add_trace(go.Indicator(
#     mode="number+delta",
#     value=b_controls,
#     delta={'reference':a_controls},
#     domain={'row': 1, 'column': 3},
#     title={"text": "<b>Controls</b>", 'font': {'size': 24}},
#     number={"font": {"size": 60}},
#         )
#     )
#
# cards.add_trace(go.Indicator(
#     mode="number+delta",
#     value=b_actions,
#     delta={'reference': a_actions},
#     domain={'row': 1, 'column': 4},
#     title={"text": "<b>Actions</b>", 'font': {'size': 24}},
#     number={"font": {"size": 60}},
#         )
#     )

control = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=controla[0],
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Manual or Automatic", 'font': {'size': 24}},
    delta={'reference': controlb[0], 'increasing': {'color': "RebeccaPurple"}},
    gauge={
        'axis': {'range': [None, 1500], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#008080"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "silver",
        'steps': [
            {'range': [0, 750], 'color': '#808000'},
            {'range': [750, 1500], 'color': '#800080'},

        ],

    }))

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col([html.H1('Analytics Dashboard',style={"width":"100%"})],width=12),
        ]),
    dbc.Row([
        dbc.Col([html.H4("General Numbers", style={"width": "100%"})],width=6),
        ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='stats', figure=cards)], xs=12, sm=12, md=12, lg=7, xl=7)],width=1),
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
    app.run_server(debug=False, port=8050)