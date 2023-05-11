import requests
import json
import matplotlib.pyplot as plt
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
#import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
from app import app
import plotly.graph_objs as go
#import dash_table
from dash import dash_table
from dash import html

#########################Traffic signal sensor at kasemrad junction###############################
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']

url = "https://github.com/pimmrp/rama4dataplayground/raw/master/ks.json"
response = requests.get(url)
json_data = response.json()
jsonks = pd.DataFrame(json_data)['data']
#jsonks = pd.read_json(r'/Users/pim/Desktop/datapg-main/app/ks.json')['data']

urlkt = "https://github.com/pimmrp/rama4dataplayground/raw/master/kt.json"
responsekt = requests.get(urlkt)
json_datakt = responsekt.json()
jsonkt = pd.DataFrame(json_datakt)['data']

urlnr = "https://github.com/pimmrp/rama4dataplayground/raw/master/nr.json"
responsenr = requests.get(urlnr)
json_datanr = responsenr.json()
jsonnr = pd.DataFrame(json_datanr)['data']

#jsonkt = pd.read_json(r'/Users/pim/Desktop/datapg-main/app/kt.json')['data']
#jsonnr = pd.read_json(r'/Users/pim/Desktop/datapg-main/app/nr.json')['data']
data_ks = []
data_kt = []
data_nr = []
#kasemrad
#kasemrad
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

for i in range (len(jsonnr)):
    data_nr.append({'timestamp':jsonnr[i]['timestamp'],
            'phase_1':jsonnr[i]['data']['phase_1'],
            'phase_2':jsonnr[i]['data']['phase_2'],
            'phase_3':jsonnr[i]['data']['phase_3'],
            'phase_4':jsonnr[i]['data']['phase_4'],
            'phase_5':jsonnr[i]['data']['phase_5'],
            'phase_6':jsonnr[i]['data']['phase_6'],
            'phase_7':jsonnr[i]['data']['phase_7'],
            'phase_8':jsonnr[i]['data']['phase_8']})
for i in range (len(jsonkt)):
    data_kt.append({'timestamp':jsonkt[i]['timestamp'],
            'phase_1':jsonkt[i]['data']['phase_1'],
            'phase_2':jsonkt[i]['data']['phase_2'],
            'phase_3':jsonkt[i]['data']['phase_3'],
            'phase_4':jsonkt[i]['data']['phase_4'],
            'phase_5':jsonkt[i]['data']['phase_5'],
            'phase_6':jsonkt[i]['data']['phase_6'],
            'phase_7':jsonkt[i]['data']['phase_7'],
            'phase_8':jsonkt[i]['data']['phase_8']})
df_ks = pd.DataFrame(data_ks)
df_ks.timestamp = pd.to_datetime(df_ks.timestamp)
df_ks['day']=df_ks['timestamp'].dt.day_name()
df_ks.set_index('timestamp',inplace = True)
df_nr = pd.DataFrame(data_nr)
df_nr.timestamp = pd.to_datetime(df_nr.timestamp)
df_nr['day']=df_nr['timestamp'].dt.day_name()
df_nr.set_index('timestamp',inplace = True)

df_kt = pd.DataFrame(data_kt)
df_kt.timestamp = pd.to_datetime(df_kt.timestamp)
df_kt['day']=df_kt['timestamp'].dt.day_name()
df_kt.set_index('timestamp',inplace = True)


##kasemrad
df_ksm = df_ks.between_time("07:00:00", "10:00:00")
df_kse = df_ks.between_time("16:00:00","19:00:00")
##khlong toei
df_ktm = df_kt.between_time("07:00:00", "10:00:00")
df_kte = df_kt.between_time("16:00:00","19:00:00")
### na ranong
df_nrm = df_nr.between_time("07:00:00", "10:00:00")
df_nre = df_nr.between_time("16:00:00","19:00:00")


###############
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df_ksm = df_ksm[df_ksm["day"].isin(weekdays)]
df_kse = df_kse[df_kse["day"].isin(weekdays)]

