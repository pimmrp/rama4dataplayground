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

baby7='-'+str(round(((20.34-15.5)/20.34)*100,2))+'%'
baby0='-'+str(round(((15.71-11.3)/15.71)*100,2))+'%'
baby5='-'+str(round(((19.29-18.45)/19.29)*100,2))+'%'
baby3='-'+str(round(((11.27-10.23)/11.27)*100,2))+'%'
baby6='-'+str(round(((19.93-11.69)/19.93)*100,2))+'%'
baby2='+'+str(round(((10.75-10.37)/10.37)*100,2))+'%'
baby4='-'+str(round(((8.99-8.18)/8.99)*100,2))+'%'
baby1='-'+str(round(((11.68-7.23)/11.68)*100,2))+'%'

Valen='-'+str(round(((14.8-13.82)/14.8)*100,2))+'%'
Valen5='+'+str(round(((20.63-20.11)/20.11)*100,2))+'%'
Valen4='-'+str(round(((10.35-9.35)/10.35)*100,2))+'%'
Valen1='-'+str(round(((10.72-9.34)/10.72)*100,2))+'%'


rain='-'+str(round(((14.67-14.35)/14.67)*100,2))+'%'
rain5='-'+str(round(((19.64-18.7)/19.64)*100,2))+'%'
rain4='-'+str(round(((9.79-9.46)/9.79)*100,2))+'%'
rain1='-'+str(round(((11.5-10.7)/11.5)*100,2))+'%'


datatable3 = [('Clockwise','Rama IV -> Kasem Rat',baby7,'',''),
             ('','Kasem Rat -> Sunlakakon',baby0,Valen,rain),
             ('', 'Sunlakakon -> Na Ranong',baby5,Valen5,rain5),
             ('','Na Ranong -> Rama IV',baby3,'',''),
             ('Counterclockwise', 'Kasem Rat -> Rama IV',baby6,'',''),
             ('','Rama IV -> Na Ranong',baby2,'',''),
              ('','Na Ranong -> Sunlakakon',baby4,Valen4,rain4),
             ('', 'Sunlakakon -> Kasem Rat',baby1,Valen1,rain1)]

