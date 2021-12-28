import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from pages import self_style

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('公司', style=self_style.text_normal),
                                        html.P('股價大於', style=self_style.text_bold),
                                        html.P('120', style=self_style.text_color_bold),
                                        html.P('元', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0201'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司', style=self_style.text_normal),
                                        html.P('股價小於', style=self_style.text_bold),
                                        html.P('120', style=self_style.text_color_bold),
                                        html.P('元', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0202'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司', style=self_style.text_normal),
                                        html.P('股價', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('漲/跌停', style=self_style.text_bold),
                                        html.P('3日', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0203'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('漲/跌幅', style=self_style.text_bold),
                                        html.P('均超過', style=self_style.text_normal),
                                        html.P('10%', style=self_style.text_color_bold),
                                        html.P('之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0204'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('上漲/下跌', style=self_style.text_bold),
                                        html.P('均超過', style=self_style.text_normal),
                                        html.P('20元', style=self_style.text_color_bold),
                                        html.P('之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0205'
                                    })
                                ]),
                            ])
    return content

def create_0201(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd',
                                                    'index': '0201'},
                                                options=[
                                                    {'label': '大於', 'value': '1'},
                                                    {'label': '小於', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0201'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=120,
                                                placeholder='120',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0202(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd',
                                                    'index': '0202'},
                                                options=[
                                                    {'label': '大於', 'value': '1'},
                                                    {'label': '小於', 'value': '-1'},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0202'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=120,
                                                placeholder='120',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0203(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股價連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd',
                                                    'index': '0203'},
                                                options=[
                                                    {'label': '漲停', 'value': '1'},
                                                    {'label': '跌停', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='漲停',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0203'},
                                                type='number',
                                                min=0,
                                                max=100,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.short_input_style),
                                            ], style=self_style.short_ipt_div_style),
                                            
                                            html.P('日以上', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0204(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),

                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0204'},
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.short_input_style),  
                                            ], style=self_style.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd1',
                                                    'index': '0204'},
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           

                                            html.P('內', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0204'},
                                                options=[
                                                    {'label': '漲幅', 'value': '1'},
                                                    {'label': '跌幅', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='漲幅',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('均大於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0204'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('% 之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0205(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),

                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0205'},
                                                type='number',
                                                min=0,
                                                max=999,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.short_input_style),  
                                            ], style=self_style.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd1',
                                                    'index': '0205'},
                                                    options=[
                                                        {'label': '日', 'value': 'd'},
                                                        {'label': '周', 'value': 'w'},
                                                        {'label': '月', 'value': 'm'},
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='d',
                                                    placeholder='日',
                                                    clearable=False,
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                          
                                            
                                            html.P('內', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                    'index': '0205'},
                                                    options=[
                                                        {'label': '上漲', 'value': '1'},
                                                        {'label': '下跌', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='上漲',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.P('均大於', style=self_style.text_normal),

                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0205'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=10,
                                                placeholder='20',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('元之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

