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
                                dcc.Link(
                                    "基本資訊",
                                    href="/sss_system/py_module/pages/basic_01",
                                    className="tab first",
                                    title='展開基本資訊選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "股價條件",
                                    href="/sss_system/py_module/pages/price_02",
                                    className="tab",
                                    title='展開股價條件選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "成交量值",
                                    href="/sss_system/py_module/pages/volume_03",
                                    className="tab",
                                    title='展開成交量值選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "法人籌碼", 
                                    href="/sss_system/py_module/pages/legal_04", 
                                    className="tab",
                                    title='展開法人籌碼選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "信用交易",
                                    href="/sss_system/py_module/pages/credit_05",
                                    className="tab",
                                    title='展開信用交易選項',
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "公司營收",
                                    href="/sss_system/py_module/pages/revenue_06",
                                    className="tab",
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
                        dcc.Location(id="url", refresh=False),
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
                            html.Div([
                                html.Div([html.Div([], id='0101-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0101-x')],
                                id='0101-output-container'),
                            html.Div([
                                html.Div([html.Div([], id='0201-output-inside')],
                                id='0201-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0201-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0301-output-inside')],
                                id='0301-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0301-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0401-output-inside')],
                                id='0401-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0401-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0501-output-inside')],
                                id='0501-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0501-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0601-output-inside')],
                                id='0601-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0601-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0701-output-inside')],
                                id='0701-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0701-x')]),
                            html.Div([
                                html.Div([html.Div([], id='0801-output-inside')],
                                id='0801-output-container', style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0%'}, id='0801-x')]),
                            # html.Div(id='dynamic-output-container', children=[])
                        ],style={
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

                    ], style=self.selection_style)
                ], style=self.frame_style),  # SELECTION RESULT                            
        ])#TOP DIV

        # callbacks
        @self.app.callback(Output("filter-content", "children"), [Input("url", "pathname")])
        def display_page(pathname):
            if pathname == "/sss_system/py_module/pages/basic_01":
                # return basic_01.create_layout(self.item_style, self.button_style)
                return basic_01.layout
            elif pathname == "/sss_system/py_module/pages/price_02":
                # return price_02.create_layout(self.item_style, self.button_style)
                return price_02.layout
            elif pathname == "/sss_system/py_module/pages/volume_03":
                return volume_03.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/legal_04":
                return legal_04.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/credit_05":
                return credit_05.create_layout(self.item_style, self.button_style)
            elif pathname == "/sss_system/py_module/pages/revenue_06":
                return revenue_06.create_layout(self.item_style, self.button_style)
            else:
                # return basic_01.create_layout(self.item_style, self.button_style)
                return basic_01.layout

        # initial_memory = {'0101_btn': 0, '0201_btn': 0, '0301_btn': 0}

        ## 1
        @self.app.callback(
            Output('0101-output-inside', 'children'),
            Output('0101-x', 'style'),
            Input('0101-button', 'n_clicks'),
            State('0101-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx01', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0):
                new_children = basic_01.output_layout
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0101-output-container', 'children'),
            Input('0101-x', 'n_clicks'),
            State('0101-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0101-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0101-x')],
                                id='0101-output-container')
            return blank_container

        ## 2
        @self.app.callback(
            Output('0201-output-inside', 'children'),
            Output('0201-x', 'style'),
            Input('0201-button', 'n_clicks'),
            State('0201-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx02', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0):
                new_children = price_02.output_layout
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0201-output-container', 'children'),
            Input('0201-x', 'n_clicks'),
            State('0201-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0201-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0201-x')],
                                id='0201-output-container')
            return blank_container

        ## 3
        @self.app.callback(
            Output('0301-output-inside', 'children'),
            Output('0301-x', 'style'),
            Input('0301-button', 'n_clicks'),
            State('0301-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx03', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0):
                new_children = volume_03.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0301-output-container', 'children'),
            Input('0301-x', 'n_clicks'),
            State('0301-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0301-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0301-x')],
                                id='0301-output-container')
            return blank_container

        self.app.run_server(debug=True, dev_tools_hot_reload=True)#, dev_tools_ui=False, dev_tools_props_check=False)


        ## 4
        @self.app.callback(
            Output('0401-output-inside', 'children'),
            Output('0401-x', 'style'),
            Input('0401-button', 'n_clicks'),
            State('0401-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx04', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0):
                new_children = legal_04.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0401-output-container', 'children'),
            Input('0401-x', 'n_clicks'),
            State('0401-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0401-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0401-x')],
                                id='0401-output-container')
            return blank_container

        ## 5
        @self.app.callback(
            Output('0501-output-inside', 'children'),
            Output('0501-x', 'style'),
            Input('0501-button', 'n_clicks'),
            State('0501-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx05', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0):
                new_children = credit_05.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0501-output-container', 'children'),
            Input('0501-x', 'n_clicks'),
            State('0501-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0501-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0501-x')],
                                id='0501-output-container')
            return blank_container


        ## 6
        @self.app.callback(
            Output('0601-output-inside', 'children'),
            Output('0601-x', 'style'),
            Input('0601-button', 'n_clicks'),
            State('0601-output-inside', 'children'),
        )
        def display_output(n_clicks, children):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            print('ctx06', ctx.triggered)
            if (n_clicks == None) or (n_clicks == 0):
                print('way 1')
                raise PreventUpdate
            elif (n_clicks > 0) or (data['0601_btn'] > 0):
                new_children = revenue_06.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
                print('way 2')
                # children.append(new_dropdown)
                return new_children, self.button_style
            else:
                print('way 3')
                return [], {'display':'None'}
        @self.app.callback(
            Output('0601-output-container', 'children'),
            Input('0601-x', 'n_clicks'),
            State('0601-output-container', 'children')
        )
        def remove_output(n_clicks, children):
            blank_container = html.Div([
                                html.Div([html.Div([], id='0601-output-inside')],
                                style=self.output_container_style), 
                                html.Button('x', n_clicks=0, style={'display':'None', 'height':'0px'}, id='0601-x')],
                                id='0601-output-container')
            return blank_container


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

