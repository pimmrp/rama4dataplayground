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

#note:
#Kasem-Sun = 0, Sun-Kasem=1 -> route3
#Rama4-Naranong=2,3 -> route1

#app = dash.Dash(__name__, suppress_callback_exceptions=True)


# Create a sample data frame
datatable = {'Point': ['1', '2', '3','4','5'],
        'Name': ['Kasemrat Intersection','Rama IV Intersection','Khlong Toei intersection','Na Ranong Intersection','Sunlakakon Intersection'],
        }
dftable = pd.DataFrame(datatable)
dftable.style.set_properties(**{'text-align': 'center'})

datatable2= {'Kasemrat Grid Lock Loop': ['Clockwise', 'Counterclockwise'],
        'Detail': ['Rama IV Intersection -> Kasemrat Intersection -> Sunlakakon Intersection -> Na Ranong Intersection', 
        'Kasemrat Intersection -> Rama IV Intersection -> Na Ranong Intersection -> Sunlakakon Intersection']
        }
dftable2 = pd.DataFrame(datatable2)
dftable2.style.set_properties(**{'text-align': 'center'})



#route1
#Rama4 to Na Ranong Jan10-Feb10#
folder_path2 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Rama IV - Na Ranong'
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
file_path2 = '/Users/pim/Desktop/outputfeb2023/cdf_rama4_naranong.csv'
cdf2.to_csv(file_path2, index=False)

av2=cdf2['AverageSpeed'].mean()

#Naranong to Rama4 Jan10-Feb10#
folder_path3 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Na Ranong - Rama IV'
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
cdf3 = cdf3.drop(index=3465)

#save cdf to computer (สำรอง)
file_path3 = '/Users/pim/Desktop/outputfeb2023/cdf_naranong_rama4.csv'
cdf3.to_csv(file_path3, index=False)
av3=cdf3['AverageSpeed'].mean()

#--------------------------------#

#Route2#
#Naranong to Sun Feb1-Feb28#
folder_path4 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Na Ranong - Sun'
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
file_path4 = '/Users/pim/Desktop/outputfeb2023/cdf_naranong_sun.csv'
cdf4.to_csv(file_path4, index=False)
av4=cdf4['AverageSpeed'].mean()



#Sun to Naranong Feb1-Feb28#
folder_path5 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Sunlakakon - Na Ranong'
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
file_path5 = '/Users/pim/Desktop/outputfeb2023/cdf_sun-naranong.csv'
cdf5.to_csv(file_path5, index=False)
av5=cdf5['AverageSpeed'].mean()


#--------------------------------#

#Route3#
#####Sunlakakon Intersection - Kasemrat Intersection Feb1-28#####
folder_path1 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Sunlakakon - Kasemrat'
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
file_path1 = '/Users/pim/Desktop/outputfeb2023/cdf_sun_kasem.csv'
cdf1.to_csv(file_path1, index=False)
av1=cdf1['AverageSpeed'].mean()


#Kasemrat Intersection - Sunlakakon Intersection Feb1-28#
folder_path = '/Users/pim/Desktop/outputfeb2023/BTsensors___Kasemrat - Sun'
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
file_path = '/Users/pim/Desktop/outputfeb2023/cdf_kasem_sun.csv'
cdf.to_csv(file_path, index=False)
av=cdf['AverageSpeed'].mean()




#====================================#

#Route4#
#Kasemrat - Rama4 Jan10-Feb10#
folder_path6 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Kasemrat - Rama IV'
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
file_path6 = '/Users/pim/Desktop/outputfeb2023/cdf_kasemrat-rama4.csv'
cdf6.to_csv(file_path6, index=False)
av6=cdf6['AverageSpeed'].mean()





#Rama4 - Kasemrat Jan10-Feb10#
folder_path7 = '/Users/pim/Desktop/outputfeb2023/BTsensors___Rama IV - Kasemrat'
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
file_path7 = '/Users/pim/Desktop/outputfeb2023/cdf_rama4-kasemrat.csv'
cdf7.to_csv(file_path7, index=False)
av7=cdf7['AverageSpeed'].mean()


df_concatall = pd.concat([cdf,cdf1, cdf2, cdf3, cdf4, cdf5, cdf6, cdf7], axis=0)

# Reset the index
df_concatall.reset_index(drop=True, inplace=True)

df_concatallsort= df_concatall.sort_values(by='Day', key=lambda x: x.map(day_of_week_to_number))

#save cdf to computer (สำรอง)
file_path8 = '/Users/pim/Desktop/new_outputBTphoophoo/cdf_all.csv'
df_concatallsort.to_csv(file_path8, index=False)

