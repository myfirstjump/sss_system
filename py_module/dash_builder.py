import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

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
        self.df = data

        self.external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }

        @self.app.callback(
        dash.dependencies.Output(component_id='output-container-range-slider', component_property='children'),
        [dash.dependencies.Input(component_id='my-range-slider', component_property='value')])
        def update_output(value):
            return '您的篩選條件包含 "{}"'.format(value)
        

        self.app.layout = html.Div(
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

                dcc.Markdown(
                    children=
                        """
                            請根據您的需求進行篩選，並按下查詢\n
                        """
                ),
                dcc.Dropdown(
                    id='demo-dropdown',
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='NYC',
                    multi=True
                ),
                html.Div(id='dd-output-container'),

                dcc.RangeSlider(
                    id='my-range-slider',
                    min=0,
                    max=20,
                    step=0.5,
                    value=[5, 15]
                ),
                html.Div(id='output-container-range-slider'),

                dcc.Graph(
                    id='scatter plot',
                    figure = px.scatter(self.df, x="營業額", y="每股淨值",
                                        color='industry_category', hover_name='stock_name',
                                        log_x=True, size_max=60)
                )
            ]
        )

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

