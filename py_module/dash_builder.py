import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import json

from py_module.pages import (
    basic_01,
    price_02,
    volume_03,
    legal_04,
    credit_05,
    revenue_06,
    self_style
)

class DashBuilder(object):

    def __init__(self, data):
        
        # self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

        self.external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__, suppress_callback_exceptions=True)#, external_stylesheets=self.external_stylesheets)
        self.app.config.suppress_callback_exceptions = True
        # self.app = dash.Dash(__name__)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }

        self.style = self_style.style
        self.item_style = self_style.item_style
        self.output_container_style = self_style.output_container_style
        self.filter_style = self_style.filter_style
        self.button_style = self_style.button_style
        self.selection_style = self_style.selection_style
        self.frame_style = self_style.frame_style
        self.link_div_style = self_style.link_div_style
        self.dropdown_style = self_style.dropdown_style
        self.input_style = self_style.input_style

        self.app.layout = html.Div([ # TOP DIV
                dcc.Store('memory'),
                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':self.style['margin'], 'padding':self.style['padding']})
                ]),# HEADER

                html.Div([ # FILTER & DISPLAY

                    # FILTER
                    html.Div([
                        html.Div('FILTER'),
                        html.Div([ # MENU
                            html.Div(
                                html.Button(
                                    "基本資訊",
                                    id='01-btn',
                                    n_clicks=0,
                                    title='展開基本資訊選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "股價條件",
                                    id='02-btn',
                                    title='展開股價條件選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "成交量值",
                                    id='03-btn',
                                    title='展開成交量值選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "法人籌碼", 
                                    id='04-btn',
                                    title='展開法人籌碼選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "信用交易",
                                    id='05-btn',
                                    title='展開信用交易選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "公司營收",
                                    id='06-btn',
                                    title='展開公司營收選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                        ], style={
                                    'width': '20%', 
                                    'height': '85%', 
                                    'border':'solid 1px', 
                                    'margin':'left', 
                                    'padding':'1%',
                                    'display':'inline-block',
                                    'verticalAlign':'middle'
                        }), # MENU
                        html.Div(id="filter-content", 
                            style={
                                    'width': '70%', 
                                    'height': '85%', 
                                    'border':'solid 1px', 
                                    'margin':'left', 
                                    'padding':'1%',
                                    'display':'inline-block',
                                    'verticalAlign':'middle'
                                }),
                    ], style=self.filter_style),# FILTER

                    # DISPLAY
                    html.Div([
                        "DISPLAY",
                        html.Div([
                        ],
                        id='dynamic-output-container',
                        style={
                                    'width': '95%', 
                                    'height': '85%', 
                                    'border':'solid 1px', 
                                    'margin':'left', 
                                    'padding':'1%',
                                    'display':'inline-block',
                                    'verticalAlign':'middle'
                        }),
                    ], style=self.filter_style),  # DISPLAY

                ], style=self.frame_style), # FILTER & DISPLAY

                # SELECTION RESULT
                html.Div([
                    'SELECTION RESULT',
                    html.Div([
                    ], 
                    id='dynamic-selection-result',
                    style=self.selection_style)
                ], style=self.frame_style),  # SELECTION RESULT                            
        ])#TOP DIV

        # callbacks
        @self.app.callback(
            Output('filter-content', 'children'),
            Input('01-btn', 'n_clicks'),
            Input('02-btn', 'n_clicks'),
            Input('03-btn', 'n_clicks'),
            Input('04-btn', 'n_clicks'),
            Input('05-btn', 'n_clicks'),
            Input('06-btn', 'n_clicks'),
        )
        def output_update(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, ):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            return button_id

        self.app.run_server(debug=True, dev_tools_hot_reload=True)#, dev_tools_ui=False, dev_tools_props_check=False)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

