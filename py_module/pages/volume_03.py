import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style


def create_filters(button_id):
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量平均', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('50000', style=self_style.text_normal),
                                        html.P('張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0301'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量平均', style=self_style.text_normal),
                                        html.P('小於', style=self_style.text_bold),
                                        html.P('1000', style=self_style.text_normal),
                                        html.P('張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0302'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量', style=self_style.text_normal),
                                        html.P('增加', style=self_style.text_bold),
                                        html.P('1000', style=self_style.text_normal),
                                        html.P('張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0303'
                                    })
                                ]),   
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量', style=self_style.text_normal),
                                        html.P('減少', style=self_style.text_bold),
                                        html.P('1000', style=self_style.text_normal),
                                        html.P('張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0304'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量', style=self_style.text_normal),
                                        html.P('增加', style=self_style.text_bold),
                                        html.P('20', style=self_style.text_normal),
                                        html.P('% 之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0305'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，成交量', style=self_style.text_normal),
                                        html.P('減少', style=self_style.text_bold),
                                        html.P('20', style=self_style.text_normal),
                                        html.P('% 之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style, 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0306'
                                    })
                                ]),                             
                            ])
    return content

def create_0301(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0301'},
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
                                                    'index': '0301'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量平均', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0301'},
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0301'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=50000,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    return new_children

def create_0302(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0302'},
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
                                                    'index': '0302'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量平均', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0302'},
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='小於',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0302'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=10,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0303(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0303'},
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
                                                    'index': '0303'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0303'},
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0303'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=1000,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0304(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0304'},
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
                                                    'index': '0304'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0304'},
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='減少',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0304'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=1000,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0305(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0305'},
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
                                                    'index': '0305'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0305'},
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0305'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=20,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('% 之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0306(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0306'},
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
                                                    'index': '0306'},
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
                                                    style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),                                           
                                            html.P('內，成交量', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0306'},
                                                options=[
                                                    {'label': '增加', 'value': 1},
                                                    {'label': '減少', 'value': -1},
                                                ],
                                                value='-1',
                                                placeholder='減少',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0306'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=20,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('% 之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children