import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
from app import app
import plotly.graph_objects as go
# import dash_table
from dash import dash_table
import requests
import io

url = "https://github.com/pimmrp/rama4dataplayground/raw/master/01max.csv"
response = requests.get(url).content
dfmax1 = pd.read_csv(io.StringIO(response.decode('utf-8')))

url1 = "https://github.com/pimmrp/rama4dataplayground/raw/master/01min.csv"
response1 = requests.get(url1).content
dfmin1 = pd.read_csv(io.StringIO(response1.decode('utf-8')))

url2 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec01.csv"
response2 = requests.get(url2).content
df1 = pd.read_csv(io.StringIO(response2.decode('utf-8')))
###############################33
url3 = "https://github.com/pimmrp/rama4dataplayground/raw/master/02max.csv"
response3 = requests.get(url3).content
dfmax2 = pd.read_csv(io.StringIO(response3.decode('utf-8')))

url4 = "https://github.com/pimmrp/rama4dataplayground/raw/master/02min.csv"
response4 = requests.get(url4).content
dfmin2 = pd.read_csv(io.StringIO(response4.decode('utf-8')))

url5 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec02.csv"
response5 = requests.get(url5).content
df2 = pd.read_csv(io.StringIO(response5.decode('utf-8')))
########################################
url6 = "https://github.com/pimmrp/rama4dataplayground/raw/master/03max.csv"
response6 = requests.get(url6).content
dfmax3 = pd.read_csv(io.StringIO(response6.decode('utf-8')))

url7 = "https://github.com/pimmrp/rama4dataplayground/raw/master/03min.csv"
response7 = requests.get(url7).content
dfmin3 = pd.read_csv(io.StringIO(response7.decode('utf-8')))

url8 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec03.csv"
response8= requests.get(url8).content
df3 = pd.read_csv(io.StringIO(response8.decode('utf-8')))
##################################################
url9 = "https://github.com/pimmrp/rama4dataplayground/raw/master/04max.csv"
response9 = requests.get(url9).content
dfmax4 = pd.read_csv(io.StringIO(response9.decode('utf-8')))

url10 = "https://github.com/pimmrp/rama4dataplayground/raw/master/04min.csv"
response10 = requests.get(url10).content
dfmin4 = pd.read_csv(io.StringIO(response10.decode('utf-8')))

url11 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec04.csv"
response11 = requests.get(url11).content
df4 = pd.read_csv(io.StringIO(response11.decode('utf-8')))
##################################################
url12 = "https://github.com/pimmrp/rama4dataplayground/raw/master/05max.csv"
response12 = requests.get(url12).content
dfmax5 = pd.read_csv(io.StringIO(response12.decode('utf-8')))

url13 = "https://github.com/pimmrp/rama4dataplayground/raw/master/05min.csv"
response13 = requests.get(url13).content
dfmin5 = pd.read_csv(io.StringIO(response13.decode('utf-8')))

url14 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec05.csv"
response14 = requests.get(url14).content
df5 = pd.read_csv(io.StringIO(response14.decode('utf-8')))
##################################################
url15 = "https://github.com/pimmrp/rama4dataplayground/raw/master/06max.csv"
response15 = requests.get(url15).content
dfmax6 = pd.read_csv(io.StringIO(response15.decode('utf-8')))

url16 = "https://github.com/pimmrp/rama4dataplayground/raw/master/06min.csv"
response16 = requests.get(url16).content
dfmin6 = pd.read_csv(io.StringIO(response16.decode('utf-8')))

url17 = "https://github.com/pimmrp/rama4dataplayground/raw/master/Dec06.csv"
response17 = requests.get(url17).content
df6 = pd.read_csv(io.StringIO(response17.decode('utf-8')))


