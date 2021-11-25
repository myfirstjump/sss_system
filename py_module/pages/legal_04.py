import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    content = html.Div(
                            [                              
                                html.Div([
                                    html.Span([
                                        html.P('外資', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0401'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('外資', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('小於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0402'
                                    })
                                ]),                  
                                html.Div([
                                    html.Span([
                                        html.P('投信', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0403'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('投信', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('小於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0404'
                                    })
                                ]),         
                                html.Div([
                                    html.Span([
                                        html.P('自營商', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                        
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0405'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('自營商', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('日內', style=self_style.text_normal),
                                        html.P('買超/賣超', style=self_style.text_bold),
                                        html.P('小於', style=self_style.text_bold),
                                        html.P('5000張', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0406'
                                    })
                                ]),                                                                
                            ])  
    return content



def create_0401(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('外資', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0401'},
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
                                                    'index': '0401'},
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
                                                    'index': '0401'},
                                                    options=[
                                                        {'label': '買超', 'value': '1'},
                                                        {'label': '賣超', 'value': '-1'},
                                                    ],
                                                    value='1',
                                                    placeholder='買超',
                                                    clearable=False,
                                                    style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0401'},
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
                                                    'index': '0401'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0402(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('外資', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0402'},
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
                                                    'index': '0402'},
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
                                                    'index': '0402'},
                                                options=[
                                                    {'label': '買超', 'value': '1'},
                                                    {'label': '賣超', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0402'},
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
                                                id={'type':'ip2',
                                                    'index': '0402'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0403(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('投信', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0403'},
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
                                                    'index': '0403'},
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
                                                    'index': '0403'},
                                                options=[
                                                    {'label': '買超', 'value': '1'},
                                                    {'label': '賣超', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0403'},
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
                                                    'index': '0403'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0404(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('投信', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0404'},
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
                                                    'index': '0404'},
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
                                                    'index': '0404'},
                                                options=[
                                                    {'label': '買超', 'value': '1'},
                                                    {'label': '賣超', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0404'},
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
                                                id={'type':'ip2',
                                                    'index': '0404'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0405(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('自營商', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0405'},
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
                                                    'index': '0405'},
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
                                                    'index': '0405'},
                                                options=[
                                                    {'label': '買超', 'value': '1'},
                                                    {'label': '賣超', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0405'},
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
                                                    'index': '0405'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0406(output_count):
    new_children = html.Div([
                                        html.Span([
                                            html.P('自營商', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(required = True,
                                                id={'type':'ip1',
                                                    'index': '0406'},
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
                                                    'index': '0406'},
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
                                                    'index': '0406'},
                                                options=[
                                                    {'label': '買超', 'value': '1'},
                                                    {'label': '賣超', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='買超',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0406'},
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
                                                id={'type':'ip2',
                                                    'index': '0406'},
                                                type='number',
                                                min=0,
                                                max=999999,
                                                value=5000,
                                                placeholder='5000',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('張', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children