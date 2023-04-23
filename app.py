import dash
import dataprep
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

# pull in functions from our Dataprep.py file
from dataprep import sanity_check


# Run our sanity check function on each dataframe
b_process, b_risk, b_controls, b_actions, a_process, a_risk, a_controls, a_actions, ca, cb = sanity_check()

# get the data for our Control activity gauge
controla = ca.value_counts()
controlb = cb.value_counts()

# Dash App below
#------------------------------------------------------------------------------
# Set Dash app title
app = dash.Dash(__name__, title='RACA Analytics', external_stylesheets=[dbc.themes.BOOTSTRAP])

cards = go.Figure()

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_process,
    delta={'reference': a_process},
    domain={'row': 1, 'column': 0},
    title={"text": "<b>Processes</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_risk,
    delta={'reference': a_risk},
    domain={'row': 1, 'column':2},
    title={"text": "<b>Risks</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_controls,
    delta={'reference':a_controls},
    domain={'row': 1, 'column': 4},
    title={"text": "<b>Controls</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_actions,
    delta={'reference': a_actions},
    domain={'row': 1, 'column': 6},
    title={"text": "<b>Actions</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

control = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=controla[0],
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "<b>Manual or Automatic<br>Controls<br> </b>", 'font': {'size': 24}},
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



cards.update_layout(
    grid={'rows': 1, 'columns': 12, 'pattern': "independent"},
    template={'data': {'indicator': [{
        'mode': "number+delta+gauge",
        }],
                  }}
    )



# control.update_layout(paper_bgcolor="lavender", font={'color': "darkblue", 'family': "Arial"})

# Bootstrap it up
# ------------------------------------------------------------------------------
app.layout = dbc.Container([html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([html.H1('Analytics Dashboard', style={"width": "100%"})], width=12),
    ]),
    dbc.Row([
        dbc.Col([html.H4("General Numbers", style={"width": "100%"})], width=6),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='stats', figure=cards)], className='three columns', width=6),
        dbc.Col([dcc.Graph(id='control1', figure=control)], className='three columns', width=3),
        dbc.Col([dcc.Graph(id='control2', figure=control)], className='three columns', width=3),
    ], className='row'),
    html.Hr(),
# dbc.Row([
#         dbc.Col([dcc.Graph(id='stats2', figure=cards)], width=6),
#     ]),
]),
], fluid=True)

app.run_server(debug=True)