avmon= df_concatallsort.loc[df_concatallsort['Day'] == 'Monday']['AverageSpeed'].mean()
avtues= df_concatallsort.loc[df_concatallsort['Day'] == 'Tuesday']['AverageSpeed'].mean()
avwed= df_concatallsort.loc[df_concatallsort['Day'] == 'Wednesday']['AverageSpeed'].mean()
avthurs=df_concatallsort.loc[df_concatallsort['Day'] == 'Thursday']['AverageSpeed'].mean()
avfri= df_concatallsort.loc[df_concatallsort['Day'] == 'Friday']['AverageSpeed'].mean()
avsat= df_concatallsort.loc[df_concatallsort['Day'] == 'Saturday']['AverageSpeed'].mean()
avsun= df_concatallsort.loc[df_concatallsort['Day'] == 'Sunday']['AverageSpeed'].mean()





#special conditions#
special=["Valentine's day","Heavy rain day","Exhibition day"]
#valentines dondition
#Valen = {
#     'data' : [
#         # go.Scatter(
#         #     x=cdf.FromTime,
#         #     y=cdf[cdf['Date']=='2023-02-14'].AverageSpeed,
#         #     mode='markers',
#         #     marker={'size':3, 'color':'blue'},
#         #     name='Scatter Plot'

#         # ),
#         go.Scattergl(
#             x=cdf.FromTime,
#             y=cdf[cdf['Date']=='2023-02-14'].AverageSpeed,
#             mode='lines',
#             line={'width': 1.2, 'color': 'red'},
#             name='Valen'
#             ),
#     ],'layout': {'title': f'Kasemrat Intersection to <br>Sunlakakorn Intersection','xaxis' :{'title':"Time"},
# 'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
# }

#Valen1 = {
#     'data' : [
#         # go.Scatter(
#         #     x=cdf1.FromTime,
#         #     y=cdf1[cdf1['Date']=='2023-02-14'].AverageSpeed,
#         #     mode='markers',
#         #     marker={'size':3, 'color':'blue'},
#         #     name='Scatter Plot'

#         # ),
#         go.Scattergl(
#             x=cdf1.FromTime,
#             y=cdf1[cdf1['Date']=='2023-02-14'].AverageSpeed,
#             mode='lines',
#             line={'width': 1.2, 'color': 'red'},
#             name='Valen1'
#             ),
#     ],'layout': {'title': f'Sunlakakorn Intersection to <br>Kasemrat Intersection','xaxis' :{'title':"Time"},
# 'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
# }

#Valen4 = {
#     'data' : [
#         # go.Scatter(
#         #     x=cdf4.FromTime,
#         #     y=cdf4[cdf4['Date']=='2023-02-14'].AverageSpeed,
#         #     mode='markers',
#         #     marker={'size':3, 'color':'blue'},
#         #     name='Scatter Plot'

#         # ),
#         go.Scattergl(
#             x=cdf4.FromTime,
#             y=cdf4[cdf4['Date']=='2023-02-14'].AverageSpeed,
#             mode='lines',
#             line={'width': 1.2, 'color': 'red'},
#             name='Valen4'
#             ),
#     ],'layout': {'title': f'Na Ranong Intersection to <br>Sunlakakorn Intersection','xaxis' :{'title':"Time"},
# 'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
# }

#Valen5 = {
#     'data' : [
#         # go.Scatter(
#         #     x=cdf5.FromTime,
#         #     y=cdf5[cdf5['Date']=='2023-02-14'].AverageSpeed,
#         #     mode='markers',
#         #     marker={'size':3, 'color':'blue'},
#         #     name='Scatter Plot'

#         # ),
#         go.Scattergl(
#             x=cdf5.FromTime,
#             y=cdf5[cdf5['Date']=='2023-02-14'].AverageSpeed,
#             mode='lines',
#             line={'width': 1.2, 'color': 'red'},
#             name='Valen5'
#             ),
#     ],'layout': {'title': f'Sunlakakorn Intersection to <br>Na Ranong Intersection','xaxis' :{'title':"Time"},
# 'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
# }

Valen=str(round(cdf[cdf['Date']=='2023-02-14'].AverageSpeed.mean(),2))+' km/hr'
Valen1=str(round(cdf1[cdf1['Date']=='2023-02-14'].AverageSpeed.mean(),2))+' km/hr'
Valen4=str(round(cdf4[cdf4['Date']=='2023-02-14'].AverageSpeed.mean(),2))+' km/hr'
Valen5=str(round(cdf5[cdf5['Date']=='2023-02-14'].AverageSpeed.mean(),2))+' km/hr'

rain=str(round(cdf[cdf['Date']=='2023-02-15'].AverageSpeed.mean(),2))+' km/hr'
rain1=str(round(cdf1[cdf1['Date']=='2023-02-15'].AverageSpeed.mean(),2))+' km/hr'
rain4=str(round(cdf4[cdf4['Date']=='2023-02-15'].AverageSpeed.mean(),2))+' km/hr'
rain5=str(round(cdf5[cdf5['Date']=='2023-02-15'].AverageSpeed.mean(),2))+' km/hr'

