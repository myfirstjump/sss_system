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

        # @self.app.callback(
        # dash.dependencies.Output(component_id='output-container-range-slider', component_property='children'),
        # [dash.dependencies.Input(component_id='my-range-slider', component_property='value')])
        # def update_output(value):
        #     return '您的篩選條件包含 "{}"'.format(value)

        # @self.app.callback(
        # dash.dependencies.Output(component_id='output-container-range-slider', component_property='children'),
        # [dash.dependencies.Input(component_id='my-range-slider', component_property='value')])
        # def update_output(value):
        #     return '您的篩選條件包含 "{}"'.format(value)       
        

        '''
        ---Callback test1---
        Output id is the corresponding Graph; Output property is the FIGURE? <- 從未定義過figure，但其實是Graph的一個property
        Input id is the slider and the property is slider value <- make sense.
        '''
        # @self.app.callback(
        #     dash.dependencies.Output(component_id='graph-controlled-by-slider', component_property='figure'),
        #     dash.dependencies.Input(component_id='the-slider-no1', component_property='value')
        # )
        # def update_figure(value):
        #     # filtered_df = data['股價'].between(lower_bound, upper_bound, inclusive=True)
        #     filtered_df = data[data['industry_category'] == value]
        #     fig = px.scatter(filtered_df, x="營業額", y="每股淨值",
        #                         color='industry_category', hover_name='stock_name', size='股價')
        #     fig.update_layout(transition_duration=500)

        #     return fig


        '''
        ---Callback test2---
        測試Input和RangeSlider連動 --> 失敗! Sync的功能還沒有很齊全 Slider可以，但是Rangeslider不確定。
        '''
        # @self.app.callback(
        #     [dash.dependencies.Output(component_id='price-range-slider', component_property='value')],
        #     dash.dependencies.Output(component_id='price-range-input-left', component_property='value'),
        #     [dash.dependencies.Input(component_id='price-range-slider', component_property='value')]
        #     dash.dependencies.Input(component_id='price-range-input-left', component_property='value'),
        # )
        # def update_output(slide_value, left_value, right_value):
        #     ctx = dash.callback_context
        #     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        #     if trigger_id == 'price-range-slider':
        #         low_slide, high_slide = slide_value
        #         return slide_value, low_slide, high_slide
        #     elif trigger_id == 'price-range-input-left:

        #         return [left_value, right_value]
    
        @self.app.callback(
            dash.dependencies.Output(component_id='price-range-input-right', component_property='min'),
            # [dash.dependencies.Output('price-range-slider', 'min')],
            dash.dependencies.Input(component_id='price-range-input-left', component_property='value'),
            # dash.dependencies.Output(component_id='price-range-input-right', component_property='value'),
        )
        def update_right_input_price_min(left_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最小值輸入後，最大值的min限制應該會改變。
            '''
            # ctx = dash.callback_context
            # trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            return left_value
        
        @self.app.callback(
            dash.dependencies.Output(component_id='price-range-input-left', component_property='max'),
            # [dash.dependencies.Output('price-range-slider', 'max')],
            dash.dependencies.Input(component_id='price-range-input-right', component_property='value'),
        )
        def update_left_input_price_max(right_value):
            '''
            dcc.Input股價最小值、最大值應有互相影響
            當最大值輸入後，最小值的max限制應該會改變。
            '''
            return right_value        


        @self.app.callback(
            dash.dependencies.Output(component_id='price-volume-fig', component_property='figure'),
            dash.dependencies.Input(component_id='price-range-input-right', component_property='value'),
            dash.dependencies.Input(component_id='price-range-input-left', component_property='value'),
        )
        def update_figure(high_price,low_price, ):
            '''
            Input price與scatter plot連動
            '''  
            data_filter = (data['股價'] > low_price) & (data['股價'] < high_price)
            filtered_data = data[data_filter]
            print(filtered_data)
            fig = px.scatter(
                filtered_data, x='股價', y='每股淨值', size='營業額',
                color='industry_category', hover_name='stock_name'
            )
            fig.update_layout(transition_duration=500)
            return fig


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

                # """
                #     ---Callback test1---
                #     利用Callback方式，建立一個互動的slider去控制一個scatter plot。
                #     1. 首先建立Graph
                #     2. 再來建立Slider
                #     3. 到layout前建立callback
                # """
                html.Div([
                    dcc.Markdown(
                        children=
                            """
                                請根據您想查詢的產業，進行篩選\n
                            """
                    ),
                    dcc.Dropdown(
                        id='industry-category-select',
                        options=[{'label': i, 'value': i} for i in data['industry_category'].unique()],
                        value='食品工業'
                    ),
                ],
                style={'width': '48%', 'display': 'inline-block'}),

                html.Div([
                        dcc.Markdown(
                            children=
                                """
                                    請根據您想查詢的公司名稱，進行篩選\n
                                """
                        ),
                    dcc.Dropdown(
                        id='stock-name-select',
                        options=[{'label': i, 'value': i} for i in data['stock_name'].unique()],
                        value='台積電'
                    ),
                ],
                style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
                
                html.Div(html.Br()),
                html.Div(html.Br()),

                ### Select Price Range
                html.Div([
                    dcc.Markdown(
                        children=
                            """
                                請輸入股價查詢範圍\n
                            """
                    ),
                    dcc.Input(
                        id='price-range-input-left',
                        type='number',
                        min=0,
                        max=1000,
                        # value=0,
                        placeholder='最小值'
                    ),

                    dcc.Input(
                        id='price-range-input-right',
                        type='number',
                        min=0,
                        max=1000,
                        # value=1000,
                        placeholder='最大值'
                    ),
                ],
                style={'width': '48%' ,'display': 'inline-block'}),

                # html.Div([
                #     html.Br(),
                #     dcc.RangeSlider(
                #         id='price-range-slider',
                #         min=0,
                #         max=1000,
                #         step=1,
                #         value=[0, 1000]
                #     ),
                # ]),

                html.Div([
                    html.Br(),
                    dcc.Graph(id='price-volume-fig'),
                    generate_table(data.tail())
                ],
                # style={'float': 'right'}
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

