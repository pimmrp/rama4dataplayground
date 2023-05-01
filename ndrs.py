import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
from app import app
import plotly.graph_objects as go
from dash import dash_table
df1 = pd.read_csv(r'/Users/pim/Desktop/datapg-main/top5max.csv')
df2 = pd.read_csv(r'/Users/pim/Desktop/datapg-main/top5min.csv')
df = pd.read_csv(r'/Users/pim/Desktop/datapg-main/ndrs9-10_2022.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['day_of_week'] = df['timestamp'].dt.day_of_week
df['hour_of_day'] = df['timestamp'].dt.hour
car_type_data = df.groupby(df['timestamp'].dt.day_name())[['car']].sum()
car_type_data['percentage'] = car_type_data['car'] / car_type_data['car'].sum() * 100
vehicle_types = ['7up',	'bus',	'car',	'motorcycle',	'pickup'	,'trailer'	,'truck'	] 


days_map = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


print(df.head())


ndrs_layout = html.Div([
    
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),

    dbc.Row(
        dbc.Col(html.H3("Mean Car Count by Hour",
                        className='text-center text-primary mb-4'),
                width=12)
    ),
    
    dbc.Row([
    
    
    
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': days_map[num], 'value': num} for num in days_map],
        value=[0],  # Set default value to 'Monday'
        multi=True  # Allow multiple inputs
    )]),
    
    dbc.Row([
    
    
    dcc.Graph(id='line-chart')
    ]),


    

    dbc.Row([

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

    ]),
    dbc.Row([

        dcc.Graph(id='vehicle-counts-chart')
    ]),
    
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),
    
    
    
    
    
    
    dbc.Row([
    
     html.H3('Top 5 days with the most number of cars'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df1.columns],
            data=df1.to_dict('records'),
        ),
    ], className='row'),

    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
             ])
    ]),
    
    
    dbc.Row([
     html.H3('Top 5 days with the least number of cars'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df2.columns],
            data=df2.to_dict('records')
        ),
    ], className='row')

    ])


  
    














@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')]
)


def update_line_chart(days):
    # Filter the data for the selected day of the week
    df_selected_days = df[df['day_of_week'].isin(days)]

    # Group the data by hour and calculate the mean of the total car count
    df_selected_days_by_day_hour = df_selected_days.groupby(['day_of_week', df_selected_days['timestamp'].dt.hour]).mean().reset_index()
    df_selected_days_by_day_hour['day_of_week'] = df_selected_days_by_day_hour['day_of_week'].map(days_map)


    # Create a line chart with Plotly Express
    fig = px.line(df_selected_days_by_day_hour, x='timestamp', y='total',
                  color='day_of_week', labels={'timestamp': 'Hour of Day', 'total': 'Mean Car Count'},
                  title='Mean Car Count by Hour on Selected Days of the Week')

    return fig
        

@app.callback(
    Output('vehicle-counts-chart', 'figure'),
    [Input('day-of-week-dropdown', 'value')]
)

def update_chart(day_of_week):
    # Filter data for selected day of week
    filtered_data = df[df['day_of_week'] == day_of_week]
    
    # Group by hour of day and calculate mean counts
    mean_counts = filtered_data.groupby('hour_of_day').mean().reset_index()
    
    # Exclude the 'total' column from the mean counts
    mean_counts = mean_counts.drop(columns=['total'])
    mean_counts = mean_counts.drop(columns=['day_of_week'])
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
        title='Mean Vehicle Counts by Hour of Day for {}'.format(day_of_week),
        xaxis=dict(title='Hour of Day'),
        yaxis=dict(title='Mean Vehicle Count'),
        showlegend=True
    )
    return fig