import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    ''' 0601 近(2)(月/季/年)營收(大於)(5)百萬元
        0602 營收連續(3)(月/季/年)(成長/衰退)(5)%以上
        0603 營收較去年同期(成長/衰退)(5)%以上

        0604 近(2)(月/季/年)營業毛利率(大於)(5)%
        0605 營業毛利率連續(3)(月/季/年)(成長/衰退)(5)%以上
        0606 營業毛利率較去年同期(成長/衰退)(5)%以上

        0607 近(2)(月/季/年)營業利益率(大於)(5)%
        0608 營業利益率連續(3)(月/季/年)(成長/衰退)(5)%以上
        0609 營業利益率較去年同期(成長/衰退)(5)%以上

        0610 近(2)(月/季/年)稅後淨利率(大於)(5)%
        0611 稅後淨利率連續(3)(月/季/年)(成長/衰退)(5)%以上
        0612 稅後淨利率較去年同期(成長/衰退)(5)%以上'''
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('近', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('營收', style=self_style.text_bold),
                                        html.P('合計', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('500000000元', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0601'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('營收', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0602'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上季', style=self_style.text_normal),
                                        html.P('營收', style=self_style.text_bold),
                                        html.P('較去年同期', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0603'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('近', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('營業毛利率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0604'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('營業毛利率', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0605'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('營業毛利率', style=self_style.text_bold),
                                        html.P('較去年同期', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0606'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('近', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('營業利益率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0607'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('營業利益率', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0608'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('營業利益率', style=self_style.text_bold),
                                        html.P('較去年同期', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0609'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('近', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('稅後淨利率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0610'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('稅後淨利率', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0611'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('季', style=self_style.text_normal),
                                        html.P('稅後淨利率', style=self_style.text_bold),
                                        html.P('較去年同期', style=self_style.text_normal),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0612'
                                    })
                                ]),

                            ])
    return content

def create_0601(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('近', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0601'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=2,
                                                placeholder='2',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0601'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營收合計', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0601'},
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
                                                id={'type':'ip2',
                                                    'index': '0601'},
                                                type='number',
                                                min=0,
                                                max=999999999999999,
                                                value=500000000,
                                                placeholder='500000000',
                                                style=self_style.large_input_style),
                                            ], style=self_style.large_ipt_div_style),
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

def create_0602(output_count):
    '''0602 營收連續(3)(月/季/年)(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('營收連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0602'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0602'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
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
                                                    'index': '0602'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0602'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0603(output_count):
    '''0603 營收較去年同期(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0603'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營收較去年同期', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0603'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0603'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0604(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('近', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0604'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=2,
                                                placeholder='2',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0604'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營業毛利率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0604'},
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
                                                id={'type':'ip2',
                                                    'index': '0604'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=50,
                                                placeholder='50',
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

def create_0605(output_count):
    '''0605 營業毛利率連續(3)(月/季/年)(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('營業毛利率連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0605'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0605'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
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
                                                    'index': '0605'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0605'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0606(output_count):
    '''0606 營業毛利率較去年同期(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0606'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營業毛利率較去年同期', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0606'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0606'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0607(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('近', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0607'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=2,
                                                placeholder='2',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0607'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營業利益率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0607'},
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
                                                id={'type':'ip2',
                                                    'index': '0607'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=50,
                                                placeholder='50',
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

def create_0608(output_count):
    '''0608 營業利益率連續(3)(月/季/年)(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('營業利益率連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0608'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0608'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
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
                                                    'index': '0608'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0608'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0609(output_count):
    '''0609 營業利益率較去年同期(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0609'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營業利益率較去年同期', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0609'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0609'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0610(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('近', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0610'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=2,
                                                placeholder='2',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0610'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('稅後淨利率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0610'},
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
                                                id={'type':'ip2',
                                                    'index': '0610'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=50,
                                                placeholder='50',
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

def create_0611(output_count):
    '''0611 稅後淨利率連續(3)(月/季/年)(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('稅後淨利率連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0611'},
                                                type='number',
                                                min=1,
                                                max=12,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0611'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
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
                                                    'index': '0611'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip2',
                                                    'index': '0611'},
                                                type='number',
                                                min=0,
                                                max=999999,
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

def create_0612(output_count):
    '''0612 上(季/年)稅後淨利率較去年同期(成長/衰退)(5)%以上'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('上', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0612'},
                                                options=[
                                                    {'label': '月', 'value': 'm'},
                                                    {'label': '季', 'value': 'q'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='q',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('稅後淨利率較去年同期', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0612'},
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
                                                dcc.Input(required = True,
                                                id={'type':'ip',
                                                    'index': '0612'},
                                                type='number',
                                                min=0,
                                                max=999999,
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