df_ktm = df_ktm[df_ktm["day"].isin(weekdays)]
df_kte = df_kte[df_kte["day"].isin(weekdays)]

df_nrm = df_nrm[df_nrm["day"].isin(weekdays)]
df_nre = df_nre[df_nre["day"].isin(weekdays)]

###
# df_ksm=df_ksm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()



# df_kse=df_kse.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()


# ####
# df_ktm=df_ktm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()



# df_kte=df_kte.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()


# ####3
# df_nrm=df_nrm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()



# df_nre=df_nre.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum()



df_ksm=df_ksm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)

df_kse=df_kse.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)

df_ktm=df_ktm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)

df_kte=df_kte.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)

df_nrm=df_nrm.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)

df_nre=df_nre.reset_index().groupby(pd.Grouper(key='timestamp', axis=0, freq='D')).sum(numeric_only=True)


df_ksm = df_ksm.reset_index()
df_ksm['day']=df_ksm['timestamp'].dt.day_name()
df_kse = df_kse.reset_index()
df_kse['day']=df_kse['timestamp'].dt.day_name()

df_ktm = df_ktm.reset_index()
df_ktm['day']=df_ktm['timestamp'].dt.day_name()
df_kte = df_kte.reset_index()
df_kte['day']=df_kte['timestamp'].dt.day_name()

df_nrm = df_nrm.reset_index()
df_nrm['day']=df_nrm['timestamp'].dt.day_name()
df_nre = df_nre.reset_index()
df_nre['day']=df_nre['timestamp'].dt.day_name()

# df_ksm =df_ksm.groupby(by=['day']).mean()/60
# df_ksm = df_ksm.reset_index()
# df_kse =df_kse.groupby(by=['day']).mean()/60
# df_kse = df_kse.reset_index()

# df_ktm =df_ktm.groupby(by=['day']).mean()/60
# df_ktm = df_ktm.reset_index()
# df_kte =df_kte.groupby(by=['day']).mean()/60
# df_kte = df_kte.reset_index()

# df_nrm =df_nrm.groupby(by=['day']).mean()/60
# df_nrm = df_nrm.reset_index()
# df_nre =df_nre.groupby(by=['day']).mean()/60
# df_nre = df_nre.reset_index()

df_ksm = df_ksm.groupby(by=['day']).mean(numeric_only=True)/60
df_ksm = df_ksm.reset_index()

df_kse = df_kse.groupby(by=['day']).mean(numeric_only=True)/60
df_kse = df_kse.reset_index()

df_ktm = df_ktm.groupby(by=['day']).mean(numeric_only=True)/60
df_ktm = df_ktm.reset_index()

df_kte = df_kte.groupby(by=['day']).mean(numeric_only=True)/60
df_kte = df_kte.reset_index()

df_nrm = df_nrm.groupby(by=['day']).mean(numeric_only=True)/60
df_nrm = df_nrm.reset_index()

df_nre = df_nre.groupby(by=['day']).mean(numeric_only=True)/60
df_nre = df_nre.reset_index()