dftable3 = pd.DataFrame.from_records(datatable3, columns=['Kasem Rat Grid Lock Loop', '','Baby & Kids Best Buy (Thurs 2 FEB)',"VALENTINE'S DAY (Tues 14 FEB)",'Heavy rain day (Wed 15 FEB)'])



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
        html.H4('Traffic Signal Sensors')
    ]
    )
    ]),
    dbc.Row([
    html.Li(["At Kasem Rat intersection, Phase 2 will be opened 30 minutes later in the evening than in the morning due to a large number of vehicles",html.Br(),
             "heading to the expressway and the port."
             ],style={'margin-top':'20px'}),
    html.Li(["At Klong Toei intersection, the opening time of Phase 2 in the morning will be almost twice as long as in the evening,",html.Br(),
             "and Phase 4 will be opened about 20 minutes longer in the evening. This is because Phase 2 is a phase that accepts vehicles",html.Br(),
             "into the city, while Phase 4 is a phase that releases vehicles out of the city."],style={'margin-top':'20px'})

    ]),
    dbc.Row([
    html.Div(
    style={
        'backgroundColor': '#D2DBD6',
        'padding': '10px',"margin-top": "20px"
    },
    children=[
        html.H4('NDRS Sensors')
    ]
    )
    ]),
    dbc.Row([
    html.Li(["At Soi Aree, near Big C Rama 4 branch, the busiest times in terms of car volume are 8 AM and 5 PM on weekdays. On Saturdays and Sundays,",html.Br(),
             "the number of cars in the morning is not high, but it gradually increases until reaching the peak around 5 PM. This is because people may",html.Br(), 
             "engage in activities during the day on weekends, leading to an increase in car traffic."
             ],style={'margin-top':'20px'}),
    html.Li(["At Sukhumvit 22, the busiest times in terms of car volume are 8 AM and 4 PM on weekdays. In the morning, the number of cars is significantly",html.Br(),
             "higher than in the evening because this road serves as a shortcut to Sukhumvit Road. On Saturdays and Sundays, the number of cars in the morning",html.Br(),
             "is not high, but it gradually increases until reaching the peak around 5 PM. This is because people may engage in activities during the day on weekends,",html.Br(), 
             "leading to an increase in car traffic."],style={'margin-top':'20px'}),
    html.Li(["At Ratchadaphisek Road, near Ocean Tower 1 building, the busiest times in terms of car volume are 8 AM and 5 PM on weekdays. Both morning and evening",html.Br(), 
             "periods have a relatively high number of cars because this road connects Asoke Junction and Rama 4 Junction. On Saturdays and Sundays, the number of cars",html.Br(), 
             "in the morning is not high, but it gradually increases until reaching the peak around 5 PM. This is because people may engage in activities during the day on",html.Br(),
             "weekends, leading to an increase in car traffic."
    ],style={'margin-top':'20px'}),
    html.Li(["At Khlong Toei Junction, the busiest times in terms of car volume are 8 AM and 5 PM on weekdays. The number of cars in this area is significantly high as",html.Br(),
             "it is a large four-way junction and there are important facilities nearby, such as the Queen Sirikit National Convention Center and Khlong Toei Market.",html.Br(), 
             "On Saturdays and Sundays, the number of cars in the morning is not high, but it gradually increases until reaching the peak around 5 PM. This is because",html.Br(),
             "people may engage in activities during the day on weekends, leading to an increase in car traffic."
    ],style={'margin-top':'20px'}),
    html.Li(["On Phra Ram 3 Road, near Soi 85, the highest car volume is during the 7 AM period, gradually decreasing afterward. This is because this area is relatively",html.Br(),
             "far from office locations, resulting in fewer cars in the evening. On weekends, there is less car traffic in the morning, but it gradually increases and then",html.Br(), 
             "gradually decreases after 5 PM."
    ],style={'margin-top':'20px'}),
    html.Li(["At the Expressway Authority of Thailand near the Customs Department on the Chaloem Maha Nakhon Expressway, the highest car volume is during",html.Br(), 
             "the 8 AM period, gradually decreasing afterward. This is because this area is relatively far from office locations, resulting in fewer cars",html.Br(),
             "in the evening. On weekends, there is less car traffic in the morning, but it gradually increases and then gradually decreases after 5 PM."

    ],style={'margin-top':'20px'}),
    html.Div(["In all junctions, the most common types of vehicles encountered are cars and motorcycles, which have similar volumes. This is followed by pickup trucks,",html.Br(),
              "vehicles with seven or more wheels, buses, trucks, and trailers, in that order."
    
    ],style={'margin-top':'20px'})

    ]),




    dbc.Row([
    html.Div(
    style={
        'backgroundColor': '#D2DBD6',
        'padding': '10px',"margin-top": "20px"
    },
    children=[
        html.H4('Bluetooth Sensors')
    ]
    )
    ]),
    dbc.Row([
    html.H5('Morning Rush Hours (7.00 - 10.00 AM)')

    ],style={'backgroundColor': '#F7F5EB',
        'padding': '10px',"margin-top": "20px"}),
    dbc.Row([
    html.Div('It is a period when there are many vehicles traveling to work on Sukhumvit Road.'),
    ],style={'font-size':'18px'}),
    dbc.Row([
        
    html.Li(['There will be vehicles coming from Rama 3 Road and have to travel through the Na Ranong Junction to the Rama IV Junction.']),
    html.Li(['This leads to a rapid decrease in the average speed of vehicles on Graph 4: Na Ranong to Rama IV during morning rush hours,',html.Br(),
             'starting from around 6.00 AM on regular weekdays. However, there is not much change during Saturday and Sunday.'],style={"margin-top": "10px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/graph8mon.png",alt="Monday",style={"width": "400px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/graph8sat.png",alt="Saturday",style={"width": "400px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),
    html.Li(['There are cars coming from the expressway and traveling through the Sunlakakon Junction to the Kasem Rat junction (graph8).',html.Br(), 
             'It can be observed that there is a significant decrease in vehicle speed during the time period of 6.30-7.00 AM ',html.Br(), 'compared to the previous time period on weekdays,'
             'while there is not much change on weekends.'

    ],style={"margin-top": "40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD%202566-05-07%20%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%2019.53.58.png",alt="Monday",style={"width": "400px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/graph4sat.png",alt="Saturday",style={"width": "400px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),
    html.Li(['There are vehicles coming from On Nut and Bangna, traveling through Kasem Rat Junction to Rama IV Junction (graph5)',html.Br(), 
             'and turning up towards Sirikit Center. Speed reduction starts at 7.00 AM and is noticeable',html.Br(),'when compared to Monday and Saturday, where there is almost no change in speed due to work closures.'
    ],style={"margin-top": "40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/graph5mon.png",alt="Monday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/graph5sat.png",alt="Saturday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),
    dbc.Row([
    html.H5('Evening Rush Hours (4.00 - 7.00 PM)')

    ],style={'backgroundColor': '#F7F5EB',
        'padding': '10px',"margin-top": "70px"}),

    ]),
    dbc.Row([
    html.Li(['There are converging points of vehicles from the shortcut roads of Sukhumvit 22, 24, and 26',html.Br(), 
             'to the expressway at the Sunlakakon junction. Some vehicles also need to turn onto Sukhumvit Road, causing the traffic to move slowly.'
    ]
    ,style={"margin-top": "20px"}
    ),
    html.Li(['On the link from Rama IV to Kasem Rat (graph 1), there are a lot of vehicles coming out, resulting in a reduction in speed from the usual',html.Br(),
             '20 km/h during the afternoon to just 9 km/h in the evening. This is a common issue during the evening rush hours, as people are returning from work,',html.Br(), 
             'that the route is opposite from the morning. At around 5:00 PM, the speed drops to as low as 7 km/hr but this situation does not occur on Saturday.',html.Br(), 
             'Additionally, there is a gas station along the road between Rama IV and Kasem Rat junction, which can contribute to traffic congestion.'
    ],style={"margin-top": "10px"}),

    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g1mon.png",alt="Monday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g1sat.png",alt="Saturday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),
    ]),

    dbc.Row([
    html.Li(['And in graph 2, the speed decreases from 6:00 AM to 6:00 PM on weekdays because it is the route to the expressway and there may be ',html.Br(),'vehicles throughout.'
             'Whereas on weekends, there is a range where the speed decreases less, particularly in the afternoon.'
    ]
    ,style={"margin-top": "40px"}
    ),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g2mon.png",alt="Monday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g2sat.png",alt="Saturday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),

    ]),
    dbc.Row([
    html.H5('Special Information')

    ],style={'backgroundColor': '#F7F5EB',
        'padding': '10px',"margin-top": "70px"}),

    dbc.Row([
    html.Li(['In the section of Graph 6, which is the route from Rama IV Junction to Na Ranong Junction, a hotspot in the city with the Khlong Toei Market,',html.Br(), 
             'the speed of vehicles is consistently maintained throughout the route, which is clearly noticeable.'
    ]
    ,style={"margin-top": "20px"}
    ),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g6mon.png",alt="Monday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Monday"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g6sat.png",alt="Saturday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Saturday"],style={"margin-left": "140px"})

    ]),

    ]),
    dbc.Row([
    html.Li(['On all the weekdays, in graph 3 (Sunlakakon Junction to Na Ranong Junction), the speed decreases around 7:00 AM',html.Br(),'and remains constant throughout the day.']),
    html.Li(['On all the weekdays, in graph 7 (Na Ranong Junction to Sunlakakon Junction), the speed varies but not significantly,',html.Br(),
             'with the data range starting to decrease around 8:00 AM and remaining constant thereafter. These observations correspond to the fact',html.Br(),'that this route does not experience a significant amount of traffic congestion.'
    ],style={"margin-top": "10px"}
    ),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g3.png",alt="Monday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Graph3"],style={"margin-left": "140px"})
    
    ],style={"margin-left":"40px"}),
    dbc.Col([
    html.Img(src=f"https://github.com/pimmrp/rama4dataplayground/raw/master/g7.png",alt="Saturday",style={"width": "330px", "height": "270px","margin-top": "20px"}),#, style={"float": "left", "margin-right": "0px","display": "block", "margin": "0 auto", "width": "400px", "height": "270px"}),
    html.Div(["Graph7"],style={"margin-left": "140px"})

    ]),

    ] ,style={"margin-top": "40px"}),

    dbc.Row([
    html.Li(['Table summarizing vehicles speed data on special days that differ from normal weekdays except the special days.',html.Br(),'(Present the data in the form of percentage decrease or increase.)'
    
    ])

    ],style={"margin-top": "40px"}),
    dbc.Row([
        #html.Div(style={'height': '20px'}),
        dash_table.DataTable(
        id='table',
        columns=[{'name': j, 'id': j} for j in dftable3.columns],
        data=dftable3.to_dict('records'),#,
        #style={"margin-top":"20px","margin-bottom": "20px"}
        style_cell={'textAlign': 'center','font-size': '13px'}
        )
        ],style= {"margin-bottom": "20px","margin-top": "20px",'textAlign': 'center','font': {'size': 7}}
        ),

    dbc.Row([
    html.Div("From the table above, it can be summarized that:"),
    html.Li(["When events are held at Sirikit Convention Center, there is a decrease in overall vehicle speed, especially in the following routes:"],style= {"margin-top": "10px"}),
    html.Div(['- Rama IV -> Kasem Rat and Kasem Rat -> Sunlakakon: This is due to the congestion caused by people returning from work,',html.Br(),
              'while trying to make way for vehicles coming to attend the event at the convention center.'],style= {"margin-left": "40px"}),
    html.Div(['- Kasem Rat -> Rama IV and Sunlakakon -> Kasem Rat: Due to the high demand for transportation to attend the exhibition event.'],style= {"margin-left": "40px"}),
    html.Li(['During various festivals and when it is raining, there is a decrease in overall vehicle speed on all links.'])
    


    ],style={"margin-bottom": "40px"})

    




    ]),

        

    