###################################333
# dfmax1 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/01max.csv')
# dfmin1 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/01min.csv')
# df1 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec01.csv')
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df1['day of week'] = df1['timestamp'].dt.day_of_week
df1['hour_of_day'] = df1['timestamp'].dt.hour
# ###################################333
# dfmax2 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/02max.csv')
# dfmin2 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/02min.csv')
# df2 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec02.csv')
df2['timestamp'] = pd.to_datetime(df2['timestamp'])
df2['day of week'] = df2['timestamp'].dt.day_of_week
df2['hour_of_day'] = df2['timestamp'].dt.hour
# ###################################333
# dfmax3 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/03max.csv')
# dfmin3 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/03min.csv')
# df3 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec03.csv')
df3['timestamp'] = pd.to_datetime(df3['timestamp'])
df3['day of week'] = df3['timestamp'].dt.day_of_week
df3['hour_of_day'] = df3['timestamp'].dt.hour

# ###################################333
# dfmax4 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/04max.csv')
# dfmin4 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/04min.csv')
# df4 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec04.csv')
df4['timestamp'] = pd.to_datetime(df4['timestamp'])
df4['day of week'] = df4['timestamp'].dt.day_of_week
df4['hour_of_day'] = df4['timestamp'].dt.hour

# ###################################333
# dfmax5 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/05max.csv')
# dfmin5 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/05min.csv')
# df5 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec05.csv')
df5['timestamp'] = pd.to_datetime(df5['timestamp'])
df5['day of week'] = df5['timestamp'].dt.day_of_week
df5['hour_of_day'] = df5['timestamp'].dt.hour

# ###################################333
# dfmax6 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/06max.csv')
# dfmin6 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/06min.csv')
# df6 = pd.read_csv(r'C:/Users/whai/Desktop/Senior Project/dataplayground/Dec06.csv')
df6['timestamp'] = pd.to_datetime(df6['timestamp'])
df6['day of week'] = df6['timestamp'].dt.day_of_week
df6['hour_of_day'] = df6['timestamp'].dt.hour











vehicle_types = ['7up',	'bus',	'car',	'motorcycle',	'pickup'	,'trailer'	,'truck'	] 
ndrslo = {'Location': ['1', '2', '3','4','5','6'],
        'Name': ['Soi Ari, BigC Rama4','Soi Sukhumvit 22','Ratchadaphisek Road, Ocean Tower 1',
                 'Khlong Toei Intersection ',
                 'Rama 3 Road, Soi 85','Police station Expressway 1'],
        }
dfndrslo = pd.DataFrame(ndrslo)
dfndrslo.style.set_properties(**{'text-align': 'center'})

days_map = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}





ndrs_layout = html.Div([
    
  
    dbc.Row([
         dbc.Col([
            
            html.Img(src='https://sv1.picz.in.th/images/2023/05/09/yG9QJv.jpg',  style={"float": "left", "margin-right": "20px","display": "block", "margin": "0 auto", "width": "550px", "height": "400px"})
        ],
         style={"margin-top": "30px", "margin-bottom": "60px"}
           
        ),
        dbc.Col([
         
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
          html.H3('Sensor Locations'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfndrslo.columns],
            data=dfndrslo.to_dict('records'),
        ),
           
        ], #width={'size':5, 'offset':0, 'order':2},
           ),
       
       
       
       
       
       
    ]),
    
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),

    
    
    dbc.Row([
        html.H3('Location 1: Soi Ari, BigC Rama4'),
        dbc.Col([
    
    
    
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
    dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart')

    ])
    ]),


    

   
   
    
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),
    
    
    
    
    
    
    dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax1.columns],
            data=dfmax1.to_dict('records'),
        ),
    ], className='row'),

    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
    dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin1.columns],
            data=dfmin1.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
dbc.Row([
        html.H4('Location 2: Soi Sukhumvit 22, Soi Sai Nam Thip'),
        dbc.Col([dcc.Dropdown(id='day-dropdown2',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown2',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart2')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart2')

    ])
    ]),



dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax2.columns],
            data=dfmax2.to_dict('records'),
        ),
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin2.columns],
            data=dfmin2.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),
dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),


################################################################
dbc.Row([
        html.H3('Location 3: Ratchadaphisek Road, Ocean Tower 1'),
        dbc.Col([
    
    
    
    dcc.Dropdown(
        id='day-dropdown3',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown3',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart3')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart3')

    ])
    ]),
dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax3.columns],
            data=dfmax3.to_dict('records'),
        ),
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin3.columns],
            data=dfmin3.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),
dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),





###############################################################
dbc.Row([
        html.H3('Location 4: Khlong Toei Junction '),
        dbc.Col([
    
    
    
    dcc.Dropdown(
        id='day-dropdown4',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown4',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart4')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart4')

    ])
    ]),
dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax4.columns],
            data=dfmax4.to_dict('records'),
        ),
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin4.columns],
            data=dfmin4.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),
dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
#######################################3
dbc.Row([
        html.H3('Location 5: Rama 3 Road, Soi 85 '),
        dbc.Col([
    
    
    
    dcc.Dropdown(
        id='day-dropdown5',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown5',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart5')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart5')

    ])
    ]),
dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax5.columns],
            data=dfmax5.to_dict('records'),
        ),
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin5.columns],
            data=dfmin5.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),
dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ]),
####################################################3

dbc.Row([
        html.H3('Location 6: Police station Expressway 1 '),
        dbc.Col([
    
    
    
    dcc.Dropdown(
        id='day-dropdown6',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    ),]),
    dbc.Col([
dcc.Dropdown(
    id='day-of-week-dropdown6',
    options=[
        {'label': 'Monday', 'value': 0},
        {'label': 'Tuesday', 'value': 1},
        {'label': 'Wednesday', 'value': 2},
        {'label': 'Thursday', 'value': 3},
        {'label': 'Friday', 'value': 4},
        {'label': 'Saturday', 'value': 5},
        {'label': 'Sunday', 'value': 6}
    ],
    value=0,  # Set initial value
    placeholder='Select a day of the week'
)
,

    ])
    
    
    
    
    ]),
    
dbc.Row([
    dbc.Col([
    
    dcc.Graph(id='line-chart6')
    ]),
    dbc.Col([

dcc.Graph(id='vehicle-counts-chart6')

    ])
    ]),
dbc.Row([
         html.Br(),
          html.Br(),
    
     html.H4('Top 5 days with the most number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmax6.columns],
            data=dfmax6.to_dict('records'),
        ),
    ], className='row'),

dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             html.Br(),
             ])
    ]),
    
    
dbc.Row([
     html.H4('Top 5 days with the least number of vehicles'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfmin6.columns],
            data=dfmin6.to_dict('records')
        ),
         html.Br(),
          html.Br()
    ], className='row'),
dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
             ])
    ])

])
  
    














@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')])

def update_line_chart(days):
    # Filter the data for the selected day of the week
    df_selected_days = df1[df1['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', df_selected_days['timestamp'].dt.hour]).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart', 'figure'),
    [Input('day-of-week-dropdown', 'value')]
)

def update_chart(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df1[df1['day of week'] == day_of_week]
    filtered_data = df1.loc[df1['day of week'] == day_of_week].copy()
    
    # Group by hour of day and calculate mean counts
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    # Convert hour_of_day column to numeric
    #mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Exclude the 'total' column from the mean counts
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart
    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig
##02####3
@app.callback(
    dash.dependencies.Output('line-chart2', 'figure'),
    [dash.dependencies.Input('day-dropdown2', 'value')]
)


def update_line_chart2(days):
    # Filter the data for the selected day of the week
    df_selected_days = df2[df2['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    #df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', df_selected_days['timestamp'].dt.hour]).mean().reset_index()
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart2', 'figure'),
    [Input('day-of-week-dropdown2', 'value')]
)

def update_chart2(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df2[df2['day of week'] == day_of_week]
    filtered_data = df2.loc[df2['day of week'] == day_of_week].copy()
    # Group by hour of day and calculate mean counts
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    # Convert hour_of_day column to numeric
    #mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Exclude the 'total' column from the mean counts
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart

    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig

##03####
@app.callback(
    dash.dependencies.Output('line-chart3', 'figure'),
    [dash.dependencies.Input('day-dropdown3', 'value')]
)


def update_line_chart3(days):
    # Filter the data for the selected day of the week
    df_selected_days = df3[df3['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', df_selected_days['timestamp'].dt.hour]).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart3', 'figure'),
    [Input('day-of-week-dropdown3', 'value')]
)

