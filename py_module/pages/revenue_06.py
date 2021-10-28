import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    '''近(2)(月/季/年)營收(大於)(5)百萬元'''
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('近', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_bold),
                                        html.P('季', style=self_style.text_bold),
                                        html.P('營收', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_bold),
                                        html.P('百萬元', style=self_style.text_normal),
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

                            ])
    return content

def create_0601(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('近', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
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
                                                    {'label': '季', 'value': 's'},
                                                    {'label': '年', 'value': 'y'},
                                                ],
                                                value='s',
                                                placeholder='季',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('營收', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0202'},
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
                                                    'index': '0601'},
                                                type='number',
                                                min=0,
                                                max=9999,
                                                value=100,
                                                placeholder='100',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('百萬元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children