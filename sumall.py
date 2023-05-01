import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from app import app
import os
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
from dash import dash_table
import numpy as np
pd.options.plotting.backend = "plotly"

sumall_layout = html.Div(
    [
    dbc.Row([
        dbc.Col(html.H1("Summary of data",
                        className='text-center text-primary mb-4'),
                width=12)
    ],style={
            "margin-top": "20px"
        },
    ),
    dbc.Row([
    html.Div(
    style={
        'backgroundColor': '#D2DBD6',
        'padding': '10px',"margin-top": "20px"
    },
    children=[
        html.H4('Morning Rush Hour (7.00-10.00 am)')
    ]
    )
    ]),
    dbc.Row([
        html.P(['People have to try to catch a ride to work and get on Sukhumvit Road. There will be cars coming from Rama III Road',html.Br(),
               'that have to pass through Na Ranong Intersection to Rama IV Intersection.',html.Br(),
                'The data collected shows that this is related to information from all sensors:'],style={'font-size':'16px'}),
        html.Li([
            'The number of cars is higher than usual.'],style={'font-size':'14px'}
        ),
        html.Li([
            'The speed of the cars is lower than usual.'],style={'font-size':'14px'}
        ),
        html.Li([
            'There is a traffic light phase that allows cars to move more smoothly.'],style={'font-size':'14px'}
        ),
        html.Li([
            'There are cars coming from the expressway at the port and traveling through the Sunlakakon intersection to the Kasemrat intersection.'],style={'font-size':'14px'}
        ),
        html.Li([
            'There are cars coming from On Nut and Bangna that travel through Kasemrat to Rama IV and turn up to Sirikit Center.'],style={'font-size':'14px'}
        ),
        html.P(['There may also be some parts from Rama IV to Klong Toei that are congested as well.'],style={'font-size':'16px'}),
    
    ], style={
        'backgroundColor': '#FFF8F8',
        'padding': '10px',"margin-top": "20px"}
    ),
    
    dbc.Row([
    html.Div(
    style={
        'backgroundColor': '#D2DBD6',
        'padding': '10px',"margin-top": "20px"
    },
    children=[
        html.H4('Evening Rush Hour (4.00-7.00 pm)')
    ]
    )
    ]),
    dbc.Row([
        html.P(['There are convergence points of cars from the shortcut roads of Sukhumvit 22, 24, and 26',html.Br(),
               'to the expressway at the Sunlakakon intersection. Therefore, there is more Phase 2 traffic light opening',html.Br(),
                'than in the morning.'],style={'font-size':'16px'}),
        html.Li([
            'There is a need to travel through Kasemrat to Sunlakakon and congestion between Rama IV to Kasemrat.'],style={'font-size':'14px'}
        ),
        html.Li([
            'Some cars also need to turn onto Sukhumvit Road, causing the traffic to move slowly.'],style={'font-size':'14px'}
        ),
        html.P(['The route from Klong Toei intersection to Rama IV will have more cars because in the evening rush hour,',html.Br(),
                'people need to travel back home, alternating with Rama IV to Na Ranong or the expressway.'],style={'font-size':'16px'}),
    
    ], style={
        'backgroundColor': '#FFF8F8',
        'padding': '10px',"margin-top": "20px"}
    ),
    dbc.Row([
    html.Div(
    style={
        'backgroundColor': '#D2DBD6',
        'padding': '10px',"margin-top": "20px"
    },
    children=[
        html.H4('Additional information')
    ]
    )
    ]),
    dbc.Row([
        html.Li([
            "On Valentine's Day and rainy days, there will be more traffic congestion than usual, and the speed of cars will be slower than normal."],style={'font-size':'14px'}
        ),
        html.Li([
            'Kasemrat to Rama IV has many double-parked cars, which take up one lane. This may cause more cars than usual',html.Br(),
            'and the speed of the cars that are close to 0 km/hr is higher than in other areas.'
            ],style={'font-size':'14px'}
        ),
    ], style={
        'backgroundColor': '#FFF8F8',
        'padding': '10px',"margin-top": "20px"}
    ),











    # dbc.Row([
    # html.P([
    #     html.Ul([
    #     html.Li(["From the graph1"],style={'font-size': '12px'}),
    #     html.P(["It was found that the trend of this route is that the vehicle speed is very slow in the evening (traffic congestion).", html.Br(),
    #                    "This is due to the fact that in the evening, many vehicles need to use this route.",html.Br(),
    #                    "Moreover, there are converging points of cars from the shortcut roads of Sukhumvit 22, 24, and 26 to the expressway at the Sunlakakon intersection.",html.Br(),
    #                    "Some also need to turn onto Sukhumvit Road, causing the traffic to move slowly."],style={'font-size': '10px'}),
    #     html.Li(["From the graph2"],style={'font-size': '12px'}),
    #     html.Li(["From the graph3"],style={'font-size': '12px'}),
    #     html.Li(["From the graph4"],style={'font-size': '12px'})
    #     ])

    # ])
    # ])
])