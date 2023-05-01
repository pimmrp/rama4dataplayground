import requests
import json
import matplotlib.pyplot as plt
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
from app import app
import plotly.graph_objs as go


#########################Traffic signal sensor at kasemrad junction###############################
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
jsonks = pd.read_json(r'Signalkasem.json')['data']
data_ks = []
for i in range (len(jsonks)):
    data_ks.append({'timestamp':jsonks[i]['timestamp'],
            'phase_1':jsonks[i]['data']['phase_1'],
            'phase_2':jsonks[i]['data']['phase_2'],
            'phase_3':jsonks[i]['data']['phase_3'],
            'phase_4':jsonks[i]['data']['phase_4'],
            'phase_5':jsonks[i]['data']['phase_5'],
            'phase_6':jsonks[i]['data']['phase_6'],
            'phase_7':jsonks[i]['data']['phase_7'],
            'phase_8':jsonks[i]['data']['phase_8']})
df_ks = pd.DataFrame(data_ks)
df_ks.timestamp = pd.to_datetime(df_ks.timestamp)
df_ks['day']=df_ks['timestamp'].dt.day_name()
df_ks.set_index('timestamp',inplace = True)
df_ksm = df_ks.between_time('7:00','10:00').groupby(by=['day']).mean()
df_kse = df_ks.between_time('16:00','19:00').groupby(by=['day']).mean()
df_ksm = df_ksm.reset_index()
df_kse = df_kse.reset_index()


#######################################Layout##############################################
tf_layout = html.Div(
    [
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),

    dbc.Row(
        dbc.Col(html.H3("Traffic Signal Phase",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

    dbc.Row([
        html.Img(src='https://i.ibb.co/d6vvqbg/2565-11-03-01-22-06.png', alt='image',height="240",width="6")
    ]),
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
        ])
    ]),
    dbc.Row([

       dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in df_ksm['day'].unique()],
        value=df_ksm['day'].unique()[0]
    )]),
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            ])
    ]),

    dbc.Row([
        dbc.Col(html.H4("mornig rush hour",
                        className='text-center text-warning mb-4'),
                width=6),
        dbc.Col(html.H4("evening rush hour",
                        className='text-center text-warning mb-4'),
                width=6),
                ]),


    dbc.Row([
        dbc.Col([
            
            dcc.Graph(id='bar-chart-1')
        ],width=6#width={'size':5, 'offset':0, 'order':2},
           
        ),
        dbc.Col([
           
            dcc.Graph(id='bar-chart-2', figure={})
        ], #width={'size':5, 'offset':0, 'order':2},
           width=6),
    
    ]),
])

##########################callback##########################################

@app.callback(
    dash.dependencies.Output('bar-chart-1', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')])

def update_bar_chart(selected_day):
    filtered_data = df_ksm[df_ksm['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'], y=values)
    return {'data': [bar_chart]}
    
    
@app.callback(
    dash.dependencies.Output('bar-chart-2', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')])
def update_bar_chart_2(selected_day):
    filtered_data = df_kse[df_kse['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'], y=values)
    return {'data': [bar_chart]}