import os

from py_module.config import Configuration
from py_module.data_reader import DataReader
from py_module.dash_builder import DashBuilder
from py_module.data_processing import DataProcessing

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State, ALL
from dash.exceptions import PreventUpdate
import dash_table
from dash_table.Format import Format, Group
import plotly.express as px
import pandas as pd
import json
import ast
import time
import datetime
from datetime import timedelta

from pages import (
    basic_01,
    price_02,
    volume_03,
    legal_04,
    credit_05,
    revenue_06,
    self_style,
    query_sentence
)

from flask import Flask

server = Flask(__name__)  # object to be referenced by WSGI handler

app = dash.Dash(server=server, suppress_callback_exceptions=True)#, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
app.title = 'Stock Target Selection'


arrow_img = 'assets/arrow_img.png'
clear_img = 'assets/all_clear_unclicked.png'
start_img = 'assets/start_unclicked.png'

config_obj = Configuration()
reader_obj = DataReader()
process_obj = DataProcessing()

file_path = os.path.join(config_obj.data_folder, config_obj.taiwan_stock_info)
print('file_path', file_path)
stock_data = reader_obj.read_csv_data(file_path)
stock_data = process_obj.sss_data_preprocessing(stock_data) #產業別篩選使用
stock_options = process_obj.get_stock_id_and_stock_name_list(stock_data) #個股查詢使用

app.layout = html.Div([
    html.Div([
                html.H1('股票篩選器', style=self_style.header_text_style),
                dcc.Store(
                    id='stored_data',
                    storage_type='session',
                ),
                dcc.Store(
                    id='download_data',
                    storage_type='session',
                ),
        ],style=self_style.header_div_style), # header-div
    
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='股票篩選', children=[
                # 工具1: 篩選股票
                html.Div([

                    html.Div([
                        html.Div([ # menu-1
                            html.Button(
                                ["基本資訊　＞",],
                                id='01-btn',
                                n_clicks=0,
                                title='展開基本資訊選項',
                                style=self_style.menu_btn,
                            ),                        
                        ],  
                        style=self_style.link_div_style),
                        # html.Br(),
                        html.Div([ # menu-2
                            html.Button(
                                ["股價條件　＞"],
                                id='02-btn',
                                title='展開股價條件選項',
                                className='menu-btn'
                            ),                        
                        ],
                        style=self_style.link_div_style),
                        # html.Br(),
                        html.Div([ # menu-3
                            html.Button(
                                ["成交量值　＞"],
                                id='03-btn',
                                title='展開成交量值選項',
                                className='menu-btn'
                            ),                        
                        ],
                        style=self_style.link_div_style),
                        # html.Br(),
                        html.Div([ # menu-4
                            html.Button(
                                ["法人籌碼　＞"],
                                id='04-btn',
                                title='展開法人籌碼選項',
                                className='menu-btn'
                            ),                        
                        ],
                        style=self_style.link_div_style),
                        # html.Br(),
                        html.Div([ # menu-5
                            html.Button(
                                ["信用交易　＞"],
                                id='05-btn',
                                title='展開信用交易選項',
                                className='menu-btn'
                            ),                        
                        ],
                        style=self_style.link_div_style),
                        # html.Br(),
                        html.Div([ # menu-6
                            html.Button(
                                ["公司營收　＞"],
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
                                html.Img(src=start_img,
                                    id='selection-btn',
                                    style=self_style.selection_btn,
                                    className='selection-btn'),
                                html.Img(src=clear_img,
                                    id='clear-all-btn',
                                    style=self_style.selection_btn,
                                    className='clear-btn')
                            ], self_style.selection_btn_div_style),
                        ], style=self_style.condition_frame),

                        html.Div([
                            html.Div(['篩選結果'], style=self_style.frame_text_style),
                            
                            dcc.Tabs(id='results-tabs', value='dynamic-selection-result-twse', # value是預設顯示值
                                children=[
                                    dcc.Tab(label='台灣證券交易所 TWSE (上市)', id='dynamic-selection-result-twse', value='dynamic-selection-result-twse', style=self_style.result_words, selected_style=self_style.result_words_onclick),
                                    dcc.Tab(label='櫃買中心 TPEX (上櫃)', id='dynamic-selection-result-tpex', value='dynamic-selection-result-tpex', style=self_style.result_words, selected_style=self_style.result_words_onclick),
                                    dcc.Tab(label='上市 ETF', id='dynamic-selection-result-twse-etf', value='dynamic-selection-result-twse-etf', style=self_style.result_words, selected_style=self_style.result_words_onclick),
                                    dcc.Tab(label='上櫃 ETF', id='dynamic-selection-result-tpex-etf', value='dynamic-selection-result-tpex-etf', style=self_style.result_words, selected_style=self_style.result_words_onclick),
                            ]),
                            dcc.Loading(
                                id='result-content-loading',
                                type='default',
                                children=html.Div([], style=self_style.result_content),
                                color='red',
                            ),
                        ], style=self_style.result_frame) # Results
                    ], style=self_style.inner_frame_style), # inner-frame
                ], style=self_style.top_frame_style), # top-frame
            ], style=self_style.top_tab, selected_style=self_style.top_tab_onclick),

            dcc.Tab(label='個股查詢', children=[

                #1. individual query 個股查詢

                dcc.Store(
                    id='stored_stock_id',
                    storage_type='session',
                ),
                html.Div([
                    html.Div([
                        html.Div([], style=self_style.iq_l1_blank,),
                        dcc.Dropdown(
                            id='iq-dd',
                            options=stock_options,
                            placeholder='股票代號/公司名稱',
                            style=self_style.iq_l1_dd,
                        ),
                        html.Button(
                            children=['查詢'],
                            id='iq-btn',
                            style=self_style.iq_l1_query_btn,
                        ),
                    ],style=self_style.iq_l1),
                    html.Div(
                        children=[#公司名稱等基本資訊
                            # html.Div(['公司名稱(中文)'], style=self_style.iq_l21),
                            # html.Div(['公司代號'], style=self_style.iq_l22),
                            # html.Div(['上市上櫃'], style=self_style.iq_l23),
                            # html.Div(['公司產業別'], style=self_style.iq_l24),
                        ],
                        id='iq-stock-info',
                        style=self_style.iq_l2
                    ),
                    html.Div(
                        children=[#漲跌等每日基本數據
                            # html.Div(['當日股價'], style=self_style.iq_l31),
                            # html.Div(['其他資訊表格'], style=self_style.iq_l32),
                        ],
                        id='iq-stock-data1',
                        style=self_style.iq_l3),
                    html.Div(
                        children=[#基本資料、財務報表、籌碼分析等三個Tabs
                        ],
                        id='iq-stock-data2',
                        style=self_style.iq_l4),
                ], style=self_style.iq_div),

            ], style=self_style.top_tab, selected_style=self_style.top_tab_onclick),
        ]),
    ]),
], style=self_style.top_div_style) # canvas-div