#     dbc.Row([
#     html.Div(
#     style={
#         'backgroundColor': '#D2DBD6',
#         'padding': '10px',"margin-top": "18px"
#     },
#     children=[
#         html.H4('Morning Rush Hours (7.00-10.00 am)')
#     ]
#     )
#     ]),
#     dbc.Row([
#         html.P(['People have to try to catch a ride to work and get on Sukhumvit Road. There will be cars coming from Rama III Road',html.Br(),
#                'that have to pass through Na Ranong Intersection to Rama IV Intersection.',html.Br(),
#                 'The data collected shows that this is related to information from all sensors:'],style={'font-size':'16px'}),
#         html.Li([
#             'The number of cars is higher than usual.'],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'The speed of the cars is lower than usual.'],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'There is a traffic light phase that allows cars to move more smoothly.'],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'There are cars coming from the expressway at the port and traveling through the Sunlakakon intersection to the Kasemrat intersection.'],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'There are cars coming from On Nut and Bangna that travel through Kasemrat to Rama IV and turn up to Sirikit Center.'],style={'font-size':'14px'}
#         ),
#         html.P(['There may also be some parts from Rama IV to Klong Toei that are congested as well.'],style={'font-size':'16px'}),
    
#     ], style={
#         'backgroundColor': '#FFF8F8',
#         'padding': '10px',"margin-top": "20px"}
#     ),
    
