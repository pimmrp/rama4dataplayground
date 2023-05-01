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

# button = html.Button('DOWNLOAD DATA FROM BLUETOOTH SENSORS', id='download-button')

datatable = {'Point': ['1', '2', '3','4','5'],
        'Name': ['Kasemrat Intersection','Rama IV Intersection','Khlong Toei intersection','Na Ranong Intersection','Sunlakakon Intersection'],
        }
dftable = pd.DataFrame(datatable)
dftable.style.set_properties(**{'text-align': 'center'})

# @app.callback(
#     Output('url', 'pathname'),
#     [Input('download-button', 'n_clicks')]
# )
# def download_zip(n_clicks):
#     if n_clicks is not None:
#         return 'https://github.com/pimmrp/Rama4-dataplayground/raw/main/BTsensors_Jan-Feb2023.zip'

info_layout = html.Div(
    [
    dbc.Row([
        dbc.Col(html.H1("Information about the project",
                        className='text-center text-primary mb-4'),
                width=12)
    ],style={
            "margin-top": "20px"
        },
    ),

        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#D8F1F1',
            'padding': '20px',"margin-top": "20px"
        },
        children=[
            html.H3('About us')
        ]
    )
    ]),
    dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '5px',"margin-top": "20px"
        },
        children=[
            html.P(
                    ['     This project is a part of the Rama 4 Model that utilizes traffic data from January-February 2566 obtained from Bluetooth sensors, NDRS sensors,',html.Br(),
                    'and Traffic Signal sensors installed in the Rama 4 Model project. The data was collected at the intersection of Rama 4 Road and Kasemrat Road,',html.Br(),
                     'as well as on Rama 4 Road in the Khlong Toei district, to create a Data Playground that includes visualization of the data analysis.',html.Br(),'The areas are shown in the table below.'])
        ]
        
    )

    ]),

        dbc.Row([
        dbc.Col([
        html.Img(src="https://sv1.picz.in.th/images/2023/04/29/yx13sa.png", style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"})
        ],
            #style={"display": "flex", "justify-content": "left", "align-items": "left","margin-top": "30px", "margin-bottom": "60px"},
            style={"margin-top": "30px", "margin-bottom": "60px","margin-right":"0px"}
        ),
        dbc.Col([
        html.H5("The names of each point",style={"margin-top": "40px","margin-left": "20"}),
        dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in dftable.columns],
        data=dftable.to_dict('records')#,
        #style={"margin-bottom": "60px"}
        ),
        ]),
        dbc.Col([
        html.H5("          ")
    

        ])

    ]),
        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F5FBFF',
            'padding': '10px',"margin-top": "20px"
        },
        children=[
            html.P('Traffic Signal sensors',style={'font-size': '22px'})
        ]
        )
        ]),
        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '5px',"margin-top": "20px"
        },
        children=[
            html.Li(
                    ['There is data from 3 sensors located at major intersections in Nakhon Ratchasima, Khlong Toei, and Kasemrat.'
                     ],style={'font-size':'14px'}),
            html.Li(
                    ['The sensors will detect the status of traffic lights in all formats at those intersections, with data from February 2023.'
        ],style={'font-size':'14px'}),
        ]
        
    )

        ]),
        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F5FBFF',
            'padding': '10px',"margin-top": "20px"
        },
        children=[
            html.P('NDRS sensors',style={'font-size': '22px'})
        ]
        )
        ]),
                dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '5px',"margin-top": "20px"
        },
        children=[
            html.Li(
                    ['There are 5 sensor points in the vicinity of the 5 aforementioned intersections on the table.'
                     ],style={'font-size':'14px'}),
            html.Li(
                    ['The data includes the number and type of vehicles detected by cameras during the period of sufficient light, which is data from January 2023 between 6:00 am and 1:00 pm.'
        ],style={'font-size':'14px'}),
        ]
        
    )

        ]),
        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F5FBFF',
            'padding': '10px',"margin-top": "20px"
        },
        children=[
            html.P('Bluetooth sensors',style={'font-size': '22px'})
        ]
        )
        ]),

        dbc.Row([
        html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '5px',"margin-top": "20px"
        },
        children=[
            html.Li(
                    ['There is data from sensors on the main route between the 5 aforementioned intersections on the table.'
                     ],style={'font-size':'14px'}),
            html.Li(
                    ['The sensors will detect the speed of passing cars every 5 minutes, with data from January-February 2023.'
        ],style={'font-size':'14px'}),
        ]
        
    )

        ]),

    dbc.Row([
    html.Div([
        html.A("Download file", href='https://github.com/pimmrp/Rama4-dataplayground')
    ],style={'font-size':'30px',"margin-top": "50px"})


    ])
])