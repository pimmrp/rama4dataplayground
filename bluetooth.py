# Rama IV under Tollway Intersection Nana Intersection
# Asok Intersection
# Rama IV Intersection
# Na Ranong Intersection
# Sai Nam Phueng Intersection Sawatdi Intersection
# Kasemrat Intersection
# Sunlakakon Intersection

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
import plotly.graph_objs as go
from app import app
import os
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
import dash_table
pd.options.plotting.backend = "plotly"

#note:
#Kasem-Sun = 0, Sun-Kasem=1 -> route3
#Rama4-Naranong=2,3 -> route1




# Create a sample data frame
datatable = {'Point': ['1', '2', '3','4','5'],
        'Name': ['Rama IV Intersection','Khlong Toei intersection','Na Ranong Intersection','Sunlakakon Intersection','Kasemrat Intersection'],
        }
dftable = pd.DataFrame(datatable)

datatable2= {'Route)': ['1', '2', '3','4'],
        'Name': ['Rama IV Intersection - Na Ranong Intersection','Na Ranong Intersection - Sunlakakon Intersection','Sunlakakon Intersection - Kasemrat Intersection',
        'Kasemrat Intersection - Rama IV Intersection']
        }
dftable2 = pd.DataFrame(datatable2)



#route1
#Rama4 to Na Ranong Jan11-Feb24#
folder_path2 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Rama IV - Na Ranong'
csv_files2 = [f2 for f2 in os.listdir(folder_path2) if f2.endswith('.csv')]
dfs2 = []
for file_name2 in csv_files2:
    file_path2 = os.path.join(folder_path2, file_name2)
    # read the CSV file into a pandas dataframe
    df2 = pd.read_csv(file_path2)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts2 = file_name2.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts2[-1].replace('.csv', '')
    df2['FromTime'] = df2['FromTime'].str.slice(stop=-3)
    df2['Date'] = Date
    df2['Date'] = pd.to_datetime(df2['Date'], format='%Y-%b-%d')
    df2['Day'] = df2['Date'].dt.day_name()
    dfs2.append(df2)