def update_chart3(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df3[df3['day of week'] == day_of_week]
    filtered_data = df3.loc[df3['day of week'] == day_of_week].copy()
    # Group by hour of day and calculate mean counts
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    # Convert hour_of_day column to numeric
    #mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    # Exclude the 'total' column from the mean counts
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart
    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig

##04####
@app.callback(
    dash.dependencies.Output('line-chart4', 'figure'),
    [dash.dependencies.Input('day-dropdown4', 'value')]
)


def update_line_chart4(days):
    # Filter the data for the selected day of the week
    df_selected_days = df4[df4['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', df_selected_days['timestamp'].dt.hour]).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart4', 'figure'),
    [Input('day-of-week-dropdown4', 'value')]
)

def update_chart4(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df4[df4['day of week'] == day_of_week]
    filtered_data = df4.loc[df4['day of week'] == day_of_week].copy()
    # Group by hour of day and calculate mean counts
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    # Convert hour_of_day column to numeric
    # mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day']) 
    # Exclude the 'total' column from the mean counts
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart
    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig
##05####
@app.callback(
    dash.dependencies.Output('line-chart5', 'figure'),
    [dash.dependencies.Input('day-dropdown5', 'value')]
)


def update_line_chart5(days):
    # Filter the data for the selected day of the week
    df_selected_days = df5[df5['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart5', 'figure'),
    [Input('day-of-week-dropdown5', 'value')]
)

def update_chart5(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df5[df5['day of week'] == day_of_week]
    filtered_data = df5.loc[df5['day of week'] == day_of_week].copy()
    # Group by hour of day and calculate mean counts
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    # Convert hour_of_day column to numeric
    #mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day']) 
    # Exclude the 'total' column from the mean counts
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart
    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig
##06####
@app.callback(
    dash.dependencies.Output('line-chart6', 'figure'),
    [dash.dependencies.Input('day-dropdown6', 'value')]
)


def update_line_chart6(days):
    # Filter the data for the selected day of the week
    df_selected_days = df6[df6['day of week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    #df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', df_selected_days['timestamp'].dt.hour]).mean().reset_index(drop=True)
    df_selected_days['timestamp'] = df_selected_days['timestamp'].dt.hour
    df_selected_days_by_day_hour = df_selected_days.groupby(['day of week', 'timestamp']).mean().reset_index()
    #df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)
    df_selected_days_by_day_hour['day of week'] = df_selected_days_by_day_hour['day of week'].map(days_map)

    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day of week', labels={'timestamp': 'Hour of Day (6:00AM - 8:00PM)', 'total': 'Number of vehicles'},
                  title='Mean vehicles count per minute on selected days')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart6', 'figure'),
    [Input('day-of-week-dropdown6', 'value')]
)

def update_chart6(day_of_week):
    # Filter data for selected day of week
    #filtered_data = df6[df6['day of week'] == day_of_week]
    filtered_data = df6.loc[df6['day of week'] == day_of_week].copy()
    # Group by hour of day and calculate mean counts
    #mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    mean_counts = filtered_data.groupby('hour_of_day', as_index=False).mean(numeric_only=True)
    # Convert hour_of_day column to numeric
    #mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])   
    # Exclude the 'total' column from the mean counts
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day of week'])
    mean_counts['hour_of_day'] = pd.to_numeric(mean_counts['hour_of_day'])
    # Create a stacked area chart
    fig = go.Figure()
    for col in mean_counts.columns[1:]:
        fig.add_trace(go.Scatter(
            x=mean_counts['hour_of_day'],
            y=mean_counts[col],
            mode='lines',
            stackgroup='one',
            name=col
        ))
    
    # Update chart layout
    fig.update_layout(
        title='Mean types of vehicle counts per minute on selected days',
        xaxis=dict(title='Hour of Day (6:00AM - 8:00PM)'),
        yaxis=dict(title='Number of vehicles'),
        showlegend=True
    )
    fig.update_xaxes(showticklabels=False)
    return fig