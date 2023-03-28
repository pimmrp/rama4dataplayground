import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
import plotly.graph_objs as go
from app import app

#back end#

import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.plotting.backend = "plotly"

df1 = pd.read_csv(r'/Users/pim/Desktop/datapg-main/BTsensors___Kasemrat - Sunlakakon__2023-Feb-01 .csv')
df2 = pd.read_csv(r'/Users/pim/Desktop/datapg-main/BTsensors___Kasemrat - Sunlakakon__2023-Feb-02.csv')
df1['Date']='2023-02-01'
df1['day_name']='Wednesday'
df2['Date']='2023-02-02'
df2['day_name']='Thursday'
# Merge the files using concat
df = pd.concat([df1, df2])

# Save the merged dataframe to a new CSV file
df.to_csv('merged_file.csv', index=False)
columnlist = list(df.keys())



#dropdown_options = [{'label': i, 'value': i} for i in df['day_name'].unique()]

#front end#

#date = ['MON','TUE','WED','THU','FRI','SAT','SUN']

bt_layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H5("Data from Bluetooth Sensors",
                        className='text-center text-secondary mb-4'),
            dcc.Dropdown(id='day-dropdown',options=[{'label': day, 'value': day} for day in df['day_name'].unique()],value='Wednesday'),
            #dcc.Dropdown(id='category-dropdown',options=dropdown_options,value=df['day_name'].iloc[0]),
            
             dcc.Graph(id='speed-vs-time-graph')
        ],
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
  
 ]) # Horizontal:start,center,end,between,around
])

#callback#

# Wednesday= df.loc[df['day_name'] == 'Wednesday']
# Thursday= df.loc[df['day_name'] == 'Thursday']

# @app.callback(
#     Output('example-graph', 'figure'),
#     [Input('category-dropdown', 'value')]
# )

@app.callback(
    Output(component_id='speed-vs-time-graph', component_property='figure'),
    Input(component_id='day-dropdown', component_property='value')
)
def update_graph(selected_day):
    filtered_df = df[df['day_name'] == selected_day]
    fig = {
        'data': [{'x': filtered_df.FromTime, 'y': filtered_df.AverageSpeed, 'type': 'line'}],
        'layout': {'title': f'Speed vs. Time on {selected_day}'}
    }
    # fig.update_layout(
    #      xaxis_title="Time",
    #      yaxis_title="Average speed (km/hr)"
    # )
    return fig

# def update_graph(selected_category):
#     filtered_df = df[df['day_name'] == selected_category]
#     fig = px.line(filtered_df,x=df.FromTime, y=df.AverageSpeed, title=f'{selected_category} Data')
#     #fig = px.line(filtered_df,x=df.FromTime, y=df.AverageSpeed, title=f'{selected_category} Data')
#     fig.update_layout(
#         xaxis_title="Time",
#         yaxis_title="Average speed (km/hr)"
#     )
#     return fig




