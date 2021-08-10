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
        self.app = dash.Dash(__name__, suppress_callback_exceptions=True)#, external_stylesheets=self.external_stylesheets)
        # self.app = dash.Dash(__name__)
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

        self.link_div_style = {
            'margin':'5%',
            'padding':'5%'
        }

        self.dropdown_style = {
            'display':'inline-block',
            'verticalAlign': 'middle',
            'padding':'0% 1% 0% 1%',
            'width': '65px',
        }
        self.input_style = {
            'display':'inline-block',
            'verticalAlign': 'middle',
            'width': '20%',
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
                return basic_01.create_layout(self.item_style, self.button_style)


        @self.app.callback(
            Output('0101-output-text', 'children'),
            Input('basic-0101-button', 'n_clicks'),
        )
        def update_output(n_clicks):
            # ctx = dash.callback_context
            # button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if n_clicks > 0:
                return basic_01.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
            else:
                return ''

        @self.app.callback(
            Output('basic-0101-button', 'n_clicks'),
            Input('basic-0101-x', 'n_clicks'),
        )
        def update_output(n_clicks):
            return 0



        # @self.app.callback(
        #     Output('0201-output-text', 'children'),
        #     Input('price-0201-button', 'n_clicks'),
        # )
        # def update_output(n_clicks):
        #     if n_clicks > 0:
        #         return price_02.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #     else:
        #         return ""
        # @self.app.callback(
        #     Output('price-0201-button', 'n_clicks'),
        #     Input('price-0201-x', 'n_clicks'),
        # )
        # def update_output(n_clicks):
        #     return 0  




        # for _ in ('basic-0101', 'price-0201', 'volume-0301', 'legal-0401', 'credit-0501', 'revenue-0601'):

        #     page, num = _.split('-')
        #     @self.app.callback(
        #         Output('{}-output-text'.format(num), 'children'),
        #         Input('{}-button'.format(_), 'n_clicks'),
        #     )
        #     def update_output(n_clicks):
        #         if page == 'basic':
        #             if n_clicks > 0:
        #                 return basic_01.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         elif page == 'price':
        #             if n_clicks > 0:
        #                 return price_02.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         elif page == 'volume':
        #             if n_clicks > 0:
        #                 return volume_03.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         elif page == 'legal':
        #             if n_clicks > 0:
        #                 return legal_04.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         elif page == 'credit':
        #             if n_clicks > 0:
        #                 return credit_05.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         elif page == 'revenue':
        #             if n_clicks > 0:
        #                 return revenue_06.create_output(self.item_style, self.button_style, self.dropdown_style, self.input_style)
        #             else:
        #                 return ""
        #         else:
        #             return ""

        #     @self.app.callback(
        #         Output('{}-button'.format(_), 'n_clicks'),
        #         Input('{}-x'.format(_), 'n_clicks'),
        #     )
        #     def update_output(n_clicks):
        #         return 0



        self.app.layout = html.Div([ # TOP DIV

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
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "股價條件",
                                    href="/sss_system/py_module/pages/price_02",
                                    className="tab",
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "成交量值",
                                    href="/sss_system/py_module/pages/volume_03",
                                    className="tab",
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "法人籌碼", 
                                    href="/sss_system/py_module/pages/legal_04", 
                                    className="tab",
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "信用交易",
                                    href="/sss_system/py_module/pages/credit_05",
                                    className="tab",
                                    style={'margin':'5%'}
                                ),
                            style=self.link_div_style),
                            html.Div(
                                dcc.Link(
                                    "公司營收",
                                    href="/sss_system/py_module/pages/revenue_06",
                                    className="tab",
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
                                    'width': '75%', 
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
                            html.Div(id='0101-output-text',),
                            html.Div(id='0201-output-text',),
                            html.Div(id='0301-output-text',),
                            html.Div(id='0401-output-text',),
                            html.Div(id='0501-output-text',),
                            html.Div(id='0601-output-text',),
                            html.Div(id='0701-output-text',),
                            html.Div(id='0801-output-text',),
                            html.Div(id='0901-output-text',),
                            html.Div(id='1001-output-text',),
                            html.Div(id='1101-output-text',),
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

