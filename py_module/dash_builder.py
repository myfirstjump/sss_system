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
        self.app = dash.Dash(__name__)#, external_stylesheets=self.external_stylesheets)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }
        self.style = {
            'query_statment_width': '15%',
            'input_height': '25px',
            'dropdown_width': '50px',
            'n_day_input_with': '50px',
            'unit_input_width': '120px',
            '2-words-checklist-width': '80px',
            '3-words-checklist-width': '100px'
        }

        self.dcc_elements = {
            'dropdown_placeholder': '日',
            'input_placeholder': '---',
        }

        self.app.layout = html.Div([ # TOP DIV

                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':'10px 15px 10px 30px', 'padding':'10px'})
                ]),# HEADER

                html.Div([ # FILTER & DISPLAY

                    # FILTER
                    html.Div([
                        'FILTER',
                        html.Div([
                            html.P('選項一', style={'display': 'inline-block'}),
                            html.Button('>>', style={'display': 'inline-block','position':'absolute', 'right':'0'})
                        ], style={'position': 'relative', 'margin':'10px 30px 10px 30px', 'padding':'10px'}),
                        html.Div([
                            html.P('選項二', style={'display': 'inline-block'}),
                            html.Button('>>', style={'display': 'inline-block','position':'absolute', 'right':'0'})
                        ], style={'position': 'relative', 'margin':'10px 30px 10px 30px', 'padding':'10px'}),
                    ], style={'display': 'inline-block', 'width': '45%', 'height': '500px', 'border':'solid', 'verticalAlign': "middle", 'margin':'10px 15px 10px 30px', 'padding':'10px'}),# FILTER

                    # DISPLAY
                    html.Div([
                        "DISPLAY"
                    ], style={'display': 'inline-block', 'width': '45%', 'height': '500px', 'border':'solid', 'verticalAlign': "middle", 'margin':'10px 30px 10px 15px', 'padding':'10px'}),  # DISPLAY

                ]), # FILTER & DISPLAY

                # SELECTION RESULT
                html.Div([
                    'SELECTION RESULT'
                ], style={'display': 'inline-block', 'width': '100%', 'height': '100%', 'border':'solid', 'margin':'10px 30px 10px 30px', 'padding':'10px'}),  # SELECTION RESULT                            
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

