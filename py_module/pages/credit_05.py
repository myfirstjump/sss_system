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
                                        html.P('融資於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' 張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0501'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融資於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' %之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0502'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融券於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' 張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0503'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('融券於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' %之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0504'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('借券於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' 張之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0505'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('借券於', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_bold),
                                        html.P('日內，', style=self_style.text_normal),
                                        html.P('增加/減少', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_normal),
                                        html.P(' %之股票', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0506'
                                    })
                                ]),
                            ])
    return content



def create_0501(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('融資於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0501'},
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
                                                    'index': '0501'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0501'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0501'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children

def create_0502(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('融資於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0502'},
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
                                                    'index': '0502'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0502'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0502'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children

def create_0503(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('融券於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0503'},
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
                                                    'index': '0503'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0503'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0503'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children

def create_0504(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('融券於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0504'},
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
                                                    'index': '0504'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0504'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0504'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children

def create_0505(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('借券於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0505'},
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
                                                    'index': '0505'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0505'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0505'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('張之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children

def create_0506(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('借券於', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0506'},
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
                                                    'index': '0506'},
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
                                            html.P('內，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0506'},
                                                options=[
                                                    {'label': '增加', 'value': '1'},
                                                    {'label': '減少', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='增加',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0506'},
                                                type='number',
                                                min=0,
                                                max=9999999,
                                                value=100,
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('%之股票', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])
    
    return new_children