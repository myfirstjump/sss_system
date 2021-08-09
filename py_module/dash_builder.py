import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.express as px
import pandas as pd

from py_module.pages import (
    basic_01,
    price_02,
    volume_03,
    legal_04,
    credit_05,
    revenue_06
)


class DashBuilder(object):
    
    ### 特色:
    # 0. Reference: https://dash.plot.ly/
    # 1. hot-reloading
    # 2. dash語法可直接轉換至html
    # 3. pandas dataframe 可快速轉換成 html table
    # 4. dcc.Graph renders interactive data visualizations, over 35 chart types
    # 5. 可以利用Markdown語法編寫html by dcc.Markdown

    def __init__(self, data):
        
        # self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

        self.external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        # self.app = dash.Dash(__name__,suppress_callback_exceptions=True)#, external_stylesheets=self.external_stylesheets)
        self.app = dash.Dash(__name__)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }

        self.style = {
            'margin':'10px 15px 10px 30px', 
            'padding':'10px'
        }

        self.item_style = {
            'position': 'relative', 
            'margin':'10px 30px 10px 30px', 
            'padding':'8px',
            'border':'solid 1px #bfd5f5',
            'border-radius':'3px',
            'background-color': '#D7EAFA',
        }

        self.button_style = {
            'display': 'inline-block', 
            'float':'right',
            'margin': '15px',
        }

        self.filter_style = {
            'display': 'inline-block', 
            'width': '45%', 
            'height': '500px', 
            'border':'solid 1px', 
            'verticalAlign': "middle",
            'border-radius':'30px',
            'margin':'1%', 
            'padding':'1%'
        }

        self.selection_style = { 
            'width': '90%', 
            'height': '500px', 
            'border':'solid 1px', 
            'verticalAlign': "middle",
            'border-radius':'30px',
            'margin':'auto', 
            'padding':'1%'
        }

        self.frame_style = {
            'width': '90%', 
            'height': '100%', 
            'border':'solid 1px', 
            'margin':'auto', 
            'padding':'1%',            
        }

        @self.app.callback(Output("filter-content", "children"), [Input("url", "pathname")])
        def display_page(pathname):
            if pathname == "/sss_system/py_module/pages/basic_01":
                return basic_01.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/price_02":
                return price_02.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/volume_03":
                return volume_03.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/legal_04":
                return legal_04.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/credit_05":
                return credit_05.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/revenue_06":
                return revenue_06.create_layout(self.item_style, self.button_style)
            else:
                return basic_01.create_layout(self.item_style)


        @self.app.callback(
            Output('01-output-text', 'children'),
            Input('basic_01', 'n_clicks'),
            State('basic_01P', 'children')
        )
        def update_output(n_clicks, text):
            return text


        self.app.layout = html.Div([ # TOP DIV

                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':self.style['margin'], 'padding':self.style['padding']})
                ]),# HEADER

                html.Div([ # FILTER & DISPLAY

                    # FILTER
                    html.Div([
                        'FILTER',
                        html.Div([
                            dcc.Link(
                                "公司基本資訊",
                                href="/sss_system/py_module/pages/basic_01",
                                className="tab first",
                                style={'margin':'5%'}
                            ),
                            dcc.Link(
                                "公司股價",
                                href="/sss_system/py_module/pages/price_02",
                                className="tab",
                                style={'margin':'5%'}
                            ),
                            dcc.Link(
                                "股票成交量",
                                href="/sss_system/py_module/pages/volume_03",
                                className="tab",
                                style={'margin':'5%'}
                            ),
                            dcc.Link(
                                "法人籌碼", 
                                href="/sss_system/py_module/pages/legal_04", 
                                className="tab",
                                style={'margin':'5%'}
                            ),
                            dcc.Link(
                                "信用交易",
                                href="/sss_system/py_module/pages/credit_05",
                                className="tab",
                                style={'margin':'5%'}
                            ),
                            dcc.Link(
                                "公司營收",
                                href="/sss_system/py_module/pages/revenue_06",
                                className="tab",
                                style={'margin':'5%'}
                            ),
                        ], style={
                                    'width': '90%', 
                                    'height': '10%', 
                                    'border':'solid 1px', 
                                    'margin':'auto', 
                                    'padding':'1%',
                        }),
                        dcc.Location(id="url", refresh=False),
                        html.Div(id="filter-content"),
                    ], style=self.filter_style),# FILTER

                    # DISPLAY
                    html.Div([
                        "DISPLAY",
                        html.Div([
                            html.Div(id='01-output-text',),
                            html.Div(id='02-output-text',),
                            html.Div(id='03-output-text',),
                            html.Div(id='04-output-text',),
                            html.Div(id='05-output-text',),
                            html.Div(id='06-output-text',),
                            html.Div(id='07-output-text',),
                            html.Div(id='08-output-text',),
                            html.Div(id='09-output-text',),
                            html.Div(id='10-output-text',),
                            html.Div(id='11-output-text',),
                        ],),
                    ], style=self.filter_style),  # DISPLAY

                ], style=self.frame_style), # FILTER & DISPLAY

                # SELECTION RESULT
                html.Div([
                    'SELECTION RESULT',
                    html.Div([

                    ], style=self.selection_style)
                ], style=self.frame_style),  # SELECTION RESULT                            
        ])#TOP DIV

        self.app.run_server(debug=True, dev_tools_hot_reload=True)



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

