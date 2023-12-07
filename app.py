#!/usr/bin/env python3

# Bibliotecas
from dash import dash, dcc, html, Input, Output # acrescentando os módulos
import dash_bootstrap_components as dbc # estilização do bootstrap
import dash_daq as daq # estilização do daq
from modbusrtu import *


# Estilização externa
external_stylesheets=[dbc.themes.LUMEN]

# Cria app com dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout do app
app.layout = html.Div([ 
    
    html.Div([  # Título
        html.Div(html.Img(src=app.get_asset_url('logo-ifce.png')), id='logoif'),
        html.H1('Supervisório do Tank'),
    ], id='div_titulo'),

    html.Div([  
        html.Div([   
            html.Div([
                daq.LEDDisplay(id='display1',label="Temperatura",value="0000",color="red",backgroundColor="black",size=64,),
                daq.LEDDisplay(id='display2',label="Tensão",value="0000",color="red",backgroundColor="black",size=64),
                daq.Gauge(labelPosition='bottom',id='gauge1',label="Tensão (V)",value=0,showCurrentValue=True,max=100,min=0,color={"gradient":True,"ranges":{"green":[0,40],"yellow":[40,80],"red":[80,100]}}),
            ],id='div_titulo1'),

            html.Div([
                daq.LEDDisplay(id='display3',label="Vibração",value="0000",color="red",backgroundColor="black",size=64),
                daq.LEDDisplay(id='display4',label="Corrente",value="0000",color="red",backgroundColor="black",size=64),
                daq.Gauge(labelPosition='bottom',id='gauge2',label="Corrente (A)",value=0,showCurrentValue=True,max=20,min=0,color={"gradient":True,"ranges":{"green":[0,12],"yellow":[12,16],"red":[16,20]}}),
            ],id='div_titulo2'), 
        ],id='div_ledgau'), 

        html.Div([
            daq.Tank(id='tank1',value=0,min=0,max=1000,showCurrentValue=True,color='red',label="Default",height=475,width=350),
        ],id='div_tank'),     
    ],id='div_layout'),     

    dcc.Interval(interval=2000,n_intervals=0,id='tempo')
],id='tudo')

@app.callback(
    [Output('display1', 'value'),
    Output('display2', 'value'),
    Output('display3', 'value'),
    Output('display4', 'value'),
    Output('gauge1', 'value'),
    Output('gauge2', 'value'),
    Output('tank1', 'value')],
    Input('tempo', 'n_intervals'),
)

def update_output(input):   
    global tensao, corrente, temp, vibracao, vtank
    tensao, corrente, temp, vibracao, vtank = read_register()
    display1_value = temp
    display2_value = tensao
    display3_value = vibracao
    display4_value = corrente
    gauge1_value = tensao
    gauge2_value = corrente
    tank1_value = vtank

    return (
        f"{int(display1_value):04d}",
        f"{int(display2_value):04d}",
        f"{int(display3_value):04d}", 
        f"{int(display4_value):04d}",
        gauge1_value,
        gauge2_value,
        tank1_value
    )


if __name__ == '__main__':
    app.run_server(debug=True)