av00=str(round(av,2))+' km/hr'
av11=str(round(av1,2))+' km/hr'
av44=str(round(av4,2))+' km/hr'
av55=str(round(av5,2))+' km/hr'
# indexx = pd.MultiIndex.from_tuples([
#     ('column1', 'row1', 'row2'),
#     ('column1', 'row3', 'row4')
# ])
# Define the data for the table
datatable3 = [('Clockwise', 'Kasemrat -> Sunlakakon',Valen,rain,av00),
             ('', 'Sunlakakon -> Na Ranong',Valen5,rain5,av55),
             ('Counterclockwise', 'Na Ranong -> Sunlakakon',Valen4,rain4,av44),
             ('', 'Sunlakakon -> Kasemrat',Valen1,rain1,av11)]

dftable3 = pd.DataFrame.from_records(datatable3, columns=['Kasemrat Grid Lock Loop', '',"VALENTINE'S DAY (14 FEB 2023)",'Heavy rain day (15 FEB 2023)','Overall data'])
dftable3.style.set_properties(**{'text-align': 'center'})



# datatable4 = [('Clockwise', 'Kasemrat Intersection -> Sunlakakon Intersection',round(Valen,2)),
#              ('', 'Sunlakakon Intersection -> Na Ranong Intersection',round(Valen1,2)),
#              ('Counterclockwise', 'Na Ranong Intersection -> Sunlakakon Intersection',round(Valen4,2)),
#              ('', 'Sunlakakon Intersection -> Kasemrat Intersection',round(Valen5,2))]

# dftable4 = pd.DataFrame.from_records(datatable4, columns=['Kasemrat Grid Lock Loop', '','Average Speed (km/hr)'])
# dftable4.style.set_properties(**{'text-align': 'center'})

# datatable3= {'Kasemrat Grid Lock Loop Clockwise': ["Kasemrat Intersection -> Sunlakakon Intersection","Sunlakakon Intersection -> Na Ranong Intersection"],
#         'Average Speed (km/hr)': [Valen,Valen1]
#         }
# dftable3 = pd.DataFrame(datatable3)
##==================================================================================##
#&&&&&front end&&&&&&#

