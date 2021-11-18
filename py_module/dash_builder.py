import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State, ALL
from dash.exceptions import PreventUpdate
import dash_table
import plotly.express as px
import pandas as pd
import json
import ast
import time
import datetime
from datetime import timedelta

from py_module.pages import (
    basic_01,
    price_02,
    volume_03,
    legal_04,
    credit_05,
    revenue_06,
    self_style,
    query_sentence
)

class DashBuilder(object):

    def __init__(self, stock_data):
        
        # self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

        self.app = dash.Dash(__name__, suppress_callback_exceptions=True)#, external_stylesheets=self.external_stylesheets)
        self.app.config.suppress_callback_exceptions = True
        # self.app = dash.Dash(__name__)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }

        self.arrow_img = 'assets/arrow_img.png'
        self.clear_img = 'assets/全部取消_未.png'
        self.start_img = 'assets/開始選股_未點擊.png'

        self.app.layout = html.Div([
            html.Div([
                        html.H1('股票篩選器', style=self_style.header_div_style),
                        dcc.Store(
                            id='stored_data',
                            storage_type='memory',
                        )
                ]), # header-div
            
            html.Div([

                html.Div([
                    html.Div([ # menu-1
                        html.Button(
                            ["基本資訊", html.Img(src=self.arrow_img, style=self_style.menu_arrow)],
                            id='01-btn',
                            n_clicks=0,
                            title='展開基本資訊選項',
                            className='menu-btn',
                            style=self_style.menu_btn,
                        ),                        
                    ],  
                    style=self_style.link_div_style),
                    html.Div([ # menu-2
                        html.Button(
                            ["股價條件", html.Img(src=self.arrow_img, style=self_style.menu_arrow),],
                            id='02-btn',
                            title='展開股價條件選項',
                            className='menu-btn'
                        ),                        
                    ],
                    style=self_style.link_div_style),
                    html.Div([ # menu-3
                        html.Button(
                            ["成交量值", html.Img(src=self.arrow_img, style=self_style.menu_arrow),],
                            id='03-btn',
                            title='展開成交量值選項',
                            className='menu-btn'
                        ),                        
                    ],
                    style=self_style.link_div_style),
                    html.Div([ # menu-4
                        html.Button(
                            ["法人籌碼", html.Img(src=self.arrow_img, style=self_style.menu_arrow),],
                            id='04-btn',
                            title='展開法人籌碼選項',
                            className='menu-btn'
                        ),                        
                    ],
                    style=self_style.link_div_style),
                    html.Div([ # menu-5
                        html.Button(
                            ["信用交易", html.Img(src=self.arrow_img, style=self_style.menu_arrow),],
                            id='05-btn',
                            title='展開信用交易選項',
                            className='menu-btn'
                        ),                        
                    ],
                    style=self_style.link_div_style),
                    html.Div([ # menu-6
                        html.Button(
                            ["公司營收", html.Img(src=self.arrow_img, style=self_style.menu_arrow),],
                            id='06-btn',
                            title='展開公司營收選項',
                            className='menu-btn'
                        ),                        
                    ],                                
                    style=self_style.link_div_style),
                ], style=self_style.menu_style), # menu

                html.Div([

                    html.Div([ # filter-frame
                        html.Div('請由左方加入篩選類別', style=self_style.frame_text_style),
                        html.Div([], id="filter-content"),
                    ],style=self_style.filter_frame),
                    html.Div([ # condition-frame
                        html.Div('您的選股條件', style=self_style.frame_text_style),
                        html.Div([],
                            id='dynamic-output-container',
                            style=self_style.dynamic_output_container_style),
                        html.Div([
                            html.Img(src=self.start_img,
                                id='selection-btn',
                                style=self_style.selection_btn,
                                className='selection-btn'),
                            html.Img(src=self.clear_img,
                                id='clear-all-btn',
                                style=self_style.selection_btn,
                                className='clear-btn')
                        ]),
                    ], style=self_style.condition_frame),

                    html.Div([
                        html.Div(['篩選結果'], style=self_style.frame_text_style),
                        
                        dcc.Tabs(id='results-tabs', value='dynamic-selection-result-twse', # value是預設顯示值
                            children=[
                                dcc.Tab(label='台灣證券交易所 TWSE (上市)', value='dynamic-selection-result-twse', style=self_style.result_words),
                                dcc.Tab(label='櫃買中心 TPEX (上櫃)', value='dynamic-selection-result-tpex', style=self_style.result_words),
                                dcc.Tab(label='上市 ETF', value='dynamic-selection-result-twse-etf', style=self_style.result_words),
                                dcc.Tab(label='上櫃 ETF', value='dynamic-selection-result-tpex-etf', style=self_style.result_words),
                        ]),
                        dcc.Loading(
                            id='result-content-loading',
                            type='default',
                            children=html.Div([],id='result-content', style=self_style.result_content),
                            color='red',
                        ),
                    ], style=self_style.result_frame) # Results
                ], style=self_style.inner_frame_style), # inner-frame
            ], style=self_style.top_frame_style), # top-frame
        ], style=self_style.top_div_style) # canvas-div

        ### callbacks
        # 1. Links -> filter-content
        @self.app.callback(
            Output('filter-content', 'children'),
            Output('01-btn', 'style'),
            Output('02-btn', 'style'),
            Output('03-btn', 'style'),
            Output('04-btn', 'style'),
            Output('05-btn', 'style'),
            Output('06-btn', 'style'),
            Input('01-btn', 'n_clicks'),
            Input('02-btn', 'n_clicks'),
            Input('03-btn', 'n_clicks'),
            Input('04-btn', 'n_clicks'),
            Input('05-btn', 'n_clicks'),
            Input('06-btn', 'n_clicks'),
        )
        def filter_update(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, ):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == '01-btn':
                content = basic_01.create_filters(button_id)
                style_1 = self_style.menu_btn_onclick; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn
            elif button_id == '02-btn':
                content = price_02.create_filters(button_id)
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn_onclick; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn
            elif button_id == '03-btn':
                content = volume_03.create_filters(button_id)
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn_onclick; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn
            elif button_id == '04-btn':
                content = legal_04.create_filters(button_id)
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn_onclick; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn
            elif button_id == '05-btn':
                content = credit_05.create_filters(button_id)
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn_onclick; style_6 = self_style.menu_btn
            elif button_id == '06-btn':
                content = revenue_06.create_filters(button_id)     
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn_onclick
            else:
                content = html.Div([])
                style_1 = self_style.menu_btn; style_2 = self_style.menu_btn; style_3 = self_style.menu_btn; style_4 = self_style.menu_btn; style_5 = self_style.menu_btn; style_6 = self_style.menu_btn
            return content, style_1, style_2, style_3, style_4, style_5, style_6

        # 2. filter-content -> dynamic-output-container
        self.all_btn = (
            # 1
            '{"index":"01-btn-add-0101","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0102","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0103","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0104","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0105","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0106","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0107","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0108","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0109","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0110","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0111","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0112","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0113","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0114","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0115","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0116","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0117","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0118","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0119","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0120","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0121","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0122","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0123","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0124","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0125","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0126","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0127","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0128","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0129","type":"filter-btn"}.n_clicks',
            # 2
            '{"index":"02-btn-add-0201","type":"filter-btn"}.n_clicks',
            '{"index":"02-btn-add-0202","type":"filter-btn"}.n_clicks',
            '{"index":"02-btn-add-0203","type":"filter-btn"}.n_clicks',
            '{"index":"02-btn-add-0204","type":"filter-btn"}.n_clicks',
            '{"index":"02-btn-add-0205","type":"filter-btn"}.n_clicks',                        
            # 3
            '{"index":"03-btn-add-0301","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add-0302","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add-0303","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add-0304","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add-0305","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add-0306","type":"filter-btn"}.n_clicks',
            # 4
            '{"index":"04-btn-add-0401","type":"filter-btn"}.n_clicks',
            '{"index":"04-btn-add-0402","type":"filter-btn"}.n_clicks', 
            '{"index":"04-btn-add-0403","type":"filter-btn"}.n_clicks', 
            '{"index":"04-btn-add-0404","type":"filter-btn"}.n_clicks', 
            '{"index":"04-btn-add-0405","type":"filter-btn"}.n_clicks', 
            '{"index":"04-btn-add-0406","type":"filter-btn"}.n_clicks',
            # 5           
            '{"index":"05-btn-add-0501","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add-0502","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add-0503","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add-0504","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add-0505","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add-0506","type":"filter-btn"}.n_clicks',
            # 6
            '{"index":"06-btn-add-0601","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0602","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0603","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0604","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0605","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0606","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0607","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0608","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0609","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0610","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0611","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add-0612","type":"filter-btn"}.n_clicks',
        )
        @self.app.callback(
            Output('dynamic-output-container', 'children'),
            Output('stored_data', 'data'),
            Input({'type':'filter-btn', 'index': ALL}, 'n_clicks'),
            Input({'type':'output-btn', 'index': ALL}, 'n_clicks'),
            Input('clear-all-btn', 'n_clicks'),
            State('dynamic-output-container', 'children'),
            State('stored_data', 'data'),
        )
        def output_update(f_btn, x_btn, clear_btn, children, stored_data):
            # if (len(f_btn) == 0):
            #     raise PreventUpdate

            triggered = [t["prop_id"] for t in dash.callback_context.triggered]
            print(triggered)
            # adding = len([1 for i in triggered if i in ('{"index":"01-btn-add","type":"filter-btn"}.n_clicks')])
            adding = len([1 for i in triggered if i in self.all_btn])
            # clearing = len([1 for i in triggered[0].split('"')[7] if i in ('output-btn')]) 
            clearing = len([1 for i in triggered if 'output-btn' in i]) # {"index":"100","type":"output-btn"}
            clear_all = len([1 for i in triggered if i in ('clear-all-btn.n_clicks')])

            if adding:
                ctx = dash.callback_context
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('filter clicked! And button id is:', button_id)
                f_btn = f_btn[0]
                print('f_btn is:', f_btn)

                if (button_id == '{"index":"01-btn-add-0101","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0101 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0101')
                    print('Record:', stored_data['selection_record'])    

                    new_children = basic_01.create_0101(stored_data['output_count'], stock_data)
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0102","type":"filter-btn"}'):
                    print('filter 0102 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0102')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0102(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0103","type":"filter-btn"}'):
                    print('filter 0103 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0103')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0103(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0104","type":"filter-btn"}'):
                    print('filter 0104 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0104')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0104(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0105","type":"filter-btn"}'):
                    print('filter 0105 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0105')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0105(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0106","type":"filter-btn"}'):
                    print('filter 0106 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0106')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0106(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0107","type":"filter-btn"}'):
                    print('filter 0107 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0107')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0107(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0108","type":"filter-btn"}'):
                    print('filter 0108 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0108')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0108(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0109","type":"filter-btn"}'):
                    print('filter 0109 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0109')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0109(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0110","type":"filter-btn"}'):
                    print('filter 0110 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0110')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0110(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0111","type":"filter-btn"}'):
                    print('filter 0111 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0111')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0111(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0112","type":"filter-btn"}'):
                    print('filter 0112 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0112')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0112(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0113","type":"filter-btn"}'):
                    print('filter 0113 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0113')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0113(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0114","type":"filter-btn"}'):
                    print('filter 0114 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0114')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0114(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0115","type":"filter-btn"}'):
                    print('filter 0115 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0115')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0115(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0116","type":"filter-btn"}'):
                    print('filter 0116 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0116')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0116(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0117","type":"filter-btn"}'):
                    print('filter 0117 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0117')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0117(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0118","type":"filter-btn"}'):
                    print('filter 0118 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0118')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0118(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0119","type":"filter-btn"}'):
                    print('filter 0119 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0119')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0119(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0120","type":"filter-btn"}'):
                    print('filter 0120 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0120')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0120(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0121","type":"filter-btn"}'):
                    print('filter 0121 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0121')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0121(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0122","type":"filter-btn"}'):
                    print('filter 0122 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0122')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0122(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0123","type":"filter-btn"}'):
                    print('filter 0123 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0123')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0123(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0124","type":"filter-btn"}'):
                    print('filter 0124 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0124')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0124(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0125","type":"filter-btn"}'):
                    print('filter 0125 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0125')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0125(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0126","type":"filter-btn"}'):
                    print('filter 0126 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0126')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0126(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0127","type":"filter-btn"}'):
                    print('filter 0127 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0127')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0127(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0128","type":"filter-btn"}'):
                    print('filter 0128 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0128')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0128(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"01-btn-add-0129","type":"filter-btn"}'):
                    print('filter 0129 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0129')
                    print('Record:', stored_data['selection_record'])
                    new_children = basic_01.create_0129(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"02-btn-add-0201","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0201 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0201')
                    print('Record:', stored_data['selection_record'])
                    new_children = price_02.create_0201(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"02-btn-add-0202","type":"filter-btn"}'):
                    print('filter 0202 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0202')
                    print('Record:', stored_data['selection_record']) 
                    new_children = price_02.create_0202(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"02-btn-add-0203","type":"filter-btn"}'):
                    print('filter 0203 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0203')
                    print('Record:', stored_data['selection_record'])
                    new_children = price_02.create_0203(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"02-btn-add-0204","type":"filter-btn"}'):
                    print('filter 0204 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0204')
                    print('Record:', stored_data['selection_record'])
                    new_children = price_02.create_0204(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"02-btn-add-0205","type":"filter-btn"}'):
                    print('filter 0205 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0205')
                    print('Record:', stored_data['selection_record'])
                    new_children = price_02.create_0205(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0301","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0301 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0301')
                    print('Record:', stored_data['selection_record'])
                    new_children = volume_03.create_0301(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0302","type":"filter-btn"}'):
                    print('filter 0302 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0302')
                    print('Record:', stored_data['selection_record']) 
                    new_children = volume_03.create_0302(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0303","type":"filter-btn"}'):
                    print('filter 0303 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0303')
                    print('Record:', stored_data['selection_record'])
                    new_children = volume_03.create_0303(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0304","type":"filter-btn"}'):
                    print('filter 0304 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0304')
                    print('Record:', stored_data['selection_record'])
                    new_children = volume_03.create_0304(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0305","type":"filter-btn"}'):
                    print('filter 0305 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0305')
                    print('Record:', stored_data['selection_record'])
                    new_children = volume_03.create_0305(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"03-btn-add-0306","type":"filter-btn"}'):
                    print('filter 0306 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0306')
                    print('Record:', stored_data['selection_record']) 
                    new_children = volume_03.create_0306(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data               
                elif (button_id == '{"index":"04-btn-add-0401","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0401 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0401')
                    print('Record:', stored_data['selection_record'])
                    new_children = legal_04.create_0401(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"04-btn-add-0402","type":"filter-btn"}'):
                    print('filter 0402 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0402')
                    print('Record:', stored_data['selection_record'])
                    new_children = legal_04.create_0402(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"04-btn-add-0403","type":"filter-btn"}'):
                    print('filter 0403 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0403')
                    print('Record:', stored_data['selection_record'])
                    new_children = legal_04.create_0403(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"04-btn-add-0404","type":"filter-btn"}'):
                    print('filter 0404 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0404')
                    print('Record:', stored_data['selection_record']) 
                    new_children = legal_04.create_0404(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"04-btn-add-0405","type":"filter-btn"}'):
                    print('filter 0405 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0405')
                    print('Record:', stored_data['selection_record'])
                    new_children = legal_04.create_0405(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"04-btn-add-0406","type":"filter-btn"}'):
                    print('filter 0406 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0406')
                    print('Record:', stored_data['selection_record'])
                    new_children = legal_04.create_0406(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"05-btn-add-0501","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0501 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0501')
                    print('Record:', stored_data['selection_record'])
                    new_children = credit_05.create_0501(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"05-btn-add-0502","type":"filter-btn"}'):
                    print('filter 0502 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0502')
                    print('Record:', stored_data['selection_record'])
                    new_children = credit_05.create_0502(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"05-btn-add-0503","type":"filter-btn"}'):
                    print('filter 0503 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0503')
                    print('Record:', stored_data['selection_record'])
                    new_children = credit_05.create_0503(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data 
                elif (button_id == '{"index":"05-btn-add-0504","type":"filter-btn"}'):
                    print('filter 0504 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0504')
                    print('Record:', stored_data['selection_record'])
                    new_children = credit_05.create_0504(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data 
                elif (button_id == '{"index":"05-btn-add-0505","type":"filter-btn"}'):
                    print('filter 0505 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0505')
                    print('Record:', stored_data['selection_record']) 
                    new_children = credit_05.create_0505(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data 
                elif (button_id == '{"index":"05-btn-add-0506","type":"filter-btn"}'):
                    print('filter 0506 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0506')
                    print('Record:', stored_data['selection_record'])
                    new_children = credit_05.create_0506(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data 
                elif (button_id == '{"index":"06-btn-add-0601","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0601 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0601')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0601(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0602","type":"filter-btn"}'):
                    print('filter 0602 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0602')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0602(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0603","type":"filter-btn"}'):
                    print('filter 0603 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0603')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0603(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0604","type":"filter-btn"}'):
                    print('filter 0604 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0604')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0604(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0605","type":"filter-btn"}'):
                    print('filter 0605 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0605')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0605(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0606","type":"filter-btn"}'):
                    print('filter 0606 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0606')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0606(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0607","type":"filter-btn"}'):
                    print('filter 0607 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0607')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0607(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0608","type":"filter-btn"}'):
                    print('filter 0608 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0608')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0608(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0609","type":"filter-btn"}'):
                    print('filter 0609 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0609')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0609(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0610","type":"filter-btn"}'):
                    print('filter 0610 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0610')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0610(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0611","type":"filter-btn"}'):
                    print('filter 0611 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0611')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0611(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                elif (button_id == '{"index":"06-btn-add-0612","type":"filter-btn"}'):
                    print('filter 0612 clicked!')
                    # record
                    stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                    stored_data['output_count'] += 1
                    stored_data['output_record'].append(stored_data['output_count'])
                    print('Record:', stored_data['output_record'])
                    stored_data['selection_record'].append('0612')
                    print('Record:', stored_data['selection_record']) 
                    new_children = revenue_06.create_0612(stored_data['output_count'])
                    children.append(new_children)
                    return children, stored_data
                else:
                    return children, stored_data
            elif clearing:
                ctx = dash.callback_context 
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('output clicked! And button id is:', button_id)

                remove_number = int(button_id.split('"')[3]) # 流水號
                remove_idx = stored_data['output_record'].index(remove_number)
                print('remove_number:', remove_number, 'remove_idx:', remove_idx)
                stored_data['output_record'].remove(remove_number)
                del stored_data['selection_record'][remove_idx]
                del children[remove_idx]
                print('Record:', stored_data['output_record'])
                print('Record:', stored_data['selection_record'])
                
            elif clear_all:
                stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
                stored_data['output_record'] = []
                stored_data['selection_record'] = []
                return [], stored_data

            else:
                print('Dont know which filter was clicked!')

            return children, stored_data


        # 3. dynamic-output-container -> dynamic-selection-result
 
        @self.app.callback(
            Output('result-content', 'children'),
            Input('selection-btn', 'n_clicks'),
            Input('results-tabs', 'value'),
            State({'type': ALL, 'index': '0101'}, 'value'), State({'type': ALL, 'index': '0102'}, 'value'), State({'type': ALL, 'index': '0103'}, 'value'), State({'type': ALL, 'index': '0104'}, 'value'), State({'type': ALL, 'index': '0105'}, 'value'), State({'type': ALL, 'index': '0106'}, 'value'), State({'type': ALL, 'index': '0107'}, 'value'), State({'type': ALL, 'index': '0108'}, 'value'), State({'type': ALL, 'index': '0109'}, 'value'), State({'type': ALL, 'index': '0110'}, 'value'), 
            State({'type': ALL, 'index': '0111'}, 'value'), State({'type': ALL, 'index': '0112'}, 'value'), State({'type': ALL, 'index': '0113'}, 'value'), State({'type': ALL, 'index': '0114'}, 'value'), State({'type': ALL, 'index': '0115'}, 'value'), State({'type': ALL, 'index': '0116'}, 'value'), State({'type': ALL, 'index': '0117'}, 'value'), State({'type': ALL, 'index': '0118'}, 'value'), State({'type': ALL, 'index': '0119'}, 'value'), State({'type': ALL, 'index': '0120'}, 'value'), 
            State({'type': ALL, 'index': '0121'}, 'value'), State({'type': ALL, 'index': '0122'}, 'value'), State({'type': ALL, 'index': '0123'}, 'value'), State({'type': ALL, 'index': '0124'}, 'value'), State({'type': ALL, 'index': '0125'}, 'value'), State({'type': ALL, 'index': '0126'}, 'value'), State({'type': ALL, 'index': '0127'}, 'value'), State({'type': ALL, 'index': '0128'}, 'value'), State({'type': ALL, 'index': '0129'}, 'value'),
            State({'type': ALL, 'index': '0201'}, 'value'), State({'type': ALL, 'index': '0202'}, 'value'), State({'type': ALL, 'index': '0203'}, 'value'), State({'type': ALL, 'index': '0204'}, 'value'), State({'type': ALL, 'index': '0205'}, 'value'),
            State({'type': ALL, 'index': '0301'}, 'value'), State({'type': ALL, 'index': '0302'}, 'value'), State({'type': ALL, 'index': '0303'}, 'value'), State({'type': ALL, 'index': '0304'}, 'value'), State({'type': ALL, 'index': '0305'}, 'value'), State({'type': ALL, 'index': '0306'}, 'value'),
            State({'type': ALL, 'index': '0401'}, 'value'), State({'type': ALL, 'index': '0402'}, 'value'), State({'type': ALL, 'index': '0403'}, 'value'), State({'type': ALL, 'index': '0404'}, 'value'), State({'type': ALL, 'index': '0405'}, 'value'), State({'type': ALL, 'index': '0406'}, 'value'),
            State({'type': ALL, 'index': '0501'}, 'value'), State({'type': ALL, 'index': '0502'}, 'value'), State({'type': ALL, 'index': '0503'}, 'value'), State({'type': ALL, 'index': '0504'}, 'value'), State({'type': ALL, 'index': '0505'}, 'value'), State({'type': ALL, 'index': '0506'}, 'value'),
            State({'type': ALL, 'index': '0601'}, 'value'), State({'type': ALL, 'index': '0602'}, 'value'), State({'type': ALL, 'index': '0603'}, 'value'), State({'type': ALL, 'index': '0604'}, 'value'), State({'type': ALL, 'index': '0605'}, 'value'), State({'type': ALL, 'index': '0606'}, 'value'), State({'type': ALL, 'index': '0607'}, 'value'), State({'type': ALL, 'index': '0608'}, 'value'), State({'type': ALL, 'index': '0609'}, 'value'), State({'type': ALL, 'index': '0610'}, 'value'), State({'type': ALL, 'index': '0611'}, 'value'), State({'type': ALL, 'index': '0612'}, 'value'), 
            State('stored_data', 'data'),
        )
        def output_result(btn, tab_value, 
        value0101, value0102, value0103, value0104, value0105, value0106, value0107, value0108, value0109, value0110, 
        value0111, value0112, value0113, value0114, value0115, value0116, value0117, value0118, value0119, value0120, 
        value0121, value0122, value0123, value0124, value0125, value0126, value0127, value0128, value0129, 
        value0201, value0202, value0203, value0204, value0205, 
        value0301, value0302, value0303, value0304, value0305, value0306, 
        value0401, value0402, value0403, value0404, value0405, value0406, 
        value0501, value0502, value0503, value0504, value0505, value0506, 
        value0601, value0602, value0603, value0604, value0605, value0606, value0607, value0608, value0609, value0610, 
        value0611, value0612, stored_data):
            
            print('selection-btn:', btn)
            value_dict = {
                '0101': value0101, '0102': value0102, '0103': value0103, '0104': value0104, '0105': value0105, '0106': value0106, '0107': value0107, '0108': value0108, '0109': value0109, '0110': value0110,
                '0111': value0111, '0112': value0112, '0113': value0113, '0114': value0114, '0115': value0115, '0116': value0116, '0117': value0117, '0118': value0118, '0119': value0119, '0120': value0120, 
                '0121': value0121, '0122': value0122, '0123': value0123, '0124': value0124, '0125': value0125, '0126': value0126, '0127': value0127, '0128': value0128, '0129': value0129,
                '0201': value0201, '0202': value0202, '0203': value0203, '0204': value0204, '0205': value0205, 
                '0301': value0301, '0302': value0302, '0303': value0303, '0304': value0304, '0305': value0305, '0306': value0306,
                '0401': value0401, '0402': value0402, '0403': value0403, '0404': value0404, '0405': value0405, '0406': value0406,
                '0501': value0501, '0502': value0502, '0503': value0503, '0504': value0504, '0505': value0505, '0506': value0506,
                '0601': value0601, '0602': value0602, '0603': value0603, '0604': value0604, '0605': value0605, '0606': value0606, '0607': value0607, '0608': value0608, '0609': value0609, '0610': value0610, '0611': value0611, '0612': value0612, 
            }
            print('value_dict:', value_dict)
            if btn == None:
                raise PreventUpdate

            if btn > 0:
                condition_number = len(stored_data['output_record'])
                query_dict = {}
                for idx in range(condition_number):
                    # if stored_data['selection_record'][idx] == '0101':
                    selection_code = stored_data['selection_record'][idx]
                    if selection_code == '0101':
                        query = query_sentence.create_query_0101(value_dict[selection_code][0])
                        query_dict[idx] = query
                    elif selection_code == '0102':
                        query = query_sentence.create_query_0102(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0103':
                        query = query_sentence.create_query_0103(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0104':
                        query = query_sentence.create_query_0104(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0105':
                        query = query_sentence.create_query_0105(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0106':
                        query = query_sentence.create_query_0106(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0107':
                        query = query_sentence.create_query_0107(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0108':
                        query = query_sentence.create_query_0108(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0109':
                        query = query_sentence.create_query_0109(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0110':
                        query = query_sentence.create_query_0110(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0111':
                        query = query_sentence.create_query_0111(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0112':
                        query = query_sentence.create_query_0112(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0113':
                        query = query_sentence.create_query_0113(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0114':
                        query = query_sentence.create_query_0114(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0115':
                        query = query_sentence.create_query_0115(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0116':
                        query = query_sentence.create_query_0116(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0117':
                        query = query_sentence.create_query_0117(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0118':
                        query = query_sentence.create_query_0118(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0119':
                        query = query_sentence.create_query_0119(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0120':
                        query = query_sentence.create_query_0120(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0121':
                        query = query_sentence.create_query_0121(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0122':
                        query = query_sentence.create_query_0122(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0123':
                        query = query_sentence.create_query_0123(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0124':
                        query = query_sentence.create_query_0124(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0125':
                        query = query_sentence.create_query_0125(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0126':
                        query = query_sentence.create_query_0126(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0127':
                        query = query_sentence.create_query_0127(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0128':
                        query = query_sentence.create_query_0128(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0129':
                        query = query_sentence.create_query_0129(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0201':
                        query = query_sentence.create_query_0201(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0202':
                        query = query_sentence.create_query_0202(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0203':
                        query = query_sentence.create_query_0203(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0204':
                        query = query_sentence.create_query_0204(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0205':
                        query = query_sentence.create_query_0205(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0301':
                        query = query_sentence.create_query_0301(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0302':
                        query = query_sentence.create_query_0302(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0303':
                        query = query_sentence.create_query_0303(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0304':
                        query = query_sentence.create_query_0304(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0305':
                        query = query_sentence.create_query_0305(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0306':
                        query = query_sentence.create_query_0306(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0401':
                        query = query_sentence.create_query_0401(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0402':
                        query = query_sentence.create_query_0402(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0403':
                        query = query_sentence.create_query_0403(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0404':
                        query = query_sentence.create_query_0404(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0405':
                        query = query_sentence.create_query_0405(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0406':
                        query = query_sentence.create_query_0406(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                        query_dict[idx] = query
                    elif selection_code == '0501':
                        query = query_sentence.create_query_0501(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0502':
                        query = query_sentence.create_query_0502(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0503':
                        query = query_sentence.create_query_0503(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0504':
                        query = query_sentence.create_query_0504(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0505':
                        query = query_sentence.create_query_0505(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0506':
                        query = query_sentence.create_query_0506(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0601':
                        query = query_sentence.create_query_0601(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0602':
                        query = query_sentence.create_query_0602(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0603':
                        query = query_sentence.create_query_0603(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0604':
                        query = query_sentence.create_query_0604(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0605':
                        query = query_sentence.create_query_0605(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0606':
                        query = query_sentence.create_query_0606(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0607':
                        query = query_sentence.create_query_0607(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0608':
                        query = query_sentence.create_query_0608(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0609':
                        query = query_sentence.create_query_0609(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    elif selection_code == '0610':
                        query = query_sentence.create_query_0610(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0611':
                        query = query_sentence.create_query_0611(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                        query_dict[idx] = query
                    elif selection_code == '0612':
                        query = query_sentence.create_query_0612(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                        query_dict[idx] = query
                    else:
                        pass
                    
                print('Query Dict:', query_dict)
                total_query = query_sentence.query_combine(query_dict)
                print('Final Query:', total_query)
                data = query_sentence.sql_execute(total_query)
                
                if len(data) == 0:
                    return '無符合項目'
                else:
                    data = pd.DataFrame.from_records(data)
                    df_twse, df_tpex, df_etf_twse, df_etf_tpex = stock_classifier(data)
                    df_twse.to_csv('test_file.csv')
                    if df_twse.shape[0] == 0:
                        df_twse = '無符合項目'
                    else:
                        df_twse = generate_table(df_twse)
                    
                    if df_tpex.shape[0] == 0:
                        df_tpex = '無符合項目'
                    else:
                        df_tpex = generate_table(df_tpex)
                    
                    if df_etf_twse.shape[0] == 0:
                        df_etf_twse = '無符合項目'
                    else:
                        df_etf_twse = generate_table(df_etf_twse)
                    
                    if df_etf_tpex.shape[0] == 0:
                        df_etf_tpex = '無符合項目'
                    else:
                        df_etf_tpex = generate_table(df_etf_tpex)
                    
                if tab_value == 'dynamic-selection-result-twse':
                    return df_twse
                elif tab_value == 'dynamic-selection-result-tpex':
                    return df_tpex
                elif tab_value == 'dynamic-selection-result-twse-etf':
                    return df_etf_twse 
                else:
                    return df_etf_tpex 

                # my_table, _, _, _ = stock_classifier(stock_data)
                # my_table = generate_table(my_table)
                # return my_table

                # return total_query
                # return ['{}\n'.format(i) for i in range(9999)]
            else:
                return ''

        self.app.run_server(debug=True, dev_tools_hot_reload=True)#, dev_tools_ui=False, dev_tools_props_check=False)

def generate_table(stock_data, max_rows=5000):
    return dash_table.DataTable(
                    columns = [{"name": i, "id": i} for i in stock_data.columns],
                    data=stock_data.to_dict('records'),
                    fixed_rows={'headers': True},
                    style_cell={'minWidth': '90px', 'maxWidth': '250px'},
                )

def stock_classifier(data):
    
    data = data.rename(columns={'stock_id':'股票代碼', 'stock_name': '公司', 'industry_category':'產業別'})
    
    data['產業別'] = data.groupby(['股票代碼'])['產業別'].transform(lambda x: ','.join(x))
    data = data.drop_duplicates(subset=['股票代碼'])

    df_etf_all = data[data['產業別'].isin(['ETF', '上櫃指數股票型基金(ETF)', '指數投資證券(ETN)', '受益證券'])]
    df_all = data[~data['產業別'].isin(['ETF', '上櫃指數股票型基金(ETF)', '指數投資證券(ETN)', '受益證券'])]

    df_etf_twse = df_etf_all[df_etf_all['type'].isin(['twse'])]
    df_etf_tpex = df_etf_all[df_etf_all['type'].isin(['tpex'])]
    df_twse = df_all[df_all['type'].isin(['twse'])]
    df_tpex = df_all[df_all['type'].isin(['tpex'])]

    df_twse = df_twse.drop(['type'], axis=1)
    df_tpex = df_tpex.drop(['type'], axis=1)
    df_etf_twse = df_etf_twse.drop(['type'], axis=1)
    df_etf_tpex = df_etf_tpex.drop(['type'], axis=1)

    return df_twse, df_tpex, df_etf_twse, df_etf_tpex

