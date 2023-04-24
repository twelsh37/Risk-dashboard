import dash
import dataprep
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# pull in functions from our Dataprep.py file
from dataprep import sanity_check


# Run our sanity check function on each dataframe
y2020raca, y2021raca, y2022raca, b_process, b_risk, b_controls, b_actions, a_process, a_risk, a_controls, a_actions, ca, cb\
    = sanity_check()

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
    domain={'row': 1, 'column': 1},
    title={"text": "<b>Processes</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_risk,
    delta={'reference': a_risk},
    domain={'row': 1, 'column':4},
    title={"text": "<b>Risks</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_controls,
    delta={'reference':a_controls},
    domain={'row': 1, 'column': 7},
    title={"text": "<b>Controls</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.add_trace(go.Indicator(
    mode="number+delta",
    value=b_actions,
    delta={'reference': a_actions},
    domain={'row': 1, 'column': 10},
    title={"text": "<b>Actions</b>", 'font': {'size': 24}},
    number={"font": {"size": 48}},
        )
    )

cards.update_layout(
    grid={'rows': 1, 'columns': 12, 'pattern': "independent"},
    template={'data': {'indicator': [{
        'mode': "number+delta+gauge",
        }],
                  }}
    )

control = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=controla[0],
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "<b>Manual or Automatic<br>Controls<br> </b>", 'font': {'size': 24}},
    delta={'reference': controlb[0], 'increasing': {'color': "RebeccaPurple"}},
    gauge={
        'axis': {'range': [None, 1500], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#000080"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "silver",
        'steps': [
            {'range': [0, 1500], 'color': '#808000'},
                   ],

    }))

controlactivity = go.Figure()

# Add the histogram traces to the figure
for column_header in ['control_activity']:
    controlactivity.add_trace(go.Histogram(x=y2020raca[column_header], name='2020', marker={'color': '#AA4639'}))
    controlactivity.add_trace(go.Histogram(x=y2021raca[column_header], name='2021', marker = {'color': '#AA7139'}))
    controlactivity.add_trace(go.Histogram(x=y2022raca[column_header], name='2022', marker = {'color': '#255C69'}))

# See Plotly documentation for customizations: https://plotly.com/python/reference/histogram/
controlactivity.update_layout(
    xaxis_title='control_activity',
    title='<b>Control Activity by Type<b>',
    barmode='group',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_linecolor = 'Black',
    yaxis_linecolor = 'Black',
    xaxis_categoryorder = "category ascending",
    yaxis_title='Number',
)

de_oe = go.Figure()


# Add the histogram traces to the figure
for column_header in ['de_oe']:
    de_oe.add_trace(go.Histogram(x=y2020raca[column_header], name='2020', marker = {'color': '#AA4639'}))
    de_oe.add_trace(go.Histogram(x=y2021raca[column_header], name='2021', marker = {'color': '#AA7139'}))
    de_oe.add_trace(go.Histogram(x=y2022raca[column_header], name='2022', marker = {'color': '#255C69'}))
# Update the layout

de_oe.update_layout(
	xaxis_title='Do the Risk Owners regard the Controls Effective',
    title='<b>Control Effectiveness?<b>',
    barmode='group',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_linecolor = 'Black',
    yaxis_linecolor = 'Black',
    xaxis_categoryorder = "category ascending",
    yaxis_title='Number'
)

sun = px.sunburst(
    data_frame=y2022raca,
    # Lays out the sunburst from our L1, to L2, to level 3 risk categories
    path=['risk_types', 'risk', 'level3'],
    color_continuous_scale=px.colors.sequential.BuGn,
    maxdepth=3,
    branchvalues='total',  # other option is 'remainder'
    hover_name='risk_types',
    title='Breakdown of Risk by Risk Type',
    template='presentation',
)

sun.update_layout(title_x=0.5, height=900, uniformtext=dict(minsize=10))
sun.update_traces(textinfo='label+percent parent+value', insidetextorientation='radial')




# Bootstrap it up
# ------------------------------------------------------------------------------
app.layout = dbc.Container([html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([html.H1('RACA Dashboard', style={"width": "100%"})],  width=12),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='stats', figure=cards)], className='three columns', width=6),
        dbc.Col([dcc.Graph(id='control1', figure=controlactivity)], className='three columns', width=3),
        dbc.Col([dcc.Graph(id='control2', figure=de_oe)], className='three columns', width=3),
    ], className='row'),
        dbc.Col([dcc.Graph(id='sunburst', figure=sun)], className='three columns', width=6),
    ]),
], fluid=True)

app.run_server(debug=True)

