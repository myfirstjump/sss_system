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
                                    html.Img(src=add_img_path, n_clicks=0, style=self_style.button_style, 
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
                                    html.Img(src=add_img_path, n_clicks=0, style=self_style.button_style, 
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
                                    html.Img(src=add_img_path, n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0103'
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
                                        html.Img(src=delete_img_path, n_clicks=0, style=self_style.button_style,
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
                                        html.Img(src=delete_img_path, n_clicks=0, style=self_style.button_style,
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
                                        html.Img(src=delete_img_path, n_clicks=0, style=self_style.button_style,
                                            id={'type':'output-btn',
                                                'index': str(output_count)})
                                    ])
    return new_children
    