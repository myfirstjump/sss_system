import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.express as px
import pandas as pd

from py_module.utils import Header, make_dash_table

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
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }
        self.style = {
            'query_statment_width': '150px',
            'input_height': '25px',
            'dropdown_width': '50px',
            'n_day_input_with': '50px',
            'unit_input_width': '120px',
            '2-words-checklist-width': '80px',
            '3-words-checklist-width': '100px'
        }

        self.dcc_elements = {
            'dropdown_placeholder': '日',
            'input_placeholder': '10',
        }

        # 股本
        @self.app.callback(
            Output('equity-right', 'min'),
            Input('equity-left', 'value'),
        )        
        def update_equity_min(left_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最小值輸入後，最大值的min限制應該會改變。
            '''
            return left_value
        
        @self.app.callback(
            Output('equity-left', 'max'),
            Input('equity-right', 'value'),
        )
        def update_equity_max(right_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最大值輸入後，最小值的max限制應該會改變。
            '''
            return right_value
        
        # 股價
        @self.app.callback(
            Output('price-right', 'min'),
            Input('price-left', 'value'),
        )        
        def update_price_min(left_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最小值輸入後，最大值的min限制應該會改變。
            '''
            return left_value
        
        @self.app.callback(
            Output('price-left', 'max'),
            Input('price-right', 'value'),
        )
        def update_price_max(right_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最大值輸入後，最小值的max限制應該會改變。
            '''
            return right_value


        # 振幅
        @self.app.callback(
            Output('amplitude-right', 'min'),
            Input('amplitude-left', 'value'),
        )        
        def update_amplitude_min(left_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最小值輸入後，最大值的min限制應該會改變。
            '''
            return left_value
        
        @self.app.callback(
            Output('amplitude-left', 'max'),
            Input('amplitude-right', 'value'),
        )
        def update_amplitude_max(right_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最大值輸入後，最小值的max限制應該會改變。
            '''
            return right_value      

        # 漲跌幅百分比
        @self.app.callback(
            Output('amplitude-percentage-right', 'min'),
            Input('amplitude-percentage-left', 'value'),
        )        
        def update_amplitude_percent_min(left_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最小值輸入後，最大值的min限制應該會改變。
            '''
            return left_value
        
        @self.app.callback(
            Output('amplitude-percentage-left', 'max'),
            Input('amplitude-percentage-right', 'value'),
        )
        def update_amplitude_percent_max(right_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最大值輸入後，最小值的max限制應該會改變。
            '''
            return right_value
        

        @self.app.callback(
            Output('01-output-text', 'children'),
            Input('submit-button', 'n_clicks'),
            State('equity-left', 'value'),
            State('equity-right', 'value')
        )
        def update_output(n_clicks, equity_left, equity_right):
            if (equity_left != None) and (equity_right != None):
                text = u'''股本範圍介於 {} 億元至 {} 億元之股票'''.format(equity_left, equity_right)
            else:
                text = ''
            return text


        self.app.layout = html.Div( # TOP DIV
            style={'backgroundColor': self.colors['background']}, 
            children=[
                html.H1(
                    children='台股選股系統',
                    style={
                        'textAlign': 'left',
                        'color': self.colors['text']
                    }
                ),
                # 2. Div 
                html.Div(
                    children='''A web application framework for TW stock information.''', 
                    style={
                        'textAlign': 'left',
                        'color': self.colors['text']
                    }
                ),

                html.Div( # FILTER CONDITION DIV
                    children=[    
                    dcc.Markdown(
                        "請新增篩選條件，新增完畢後按下送出"
                    ),
                    # 1.
                    html.Div([
                            html.P("01 股本範圍",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                id='equity-left',
                                type='number',
                                min=0,
                                max=999999,
                                placeholder='最小值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 億   ~",
                                style={'width': '15%', 'display': 'inline-block'}), 
                            dcc.Input(
                                id='equity-right',
                                type='number',
                                min=0,
                                max=999999,
                                placeholder='最大值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 億",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block"
                    }),
                    html.Br(),
                    # 2.
                    html.Div([
                            html.P("02 股價範圍",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                id='price-left',
                                type='number',
                                min=0,
                                max=999999,
                                placeholder='最小值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 元   ~",
                                style={'width': '15%', 'display': 'inline-block'}), 
                            dcc.Input(
                                id='price-right',
                                type='number',
                                min=0,
                                max=999999,
                                placeholder='最大值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 元",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block"
                    }),
                    html.Br(),
                    # 3.
                    html.Div([
                            html.P("03 平均振幅",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle",'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" ", id='',
                                style={'width': '80px', 'display': 'inline-block'}), 
                            dcc.Input(
                                id='amplitude-left',
                                type='number',
                                min=-100,
                                max=100,
                                placeholder='最小值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" %   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                id='amplitude-right',
                                type='number',
                                min=-100,
                                max=100,
                                placeholder='最大值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" % ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    # 4.1
                    html.Div([
                            html.P("04 漲跌幅百分比",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}),
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}),  
                            html.P(" ", id='',
                                style={'width': '80px', 'display': 'inline-block'}), 
                            dcc.Input(
                                id='amplitude-percentage-left',
                                type='number',
                                min=-100,
                                max=100,
                                placeholder='最小值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" %   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                id='amplitude-percentage-right',
                                type='number',
                                min=-100,
                                max=100,
                                placeholder='最大值',
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" % ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    # 4.2
                    html.Div([
                            html.P("05 漲跌幅價格",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}),
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" ", id='',
                                style={'width': '80px', 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 元   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 元 ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    # 7.1
                    html.Div([
                            html.P("06 成交張數",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}),
                            html.P(" 平均 ", id='',
                                style={'width': '80px', 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張 ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    html.Br(),
                    # 8.1
                    html.Div([
                            html.P("07 成交量增減張數",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle",'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '增加', 'value': 'increase'},
                                    {'label': '減少', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': self.style['2-words-checklist-width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張 ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    html.Br(),
                    # 8.2
                    html.Div([
                            html.P("08 成交量增減%",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle",'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '增加', 'value': 'increase'},
                                    {'label': '減少', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': self.style['2-words-checklist-width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" %   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" % ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    # 9~12
                    html.Div([
                            html.P("09 法人買賣超",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '外資', 'value': 'foreign'},
                                    {'label': '投信', 'value': 'trust'},
                                    {'label': '自營商', 'value': 'dealer'},
                                ],
                                style={'verticalAlign': "middle", 'width': self.style['3-words-checklist-width'], 'display': 'inline-block'}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '買超', 'value': 'buy'},
                                    {'label': '賣超', 'value': 'sell'},
                                ],
                                style={'verticalAlign': "middle", 'width': self.style['2-words-checklist-width'], 'display': 'inline-block'}), 
                            
                            html.Div([
                                html.P("張數",
                                    style={'width': '70px', 'display': 'inline-block'}),
                                dcc.Input(
                                    placeholder=self.dcc_elements['input_placeholder'],
                                    style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}),
                                html.Br(),
                                html.P("金額",
                                    style={'width': '70px', 'display': 'inline-block'}),
                                dcc.Input(
                                    placeholder=self.dcc_elements['input_placeholder'],
                                    style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}),
                                html.Br(),
                                html.P("發行張數",
                                    style={'width': '70px', 'display': 'inline-block'}),
                                dcc.Input(
                                    placeholder=self.dcc_elements['input_placeholder'],
                                    style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}),
                                html.Br(),
                                html.P("成交比重",
                                    style={'width': '70px', 'display': 'inline-block'}),
                                dcc.Input(
                                    placeholder=self.dcc_elements['input_placeholder'],
                                    style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}),
                            ],style={'verticalAlign': "middle", 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    # 13~15
                    html.Div([
                            html.P("10 融資融券張數",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle",'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '增加', 'value': 'increase'},
                                    {'label': '減少', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': self.style['2-words-checklist-width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 張 ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    html.Br(),
                    html.Div([
                            html.P("11 融資融券增減%",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'verticalAlign': "middle", 'width': self.style['n_day_input_with'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Dropdown(
                                options=[
                                    {'label': '日', 'value': 'd'},
                                    {'label': '週', 'value': 'w'},
                                    {'label': '月', 'value': 'm'},
                                    {'label': '季', 'value': 's'},
                                    {'label': '年', 'value': 'y'}
                                ],
                                value='日',
                                placeholder=self.dcc_elements['dropdown_placeholder'],
                                style={'verticalAlign': "middle",'width': self.style['dropdown_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '增加', 'value': 'increase'},
                                    {'label': '減少', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': self.style['2-words-checklist-width'], 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" %   ~ ",
                                style={'width': '10%', 'display': 'inline-block'}),
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" % ",
                                style={'width': '10%', 'display': 'inline-block'})
                    ], style={
                                "white-space": "pre",
                                "display": "inline-block",
                    }),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        html.Button('送出篩選條件', id='submit-button', n_clicks=0)
                    ], style={'textAlign': 'center'}
                    )                       
                    ], style={ 'verticalAlign': "middle", 'height': '700px', 'width': '49%', 'display': 'inline-block', 'border': 'solid'}
                ),# FILTER CONDITION DIV

                html.Div( # CONDITION DISPLAY DIV
                    children=[    
                        dcc.Markdown(
                            "您所增加的篩選條件"
                        ),
                        html.Div([
                            html.Plaintext(id='01-output-text',)
                        ],
                        )
                    ],
                    style={ 'verticalAlign': "middle", 'height': '700px', 'width': '49%', 'display': 'inline-block', 'border': 'solid'}
                )# CONDITION DISPLAY DIV
            ]
        )#TOP DIV

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