dfconcat2 = pd.concat(dfs2, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf2 = dfconcat2.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path2 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_rama4_naranong.csv'
cdf2.to_csv(file_path2, index=False)


#Naranong to Rama4 Jan11-Feb24#
folder_path3 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Na Ranong - Rama IV'
csv_files3 = [f3 for f3 in os.listdir(folder_path3) if f3.endswith('.csv')]
dfs3 = []
for file_name3 in csv_files3:
    file_path3 = os.path.join(folder_path3, file_name3)
    # read the CSV file into a pandas dataframe
    df3 = pd.read_csv(file_path3)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts3 = file_name3.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts3[-1].replace('.csv', '')
    df3['FromTime'] = df3['FromTime'].str.slice(stop=-3)
    df3['Date'] = Date
    df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%b-%d')
    df3['Day'] = df3['Date'].dt.day_name()
    dfs3.append(df3)
dfconcat3 = pd.concat(dfs3, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf3 = dfconcat3.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path3 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_naranong_rama4.csv'
cdf3.to_csv(file_path3, index=False)


#--------------------------------#

#Route2#
#Naranong to Sun Jan11-Feb24#
folder_path4 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Na Ranong - Sun'
csv_files4 = [f4 for f4 in os.listdir(folder_path4) if f4.endswith('.csv')]
dfs4 = []
for file_name4 in csv_files4:
    file_path4 = os.path.join(folder_path4, file_name4)
    # read the CSV file into a pandas dataframe
    df4 = pd.read_csv(file_path4)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts4 = file_name4.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts4[-1].replace('.csv', '')
    df4['FromTime'] = df4['FromTime'].str.slice(stop=-3)
    df4['Date'] = Date
    df4['Date'] = pd.to_datetime(df4['Date'], format='%Y-%b-%d')
    df4['Day'] = df4['Date'].dt.day_name()
    dfs4.append(df4)
dfconcat4 = pd.concat(dfs4, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf4 = dfconcat4.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path4 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_naranong_sun.csv'
cdf4.to_csv(file_path4, index=False)

#Sun to Naranong Jan11-Feb24#
folder_path5 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Sunlakakon - Na Ranong'
csv_files5 = [f5 for f5 in os.listdir(folder_path5) if f5.endswith('.csv')]
dfs5 = []
for file_name5 in csv_files5:
    file_path5 = os.path.join(folder_path5, file_name5)
    # read the CSV file into a pandas dataframe
    df5 = pd.read_csv(file_path5)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts5 = file_name5.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts5[-1].replace('.csv', '')
    df5['FromTime'] = df5['FromTime'].str.slice(stop=-3)
    df5['Date'] = Date
    df5['Date'] = pd.to_datetime(df5['Date'], format='%Y-%b-%d')
    df5['Day'] = df5['Date'].dt.day_name()
    dfs5.append(df5)
dfconcat5 = pd.concat(dfs5, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf5 = dfconcat5.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path5 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_sun-naranong.csv'
cdf5.to_csv(file_path5, index=False)



#--------------------------------#

#Route3#
#####Sunlakakon Intersection - Kasemrat Intersection Jan11-Feb24#####
folder_path1 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Sunlakakon - Kasemrat'
csv_files1 = [f1 for f1 in os.listdir(folder_path1) if f1.endswith('.csv')]
dfs1 = []
for file_name1 in csv_files1:
    file_path1 = os.path.join(folder_path1, file_name1)
    # read the CSV file into a pandas dataframe
    df1 = pd.read_csv(file_path1)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts1 = file_name1.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date1 = parts1[-1].replace('.csv', '')
    df1['FromTime'] = df1['FromTime'].str.slice(stop=-3)
    df1['Date'] = Date1
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%b-%d')
    df1['Day'] = df1['Date'].dt.day_name()
    dfs1.append(df1)
dfconcat1 = pd.concat(dfs1, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf1 = dfconcat1.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path1 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_sun_kasem.csv'
cdf1.to_csv(file_path1, index=False)


#Kasemrat Intersection - Sunlakakon Intersection Jan11-Feb24#
folder_path = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Kasemrat - Sun'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
dfs = []
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    # read the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts = file_name.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts[-1].replace('.csv', '')
    df['FromTime'] = df['FromTime'].str.slice(stop=-3)
    df['Date'] = Date
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%b-%d')
    df['Day'] = df['Date'].dt.day_name()
    dfs.append(df)
dfconcat = pd.concat(dfs, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf = dfconcat.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_kasem_sun.csv'
cdf.to_csv(file_path, index=False)





#====================================#

#Route4#
#Kasemrat - Rama4 Jan11-Feb24#
folder_path6 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Kasemrat - Rama IV'
csv_files6 = [f6 for f6 in os.listdir(folder_path6) if f6.endswith('.csv')]
dfs6 = []
for file_name6 in csv_files6:
    file_path6 = os.path.join(folder_path6, file_name6)
    # read the CSV file into a pandas dataframe
    df6 = pd.read_csv(file_path6)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts6 = file_name6.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts6[-1].replace('.csv', '')
    df6['FromTime'] = df6['FromTime'].str.slice(stop=-3)
    df6['Date'] = Date
    df6['Date'] = pd.to_datetime(df6['Date'], format='%Y-%b-%d')
    df6['Day'] = df6['Date'].dt.day_name()
    dfs6.append(df6)
dfconcat6 = pd.concat(dfs6, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf6 = dfconcat6.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path6 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_kasemrat-rama4.csv'
cdf6.to_csv(file_path6, index=False)


#Rama4 - Kasemrat Jan11-Feb24#
folder_path7 = '/Users/pim/Desktop/new_outputBTphoophoo/btsensors/BTsensors___Rama IV - Kasemrat'
csv_files7 = [f7 for f7 in os.listdir(folder_path7) if f7.endswith('.csv')]
dfs7 = []
for file_name7 in csv_files7:
    file_path7 = os.path.join(folder_path7, file_name7)
    # read the CSV file into a pandas dataframe
    df7 = pd.read_csv(file_path7)
    # extract a part of the file name and add it as a new column to the dataframe
    # split the filename into a list using '_' as the separator
    parts7 = file_name7.split('_')
    # the date is the last element in the list, so we can access it with parts[-1]
    Date = parts7[-1].replace('.csv', '')
    df7['FromTime'] = df7['FromTime'].str.slice(stop=-3)
    df7['Date'] = Date
    df7['Date'] = pd.to_datetime(df7['Date'], format='%Y-%b-%d')
    df7['Day'] = df7['Date'].dt.day_name()
    dfs7.append(df7)
dfconcat7 = pd.concat(dfs7, ignore_index=True)
# define a function to map days of the week to numerical values
def day_of_week_to_number(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day)
# sort the dataframe by the 'Day' column in the order Monday to Sunday
cdf7 = dfconcat7.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path7 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_rama4-kasemrat.csv'
cdf7.to_csv(file_path7, index=False)








##==================================================================================##
#&&&&&front end&&&&&&#

bt_layout = dbc.Container([

    dbc.Row([
        html.H1("Data from Bluetooth Sensors",
                        className='text-center text-secondary mb-4'),
    ]),
    #รูปแผนที่และตาราง๒
    dbc.Row([
        dbc.Col([
        html.Img(src="https://sv1.picz.in.th/images/2023/04/03/mcVs3J.png", style={"float": "left", "margin-right": "20px","display": "block", "margin": "0 auto", "width": "550px", "height": "400px"})
        ],
            #style={"display": "flex", "justify-content": "left", "align-items": "left","margin-top": "30px", "margin-bottom": "60px"},
            style={"margin-top": "30px", "margin-bottom": "60px"}
        ),
        dbc.Col([
        html.H5("The names of each point",style={"margin-top": "20px"}),
        dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in dftable.columns],
        data=dftable.to_dict('records')#,
        #style={"margin-bottom": "60px"}
        ),
        html.Div(style={'height': '20px'}),
        dash_table.DataTable(
        id='table1',
        columns=[{'name': e, 'id': e} for e in dftable2.columns],
        data=dftable2.to_dict('records')#,
        #style={"margin-top":"20px","margin-bottom": "20px"}
        )
        ],style= {"margin-bottom": "20px"})
        #]#,style={ "margin-bottom": "60px"})

        #])#style={"margin-top": "40px", "margin-bottom": "60px"})


    ]),
   #dbc.Row([
        # dash_table.DataTable(
        # id='table1',
        # columns=[{'name': e, 'id': e} for e in dftable2.columns],
        # data=dftable2.to_dict('records'))
        # ],style={ "margin-bottom": "60px"}),
    
    #text ก่อน dropdown
    dbc.Row([
        dbc.Col([
            html.Div("        Select a weekday to display a relationship between average speed and time for that day",
            style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '16px',"justify-content": "center", "align-items": "center"#, "margin-bottom": "-5px"
            }),
            # html.P("        between average speed and time for that day",
            # style={
            #     'font-family': 'Arial, sans-serif',
            #     'font-size': '16px',
            # }
            # )
        ]#,
          # xs=12, sm=12, md=12, lg=5, xl=5
        )
    
    ]),

    #dropdown#
    dbc.Row([
        dbc.Col([
            # html.H1("Data from Bluetooth Sensors",
            #             className='text-center text-secondary mb-4'),
            dcc.Dropdown(id='day-dropdown',options=[{'label': day, 'value': day} for day in cdf['Day'].unique()],value='Monday'),
            html.H5(id='day',style={"margin-top": "20px"}),
            # dcc.Graph(id='speed-vs-time-graph')
        ],
           #xs=12, sm=12, md=12, lg=5, xl=5
           #xs=13, sm=13, md=13, lg=6, xl=6
        ),
    ]),

    #route1#
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph2')
        ],
           #xs=12, sm=12, md=12, lg=5, xl=5
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph3')
        ],
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
    ]),


    #route2#
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph4')
        ],
           #xs=12, sm=12, md=12, lg=5, xl=5
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph5')
        ],
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
    ]),

    #original-route3#
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph')
        ],
           #xs=12, sm=12, md=12, lg=5, xl=5
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph1')
        ],
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
    ]),

    #route4#
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph6')
        ],
           #xs=12, sm=12, md=12, lg=5, xl=5
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
        dbc.Col([
            dcc.Graph(id='speed-vs-time-graph7')
        ],
           xs=13, sm=13, md=13, lg=6, xl=6
        ),
    ])




    
])




