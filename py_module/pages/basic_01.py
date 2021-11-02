import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
import os
import base64
from py_module.pages import self_style
from py_module.data_reader import DataReader
from py_module.config import Configuration

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('公司隸屬產業別篩選', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={ 
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0101'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股本', style=self_style.text_normal), # normal text
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('5', style=self_style.text_bold),
                                        html.P('億元', style=self_style.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0102'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('公司股本', style=self_style.text_normal), # normal text
                                        html.P('小於', style=self_style.text_bold), # bold text
                                        html.P('5', style=self_style.text_bold),
                                        html.P('億元', style=self_style.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0103'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('董監持股比例', style=self_style.text_normal), # normal text
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('50', style=self_style.text_bold),
                                        html.P('%之股票', style=self_style.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0104'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('董監質押比例', style=self_style.text_normal), # normal text
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%之股票', style=self_style.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0105'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('每股淨值', style=self_style.text_normal), # normal text
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('10', style=self_style.text_bold),
                                        html.P('元之股票', style=self_style.text_normal),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0106'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal), # normal text
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold), # bold text
                                        html.P('平均EPS', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('元', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0111'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('EPS連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_bold),
                                        html.P('%以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0112'
                                    })
                                ]),
                            ])   
    return content

def create_0101(output_count, data):

    stock_types = data['industry_category'].unique()
    cate_ops = []
    for idx, types_str  in enumerate(stock_types):
        cate_ops.append({'label': types_str, 'value': types_str})
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司隸屬產業別為', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0101'},
                                                    options=cate_ops,
                                                    value=['電子工業'],
                                                    placeholder='電子工業',
                                                    style=self_style.large_dropdown_style,
                                                    multi=True,
                                                    clearable=True),
                                            ], style=self_style.dp_div_style),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children


def create_0102(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股本', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0102'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    style=self_style.dropdown_style,
                                                    clearable=False),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip',
                                                        'index': '0102'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=5,
                                                    placeholder='5',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('億元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0103(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('公司股本', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0103'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='-1',
                                                    placeholder='小於',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip',
                                                        'index': '0103'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=5,
                                                    placeholder='5',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('億元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children


def create_0104(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('董監持股比例', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0104'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip',
                                                        'index': '0104'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=50,
                                                    placeholder='50',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0105(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('董監質押比例', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0105'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip',
                                                        'index': '0105'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0106(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('每股淨值', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0106'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip',
                                                        'index': '0106'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
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

def create_0111(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0111'},
                                                    type='number',
                                                    min=1,
                                                    max=30,
                                                    value=2,
                                                    placeholder='2',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd1',
                                                        'index': '0111'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均EPS', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0111'},
                                                    options=[
                                                        {'label': '大於', 'value': '1'},
                                                        {'label': '小於', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='大於',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip2',
                                                        'index': '0111'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
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


def create_0112(output_count):
    '''0112 EPS連續(3)(季/年)(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('EPS連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0112'},
                                                type='number',
                                                min=0,
                                                max=10,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0112'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0112'},
                                                options=[
                                                    {'label': '成長', 'value': '1'},
                                                    {'label': '衰退', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='成長',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip',
                                                    'index': '0112'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=5,
                                                placeholder='5',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%以上', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children