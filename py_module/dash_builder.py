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

from py_module.pages import (
    # basic_01,
    # price_02,
    # volume_03,
    # legal_04,
    # credit_05,
    # revenue_06,
    self_style
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

        self.top_div_style = self_style.top_div_style
        self.style = self_style.style
        # self.category_btn_style = self_style.category_btn_style
        self.menu_style = self_style.menu_style
        self.item_style = self_style.item_style
        self.add_text_style = self_style.add_text_style
        self.output_text_style = self_style.output_text_style
        self.left_frame_style = self_style.left_frame_style
        self.filter_content_style = self_style.filter_content_style
        self.right_frame_style = self_style.right_frame_style
        self.dynamic_output_container_style = self_style.dynamic_output_container_style
        self.display_content_style = self_style.display_content_style
        self.output_item_style = self_style.output_item_style
        self.button_style = self_style.button_style
        self.selection_btn = self_style.selection_btn
        self.selection_style = self_style.selection_style
        self.frame_style = self_style.frame_style
        self.link_div_style = self_style.link_div_style
        self.dropdown_style = self_style.dropdown_style
        self.short_dropdown_style = self_style.short_dropdown_style
        self.dp_div_style = self_style.dp_div_style
        self.input_style = self_style.input_style
        self.short_input_style = self_style.short_input_style
        self.ipt_div_style = self_style.ipt_div_style
        self.short_ipt_div_style = self_style.short_ipt_div_style

        self.text_normal = self_style.text_normal
        self.text_bold = self_style.text_bold

        self.app.layout = html.Div([ # TOP DIV
                dcc.Store('memory'),
                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':self.style['margin'], 'padding':self.style['padding']})
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
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "股價條件",
                                    id='02-btn',
                                    title='展開股價條件選項',
                                    className='menu-btn'
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "成交量值",
                                    id='03-btn',
                                    title='展開成交量值選項',
                                    className='menu-btn'
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "法人籌碼", 
                                    id='04-btn',
                                    title='展開法人籌碼選項',
                                    className='menu-btn'
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "信用交易",
                                    id='05-btn',
                                    title='展開信用交易選項',
                                    className='menu-btn'
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "公司營收",
                                    id='06-btn',
                                    title='展開公司營收選項',
                                    className='menu-btn'
                                ),
                            style=self.link_div_style),
                        ], style=self.menu_style), # MENU
                        
                        html.Div([
                            html.Div('請由左方加入篩選類別', style=self.add_text_style),
                            html.Div([], id="filter-content"),
                        ],style=self.filter_content_style),
                        
                        html.Br(style={'border':'solid 1px'}),
                        html.Br(style={'border':'solid 1px'}),
                        html.Div([
                            # "DISPLAY",
                            html.Div([
                                html.Div('您的選股條件', style=self.output_text_style),
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
                            style=self.dynamic_output_container_style),
                        ], id='display-content', 
                        style=self.display_content_style)
                    ], style=self.left_frame_style),# FILTER

                    # DISPLAY
                    html.Div([
                        html.Div([
                            html.Div(['查詢結果'], style=self.add_text_style),
                            html.Div([
                                dcc.Loading(
                                    id='result-loading',
                                    type='default',
                                    children=html.Div([],id='dynamic-selection-result'),
                                    color='red',
                                )
                            ])
                        ], 
                        style=self.selection_style)
                    ], style=self.right_frame_style),  # DISPLAY

                ], style=self.frame_style), # FILTER & DISPLAY

                # SELECTION RESULT
                # html.Div([
                #     html.Div([
                #         html.Div(['查詢結果'], style=self.add_text_style),
                #         html.Div([],id='dynamic-selection-result')
                #     ], 
                #     style=self.selection_style)
                # ], style=self.frame_style),  # SELECTION RESULT                            
        ], style=self.top_div_style)#TOP DIV

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
                content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('公司隸屬產業別為', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0101'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股本', style=self.text_normal), # normal text
                                        html.P('大於', style=self.text_bold), # bold text
                                        html.P('5', style=self.text_bold),
                                        html.P('億元', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0102'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股本', style=self.text_normal), # normal text
                                        html.P('小於', style=self.text_bold), # bold text
                                        html.P('5', style=self.text_bold),
                                        html.P('億元', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0103'
                                    })                                    
                                ]),
                            ])   
            elif button_id == '02-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('公司股價', style=self.text_normal),
                                        html.P('大於', style=self.text_bold),
                                        html.P('120', style=self.text_bold),
                                        html.P('元', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0201'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股價', style=self.text_normal),
                                        html.P('小於', style=self.text_bold),
                                        html.P('120', style=self.text_bold),
                                        html.P('元', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0202'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股價連續', style=self.text_normal),
                                        html.P('漲/跌停', style=self.text_bold),
                                        html.P('3', style=self.text_bold),
                                        html.P('日以上', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0203'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('漲/跌幅', style=self.text_bold),
                                        html.P('超過', style=self.text_normal),
                                        html.P('10%', style=self.text_bold),
                                        html.P('之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0204'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('上漲/下跌', style=self.text_bold),
                                        html.P('超過', style=self.text_normal),
                                        html.P('20元', style=self.text_bold),
                                        html.P('之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0205'
                                    })
                                ]),
                            ])
            elif button_id == '03-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量平均', style=self.text_normal),
                                        html.P('大於', style=self.text_bold),
                                        html.P('50000', style=self.text_normal),
                                        html.P('張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0301'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量平均', style=self.text_normal),
                                        html.P('小於', style=self.text_bold),
                                        html.P('1000', style=self.text_normal),
                                        html.P('張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0302'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量', style=self.text_normal),
                                        html.P('增加', style=self.text_bold),
                                        html.P('1000', style=self.text_normal),
                                        html.P('張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0303'
                                    })
                                ]),   
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量', style=self.text_normal),
                                        html.P('減少', style=self.text_bold),
                                        html.P('1000', style=self.text_normal),
                                        html.P('張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0304'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量', style=self.text_normal),
                                        html.P('增加', style=self.text_bold),
                                        html.P('20', style=self.text_normal),
                                        html.P('% 之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0305'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，成交量', style=self.text_normal),
                                        html.P('減少', style=self.text_bold),
                                        html.P('20', style=self.text_normal),
                                        html.P('% 之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0306'
                                    })
                                ]),                             
                            ])
            elif button_id == '04-btn':
                content = html.Div(
                            [                              
                                html.Div([
                                    html.Span([
                                        html.P('外資', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('大於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0401'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('外資', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('小於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0402'
                                    })
                                ]),                  
                                html.Div([
                                    html.Span([
                                        html.P('投信', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('大於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0403'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('投信', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('小於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0404'
                                    })
                                ]),         
                                html.Div([
                                    html.Span([
                                        html.P('自營商', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('大於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0405'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('自營商', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內', style=self.text_normal),
                                        html.P('買超/賣超', style=self.text_bold),
                                        html.P('小於', style=self.text_bold),
                                        html.P('5000', style=self.text_bold),
                                        html.P('張', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0406'
                                    })
                                ]),                                                                
                            ])        
            elif button_id == '05-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('融資於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' 張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0501'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融資於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' %之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0502'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融券於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' 張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0503'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融券於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' %之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0504'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('借券於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' 張之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0505'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('借券於', style=self.text_normal),
                                        html.P('3', style=self.text_bold),
                                        html.P('日內，', style=self.text_normal),
                                        html.P('增加/減少', style=self.text_bold),
                                        html.P('100', style=self.text_normal),
                                        html.P(' %之股票', style=self.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0506'
                                    })
                                ]),
                            ])
            elif button_id == '06-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('營收', style=self.text_normal),
                                        html.P('大於', style=self.text_bold),
                                        html.P('5', style=self.text_bold),
                                        html.P('億元', style=self.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0601'
                                    })
                                ]),

                            ])          
            else:
                content = html.Div([])
            return content

        # 2. filter-content -> dynamic-output-container
        self.output_count = 0
        self.output_record = []
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
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司隸屬產業別為', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                            id={'type':'output-btn',
                                                'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"01-btn-add-0102","type":"filter-btn"}'):
                    print('filter 0102 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股本', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0101-dd',
                                                    options=[
                                                        {'label': '大於', 'value': 1},
                                                        {'label': '小於', 'value': -1},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    style=self.dropdown_style,
                                                    clearable=False),
                                            ], style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    # id='0101-ip',
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=5,
                                                    placeholder='5',
                                                    style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('億元', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                            id={'type':'output-btn',
                                                'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"01-btn-add-0103","type":"filter-btn"}'):
                    print('filter 0103 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股本', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0101-dd',
                                                    options=[
                                                        {'label': '大於', 'value': 1},
                                                        {'label': '小於', 'value': -1},
                                                    ],
                                                    value='-1',
                                                    placeholder='小於',
                                                    clearable=False,
                                                    style=self.dropdown_style),
                                            ], style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    # id='0101-ip',
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=5,
                                                    placeholder='5',
                                                    style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('億元', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                            id={'type':'output-btn',
                                                'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0201","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0201 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=120,
                                                placeholder='120',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('元', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0202","type":"filter-btn"}'):
                    print('filter 0202 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=120,
                                                placeholder='120',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('元', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0203","type":"filter-btn"}'):
                    print('filter 0203 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價連續', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '漲停', 'value': 1},
                                                    {'label': '跌停', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='漲停',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=100,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),
                                            ], style=self.short_ipt_div_style),
                                            
                                            html.P('日以上', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0204","type":"filter-btn"}'):
                    print('filter 0204 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),

                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           

                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '漲幅', 'value': 1},
                                                    {'label': '跌幅', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='漲幅',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.P('超過', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=10,
                                                placeholder='10',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('% 之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add-0205","type":"filter-btn"}'):
                    print('filter 0205 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),

                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                          
                                            
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '上漲', 'value': 1},
                                                        {'label': '下跌', 'value': -1},
                                                    ],
                                                    value='1',
                                                    placeholder='上漲',
                                                    clearable=False,
                                                    style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.P('超過', style=self.text_normal),

                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=10,
                                                placeholder='20',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('元之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0301","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0301 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量平均', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=50000,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0302","type":"filter-btn"}'):
                    print('filter 0302 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量平均', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=10,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0303","type":"filter-btn"}'):
                    print('filter 0303 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=1000,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0304","type":"filter-btn"}'):
                    print('filter 0304 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='減少',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=1000,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0305","type":"filter-btn"}'):
                    print('filter 0305 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=20,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('% 之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add-0306","type":"filter-btn"}'):
                    print('filter 0306 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，成交量', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='減少',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=20,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('% 之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children               
                elif (button_id == '{"index":"04-btn-add-0401","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0401 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('外資', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0401-dd',
                                                    options=[
                                                        {'label': '買超', 'value': 1},
                                                        {'label': '賣超', 'value': -1},
                                                    ],
                                                    value='1',
                                                    placeholder='買超',
                                                    clearable=False,
                                                    style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),    
                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0402","type":"filter-btn"}'):
                    print('filter 0402 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('外資', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd',
                                                options=[
                                                    {'label': '買超', 'value': 1},
                                                    {'label': '賣超', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0403","type":"filter-btn"}'):
                    print('filter 0403 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('投信', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd',
                                                options=[
                                                    {'label': '買超', 'value': 1},
                                                    {'label': '賣超', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),                                          
                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0404","type":"filter-btn"}'):
                    print('filter 0404 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('投信', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd',
                                                options=[
                                                    {'label': '買超', 'value': 1},
                                                    {'label': '賣超', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            

                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0405","type":"filter-btn"}'):
                    print('filter 0405 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('自營商', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd',
                                                options=[
                                                    {'label': '買超', 'value': 1},
                                                    {'label': '賣超', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            

                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add-0406","type":"filter-btn"}'):
                    print('filter 0406 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('自營商', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd',
                                                options=[
                                                    {'label': '買超', 'value': 1},
                                                    {'label': '賣超', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0401-dd2',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            

                                            html.Div([
                                                dcc.Input(
                                                # id='0401-ip',
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('張', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0501","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0501 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('融資於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0502","type":"filter-btn"}'):
                    print('filter 0502 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('融資於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('%之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add-0503","type":"filter-btn"}'):
                    print('filter 0503 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('融券於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0504","type":"filter-btn"}'):
                    print('filter 0504 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('融券於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('%之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0505","type":"filter-btn"}'):
                    print('filter 0505 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('借券於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('張之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"05-btn-add-0506","type":"filter-btn"}'):
                    print('filter 0506 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('借券於', style=self.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self.short_input_style),  
                                            ], style=self.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    # id='0201-dd',
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 's'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self.short_dropdown_style),
                                            ],style=self.dp_div_style),                                           
                                            html.P('內，', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                # id='0201-dd',
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                # id='0201-ip',
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            html.P('%之股票', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children 
                elif (button_id == '{"index":"06-btn-add-0601","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 0601 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.Span([
                                            html.P('營收', style=self.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id='0601-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self.dropdown_style),
                                            ],style=self.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id='0601-ip',
                                                type='number',
                                                min=0,
                                                max=99999,
                                                value=5,
                                                placeholder='5',
                                                style=self.input_style),
                                            ], style=self.ipt_div_style),
                                            
                                            html.P('億元', style=self.text_normal),
                                        ], style=self.output_item_style),
                                        html.Button('x', n_clicks=0, style=self.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ])
                    children.append(new_children)
                    return children
                else:
                    return children
            elif clearing:
                ctx = dash.callback_context 
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('output clicked! And button id is:', button_id)

                remove_number = int(button_id.split('"')[3])
                remove_idx = self.output_record.index(remove_number)
                print('remove_number:', remove_number, 'remove_idx:', remove_idx)
                self.output_record.remove(remove_number)
                del children[remove_idx]
                print('Record:', self.output_record)
                
            elif clear_all:
                self.output_record = []
                return []

            else:
                print('Dont know which filter clicked!')

            return children


        # 3. dynamic-output-container -> dynamic-selection-result
 
        @self.app.callback(
            Output('dynamic-selection-result', 'children'),
            Input('selection-btn', 'n_clicks'),
            State('dynamic-output-container', 'children'),
        )
        def output_result(btn, children):
            # time.sleep(1)
            if btn == None:
                raise PreventUpdate
            if btn > 0:
                return 'Query from Database.'
            else:
                return ''

        # 4. clear-all btn -> clear all dynamic-selection-results
        # @self.app.callback(
        #     Output('display-content', 'children'),
        #     Input('clear-all-btn', 'n_clicks')
        # )
        # def clear_all_results(btn):
        #     self.output_record = []
        #     pure_content = [
        #                     # "DISPLAY",
        #                     html.Div([
        #                         html.Div('您的選股條件', style=self.output_text_style),
        #                         html.Div([
        #                             html.Button('開始選股',
        #                                 id='selection-btn',
        #                                 style=self.selection_btn),
        #                             html.Button('全部清除',
        #                                 id='clear-all-btn',
        #                                 style=self.selection_btn)
        #                         ]),
        #                     ]),
        #                     html.Div([
        #                     ],
        #                     id='dynamic-output-container',
        #                     style=self.dynamic_output_container_style),
        #                 ]
        #     return pure_content

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