bt_layout = dbc.Container([

    dbc.Row([
        html.H1("Data from Bluetooth Sensors",
                        className='text-center text-secondary mb-4'),
    ]),
    #รูปแผนที่และตาราง
    dbc.Row([
        dbc.Col([
        html.Img(src="https://sv1.picz.in.th/images/2023/04/29/yx13sa.png", style={"float": "left", "margin-right": "20px","display": "block", "margin": "0 auto", "width": "550px", "height": "400px"})
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
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        html.H5(["Average speed",html.Br(),"from weekday"],style={"margin-top":"20px","margin-bottom": "20px",'backgroundColor': '#F9F9F9'})]),
                    dbc.Row([
                        html.Div(["Monday:  ", round(avmon,2), "  km/hr",
                                  html.Br(),
                                  "Tuesday:  ", round(avtues,2), "  km/hr",
                                  html.Br(),
                                  "Wednesday:  ", round(avwed,2),"  km/hr",
                                  html.Br(),
                                  "Thursday:  ", round(avthurs,2),"  km/hr",
                                  html.Br(),
                                  "Friday:  ", round(avfri,2),"  km/hr",
                                  html.Br(),
                                  "Saturday:  ", round(avsat,2),"  km/hr",
                                  html.Br(),
                                  "Sunday:  ", round(avsun,2),"  km/hr",
                                  
                                  
                                  
    
                                  ])
    

                    ])

                #informations below
                ],style={ "margin-right": "-20px"}),
                dbc.Col([
                    dbc.Row([
                    html.H5(
                    ["Average speed",html.Br(),"from routes"],style={"margin-top":"20px","margin-bottom": "20px",'backgroundColor': '#F9F9F9'})]),
                    dbc.Row([
                        html.Div(["Rama IV -> Kasemrat:  ", round(av7,2), "  km/hr",
                                  html.Br(),
                                  "Kasemrat -> Sunlakakon:  ", round(av,2), "  km/hr",
                                  html.Br(),
                                  "Sunlakakon -> Na Ranong:  ", round(av5,2),"  km/hr",
                                  html.Br(),
                                  "Na Ranong -> Rama IV:  ", round(av3,2),"  km/hr",
                                  html.Br(),
                                  "Kasemrat -> Rama IV:  ", round(av6,2),"  km/hr",
                                  html.Br(),
                                  "Rama IV -> Na Ranong:  ", round(av2,2),"  km/hr",
                                  html.Br(),
                                  "Na Ranong -> Sunlakakon:  ", round(av4,2),"  km/hr",
                                  html.Br(),
                                  "Sunlakakon -> Kasemrat:  ", round(av1,2),"  km/hr",
                    ])
                    ])

                #informations below

                ],style={ "margin-left": "-50px"})
        
            ])

    ],style={ "margin-left": "-50px"})
    ]),
    dbc.Row([
        dbc.Col([
        html.Div(style={'height': '20px'}),
        dash_table.DataTable(
        id='table1',
        columns=[{'name': e, 'id': e} for e in dftable2.columns],
        data=dftable2.to_dict('records')#,
        #style={"margin-top":"20px","margin-bottom": "20px"}
        )
        ],style= {"margin-bottom": "20px",'textAlign': 'center'
    })
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
        html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '20px',"margin-top": "20px"
        },
        children=[
            html.H2('Overall Data')
        ]
    )


    ]),
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
    dbc.Row([
    html.Div("        The data presented in Graphs 1, 4-6 corresponds to the period between January 10th and February 10th. Graphs 2-3 and 7-8 display data recorded between February 1st and February 28th.",
            style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '12px',"justify-content": "center", "align-items": "center"#, "margin-bottom": "-5px"
            }),
    html.Div("The scatter plot represents all the cars detected during the respective time frames.",style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '12px',"justify-content": "center", "align-items": "center"#, "margin-bottom": "-5px"
            }),
    html.Div("The line plot displays the average speed of all the weekdays selected.",style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '12px',"justify-content": "center", "align-items": "center"#, "margin-bottom": "-5px"
            })
    
    ]),

    #route1#
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(id='speed-vs-time-graph7', style={'width': '400px', 'height': '300px'})
    #     ],
    #        #xs=12, sm=12, md=12, lg=5, xl=5
    #        xs=3, sm=3, md=3, lg=5, xl=4
    #     ),
    #     dbc.Col([
    #         dcc.Graph(id='speed-vs-time-graph', style={'width': '400px', 'height': '300px'})
    #     ],
    #        xs=6, sm=6, md=6, lg=5, xl=5
    #     ),
    #     dbc.Col([
    #         dcc.Graph(id='speed-vs-time-graph5', style={'width': '400px', 'height': '300px'})
    #     ],
    #         xs=13, sm=13, md=13, lg=6, xl=6
    #     ),
    #     dbc.Col([
    #         dcc.Graph(id='speed-vs-time-graph3', style={'width': '400px', 'height': '300px'})
    #     ],
    #         xs=13, sm=13, md=13, lg=6, xl=6
    #     )
    # ]),

    dbc.Row([
            html.H5("Route1: Kasemrat Grid Lock Loop Clockwise",
            style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '16px',"justify-content": "center", "align-items": "center","margin-top": "20px"#, "margin-bottom": "-5px"
            }),
            # html.P("        between average speed and time for that day",
            # style={
            #     'font-family': 'Arial, sans-serif',
            #     'font-size': '16px',
            # }
            # )
        ]#,
          # xs=12, sm=12, md=12, lg=5, xl=5
        ),


    dbc.Row([
        dcc.Graph(id='speed-vs-time-graph7', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
            # dbc.Row([
            #     html.P(["From the graph, it was found that the trend of this route is that the vehicle speed is very slow in the evening (traffic congestion).", html.Br(),
            #            "This is due to the fact that in the evening, many vehicles need to use this route.",html.Br(),
            #            "Moreover, there are converging points of cars from the shortcut roads of Sukhumvit 22, 24, and 26 to the expressway at the Sunlakakorn intersection.",html.Br(),
            #            "Some also need to turn onto Sukhumvit Road, causing the traffic to move slowly."],style={'font-size': '10px'})

        dcc.Graph(id='speed-vs-time-graph', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
        dcc.Graph(id='speed-vs-time-graph5', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
        dcc.Graph(id='speed-vs-time-graph3', style={'width': '400px', 'height': '300px','margin-left': '-40px', 'margin-right': '-50px'})
        ]),
    dbc.Row([
    html.P([
        html.Ul([
        html.Li(["From the graph1"],style={'font-size': '12px'}),
        html.P(["It was found that the trend of this route is that the vehicle speed is very slow in the evening (traffic congestion).", html.Br(),
                       "This is due to the fact that in the evening, many vehicles need to use this route.",html.Br(),
                       "Moreover, there are converging points of cars from the shortcut roads of Sukhumvit 22, 24, and 26 to the expressway at the Sunlakakon intersection.",html.Br(),
                       "Some also need to turn onto Sukhumvit Road, causing the traffic to move slowly."],style={'font-size': '10px'}),
        html.Li(["From the graph2"],style={'font-size': '12px'}),
        html.Li(["From the graph3"],style={'font-size': '12px'}),
        html.Li(["From the graph4"],style={'font-size': '12px'})
        ])

    ])
    ]),

    dbc.Row([
    html.Div(id='lowest7'),
    html.Div(id='lowest'),
    html.Div(id='lowest5'),
    html.Div(id='lowest3')
    



    ]),

    dbc.Row([
            html.H5("Route2: Kasemrat Grid Lock Loop Counterclockwise",
            style={
                #'font-family': 'Arial, sans-serif',
                'font-size': '16px',"justify-content": "center", "align-items": "center","margin-top": "40px"#, "margin-bottom": "-5px"
            }),
            # html.P("        between average speed and time for that day",
            # style={
            #     'font-family': 'Arial, sans-serif',
            #     'font-size': '16px',
            # }
            # )
        ]#,
          # xs=12, sm=12, md=12, lg=5, xl=5
        ),

    #route2#
    dbc.Row([
            dcc.Graph(id='speed-vs-time-graph6', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'})
        ,
            dcc.Graph(id='speed-vs-time-graph2', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'})
        ,
            dcc.Graph(id='speed-vs-time-graph4', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'})
        ,
            dcc.Graph(id='speed-vs-time-graph1', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'})
        ,
    ]),

    
    dbc.Row([
    html.P([
        html.Ul([
        html.Li(["From the graph1,...."],style={'font-size': '10px'}),
        html.Li(["From the graph2,...."],style={'font-size': '10px'}),
        html.Li(["From the graph3,...."],style={'font-size': '10px'}),
        html.Li(["From the graph4,...."],style={'font-size': '10px'})
        ])

    ])
    ]),


    dbc.Row([
        html.Div(id='lowest6'),
        html.Div(id='lowest2'),
        html.Div(id='lowest4'),
        html.Div(id='lowest1')
    



    ]),

    dbc.Row([
    html.Div(
        style={
            'backgroundColor': '#F9F9F9',
            'padding': '20px',"margin-top": "20px"
        },
        children=[
            html.H2('The special information obtained from the data')
        ]
    ),

    dbc.Row([
    # # dbc.Col([
    # #     # html.H1("Data from Bluetooth Sensors",
    # #     #             className='text-center text-secondary mb-4'),
    # #     dcc.Dropdown(id='special-dropdown',options=[{'label': special, 'value': special} for special in special]),
    # #     html.H5(id='special',style={"margin-top": "20px"}),
    # #     # dcc.Graph(id='speed-vs-time-graph')
    # # ],
    # #     #xs=12, sm=12, md=12, lg=5, xl=5
    # #     #xs=13, sm=13, md=13, lg=6, xl=6
    # # ),
    # # ]),


    html.H4("The table of average speed on special day")
    ]),
    dbc.Row([
        html.Div(style={'height': '20px'}),
        dash_table.DataTable(
        id='table3',
        columns=[{'name': j, 'id': j} for j in dftable3.columns],
        data=dftable3.to_dict('records')#,
        #style={"margin-top":"20px","margin-bottom": "20px"}
        )
        ]#,style= {"margin-bottom": "20px",'textAlign': 'center'}
        ),

    ])
    # dbc.Row([
    #     html.H4("Heavy rain day (15 Feb 2023)")

    # ]),
    # dbc.Row([
    #     html.Div(style={'height': '20px'}),
    #     dash_table.DataTable(
    #     id='table4',
    #     columns=[{'name': j, 'id': j} for j in dftable4.columns],
    #     data=dftable4.to_dict('records')#,
    #     #style={"margin-top":"20px","margin-bottom": "20px"}
    #     )
    #     ],style= {"margin-bottom": "20px",'textAlign': 'center'}
    #     ),
        
    
    # ]),
#     dbc.Row([
#     html.H5("Grid Lock Loop clockwise")
    

#     ]),
#     dbc.Row([
#     dcc.Loading(
#         id='loading',
#         type='circle',
#         children=([
#         dcc.Graph(figure=Valen,id='Valen', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
#         dcc.Graph(figure=Valen5,id='Valen5', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
#         # html.Div(id='webgl-context', style={'display': 'none'})
#    ])
#     )
#     ]),

#     dbc.Row([
#     html.H5("Grid Lock Loop Counterclockwise")

#     ]),

#     dbc.Row([
#         dcc.Graph(figure=Valen4,id='Valen4', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
#         dcc.Graph(figure=Valen1,id='Valen1', style={'width': '400px', 'height': '300px','margin-left': '-50px', 'margin-right': '-50px'}),
#         # html.Div(id='webgl-context', style={'display': 'none'})
#     ])
#     #original-route3#
#     dbc.Row([
#         dbc.Col([
#             dcc.Graph(id='speed-vs-time-graph')
#         ],
#            #xs=12, sm=12, md=12, lg=5, xl=5
#            xs=13, sm=13, md=13, lg=6, xl=6
#         ),
#         dbc.Col([
#             dcc.Graph(id='speed-vs-time-graph1')
#         ],
#            xs=13, sm=13, md=13, lg=6, xl=6
#         ),
#     ]),

#     #route4#
#     dbc.Row([
#         dbc.Col([
#             dcc.Graph(id='speed-vs-time-graph6')
#         ],
#            #xs=12, sm=12, md=12, lg=5, xl=5
#            xs=13, sm=13, md=13, lg=6, xl=6
#         ),
#         dbc.Col([
#             dcc.Graph(id='speed-vs-time-graph7')
#         ],
#            xs=13, sm=13, md=13, lg=6, xl=6
#         ),
#     ])




    
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
    Output("speed-vs-time-graph7", "figure")#,Output('webgl-context', 'children'
                                                    #,Output("Valen", "figure"),Output("Valen1", "figure"),Output("Valen4", "figure"),Output("Valen5", "figure")#,Output("lowest", 'children'),Output("lowest1", 'children'),Output("lowest2", 'children'),Output("lowest3", 'children'),Output("lowest4", 'children'),Output("lowest5", 'children'),Output("lowest6", 'children'),Output("lowest7", 'children')
    ],

    [Input("day-dropdown", "value")#,Input('Valen', 'figure'),Input('Valen1', 'figure'),Input('Valen4', 'figure'),Input('Valen5', 'figure')
                                          ]
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
    lowest2 = serie2.loc[serie2['AverageSpeed'].idxmin()]
    lowest2=lowest2[0:5]

    serie2copy= serie2.reset_index(drop=True)
    #m2, b2 = np.polyfit(serie2copy.index, serie2copy.AverageSpeed, 1)
   # trendline2 = m2 * serie2copy.index  + b2
    #lowest2 = serie2.loc[lowest2].FromTime
    
    
    filtered_df3 = cdf3[cdf3['Day'] == selected_day]
    serie3=filtered_df3.groupby('FromTime')['AverageSpeed'].mean()
    serie3.to_frame()
    serie3 = serie3.reset_index(drop=False)
    lowest3 = serie3.loc[serie3['AverageSpeed'].idxmin()]
    lowest3=lowest3[0:5]

    serie3copy= serie3.reset_index(drop=True)
    #m3, b3 = np.polyfit(serie3copy.index, serie3copy.AverageSpeed, 1)
    #trendline3 = m3 * serie3copy.index  + b3
    #lowest3 = serie3.loc[lowest3].FromTime

    #route2#
    filtered_df4 = cdf4[cdf4['Day'] == selected_day]
    serie4=filtered_df4.groupby('FromTime')['AverageSpeed'].mean()
    serie4.to_frame()
    serie4 = serie4.reset_index(drop=False)
    lowest4 = serie4.loc[serie4['AverageSpeed'].idxmin()]
    lowest4=lowest4[0:5]

    serie4copy= serie4.reset_index(drop=True)
    #m4, b4 = np.polyfit(serie4copy.index, serie4copy.AverageSpeed, 1)
    #trendline4 = m4 * serie4copy.index  + b4
    #lowest4 = serie4.loc[lowest4].FromTime
    
    
    filtered_df5 = cdf5[cdf5['Day'] == selected_day]
    serie5=filtered_df5.groupby('FromTime')['AverageSpeed'].mean()
    serie5.to_frame()
    serie5 = serie5.reset_index(drop=False)
    lowest5 = serie5.loc[serie5['AverageSpeed'].idxmin()]
    lowest5=lowest5[0:5]

    serie5copy= serie5.reset_index(drop=True)
    #m5, b5 = np.polyfit(serie5copy.index, serie5copy.AverageSpeed, 1)
    #trendline5 = m5 * serie5copy.index  + b5
    #lowest5 = serie5.loc[lowest5].FromTime
    



    #route3#
    filtered_df = cdf[cdf['Day'] == selected_day]
    serie=filtered_df.groupby('FromTime')['AverageSpeed'].mean()
    serie.to_frame()
    serie = serie.reset_index(drop=False)
    lowest = serie.loc[serie['AverageSpeed'].idxmin()]
    lowest=lowest[0:5]

    seriecopy= serie.reset_index(drop=True)
    #m, b = np.polyfit(seriecopy.index, seriecopy.AverageSpeed, 1)
    #trendline = m * seriecopy.index  + b
    #lowest = serie.loc[lowest].FromTime
    
    
    filtered_df1 = cdf1[cdf1['Day'] == selected_day]
    serie1=filtered_df1.groupby('FromTime')['AverageSpeed'].mean()
    serie1.to_frame()
    serie1 = serie1.reset_index(drop=False)
    lowest1 = serie1.loc[serie1['AverageSpeed'].idxmin()]
    lowest1=lowest1[0:5]

    serie1copy= serie1.reset_index(drop=True)
    #m1, b1 = np.polyfit(serie1copy.index, serie1copy.AverageSpeed, 1)
    #trendline1 = m1 * serie1copy.index  + b1
    #lowest1 = serie1.loc[lowest1].FromTime


    #route4#
    filtered_df6 = cdf6[cdf6['Day'] == selected_day]
    serie6=filtered_df6.groupby('FromTime')['AverageSpeed'].mean()
    serie6.to_frame()
    serie6 = serie6.reset_index(drop=False)
    lowest6 = serie6.loc[serie6['AverageSpeed'].idxmin()]
    lowest6=lowest6[0:5]

    serie6copy= serie6.reset_index(drop=True)
    # m6, b6 = np.polyfit(serie6copy.index, serie6copy.AverageSpeed, 1)
    #trendline6 = m6 * serie6copy.index  + b6
    #lowest6 = serie6.loc[lowest6].FromTime
    
    
    filtered_df7 = cdf7[cdf7['Day'] == selected_day]
    serie7=filtered_df7.groupby('FromTime')['AverageSpeed'].mean()
    serie7.to_frame()
    serie7 = serie7.reset_index(drop=False)
    lowest7 = serie7.loc[serie7['AverageSpeed'].idxmin()]
    lowest7=lowest7[0:5]

    serie7copy= serie7.reset_index(drop=True)
    # m7, b7 = np.polyfit(serie7copy.index, serie7copy.AverageSpeed, 1)
    #trendline7 = m7 * serie7copy.index  + b7
    #lowest7 = serie7.loc[lowest7].FromTime

    # fig = {
    #     'data': [{'x': serie.FromTime, 'y': serie.AverageSpeed, 'type': 'line'},{'x': cdf.FromTime, 'y': cdf.AverageSpeed, 'type': 'scatter' }],
    #     'layout': {'title': f'Speed vs. Time on {selected_day}'}
    # }
    # fig1 = {
    #     'data': [{'x': serie1.FromTime, 'y': serie1.AverageSpeed, 'type': 'line'}],
    #     'layout': {'title': f'Speed vs. Time on {selected_day}'}
    # }
    # return fig,fig1

#'layout': {'yaxis': {'range': [0, 60]

    #route1#
    fig2 = {
        'data': [
            go.Scatter(
                x=serie2.FromTime,
                y=cdf2.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie2.FromTime,
                y=serie2.AverageSpeed,
                mode='lines',
                line={'width': 1, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie2.FromTime, y=trendline2,line={'color':'red'})

            
        ],'layout': {'title': f'Graph6: Rama IV Intersection to <br>Na Ranong Intersection ','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False
    }
    }
    # Add axis titles to layout
    fig3 = {
        'data': [
            go.Scatter(
                x=serie3.FromTime,
                y=cdf3.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie3.FromTime,
                y=serie3.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie3.FromTime, y=trendline3,line={'color':'red'},name='Trend')
            
        ],'layout': {'title': f'Graph4: Na Ranong Intersection to <br>Rama IV Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8}
    }
    }

   #route2#
    fig4 = {
        'data': [
            go.Scatter(
                x=serie4.FromTime,
                y=cdf4.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie4.FromTime,
                y=serie4.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie4.FromTime, y=trendline4,line={'color':'red'},name='Trend')
        ],'layout': {'title': f'Graph7: Na Ranong Intersection to <br>Sunlakakon Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False
    }
    }
    # Add axis titles to layout
    fig5 = {
        'data': [
            go.Scatter(
                x=serie5.FromTime,
                y=cdf5.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie5.FromTime,
                y=serie5.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie5.FromTime, y=trendline5,line={'color':'red'})
        ],'layout': {'title': f'Graph3: Sunlakakon Intersection to <br>Na Ranong Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
    }



    #route3#
    fig = {
        'data': [
            go.Scatter(
                x=serie.FromTime,
                y=cdf.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie.FromTime,
                y=serie.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie.FromTime, y=trendline,line={'color':'red'})
        ],'layout': {'title': f'Graph2: Kasemrat Intersection to <br>Sunlakakon Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False
    }
    }
    # Add axis titles to layout
    fig1 = {
        'data': [
            go.Scatter(
                x=serie1.FromTime,
                y=cdf1.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie1.FromTime,
                y=serie1.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie1.FromTime, y=trendline1,line={'color':'red'},name='Trend')
        ],'layout': {'title': f'Graph8: Sunlakakon Intersection to <br>Kasemrat Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True },'font': {'size': 8}}
    }

    #route4#
    fig6 = {
        'data': [
            go.Scatter(
                x=serie6.FromTime,
                y=cdf6.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie6.FromTime,
                y=serie6.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                )
            # go.Scattergl(
            # x=serie6.FromTime, y=trendline6,line={'color':'red'})
        ],'layout': {'title': f'Graph5: Kasemrat Intersection to <br>Rama IV Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False
    }
    }
    # Add axis titles to layout
    fig7 = {
        'data': [
            go.Scatter(
                x=serie7.FromTime,
                y=cdf7.AverageSpeed,
                mode='markers',
                marker={'size':3, 'color':'blue'},
                name='Scatter Plot'
            ),
            go.Scattergl(
                x=serie7.FromTime,
                y=serie7.AverageSpeed,
                mode='lines',
                line={'width': 1.2, 'color': 'red'},
                name='Line Plot'
                ),
            # go.Scattergl(
            # x=serie7.FromTime, y=trendline7,line={'color':'red'})
        ],'layout': {'title': f'Graph1: Rama IV Intersection to <br>Kasemrat Intersection','xaxis' :{'title':"Time"},
    'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
    }

    return fig,fig1, html.H4([
        'Speed vs. Time on  ',selected_day],style={'backgroundColor': '#F9F9F9'}),fig2,fig3,fig4,fig5,fig6,fig7#,lowest,lowest1,lowest2,lowest3,lowest4,lowest5,lowest6,lowest7

# @app.callback([Output("special", 'children'),Output("Valen", "figure"),Output("Valen1", "figure"),Output("Valen4", "figure"),Output("Valen5","figure")],
# [Input("special-dropdown","value")])



# def update_graph1(special_value):
#     if special_value == "Valentine's day":
#         Valen = {
#         'data' : [
#         # go.Scatter(
#         #     x=cdf.FromTime,
#         #     y=cdf[cdf['Date']=='2023-02-14'].AverageSpeed,
#         #     mode='markers',
#         #     marker={'size':3, 'color':'blue'},
#         #     name='Scatter Plot'

#         # ),
#             go.Scattergl(
#                 x=cdf.FromTime,
#                 y=cdf[cdf['Date']=='2023-02-14'].AverageSpeed,
#                 mode='lines',
#                 line={'width': 1.2, 'color': 'red'},
#                 name='Valen'
#                 ),
#             ],'layout': {'title': f'Kasemrat Intersection to <br>Sunlakakorn Intersection','xaxis' :{'title':"Time"},
#         'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
#         }

#         Valen1 = {
#             'data' : [
#                 # go.Scatter(
#                 #     x=cdf1.FromTime,
#                 #     y=cdf1[cdf1['Date']=='2023-02-14'].AverageSpeed,
#                 #     mode='markers',
#                 #     marker={'size':3, 'color':'blue'},
#                 #     name='Scatter Plot'

#                 # ),
#                 go.Scattergl(
#                     x=cdf1.FromTime,
#                     y=cdf1[cdf1['Date']=='2023-02-14'].AverageSpeed,
#                     mode='lines',
#                     line={'width': 1.2, 'color': 'red'},
#                     name='Valen1'
#                     ),
#             ],'layout': {'title': f'Sunlakakorn Intersection to <br>Kasemrat Intersection','xaxis' :{'title':"Time"},
#         'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
#         }

#         Valen4 = {
#             'data' : [
#                 # go.Scatter(
#                 #     x=cdf4.FromTime,
#                 #     y=cdf4[cdf4['Date']=='2023-02-14'].AverageSpeed,
#                 #     mode='markers',
#                 #     marker={'size':3, 'color':'blue'},
#                 #     name='Scatter Plot'

#                 # ),
#                 go.Scattergl(
#                     x=cdf4.FromTime,
#                     y=cdf4[cdf4['Date']=='2023-02-14'].AverageSpeed,
#                     mode='lines',
#                     line={'width': 1.2, 'color': 'red'},
#                     name='Valen4'
#                     ),
#             ],'layout': {'title': f'Na Ranong Intersection to <br>Sunlakakorn Intersection','xaxis' :{'title':"Time"},
#         'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
#         }

#         Valen5 = {
#             'data' : [
#                 # go.Scatter(
#                 #     x=cdf5.FromTime,
#                 #     y=cdf5[cdf5['Date']=='2023-02-14'].AverageSpeed,
#                 #     mode='markers',
#                 #     marker={'size':3, 'color':'blue'},
#                 #     name='Scatter Plot'

#                 # ),
#                 go.Scattergl(
#                     x=cdf5.FromTime,
#                     y=cdf5[cdf5['Date']=='2023-02-14'].AverageSpeed,
#                     mode='lines',
#                     line={'width': 1.2, 'color': 'red'},
#                     name='Valen5'
#                     ),
#             ],'layout': {'title': f'Sunlakakorn Intersection to <br>Na Ranong Intersection','xaxis' :{'title':"Time"},
#         'yaxis':{'title': "Average Speed (km/hr)",'range': [0,60], 'fixedrange': True},'font': {'size': 8},'showlegend': False}
#         }
#         return html.H4("Valentine's day (14 Feb 2023)"),Valen,Valen1,Valen4,Valen5


# def release_webgl_context(figure):
#     js_callback = '''
#         const canvas = document.getElementsByTagName('canvas')[0];
#         if (canvas != null) {
#             const gl = canvas.getContext('webgl');
#             if (gl != null) {
#                 console.log('Releasing WebGL context', gl);
#                 gl.getExtension('WEBGL_lose_context').loseContext();
#             }
#         }
#     '''
#     return html.Script(js_callback, type='text/javascript')












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






