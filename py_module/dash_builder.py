import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd6352

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
        }

        self.dcc_elements = {
            'dropdown_placeholder': '日',
            'input_placeholder': '10',
        }

        self.app.layout = html.Div( # TOP DIV
            style={'backgroundColor': self.colors['background']}, 
            children=[
                html.H1(
                    children='台股選股系統',
                    style={
                        'textAlign': 'center',
                        'color': self.colors['text']
                    }
                ),
                # 2. Div 
                html.Div(
                    children='''A web application framework for TW stock information.''', 
                    style={
                        'textAlign': 'center',
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
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 億   ~",
                                style={'width': '15%', 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
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
                                placeholder=self.dcc_elements['input_placeholder'],
                                style={'width': self.style['unit_input_width'], 'display': 'inline-block', 'height':self.style['input_height']}), 
                            html.P(" 元   ~",
                                style={'width': '15%', 'display': 'inline-block'}), 
                            dcc.Input(
                                placeholder=self.dcc_elements['input_placeholder'],
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
                                    {'label': '增', 'value': 'increase'},
                                    {'label': '減', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': '20%', 'display': 'inline-block'}), 
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
                            html.P("08 成交量增減百分比",
                                style={'width': self.style['query_statment_width'], 'display': 'inline-block'}), 
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
                                    {'label': '增', 'value': 'increase'},
                                    {'label': '減', 'value': 'decrease'},
                                ],
                                style={'verticalAlign': "middle",'width': '20%', 'display': 'inline-block'}), 
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
                                style={'verticalAlign': "middle", 'width': '20%', 'display': 'inline-block'}), 
                            dcc.Checklist(
                                options=[
                                    {'label': '買超', 'value': 'buy'},
                                    {'label': '賣超', 'value': 'sell'},
                                ],
                                style={'verticalAlign': "middle", 'width': '20%', 'display': 'inline-block'}), 
                            
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
                                            
                    ], style={ 'verticalAlign': "middle", 'height': '500px', 'width': '49%', 'display': 'inline-block', 'border': 'solid'}
                ),# FILTER CONDITION DIV

                html.Div( # CONDITION DISPLAY DIV
                    style={ 'verticalAlign': "middle", 'height': '500px', 'width': '49%', 'display': 'inline-block', 'border': 'solid'}
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

