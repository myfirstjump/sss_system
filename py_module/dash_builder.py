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
            'text': '#7FDBFF'
        }

        self.app.layout = html.Div(
            style={'backgroundColor': self.colors['background']}, 
            children=[
                html.H1(
                    children='Hello Dash',
                    style={
                        'textAlign': 'center',
                        'color': self.colors['text']
                    }
                ),
                # 2. Div 
                html.Div(
                    children='''Dash: A web application framework for Python.''', 
                    style={
                        'textAlign': 'center',
                        'color': self.colors['text']
                    }
                ),

                dcc.Markdown(
                    children=
                        """
                            Dash apps can be written in Markdown.\n
                            Dash uses the [CommonMark](http://commonmark.org/)
                            specification of Markdown.\n
                            Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
                            if this is your first introduction to Markdown!\n
                        """
                ),

                dcc.Graph(
                    id='scatter plot',
                    figure = px.scatter(self.df, x="營業額", y="每股淨值",
                                        size='population', color='continent', hover_name='country',
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