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
                                        html.P('3', style=self_style.text_bold),
                                        html.P('年內平均ROE', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0107'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('ROE連續', style=self_style.text_normal), # normal text
                                        html.P('3', style=self_style.text_bold),
                                        html.P('年', style=self_style.text_normal),
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
                                        'index': button_id + '-add-0108'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('3', style=self_style.text_bold),
                                        html.P('年內平均ROA', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0109'
                                    })                                    
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('ROA連續', style=self_style.text_normal), # normal text
                                        html.P('3', style=self_style.text_bold),
                                        html.P('年', style=self_style.text_normal),
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
                                        'index': button_id + '-add-0110'
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
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('EPS較去年同期', style=self_style.text_normal),
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
                                        'index': button_id + '-add-0113'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('平均存貨週轉率', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0114'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('季', style=self_style.text_bold),
                                        html.P('存貨週轉率', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0115'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('平均應收帳款週轉率', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0116'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('季', style=self_style.text_bold),
                                        html.P('應收帳款週轉率', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0117'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('平均流動比率', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0118'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('季', style=self_style.text_bold),
                                        html.P('流動比率', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0119'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('平均速動比率', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0120'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('季', style=self_style.text_bold),
                                        html.P('速動比率', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0121'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('平均負債比率', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0122'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('季', style=self_style.text_bold),
                                        html.P('負債比率', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_bold),
                                        html.P('%', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0123'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('3', style=self_style.text_bold),
                                        html.P('年內', style=self_style.text_normal),
                                        html.P('現金股利', style=self_style.text_bold),
                                        html.P('皆', style=self_style.text_bold),
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
                                        'index': button_id + '-add-0124'
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

def create_0107(output_count):
    '''0107 (3)季度內平均ROE(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0107'},
                                                    type='number',
                                                    min=0,
                                                    max=30,
                                                    value=3,
                                                    placeholder='3',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年內平均ROE', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0107'},
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
                                                        'index': '0107'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children


    
def create_0108(output_count):
    '''0108 ROE連續(3)年(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('ROE連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0108'},
                                                    type='number',
                                                    min=0,
                                                    max=30,
                                                    value=3,
                                                    placeholder='3',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0108'},
                                                    options=[
                                                        {'label': '成長', 'value': '1'},
                                                        {'label': '衰退', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='成長',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip2',
                                                        'index': '0108'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
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


def create_0109(output_count):
    '''0109 (3)季度內平均ROA(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0109'},
                                                    type='number',
                                                    min=0,
                                                    max=30,
                                                    value=3,
                                                    placeholder='3',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年內平均ROA', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0109'},
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
                                                        'index': '0109'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0110(output_count):
    '''0110 ROA連續(3)年(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('ROA連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0110'},
                                                    type='number',
                                                    min=0,
                                                    max=30,
                                                    value=3,
                                                    placeholder='3',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd',
                                                        'index': '0110'},
                                                    options=[
                                                        {'label': '成長', 'value': '1'},
                                                        {'label': '衰退', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='成長',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip2',
                                                        'index': '0110'},
                                                    type='number',
                                                    min=0,
                                                    max=99999,
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

def create_0113(output_count):
    '''0113 上(季/年)EPS較去年同期(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0113'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('EPS較去年同期', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0113'},
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
                                                    'index': '0113'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
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



def create_0114(output_count):
    '''0114 上(2)(季/年)平均存貨週轉率(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0114'},
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
                                                        'index': '0114'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均存貨週轉率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0114'},
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
                                                        'index': '0114'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0115(output_count):
    '''0115 (季/年)存貨週轉率(成長/衰退)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0115'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('存貨週轉率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0115'},
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
                                                    'index': '0115'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0116(output_count):
    '''上(2)(季/年)平均應收帳款週轉率(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0116'},
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
                                                        'index': '0116'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均應收帳款週轉率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0116'},
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
                                                        'index': '0116'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0117(output_count):
    '''(季/年)應收帳款週轉率(成長/衰退)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0117'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('應收帳款週轉率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0117'},
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
                                                    'index': '0117'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0118(output_count):
    '''0118 上(2)(季/年)平均流動比率(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0118'},
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
                                                        'index': '0118'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均流動比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0118'},
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
                                                        'index': '0118'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0119(output_count):
    '''0119 (季/年)流動比率(成長/衰退)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0119'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('流動比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0119'},
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
                                                    'index': '0119'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0120(output_count):
    '''0120 上(2)(季/年)平均速動比率(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0120'},
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
                                                        'index': '0120'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均速動比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0120'},
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
                                                        'index': '0120'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0121(output_count):
    '''0121 (季/年)速動比率(成長/衰退)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0121'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('速動比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0121'},
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
                                                    'index': '0121'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0122(output_count):
    '''0122 上(2)(季/年)平均負債比率(大於)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                    id={'type':'ip1',
                                                        'index': '0122'},
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
                                                        'index': '0122'},
                                                    options=[
                                                        {'label': '季', 'value': 'q'},    
                                                        {'label': '年', 'value': 'y'},                                                  
                                                    ],
                                                    value='q',
                                                    placeholder='季',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ], style=self_style.dp_div_style),
                                            html.P('平均負債比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                    id={'type':'dd2',
                                                        'index': '0122'},
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
                                                        'index': '0122'},
                                                    type='number',
                                                    min=-999,
                                                    max=99999,
                                                    value=10,
                                                    placeholder='10',
                                                    style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children

def create_0123(output_count):
    '''0123 (季/年)負債比率(成長/衰退)(10)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0123'},
                                                options=[
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('負債比率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0123'},
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
                                                    'index': '0123'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=10,
                                                placeholder='10',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0124(output_count):
    '''0124 (3)年內(現金股票股利)(皆/平均)(大於)(10)元'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0124'},
                                                type='number',
                                                min=0,
                                                max=10,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年內', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0124'},
                                                options=[
                                                    {'label': '現金股利', 'value': '1'},
                                                    {'label': '股票股利', 'value': '2'},
                                                ],
                                                value='1',
                                                placeholder='現金股利',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0124'},
                                                options=[
                                                    {'label': '皆', 'value': '1'},
                                                    {'label': '平均', 'value': '2'},
                                                ],
                                                value='1',
                                                placeholder='皆',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0124'},
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
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0124'},
                                                type='number',
                                                min=0,
                                                max=10000,
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