#######################################Layout##############################################
tf_layout = html.Div(
    [
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),

  
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
    dbc.Row([
        html.H3('Traffic Signal Phase At Kasem Rat Junction',className='text-center text-primary mb-4'),
    ]),
     

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
        dbc.Col(html.H4("Morning rush hours (7:00AM-10:00AM)",
                        className='text-center text-danger mb-4'),
                width=6),
        dbc.Col(html.H4("Evening rush hours (4:00PM-7:00PM)",
                        className='text-center text-danger mb-4'),
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

    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
     
    dbc.Row([
        html.H3('Traffic Signal Phase At Na Ranong Junction',className='text-center text-primary mb-4'),
    ]), 
     
     
    dbc.Row([
       html.Img(src='https://sv1.picz.in.th/images/2023/05/01/yEM5K0.png', alt='image',height="480",width="6")
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
        id='day-dropdown2',
        options=[{'label': day, 'value': day} for day in df_nrm['day'].unique()],
        value=df_nrm['day'].unique()[0]
    )]),
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            ])
    ]),

    dbc.Row([
        dbc.Col(html.H4("Morning rush hours (7:00AM-10:00AM)",
                        className='text-center text-danger mb-4'),
                width=6),
        dbc.Col(html.H4("Evening rush hours (4:00PM-7:00PM)",
                        className='text-center text-danger mb-4'),
                width=6),
                ]),


    dbc.Row([
        dbc.Col([
            
            dcc.Graph(id='bar-chart-3')
        ],width=6#width={'size':5, 'offset':0, 'order':2},
           
        ),
        dbc.Col([
           
            dcc.Graph(id='bar-chart-4', figure={})
        ], #width={'size':5, 'offset':0, 'order':2},
           width=6),
    
    ]),
     
      dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
     
    dbc.Row([
        html.H3('Traffic Signal Phase At Khlong Toei Junction',className='text-center text-primary mb-4'),
    ]), 
     
     
     
     
     
     
     dbc.Row([
       
       
        html.Img(src='https://sv1.picz.in.th/images/2023/05/01/yEMoat.jpg', alt='image',height="480",width="6")
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
        id='day-dropdown3',
        options=[{'label': day, 'value': day} for day in df_ktm['day'].unique()],
        value=df_ktm['day'].unique()[0]
    )]),
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            ])
    ]),

    dbc.Row([
        dbc.Col(html.H4("Morning rush hours (7:00AM-10:00AM)",
                        className='text-center text-danger mb-4'),
                width=6),
        dbc.Col(html.H4("Evening rush hours (4:00PM-7:00PM)",
                        className='text-center text-danger mb-4'),
                width=6),
                ]),


    dbc.Row([
        dbc.Col([
            
            dcc.Graph(id='bar-chart-5')
        ],width=6#width={'size':5, 'offset':0, 'order':2},
           
        ),
        dbc.Col([
           
            dcc.Graph(id='bar-chart-6', figure={})
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
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}

    
    
    
@app.callback(
    dash.dependencies.Output('bar-chart-2', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')])
def update_bar_chart_2(selected_day):
    filtered_data = df_kse[df_kse['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'], y=values)
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}

###
@app.callback(
    dash.dependencies.Output('bar-chart-3', 'figure'),
    [dash.dependencies.Input('day-dropdown2', 'value')])

def update_bar_chart3(selected_day):
    filtered_data = df_nrm[df_nrm['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4','Phase 5','Phase 6','Phase 7','Phase 8'], y=values)
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}

    
    
@app.callback(
    dash.dependencies.Output('bar-chart-4', 'figure'),
    [dash.dependencies.Input('day-dropdown2', 'value')])
def update_bar_chart4(selected_day):
    filtered_data = df_nre[df_nre['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4','Phase 5','Phase 6','Phase 7','Phase 8'], y=values)
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}




####
@app.callback(
    dash.dependencies.Output('bar-chart-5', 'figure'),
    [dash.dependencies.Input('day-dropdown3', 'value')])

def update_bar_chart5(selected_day):
    filtered_data = df_ktm[df_ktm['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4','Phase 5','Phase 6','Phase 7','Phase 8'], y=values)
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}

    
    
@app.callback(
    dash.dependencies.Output('bar-chart-6', 'figure'),
    [dash.dependencies.Input('day-dropdown3', 'value')])
def update_bar_chart6(selected_day):
    filtered_data = df_kte[df_kte['day'] == selected_day]
    values = filtered_data.iloc[0, 1:].tolist()
    bar_chart = go.Bar(x=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4','Phase 5','Phase 6','Phase 7','Phase 8'], y=values)
    layout = {'yaxis': {'title': 'Minutes'}}
    return {'data': [bar_chart], 'layout': layout}