#     dbc.Row([
#     html.Div(
#     style={
#         'backgroundColor': '#D2DBD6',
#         'padding': '10px',"margin-top": "20px"
#     },
#     children=[
#         html.H4('Evening Rush Hours (4.00-7.00 pm)')
#     ]
#     )
#     ]),
#     dbc.Row([
#         html.P(['There are convergence points of cars from the shortcut roads of Sukhumvit 22, 24, and 26',html.Br(),
#                'to the expressway at the Sunlakakon intersection. Therefore, there is more Phase 2 traffic light opening',html.Br(),
#                 'than in the morning.'],style={'font-size':'16px'}),
#         html.Li([
#             'There is a need to travel through Kasemrat to Sunlakakon and congestion between Rama IV to Kasemrat.'],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'Some cars also need to turn onto Sukhumvit Road, causing the traffic to move slowly.'],style={'font-size':'14px'}
#         ),
#         html.P(['The route from Klong Toei intersection to Rama IV will have more cars because in the evening rush hour,',html.Br(),
#                 'people need to travel back home, alternating with Rama IV to Na Ranong or the expressway.'],style={'font-size':'16px'}),
    
#     ], style={
#         'backgroundColor': '#FFF8F8',
#         'padding': '10px',"margin-top": "20px"}
#     ),
#     dbc.Row([
#     html.Div(
#     style={
#         'backgroundColor': '#D2DBD6',
#         'padding': '10px',"margin-top": "20px"
#     },
#     children=[
#         html.H4('Additional information')
#     ]
#     )
#     ]),
#     dbc.Row([
#         html.Li([
#             "On Valentine's Day and rainy days, there will be more traffic congestion than usual, and the speed of cars will be slower than normal."],style={'font-size':'14px'}
#         ),
#         html.Li([
#             'Kasemrat to Rama IV has many double-parked cars, which take up one lane. This may cause more cars than usual',html.Br(),
#             'and the speed of the cars that are close to 0 km/hr is higher than in other areas.'
#             ],style={'font-size':'14px'}
#         ),
#     ], style={
#         'backgroundColor': '#FFF8F8',
#         'padding': '10px',"margin-top": "20px"}
#     ),











#     # dbc.Row([
#     # html.P([
#     #     html.Ul([
#     #     html.Li(["From the graph1"],style={'font-size': '12px'}),
#     #     html.P(["It was found that the trend of this route is that the vehicle speed is very slow in the evening (traffic congestion).", html.Br(),
#     #                    "This is due to the fact that in the evening, many vehicles need to use this route.",html.Br(),
#     #                    "Moreover, there are converging points of cars from the shortcut roads of Sukhumvit 22, 24, and 26 to the expressway at the Sunlakakon intersection.",html.Br(),
#     #                    "Some also need to turn onto Sukhumvit Road, causing the traffic to move slowly."],style={'font-size': '10px'}),
#     #     html.Li(["From the graph2"],style={'font-size': '12px'}),
#     #     html.Li(["From the graph3"],style={'font-size': '12px'}),
#     #     html.Li(["From the graph4"],style={'font-size': '12px'})
#     #     ])

#     # ])
#     # ])
# ])