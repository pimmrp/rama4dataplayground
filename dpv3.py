import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
from info import info_layout
from traffic import tf_layout
from ndrs import ndrs_layout
from bluetooth import bt_layout
from sumall import sumall_layout
from app import app

# app = dash.Dash(__name__, suppress_callback_exceptions=True)

app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                
                dbc.Tab(label="Project Information", tab_id="tab-info", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Traffic Signal Sensor", tab_id="tab-tf", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="NDRS Sensor", tab_id="tab-ndrs", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Bluetooth Sensor", tab_id="tab-bt", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Data Summary",tab_id="tab-sumall", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger")
                  ],
            id="tabs",
            active_tab="tab-info",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([
    
    dbc.Row([
        html.Div([
            # dcc.Input(),
            html.Br(),
           
            ])
    ]),
    dbc.Row(dbc.Col(html.H2("Rama 4 model data playground",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

])

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-info":
        return info_layout
    elif tab_chosen == "tab-tf":
        return tf_layout
    elif tab_chosen == "tab-ndrs":
        return ndrs_layout
    elif tab_chosen == "tab-bt":
        return bt_layout
    elif tab_chosen == "tab-sumall":
        return sumall_layout
    
    return html.P("This shouldn't be displayed for now...")



# if __name__=='__main__':
#     app.run_server(debug= True)
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)