#--
        # dbc.Col([
        #                  dcc.Graph(id='speed-vs-time-graph1')
        # ],
        #    xs=13, sm=13, md=13, lg=6, xl=6
        # ),

        # ])
    # dbc.Row([
    #     dbc.Col([
    #          dcc.Graph(id='speed-vs-time-graph1')
    #     ],
    #        xs=13, sm=13, md=13, lg=6, xl=6
    #     ),
    # dbc.Row([
    #     dbc.Col([
    #          dcc.Graph(id='speed-vs-time-graph2')
    #     ],
    #        xs=13, sm=13, md=13, lg=6, xl=6
    #     )
    # ]),

    

  
#  ]) # Horizontal:start,center,end,between,around
# ])









##==================================================================================##
###callback###
@app.callback(
    [Output("speed-vs-time-graph", "figure"), Output("speed-vs-time-graph1", "figure"),Output("day", 'children'),Output("speed-vs-time-graph2", "figure"),
    Output("speed-vs-time-graph3", "figure"),Output("speed-vs-time-graph4", "figure"),Output("speed-vs-time-graph5", "figure"),Output("speed-vs-time-graph6", "figure"),
    Output("speed-vs-time-graph7", "figure")
    ],

    [Input("day-dropdown", "value")]
    # Output(component_id='speed-vs-time-graph1', component_property='figure'),
    # Output(component_id='speed-vs-time-graph', component_property='figure'),
    # Input(component_id='day-dropdown', component_property='value')
)
def update_graph(selected_day):
    
    
    #route1#
    filtered_df2 = cdf2[cdf2['Day'] == selected_day]
    serie2=filtered_df2.groupby('FromTime')['AverageSpeed'].mean()
    serie2.to_frame()
    serie2 = serie2.reset_index(drop=False)
    
    
    filtered_df3 = cdf3[cdf3['Day'] == selected_day]
    serie3=filtered_df3.groupby('FromTime')['AverageSpeed'].mean()
    serie3.to_frame()
    serie3 = serie3.reset_index(drop=False)

    #route2#
    filtered_df4 = cdf4[cdf4['Day'] == selected_day]
    serie4=filtered_df4.groupby('FromTime')['AverageSpeed'].mean()
    serie4.to_frame()
    serie4 = serie4.reset_index(drop=False)
    
    
    filtered_df5 = cdf5[cdf5['Day'] == selected_day]
    serie5=filtered_df5.groupby('FromTime')['AverageSpeed'].mean()
    serie5.to_frame()
    serie5 = serie5.reset_index(drop=False)
    



    #route3#
    filtered_df = cdf[cdf['Day'] == selected_day]
    serie=filtered_df.groupby('FromTime')['AverageSpeed'].mean()
    serie.to_frame()
    serie = serie.reset_index(drop=False)
    
    
    filtered_df1 = cdf1[cdf1['Day'] == selected_day]
    serie1=filtered_df1.groupby('FromTime')['AverageSpeed'].mean()
    serie1.to_frame()
    serie1 = serie1.reset_index(drop=False)


    #route4#
    filtered_df6 = cdf6[cdf6['Day'] == selected_day]
    serie6=filtered_df6.groupby('FromTime')['AverageSpeed'].mean()
    serie6.to_frame()
    serie6 = serie6.reset_index(drop=False)
    
    
    filtered_df7 = cdf7[cdf7['Day'] == selected_day]
    serie7=filtered_df7.groupby('FromTime')['AverageSpeed'].mean()
    serie7.to_frame()
    serie7 = serie7.reset_index(drop=False)

    # fig = {
    #     'data': [{'x': serie.FromTime, 'y': serie.AverageSpeed, 'type': 'line'},{'x': cdf.FromTime, 'y': cdf.AverageSpeed, 'type': 'scatter' }],
    #     'layout': {'title': f'Speed vs. Time on {selected_day}'}
    # }
    # fig1 = {
    #     'data': [{'x': serie1.FromTime, 'y': serie1.AverageSpeed, 'type': 'line'}],
    #     'layout': {'title': f'Speed vs. Time on {selected_day}'}
    # }
    # return fig,fig1



    #route1#
    fig2 = {
        'data': [
            go.Scatter(
                x=serie2.FromTime,
                y=cdf2.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie2.FromTime,
                y=serie2.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Rama IV Intersection to Na Ranong Intersection ','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}
    }
    }
    # Add axis titles to layout
    fig3 = {
        'data': [
            go.Scatter(
                x=serie3.FromTime,
                y=cdf3.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie3.FromTime,
                y=serie3.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Na Ranong Intersection to Rama IV Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}}
    }

   #route2#
    fig4 = {
        'data': [
            go.Scatter(
                x=serie4.FromTime,
                y=cdf4.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie4.FromTime,
                y=serie4.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Na Ranong Intersection to Sunlakakorn Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}
    }
    }
    # Add axis titles to layout
    fig5 = {
        'data': [
            go.Scatter(
                x=serie5.FromTime,
                y=cdf5.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie5.FromTime,
                y=serie5.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Sunlakakorn Intersection to Na Ranong Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}}
    }



    #route3#
    fig = {
        'data': [
            go.Scatter(
                x=serie.FromTime,
                y=cdf.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie.FromTime,
                y=serie.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Kasemrat Intersection to Sunlakakon Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}
    }
    }
    # Add axis titles to layout
    fig1 = {
        'data': [
            go.Scatter(
                x=serie1.FromTime,
                y=cdf1.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie1.FromTime,
                y=serie1.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Sunlakakon Intersection to Kasemrat Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}}
    }

    #route4#
    fig6 = {
        'data': [
            go.Scatter(
                x=serie6.FromTime,
                y=cdf6.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie6.FromTime,
                y=serie6.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Kasemrat Intersection to Rama IV Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}
    }
    }
    # Add axis titles to layout
    fig7 = {
        'data': [
            go.Scatter(
                x=serie7.FromTime,
                y=cdf7.AverageSpeed,
                mode='markers',
                marker={'size':4, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie7.FromTime,
                y=serie7.AverageSpeed,
                mode='lines',
                line={'width': 1.5, 'color': 'red'},
                name='Line Plot'
                )
        ],'layout': {'title': f'Rama IV Intersection to Kasemrat Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)"}}
    }



    return fig,fig1, html.Div([
        'Speed vs. Time on  ',selected_day]),fig2,fig3,fig4,fig5,fig6,fig7














        # figure={
        #     'data': [
        #         # Add the scatter plot trace
        #         go.Scatter(
        #             x=df['x'],
        #             y=df['y1'],
        #             mode='markers',
        #             marker={'size': 10, 'color': 'blue'},
        #             name='Scatter Plot'
        #         ),
        #         # Add the line plot trace
        #         go.Scattergl(
        #             x=df['x'],
        #             y=df['y2'],
        #             mode='lines',
        #             line={'width': 2, 'color': 'red'},
        #             name='Line Plot'
        #         )
        #     ]
# def update_graphs(selected_day):
#     # Subset the datasets to the selected date
#     df1_subset = df1[df1["date"] == date_value]
#     df2_subset = df2[df2["date"] == date_value]
    
#     # Create graph1
#     fig1 = px.line(df1_subset, x="date", y="value1", title="Graph 1")
    
#     # Create graph2
#     fig2 = px.line(df2_subset, x="date", y="value2", title="Graph 2")
    
#     # Return the figures
#     return fig1, fig2






