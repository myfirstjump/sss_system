import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State, ALL
from dash.exceptions import PreventUpdate
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

        self.app.layout = html.Div([ # TOP DIV
                dcc.Store('memory'),
                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':self_style.style['margin'], 'padding':self_style.style['padding']})
                ]),# HEADER

                html.Div([ # FILTER & DISPLAY

                    # FILTER
                    html.Div([
                        # html.Div('FILTER'),
                        html.Div([ # MENU
                            html.Div(
                                html.Button(
                                    "基本資訊",
                                    id='01-btn',
                                    n_clicks=0,
                                    title='展開基本資訊選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                            html.Div(
                                html.Button(
                                    "股價條件",
                                    id='02-btn',
                                    title='展開股價條件選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                            html.Div(
                                html.Button(
                                    "成交量值",
                                    id='03-btn',
                                    title='展開成交量值選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                            html.Div(
                                html.Button(
                                    "法人籌碼", 
                                    id='04-btn',
                                    title='展開法人籌碼選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                            html.Div(
                                html.Button(
                                    "信用交易",
                                    id='05-btn',
                                    title='展開信用交易選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                            html.Div(
                                html.Button(
                                    "公司營收",
                                    id='06-btn',
                                    title='展開公司營收選項',
                                    className='menu-btn'
                                ),
                            style=self_style.link_div_style),
                        ], style=self_style.menu_style), # MENU
                        
                        html.Div([
                            html.Div('請由左方加入篩選類別', style=self_style.add_text_style),
                            html.Div([], id="filter-content"),
                        ],style=self_style.filter_content_style),
                        
                        html.Br(style={'border':'solid 1px'}),
                        html.Br(style={'border':'solid 1px'}),
                        html.Div([
                            # "DISPLAY",
                            html.Div([
                                html.Div('您的選股條件', style=self_style.output_text_style),
                                html.Div([
                                    html.Button('開始選股',
                                        id='selection-btn',
                                        className='selection-btn'),
                                    html.Button('全部清除',
                                        id='clear-all-btn',
                                        className='selection-btn')
                                ]),
                            ]),
                            html.Div([
                            ],
                            id='dynamic-output-container',
                            style=self_style.dynamic_output_container_style),
                        ], id='display-content', 
                        style=self_style.display_content_style)
                    ], style=self_style.left_frame_style),# FILTER

                    # DISPLAY
                    html.Div([
                        html.Div([
                            html.Div(['查詢結果'], style=self_style.add_text_style),
                            html.Div([
                                dcc.Loading(
                                    id='result-loading',
                                    type='default',
                                    children=html.Div([],id='dynamic-selection-result'),
                                    color='red',
                                )
                            ])
                        ], 
                        style=self_style.selection_style)
                    ], style=self_style.right_frame_style),  # DISPLAY

                ], style=self_style.frame_style), # FILTER & DISPLAY

                # SELECTION RESULT
                # html.Div([
                #     html.Div([
                #         html.Div(['查詢結果'], style=self_style.add_text_style),
                #         html.Div([],id='dynamic-selection-result')
                #     ], 
                #     style=self_style.selection_style)
                # ], style=self_style.frame_style),  # SELECTION RESULT                            
        ], style=self_style.top_div_style)#TOP DIV

        ### callbacks
        # 1. Links -> filter-content
        @self.app.callback(
            Output('filter-content', 'children'),
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
            elif button_id == '02-btn':
                content = price_02.create_filters(button_id)
            elif button_id == '03-btn':
                content = volume_03.create_filters(button_id)
            elif button_id == '04-btn':
                content = legal_04.create_filters(button_id)
            elif button_id == '05-btn':
                content = credit_05.create_filters(button_id)
            elif button_id == '06-btn':
                content = revenue_06.create_filters(button_id)     
            else:
                content = html.Div([])
            return content

        # 2. filter-content -> dynamic-output-container
        self.output_count = 0
        self.output_record = []
        self.selection_record = []
        self.all_btn = (
            # 1
            '{"index":"01-btn-add-0101","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0102","type":"filter-btn"}.n_clicks',
            '{"index":"01-btn-add-0103","type":"filter-btn"}.n_clicks',
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
        )
        @self.app.callback(
            Output('dynamic-output-container', 'children'),
            Input({'type':'filter-btn', 'index': ALL}, 'n_clicks'),
            Input({'type':'output-btn', 'index': ALL}, 'n_clicks'),
            Input('clear-all-btn', 'n_clicks'),
            State('dynamic-output-container', 'children'),
        )
        def output_update(f_btn, x_btn, clear_btn, children):
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
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0101')
                    print('Record:', self.selection_record)    

                    new_children = basic_01.create_0101(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"01-btn-add-0102","type":"filter-btn"}'):
                    print('filter 0102 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0102')
                    print('Record:', self.selection_record)
                    new_children = basic_01.create_0102(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"01-btn-add-0103","type":"filter-btn"}'):
                    print('filter 0103 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0103')
                    print('Record:', self.selection_record)
                    new_children = basic_01.create_0103(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0201","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0201 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0201')
                    print('Record:', self.selection_record)
                    new_children = price_02.create_0201(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0202","type":"filter-btn"}'):
                    print('filter 0202 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0202')
                    print('Record:', self.selection_record) 
                    new_children = price_02.create_0202(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0203","type":"filter-btn"}'):
                    print('filter 0203 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0203')
                    print('Record:', self.selection_record)
                    new_children = price_02.create_0203(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0204","type":"filter-btn"}'):
                    print('filter 0204 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0204')
                    print('Record:', self.selection_record)
                    new_children = price_02.create_0204(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0205","type":"filter-btn"}'):
                    print('filter 0205 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0205')
                    print('Record:', self.selection_record)
                    new_children = price_02.create_0205(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0301","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0301 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0301')
                    print('Record:', self.selection_record)
                    new_children = volume_03.create_0301(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0302","type":"filter-btn"}'):
                    print('filter 0302 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0302')
                    print('Record:', self.selection_record) 
                    new_children = volume_03.create_0302(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0303","type":"filter-btn"}'):
                    print('filter 0303 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0303')
                    print('Record:', self.selection_record)
                    new_children = volume_03.create_0303(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0304","type":"filter-btn"}'):
                    print('filter 0304 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0304')
                    print('Record:', self.selection_record)
                    new_children = volume_03.create_0304(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0305","type":"filter-btn"}'):
                    print('filter 0305 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0305')
                    print('Record:', self.selection_record)
                    new_children = volume_03.create_0305(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0306","type":"filter-btn"}'):
                    print('filter 0306 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0306')
                    print('Record:', self.selection_record) 
                    new_children = volume_03.create_0306(self.output_count)
                    children.append(new_children)
                    return children               
                elif (button_id == '{"index":"04-btn-add-0401","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0401 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0401')
                    print('Record:', self.selection_record)
                    new_children = legal_04.create_0401(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0402","type":"filter-btn"}'):
                    print('filter 0402 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0402')
                    print('Record:', self.selection_record)
                    new_children = legal_04.create_0402(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0403","type":"filter-btn"}'):
                    print('filter 0403 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0403')
                    print('Record:', self.selection_record)
                    new_children = legal_04.create_0403(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0404","type":"filter-btn"}'):
                    print('filter 0404 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0404')
                    print('Record:', self.selection_record) 
                    new_children = legal_04.create_0404(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0405","type":"filter-btn"}'):
                    print('filter 0405 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0405')
                    print('Record:', self.selection_record)
                    new_children = legal_04.create_0405(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0406","type":"filter-btn"}'):
                    print('filter 0406 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0406')
                    print('Record:', self.selection_record)
                    new_children = legal_04.create_0406(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0501","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0501 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0501')
                    print('Record:', self.selection_record)
                    new_children = credit_05.create_0501(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0502","type":"filter-btn"}'):
                    print('filter 0502 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0502')
                    print('Record:', self.selection_record)
                    new_children = credit_05.create_0502(self.output_count)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0503","type":"filter-btn"}'):
                    print('filter 0503 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0503')
                    print('Record:', self.selection_record)
                    new_children = credit_05.create_0503(self.output_count)
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0504","type":"filter-btn"}'):
                    print('filter 0504 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0504')
                    print('Record:', self.selection_record)
                    new_children = credit_05.create_0504(self.output_count)
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0505","type":"filter-btn"}'):
                    print('filter 0505 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0505')
                    print('Record:', self.selection_record) 
                    new_children = credit_05.create_0505(self.output_count)
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0506","type":"filter-btn"}'):
                    print('filter 0506 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0506')
                    print('Record:', self.selection_record)
                    new_children = credit_05.create_0506(self.output_count)
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"06-btn-add-0601","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0601 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    self.selection_record.append('0601')
                    print('Record:', self.selection_record) 
                    new_children = revenue_06.create_0601(self.output_count)
                    children.append(new_children)
                    return children
                else:
                    return children
            elif clearing:
                ctx = dash.callback_context 
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('output clicked! And button id is:', button_id)

                remove_number = int(button_id.split('"')[3]) # 流水號
                remove_idx = self.output_record.index(remove_number)
                print('remove_number:', remove_number, 'remove_idx:', remove_idx)
                self.output_record.remove(remove_number)
                del self.selection_record[remove_idx]
                del children[remove_idx]
                print('Record:', self.output_record)
                print('Record:', self.selection_record)
                
            elif clear_all:
                self.output_record = []
                self.selection_record = []
                return []

            else:
                print('Dont know which filter was clicked!')

            return children


        # 3. dynamic-output-container -> dynamic-selection-result
 
        @self.app.callback(
            Output('dynamic-selection-result', 'children'),
            Input('selection-btn', 'n_clicks'),
            # State('dynamic-output-container', 'children'),
            State({'type': ALL, 'index': '0102'}, 'value'), State({'type': ALL, 'index': '0103'}, 'value'),
            State({'type': ALL, 'index': '0201'}, 'value'), State({'type': ALL, 'index': '0202'}, 'value'), State({'type': ALL, 'index': '0203'}, 'value'), State({'type': ALL, 'index': '0204'}, 'value'), State({'type': ALL, 'index': '0205'}, 'value'),
            State({'type': ALL, 'index': '0301'}, 'value'), State({'type': ALL, 'index': '0302'}, 'value'), State({'type': ALL, 'index': '0303'}, 'value'), State({'type': ALL, 'index': '0304'}, 'value'), State({'type': ALL, 'index': '0305'}, 'value'), State({'type': ALL, 'index': '0306'}, 'value'),
            State({'type': ALL, 'index': '0401'}, 'value'), State({'type': ALL, 'index': '0402'}, 'value'), State({'type': ALL, 'index': '0403'}, 'value'), State({'type': ALL, 'index': '0404'}, 'value'), State({'type': ALL, 'index': '0405'}, 'value'), State({'type': ALL, 'index': '0406'}, 'value'),
            State({'type': ALL, 'index': '0501'}, 'value'), State({'type': ALL, 'index': '0502'}, 'value'), State({'type': ALL, 'index': '0503'}, 'value'), State({'type': ALL, 'index': '0504'}, 'value'), State({'type': ALL, 'index': '0505'}, 'value'), State({'type': ALL, 'index': '0506'}, 'value'),
            State({'type': ALL, 'index': '0601'}, 'value'), 
        )
        def output_result(btn, value0102, value0103, value0201, value0202, value0203, value0204, value0205, value0301, value0302, value0303, value0304, value0305, value0306, value0401, value0402, value0403, value0404, value0405, value0406, value0501, value0502, value0503, value0504, value0505, value0506, value0601):
            
            print('selection-btn:', btn)
            value_dict = {
                '0102': value0102, '0103': value0103, 
                '0201': value0201, '0202': value0202, '0203': value0203, '0204': value0204, '0205': value0205, 
                '0301': value0301, '0302': value0302, '0303': value0303, '0304': value0304, '0305': value0305,  '0306': value0306,
                '0401': value0401, '0402': value0402, '0403': value0403, '0404': value0404, '0405': value0405,  '0406': value0406,
                '0501': value0501, '0502': value0502, '0503': value0503, '0504': value0504, '0505': value0505,  '0506': value0506,
                '0601': value0601, 
            }
            print('value_dict:', value_dict)
            if btn == None:
                raise PreventUpdate

            now = datetime.datetime.now()
            today = now.date()
            yesterday = today - timedelta(days=1)
            this_week_start = today - timedelta(days=now.weekday())
            this_month_start = datetime.datetime(today.year, today.month, 1).date()
            quarter_start_month = (today.month - 1) - (today.month - 1) % 3 + 1
            this_quarter_start = datetime.datetime(today.year, quarter_start_month, 1).date()
            this_year_start = datetime.datetime(today.year, 1, 1).date()

            if btn > 0:
                condition_number = len(self.output_record)
                query_dict = {}
                for idx in range(condition_number):
                    # if self.selection_record[idx] == '0101':
                    selection_code = self.selection_record[idx]
                    if selection_code == '0201':
                        query = query_sentence.create_query_0201(value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0202':
                        query = query_sentence.create_query_0202(today, value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    elif selection_code == '0203':
                        query = query_sentence.create_query_0203(today, value_dict[selection_code][0], value_dict[selection_code][1])
                        query_dict[idx] = query
                    # elif selection_code == '0204':
                    #     query = query_sentence.create_query_0204(today, value_dict[selection_code][0], value_dict[selection_code][1])
                    #     query_dict[idx] = query
                    # elif selection_code == '0205':
                    #     query = query_sentence.create_query_0205(today, value_dict[selection_code][0], value_dict[selection_code][1])
                    #     query_dict[idx] = query
                    else:
                        pass
                total_query = query_sentence.query_combine(query_dict)
                data = query_sentence.sql_execute(total_query)
                data = pd.DataFrame.from_records(data)
                data = generate_table(data)
                print('final query:', total_query)
                return data
                
            else:
                return ''


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