### callbacks
# 1. Links -> filter-content
@app.callback(
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
all_btn = (
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
    '{"index":"01-btn-add-0130","type":"filter-btn"}.n_clicks',
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
@app.callback(
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
    adding = len([1 for i in triggered if i in all_btn])
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
        elif (button_id == '{"index":"01-btn-add-0130","type":"filter-btn"}'):
            print('filter 0130 clicked!')
            # record
            stored_data = stored_data or {'output_count': 0, 'output_record': [], 'selection_record': []}
            stored_data['output_count'] += 1
            stored_data['output_record'].append(stored_data['output_count'])
            print('Record:', stored_data['output_record'])
            stored_data['selection_record'].append('0130')
            print('Record:', stored_data['selection_record'])
            new_children = basic_01.create_0130(stored_data['output_count'])
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

@app.callback(
    Output('result-content-loading', 'children'),
    Output('download_data', 'data'),
    Input('selection-btn', 'n_clicks'),
    Input('results-tabs', 'value'),
    State({'type': ALL, 'index': '0101'}, 'value'), State({'type': ALL, 'index': '0102'}, 'value'), State({'type': ALL, 'index': '0103'}, 'value'), State({'type': ALL, 'index': '0104'}, 'value'), State({'type': ALL, 'index': '0105'}, 'value'), State({'type': ALL, 'index': '0106'}, 'value'), State({'type': ALL, 'index': '0107'}, 'value'), State({'type': ALL, 'index': '0108'}, 'value'), State({'type': ALL, 'index': '0109'}, 'value'), State({'type': ALL, 'index': '0110'}, 'value'), 
    State({'type': ALL, 'index': '0111'}, 'value'), State({'type': ALL, 'index': '0112'}, 'value'), State({'type': ALL, 'index': '0113'}, 'value'), State({'type': ALL, 'index': '0114'}, 'value'), State({'type': ALL, 'index': '0115'}, 'value'), State({'type': ALL, 'index': '0116'}, 'value'), State({'type': ALL, 'index': '0117'}, 'value'), State({'type': ALL, 'index': '0118'}, 'value'), State({'type': ALL, 'index': '0119'}, 'value'), State({'type': ALL, 'index': '0120'}, 'value'), 
    State({'type': ALL, 'index': '0121'}, 'value'), State({'type': ALL, 'index': '0122'}, 'value'), State({'type': ALL, 'index': '0123'}, 'value'), State({'type': ALL, 'index': '0124'}, 'value'), State({'type': ALL, 'index': '0125'}, 'value'), State({'type': ALL, 'index': '0126'}, 'value'), State({'type': ALL, 'index': '0127'}, 'value'), State({'type': ALL, 'index': '0128'}, 'value'), State({'type': ALL, 'index': '0129'}, 'value'), State({'type': ALL, 'index': '0130'}, 'value'),
    State({'type': ALL, 'index': '0201'}, 'value'), State({'type': ALL, 'index': '0202'}, 'value'), State({'type': ALL, 'index': '0203'}, 'value'), State({'type': ALL, 'index': '0204'}, 'value'), State({'type': ALL, 'index': '0205'}, 'value'),
    State({'type': ALL, 'index': '0301'}, 'value'), State({'type': ALL, 'index': '0302'}, 'value'), State({'type': ALL, 'index': '0303'}, 'value'), State({'type': ALL, 'index': '0304'}, 'value'), State({'type': ALL, 'index': '0305'}, 'value'), State({'type': ALL, 'index': '0306'}, 'value'),
    State({'type': ALL, 'index': '0401'}, 'value'), State({'type': ALL, 'index': '0402'}, 'value'), State({'type': ALL, 'index': '0403'}, 'value'), State({'type': ALL, 'index': '0404'}, 'value'), State({'type': ALL, 'index': '0405'}, 'value'), State({'type': ALL, 'index': '0406'}, 'value'),
    State({'type': ALL, 'index': '0501'}, 'value'), State({'type': ALL, 'index': '0502'}, 'value'), State({'type': ALL, 'index': '0503'}, 'value'), State({'type': ALL, 'index': '0504'}, 'value'), State({'type': ALL, 'index': '0505'}, 'value'), State({'type': ALL, 'index': '0506'}, 'value'),
    State({'type': ALL, 'index': '0601'}, 'value'), State({'type': ALL, 'index': '0602'}, 'value'), State({'type': ALL, 'index': '0603'}, 'value'), State({'type': ALL, 'index': '0604'}, 'value'), State({'type': ALL, 'index': '0605'}, 'value'), State({'type': ALL, 'index': '0606'}, 'value'), State({'type': ALL, 'index': '0607'}, 'value'), State({'type': ALL, 'index': '0608'}, 'value'), State({'type': ALL, 'index': '0609'}, 'value'), State({'type': ALL, 'index': '0610'}, 'value'), State({'type': ALL, 'index': '0611'}, 'value'), State({'type': ALL, 'index': '0612'}, 'value'), 
    State('stored_data', 'data'),
    State('download_data', 'data'),
)
def output_result(btn, tab_value, 
value0101, value0102, value0103, value0104, value0105, value0106, value0107, value0108, value0109, value0110, 
value0111, value0112, value0113, value0114, value0115, value0116, value0117, value0118, value0119, value0120, 
value0121, value0122, value0123, value0124, value0125, value0126, value0127, value0128, value0129, value0130,
value0201, value0202, value0203, value0204, value0205, 
value0301, value0302, value0303, value0304, value0305, value0306, 
value0401, value0402, value0403, value0404, value0405, value0406, 
value0501, value0502, value0503, value0504, value0505, value0506, 
value0601, value0602, value0603, value0604, value0605, value0606, value0607, value0608, value0609, value0610, 
value0611, value0612, stored_data, download_data):
    
    print('selection-btn:', btn)
    value_dict = {
        '0101': value0101, '0102': value0102, '0103': value0103, '0104': value0104, '0105': value0105, '0106': value0106, '0107': value0107, '0108': value0108, '0109': value0109, '0110': value0110,
        '0111': value0111, '0112': value0112, '0113': value0113, '0114': value0114, '0115': value0115, '0116': value0116, '0117': value0117, '0118': value0118, '0119': value0119, '0120': value0120, 
        '0121': value0121, '0122': value0122, '0123': value0123, '0124': value0124, '0125': value0125, '0126': value0126, '0127': value0127, '0128': value0128, '0129': value0129, '0130': value0130,
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
        col_name_dict = {}
        for idx in range(condition_number):
            # if stored_data['selection_record'][idx] == '0101':
            selection_code = stored_data['selection_record'][idx]
            if selection_code == '0101':
                query, col_name = query_sentence.create_query_0101(value_dict[selection_code][0])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0102':
                query, col_name = query_sentence.create_query_0102(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0103':
                query, col_name = query_sentence.create_query_0103(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0104':
                query, col_name = query_sentence.create_query_0104(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0105':
                query, col_name = query_sentence.create_query_0105(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0106':
                query, col_name = query_sentence.create_query_0106(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0107':
                query, col_name = query_sentence.create_query_0107(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0108':
                query, col_name = query_sentence.create_query_0108(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0109':
                query, col_name = query_sentence.create_query_0109(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0110':
                query, col_name = query_sentence.create_query_0110(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0111':
                query, col_name = query_sentence.create_query_0111(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0112':
                query, col_name = query_sentence.create_query_0112(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0113':
                query, col_name = query_sentence.create_query_0113(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0114':
                query, col_name = query_sentence.create_query_0114(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0115':
                query, col_name = query_sentence.create_query_0115(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0116':
                query, col_name = query_sentence.create_query_0116(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0117':
                query, col_name = query_sentence.create_query_0117(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0118':
                query, col_name = query_sentence.create_query_0118(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0119':
                query, col_name = query_sentence.create_query_0119(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0120':
                query, col_name = query_sentence.create_query_0120(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0121':
                query, col_name = query_sentence.create_query_0121(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0122':
                query, col_name = query_sentence.create_query_0122(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0123':
                query, col_name = query_sentence.create_query_0123(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0124':
                query, col_name = query_sentence.create_query_0124(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0125':
                query, col_name = query_sentence.create_query_0125(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0126':
                query, col_name = query_sentence.create_query_0126(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0127':
                query, col_name = query_sentence.create_query_0127(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0128':
                query, col_name = query_sentence.create_query_0128(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0129':
                query, col_name = query_sentence.create_query_0129(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0130':
                query, col_name = query_sentence.create_query_0130(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0201':
                query, col_name = query_sentence.create_query_0201(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0202':
                query, col_name = query_sentence.create_query_0202(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0203':
                query, col_name = query_sentence.create_query_0203(value_dict[selection_code][0], value_dict[selection_code][1])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0204':
                query, col_name = query_sentence.create_query_0204(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0205':
                query, col_name = query_sentence.create_query_0205(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0301':
                query, col_name = query_sentence.create_query_0301(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0302':
                query, col_name = query_sentence.create_query_0302(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0303':
                query, col_name = query_sentence.create_query_0303(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0304':
                query, col_name = query_sentence.create_query_0304(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0305':
                query, col_name = query_sentence.create_query_0305(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0306':
                query, col_name = query_sentence.create_query_0306(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0401':
                query, col_name = query_sentence.create_query_0401(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0402':
                query, col_name = query_sentence.create_query_0402(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0403':
                query, col_name = query_sentence.create_query_0403(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0404':
                query, col_name = query_sentence.create_query_0404(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0405':
                query, col_name = query_sentence.create_query_0405(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0406':
                query, col_name = query_sentence.create_query_0406(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3], value_dict[selection_code][4])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0501':
                query, col_name = query_sentence.create_query_0501(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0502':
                query, col_name = query_sentence.create_query_0502(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0503':
                query, col_name = query_sentence.create_query_0503(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0504':
                query, col_name = query_sentence.create_query_0504(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0505':
                query, col_name = query_sentence.create_query_0505(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0506':
                query, col_name = query_sentence.create_query_0506(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0601':
                query, col_name = query_sentence.create_query_0601(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0602':
                query, col_name = query_sentence.create_query_0602(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0603':
                query, col_name = query_sentence.create_query_0603(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0604':
                query, col_name = query_sentence.create_query_0604(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0605':
                query, col_name = query_sentence.create_query_0605(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0606':
                query, col_name = query_sentence.create_query_0606(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0607':
                query, col_name = query_sentence.create_query_0607(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0608':
                query, col_name = query_sentence.create_query_0608(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0609':
                query, col_name = query_sentence.create_query_0609(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0610':
                query, col_name = query_sentence.create_query_0610(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0611':
                query, col_name = query_sentence.create_query_0611(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2], value_dict[selection_code][3])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            elif selection_code == '0612':
                query, col_name = query_sentence.create_query_0612(value_dict[selection_code][0], value_dict[selection_code][1], value_dict[selection_code][2])
                query_dict[idx] = query
                col_name_dict[idx] = col_name
            else:
                pass
            
        # print('Query Dict:', query_dict)
        # print('Column Name Dict:', col_name_dict)
        total_query = query_sentence.query_combine(query_dict, col_name_dict)
        
        print('Final Query:', total_query)
        data = query_sentence.sql_execute(total_query)
        
        if len(data) == 0:
            return_style = self_style.result_content_only_words
            children_content = html.Div([
                html.P('無符合項目', style=return_style)
            ])
            return children_content, None #給一個空資料給download_data
        else:
            download_data = data
            data = pd.DataFrame.from_records(data)
            df_twse, df_tpex, df_etf_twse, df_etf_tpex = stock_classifier(data)
            print(df_twse.head(5))
            # df_twse.to_csv('test_file.csv')
            if df_twse.shape[0] == 0:
                # df_twse = '無符合項目'
                # return_twse_style = self_style.result_content_only_words

                twse_children_content = html.Div([
                html.P('無符合項目', style=self_style.result_content_only_words)
                ])

            else:
                df_twse = generate_table(df_twse)
                twse_children_content = html.Div([
                    html.Button("下載股票篩選結果", id="btn-download"),
                    dcc.Download(id="download-excel"),
                    df_twse,
                ], style=self_style.result_content)
            
            if df_tpex.shape[0] == 0:
                # df_tpex = '無符合項目'
                # return_tpex_style = self_style.result_content_only_words

                tpex_children_content = html.Div([
                    html.P('無符合項目', style=self_style.result_content_only_words)
                ])
            else:
                df_tpex = generate_table(df_tpex)
                # return_tpex_style = self_style.result_content

                tpex_children_content = html.Div([
                    html.Button("下載股票篩選結果", id="btn-download"),
                    dcc.Download(id="download-excel"),
                    df_tpex,
                ], style=self_style.result_content)
            
            if df_etf_twse.shape[0] == 0:
                # df_etf_twse = '無符合項目'
                # return_etf_twse_style = self_style.result_content_only_words

                etf_twse_children_content = html.Div([
                html.P('無符合項目', style=self_style.result_content_only_words)
                ])
            else:
                df_etf_twse = generate_table(df_etf_twse)
                # return_etf_twse_style = self_style.result_content

                etf_twse_children_content = html.Div([
                    html.Button("下載股票篩選結果", id="btn-download"),
                    dcc.Download(id="download-excel"),
                    df_etf_twse,
                ], style=self_style.result_content)
            
            if df_etf_tpex.shape[0] == 0:
                # df_etf_tpex = '無符合項目'
                # return_etf_tpex_style = self_style.result_content_only_words

                etf_tpex_children_content = html.Div([
                    html.P('無符合項目', style=self_style.result_content_only_words)
                ])
            else:
                df_etf_tpex = generate_table(df_etf_tpex)
                # return_etf_tpex_style = self_style.result_content

                etf_tpex_children_content = html.Div([
                    html.Button("下載股票篩選結果", id="btn-download"),
                    dcc.Download(id="download-excel"),
                    df_etf_tpex,
                ], style=self_style.result_content)
            
        if tab_value == 'dynamic-selection-result-twse':
            return twse_children_content, download_data
        elif tab_value == 'dynamic-selection-result-tpex':
            return tpex_children_content, download_data
        elif tab_value == 'dynamic-selection-result-twse-etf':
            return etf_twse_children_content, download_data
        else:
            return etf_tpex_children_content, download_data

        # my_table, _, _, _ = stock_classifier(stock_data)
        # print(my_table.head(5))
        # my_table = generate_table(my_table)
        # return my_table

        # return total_query
        # return ['{}\n'.format(i) for i in range(9999)]
    else:
        children_content = html.Div([
                html.P('', style=self_style.result_content_only_words)
        ])
        return children_content, None

#Callback 4:  Data sheet download
@app.callback(
    Output("download-excel", "data"),
    Input("btn-download", "n_clicks"),
    State('download_data', 'data'),
    prevent_initial_call=True,
)
def func(n_clicks, download_data):
    data = pd.DataFrame.from_records(download_data)
    return dcc.send_data_frame(data.to_csv, "stock_result_" + datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + ".csv")

#Callback 5: Individual Query Btn
@app.callback(
    Output('iq-stock-info', 'children'),
    Output('iq-stock-data1', 'children'),
    Output('iq-stock-data2', 'children'),
    Output('stored_stock_id', 'data'),
    Input('iq-dd', 'value'),
    Input('iq-btn', 'n_clicks'),
    State('stored_stock_id', 'data'),
    prevent_initial_call=True,
)
def iq_interactive(stock_string, btn, stored_stock_id):
    if btn == None or stock_string == None:
        raise PreventUpdate

    if btn > 0:
        print('[{}] 查詢個股: {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), stock_string))
        stock_id = stock_string
        stored_stock_id = stored_stock_id or {'id': stock_id}

        ### 基本資料
        iq_query_info_01 = query_sentence.create_query_info_01(stock_id)
        data_info_01 = query_sentence.sql_execute(iq_query_info_01) #result: [{'stock_name': '元大台灣50', 'stock_id': '0050', 'type': 'twse', 'industry_category': 'ETF', 'price': 141.85}]
        # [{'stock_name': '台積電', 'stock_id': '2330', 'type': 'twse', 'industry_category': '半導體業', 'price': 627.0}, {'stock_name': '台積電', 'stock_id': '2330', 'type': 'twse', 'industry_category': '電子工業', 'price': 627.0}]
        # print(data_info_01)

        stock_name = data_info_01[0]['stock_name']
        stock_id_string = '(' + data_info_01[0]['stock_id'] + ')'
        stock_type_temp = data_info_01[0]['type']
        if stock_type_temp == 'twse':
            stock_type = '上市'
        else:
            stock_type = '上櫃'
        
        if len(data_info_01) == 1:

            stock_cate = data_info_01[0]['industry_category']
        else:
            stock_cate = ''
            for i in range(len(data_info_01)):
                if i > 0:
                    stock_cate = stock_cate + '、' + data_info_01[i]['industry_category']
                else:
                    stock_cate = stock_cate + data_info_01[i]['industry_category']
        stock_price = data_info_01[0]['price']

        

        iq_query_info_02 = query_sentence.create_query_info_02(stock_id)
        data_info_02 = query_sentence.sql_execute(iq_query_info_02)  #result: [{'漲跌': -1.95, '漲幅': -1.3560500695410294, '成交量': 20814, '開': 142.6, '高': 142.65, '低': 140.75, '收': 141.85}]
        data_info_02 = pd.DataFrame.from_records(data_info_02)
        data_info_02 = process_obj.iq_info_adjust(data_info_02)
        # print(data_info_02)

        if '▲' in data_info_02.iloc[0,0]: # 獲取漲跌資訊，調整CSS
            self_style.iq_l31['color'] = 'red'
        elif '▼' in data_info_02.iloc[0,0]:
            self_style.iq_l31['color'] = 'green'
        else:
            pass

        iq_query_info_03 = query_sentence.create_query_info_03(stock_id)
        data_info_03 = query_sentence.sql_execute(iq_query_info_03)[0]

        ### 表格資料
        

        # 現金&股票股利
        iq_query_01_02 = query_sentence.create_query_iq_01_02(stock_id)
        data_01_02 = query_sentence.sql_execute(iq_query_01_02)
        data_01_02 = pd.DataFrame.from_records(data_01_02)
        data_01_02 = process_obj.iq_table_round_adjust(data_01_02)

        # 每股稅後盈餘(EPS)
        iq_query_01_03 = query_sentence.create_query_iq_01_03(stock_id)
        data_01_03 = query_sentence.sql_execute(iq_query_01_03)
        data_01_03 = pd.DataFrame.from_records(data_01_03)
        data_01_03 = process_obj.iq_table_round_adjust(data_01_03)
        data_01_03 = process_obj.iq_table_01_03_adjust(data_01_03)
        

        # 殖利率
        iq_query_01_04 = query_sentence.create_query_iq_01_04(stock_id)
        data_01_04 = query_sentence.sql_execute(iq_query_01_04)
        data_01_04 = pd.DataFrame.from_records(data_01_04) 
        data_01_04 = process_obj.iq_table_round_adjust(data_01_04)

        # 本益比(P/E)
        iq_query_01_05 = query_sentence.create_query_iq_01_05(stock_id)
        data_01_05 = query_sentence.sql_execute(iq_query_01_05)
        data_01_05 = pd.DataFrame.from_records(data_01_05)

        # 法人持股 外資
        iq_query_02_01_01 = query_sentence.create_query_iq_02_01_01(stock_id)
        data_02_01_01 = query_sentence.sql_execute(iq_query_02_01_01)
        # print('Query完:', data_02_01_01)
        data_02_01_01 = pd.DataFrame.from_records(data_02_01_01)
        # print('Pandas:', data_02_01_01)

        # 法人持股 投信
        iq_query_02_01_02 = query_sentence.create_query_iq_02_01_02(stock_id)
        data_02_01_02 = query_sentence.sql_execute(iq_query_02_01_02)
        data_02_01_02 = pd.DataFrame.from_records(data_02_01_02)

        # 法人持股 自營商
        iq_query_02_01_03 = query_sentence.create_query_iq_02_01_03(stock_id)
        data_02_01_03 = query_sentence.sql_execute(iq_query_02_01_03)
        data_02_01_03 = pd.DataFrame.from_records(data_02_01_03)

        # 法人持股 三大法人
        iq_query_02_01_04 = query_sentence.create_query_iq_02_01_04(stock_id)
        data_02_01_04 = query_sentence.sql_execute(iq_query_02_01_04)
        data_02_01_04 = pd.DataFrame.from_records(data_02_01_04)

        data_02_01 = process_obj.iq_legal_table_concat(data_02_01_01, data_02_01_02, data_02_01_03, data_02_01_04)

        # 融資融卷 融資
        iq_query_02_02_01 = query_sentence.create_query_iq_02_02_01(stock_id)
        data_02_02_01 = query_sentence.sql_execute(iq_query_02_02_01)
        data_02_02_01 = pd.DataFrame.from_records(data_02_02_01)
        data_02_02_01 = process_obj.iq_table_round_adjust(data_02_02_01)

        # 融資融卷 融卷
        iq_query_02_02_02 = query_sentence.create_query_iq_02_02_02(stock_id)
        data_02_02_02 = query_sentence.sql_execute(iq_query_02_02_02)
        data_02_02_02= pd.DataFrame.from_records(data_02_02_02)
        data_02_02_02 = process_obj.iq_table_round_adjust(data_02_02_02)

        data_02_02 = process_obj.iq_margin_table_concat(data_02_02_01, data_02_02_02)

        # 融資融卷 借卷
        iq_query_02_02_03 = query_sentence.create_query_iq_02_02_03(stock_id)
        data_02_02_03 = query_sentence.sql_execute(iq_query_02_02_03)
        data_02_02_03 = pd.DataFrame.from_records(data_02_02_03)

        # 集保庫存
        iq_query_02_03 = query_sentence.create_query_iq_02_03(stock_id)
        data_02_03 = query_sentence.sql_execute(iq_query_02_03)
        data_02_03 = pd.DataFrame.from_records(data_02_03)
        data_02_03 = process_obj.iq_table_02_03_adjust(data_02_03)
        
        # 董監持股
        iq_query_02_04 = query_sentence.create_query_iq_02_04(stock_id)
        data_02_04 = query_sentence.sql_execute(iq_query_02_04)
        data_02_04 = pd.DataFrame.from_records(data_02_04)

        children_content_info = [
            html.Div(
                stock_name, 
                style=self_style.iq_l21
            ),
            html.Div(stock_id_string, style=self_style.iq_l22),
            html.Div(stock_type, style=self_style.iq_l23),
            html.Div(stock_cate, style=self_style.iq_l24),
        ]
        print('{} content info done.'.format(stock_string))
        children_content_data1 = [
            html.Div(
                stock_price, 
                style=self_style.iq_l31
            ),
            html.Div(
                children=[
                    dash_table.DataTable(
                        columns = [{"name": i, "id": i} for i in data_info_02.columns],
                        data=data_info_02.to_dict('records'),
                        style_cell={'fontSize': '30px', 'height': 'auto', 'whiteSpace': 'normal'},
                        style_data_conditional=[
                            {
                                'if':{
                                    'column_id': '漲跌',
                                    'filter_query': '{漲跌} contains "▲"',
                                },
                                'color': 'red',
                            },
                            {
                                'if':{
                                    'column_id': '漲跌',
                                    'filter_query': '{漲跌} contains "▼"',
                                },
                                'color': 'green',
                            },
                            {
                                'if':{
                                    'column_id': '漲幅',
                                    'filter_query': '{漲幅} contains "+"',
                                },
                                'color': 'red',
                            },
                            {
                                'if':{
                                    'column_id': '漲幅',
                                    'filter_query': '{漲幅} contains "-"',
                                },
                                'color': 'green',
                            },

                            # {'if': {'column_id': 'Remark'},
                            # 'width': '15%'},
                            # {'if': {'column_id': '產業別'},
                            # 'width': '20%'},
                        ],
                    ),
                ],
                style=self_style.iq_l32,
            )
        ]
        print('{} content data1 done.'.format(stock_string))
        children_content_data2 = [#基本資料、財務報表、籌碼分析等三個Tabs
            dcc.Tabs(id='iq-tabs', value='dynamic-iq-result-info', # value是預設顯示值
                children=[
                    dcc.Tab(label='基本資料', id='dynamic-iq-result-info', value='dynamic-iq-result-info', style=self_style.iq_tab, selected_style=self_style.iq_tab_onclick,
                        children=[
                            html.Table([
                                html.Tr([
                                    html.Th('公司名稱', style=self_style.info_th),
                                    html.Td(data_info_03['NAME'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('個股分類', style=self_style.info_th),
                                    html.Td(data_info_03['Category'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('掛牌類別', style=self_style.info_th), html.Td(data_info_03['TYPE'], style=self_style.info_td),
                                    html.Th('證券類別', style=self_style.info_th), html.Td(data_info_03['STOCK_CATEGORY'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('類 股', style=self_style.info_th), html.Td(data_info_03['CLASS'], style=self_style.info_td),
                                    html.Th('掛牌日期', style=self_style.info_th), html.Td(data_info_03['List_date'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('董事長', style=self_style.info_th), html.Td(data_info_03['President'], style=self_style.info_td),
                                    html.Th('總經理', style=self_style.info_th), html.Td('', style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('發言人', style=self_style.info_th), html.Td(data_info_03['Spokesman'], style=self_style.info_td),
                                    html.Th('代理發言人', style=self_style.info_th), html.Td(data_info_03['Spokesman_2nd'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('資本額(仟元)', style=self_style.info_th),
                                    html.Td(data_info_03['Capital'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('普通股股本', style=self_style.info_th), html.Td(data_info_03['Share_Capital'], style=self_style.info_td),
                                    html.Th('特別股股本', style=self_style.info_th), html.Td(data_info_03['Specail_Share_Capital'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('經營業務內容', style=self_style.info_th),
                                    html.Td(data_info_03['Business'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('公司地址', style=self_style.info_th),
                                    html.Td(data_info_03['ADDRESS'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('公司電話', style=self_style.info_th), html.Td(data_info_03['PHONE'], style=self_style.info_td),
                                    html.Th('傳 真', style=self_style.info_th), html.Td(data_info_03['Fax'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('公司網址', style=self_style.info_th), html.Td(data_info_03['WEBSITE'], style=self_style.info_td),
                                    html.Th('email', style=self_style.info_th), html.Td(data_info_03['Email'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('英文全稱', style=self_style.info_th), html.Td(data_info_03['EN_NAME'], style=self_style.info_td),
                                    html.Th('英文簡稱', style=self_style.info_th), html.Td(data_info_03['Brief_EN_NAME'], style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('英文地址', style=self_style.info_th),
                                    html.Td(data_info_03['EN_ADDRESS'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('股票過戶機構', style=self_style.info_th),
                                    html.Td(data_info_03['Transfer_Agency'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('過戶機構地址', style=self_style.info_th),
                                    html.Td(data_info_03['Agency_ADDRESS'], colSpan=3, style=self_style.info_td),
                                ]),
                                html.Tr([
                                    html.Th('過戶機構電話', style=self_style.info_th),
                                    html.Td(data_info_03['Agency_PHONE'], colSpan=3, style=self_style.info_td),
                                ]),
                            ],
                            style={'border':'1px solid', 'margin-left': 'auto', 'margin-right': 'auto', 'border-collapse': 'collapse', })
                        ]
                    ),
                    dcc.Tab(label='財務報表', id='dynamic-iq-result-financial', value='dynamic-iq-result-financial', style=self_style.iq_tab, selected_style=self_style.iq_tab_onclick,
                        children = [
                            dcc.Tabs(
                                [
                                    dcc.Tab(label='財務比率', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                        children=[
                                            html.Div(
                                                dcc.Dropdown(
                                                    id='iq-inner-dd',
                                                    options=[
                                                            {'label': '近8季', 'value': 8},
                                                            {'label': '近9~16季', 'value': [9, 16]},
                                                            {'label': '近17~24季', 'value': [17, 24]},
                                                            {'label': '近25~32季', 'value': [25, 32]},                                                     
                                                        ],
                                                    value=8,
                                                    placeholder='近8季',
                                                    style=self_style.iq_inner_dd,
                                                ),
                                                dcc.Loading(
                                                    id='iq-table1-content',
                                                    type='default',
                                                    children=html.Div([]),
                                                    color='red',
                                                ),
                                            )
                                        ]),
                                    dcc.Tab(label='現金&股票股利', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                        children = [
                                            # html.Div(['現金&股票股利']),
                                            dash_table.DataTable(
                                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_02.columns],
                                                data=data_01_02.to_dict('records'),
                                                style_cell={
                                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                                },
                                                style_header_conditional=[
                                                    {
                                                        'if': {'column_id': c},
                                                        'color': 'orange'
                                                    } for c in ['現金股利(元)','股票股利(元)','股利合計(元)']
                                                ],
                                                style_header={
                                                    'textAlign':'center',
                                                }
                                            ),
                                        ]
                                    ),
                                    dcc.Tab(label='每股稅後盈餘(EPS)', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                        children = [
                                            # html.Div(['每股稅後盈餘(EPS)']),
                                            dash_table.DataTable(
                                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_03.columns],
                                                data=data_01_03.to_dict('records'),
                                                style_cell={
                                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                                },
                                                style_header={
                                                    'textAlign':'center',
                                                }
                                            ),
                                        ]
                                    ),
                                    dcc.Tab(label='殖利率', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                        children = [
                                            # html.Div(['殖利率']),
                                            dash_table.DataTable(
                                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_04.columns],
                                                data=data_01_04.to_dict('records'),
                                                style_cell={
                                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px', 'textAlign':'left',
                                                },
                                                style_header_conditional=[
                                                    {
                                                        'if': {'column_id': c},
                                                        'color': 'orange'
                                                    } for c in ['殖利率(%)']
                                                ],
                                            ),
                                        ]
                                    ),
                                    dcc.Tab(label='本益比(P/E)', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                        children = [
                                            # html.Div(['本益比(P/E)']),
                                            dash_table.DataTable(
                                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_05.columns],
                                                data=data_01_05.to_dict('records'),
                                                style_cell={
                                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px', 'textAlign':'left',
                                                },
                                                style_header_conditional=[
                                                    {
                                                        'if': {'column_id': c},
                                                        'color': 'orange'
                                                    } for c in ['本益比']
                                                ],
                                            ),
                                        ]
                                    ),
                                ],
                            content_style=self_style.tabs_content#tabs content style: styles to the tab content container holding the children of the Tab that is selected.
                            ),
                        ]
                    ),
                    dcc.Tab(label='籌碼分析', id='dynamic-iq-result-chip', value='dynamic-iq-result-chip', style=self_style.iq_tab, selected_style=self_style.iq_tab_onclick,
                        children = [
                            dcc.Tabs([
                                dcc.Tab(label='法人持股', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                    children = [
                                        dash_table.DataTable(
                                            columns = [{"name": [legal, i], "id": i, "type": 'numeric', "format":Format().group(True)} for legal, i in zip(["","外資","外資","外資","投信","投信","投信","自營商","自營商","自營商","三大法人合計","三大法人合計","三大法人合計",], data_02_01.columns)],
                                            data=data_02_01.to_dict('records'),
                                            merge_duplicate_headers=True,
                                            style_header={
                                                    'textAlign':'center',
                                            }
                                        ),
                                    ]
                                ),
                                dcc.Tab(label='融資融券', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                    children = [
                                        dash_table.DataTable(
                                            columns = [{"name": [margin, i], "id": i, "type": 'numeric', "format":Format().group(True)} for margin, i in zip(["","融資","融資","融資","融券","融券","融券",], data_02_02.columns)],
                                            data=data_02_02.to_dict('records'),
                                            merge_duplicate_headers=True,
                                            style_header={
                                                    'textAlign':'center',
                                            }
                                        ),
                                        html.Br(),
                                        html.Div(['借券'], style=self_style.tab_content_title),
                                        dash_table.DataTable(
                                            columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_02_02_03.columns],
                                            data=data_02_02_03.to_dict('records'),
                                            style_header={
                                                    'textAlign':'center',
                                            }
                                        ),
                                    ]
                                ),
                                dcc.Tab(label='集保庫存', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                    children = [
                                        dash_table.DataTable(
                                            columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_02_03.columns],
                                            data=data_02_03.to_dict('records'),
                                            style_header={
                                                    'textAlign':'center',
                                            }
                                        ),
                                    ]
                                ),
                                dcc.Tab(label='董監持股', style=self_style.iq_tab_l2, selected_style=self_style.iq_tab_l2_onclick,
                                    children = [
                                        
                                        dash_table.DataTable(
                                            columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_02_04.columns],
                                            data=data_02_04.to_dict('records'),
                                            style_header={
                                                    'textAlign':'center',
                                            }
                                        ),
                                    ]
                                ),
                            ],
                            content_style=self_style.tabs_content), # content_style: 控制Tabs中Tab的children的style。   style: 控制Tabs本身。
                        ],
                    ),
                ]
            ),
        ]
        print('{} content data2 done.'.format(stock_string))
    else:
        children_content_info = []
        children_content_data1 = []
        children_content_data2 = []
        stored_stock_id = None
    return children_content_info, children_content_data1, children_content_data2, stored_stock_id

#Callback 6:  indivisual query tab dropdown selection
@app.callback(
    Output("iq-table1-content", "children"),
    Input("iq-inner-dd", "value"),
    State('stored_stock_id', 'data'),
)
def return_tables(recent_period, data):

    stock_id = data['id']
    # 獲利能力
    iq_query_01_01_01 = query_sentence.create_query_iq_01_01_01(stock_id, recent_period)
    data_01_01_01 = query_sentence.sql_execute(iq_query_01_01_01)
    data_01_01_01 = pd.DataFrame.from_records(data_01_01_01)
    # print('SQL Query Results: ', data_01_01_01)
    data_01_01_01 = process_obj.iq_table_01_01_adjust(data_01_01_01)
    # print('DataFrame Processing Results: ', data_01_01_01)

    # 經營績效
    iq_query_01_01_02 = query_sentence.create_query_iq_01_01_02(stock_id, recent_period)
    data_01_01_02 = query_sentence.sql_execute(iq_query_01_01_02)
    data_01_01_02 = pd.DataFrame.from_records(data_01_01_02)
    data_01_01_02 = process_obj.iq_table_01_01_adjust(data_01_01_02)

    # 償債能力
    iq_query_01_01_03 = query_sentence.create_query_iq_01_01_03(stock_id, recent_period)
    data_01_01_03 = query_sentence.sql_execute(iq_query_01_01_03)
    data_01_01_03 = pd.DataFrame.from_records(data_01_01_03)
    data_01_01_03 = process_obj.iq_table_01_01_adjust(data_01_01_03)

    # 經營能力
    iq_query_01_01_04 = query_sentence.create_query_iq_01_01_04(stock_id, recent_period)
    data_01_01_04 = query_sentence.sql_execute(iq_query_01_01_04)
    data_01_01_04 = pd.DataFrame.from_records(data_01_01_04)
    data_01_01_04 = process_obj.iq_table_01_01_adjust(data_01_01_04)


    children_content = html.Div([
                            html.Div(['獲利能力'], style=self_style.tab_content_title),
                            dash_table.DataTable(
                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_01_01.columns],
                                data=data_01_01_01.to_dict('records'),
                                style_cell={
                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                },
                                style_header={
                                    'textAlign':'center',
                                }
                            ),
                            html.Br(),
                            html.Div(['經營績效'], style=self_style.tab_content_title),
                            dash_table.DataTable(
                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_01_02.columns],
                                data=data_01_01_02.to_dict('records'),
                                style_cell={
                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                },
                                style_header={
                                    'textAlign':'center',
                                }
                            ), 
                            html.Br(),
                            html.Div(['償債能力'], style=self_style.tab_content_title),
                            dash_table.DataTable(
                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_01_03.columns],
                                data=data_01_01_03.to_dict('records'),
                                style_cell={
                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                },
                                style_header={
                                    'textAlign':'center',
                                }
                            ),
                            html.Br(),
                            html.Div(['經營能力'], style=self_style.tab_content_title),
                            dash_table.DataTable(
                                columns = [{"name": i, "id": i, "type": 'numeric', "format":Format().group(True)} for i in data_01_01_04.columns],
                                data=data_01_01_04.to_dict('records'),
                                style_cell={
                                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                },
                                style_header={
                                    'textAlign':'center',
                                }
                            ),
                        ])

    return children_content

def generate_table(stock_data, max_rows=5000):
    return dash_table.DataTable(
                columns = [{"name": i, "id": i} for i in stock_data.columns],
                data=stock_data.to_dict('records'),
                fixed_rows={'headers': True}, #固定表頭
                    
                #style_header : header, style_data : data, style_cell : cells & header一起調整
                style_header={
                    'backgroundColor': 'grey',
                    'fontWeight': 'bold',
                }, 
                style_data={}, 
                style_cell={'fontSize': '20px', 'height': 'auto', 'whiteSpace': 'normal'}, 
                style_table={'overflowX': 'auto', 'minWidth': '100%'},
                # style_as_list_view=True, #移除column分隔線
                # fill_width = False,
                style_cell_conditional=[
                    {'if': {'column_id': 'Remark'},
                    'width': '15%'},
                    {'if': {'column_id': '產業別'},
                    'width': '20%'},
                ],
                filter_action='native',
                sort_action='native',
            )

def stock_classifier(data):
    
    data = data.rename(columns={'stock_id':'股票代碼', 'stock_name': '公司', 'price':'股價', 'spread_ratio':'漲跌幅%', 'industry_category':'產業別'})
    
    data['產業別'] = data.groupby(['股票代碼'])['產業別'].transform(lambda x: ','.join(x))
    data = data.drop_duplicates(subset=['股票代碼'])
    data = round(data, 2)

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

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, dev_tools_hot_reload=True)