import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
import os
# import base64
from pages import self_style
from py_module.data_reader import DataReader
from py_module.config import Configuration

add_img_path = 'assets/add_img.png'
delete_img_path = 'assets/delete_img.png'

def create_filters(button_id):
    content = html.Div(
                            [
                                html.Div([
                                    html.Span([
                                        html.P('公司隸屬', style=self_style.text_normal),
                                        html.P('產業別', style=self_style.text_bold),
                                        html.P('篩選', style=self_style.text_normal),
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
                                        html.P('公司', style=self_style.text_normal), # normal text
                                        html.P('股本', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('5000000 仟元', style=self_style.text_color_bold),
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
                                        html.P('公司', style=self_style.text_normal), # normal text
                                        html.P('股本', style=self_style.text_bold),
                                        html.P('小於', style=self_style.text_bold), # bold text
                                        html.P('5000000 仟元', style=self_style.text_color_bold),
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
                                        html.P('董監持股', style=self_style.text_bold), # normal text
                                        html.P('比例', style=self_style.text_normal), 
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('50%', style=self_style.text_color_bold),
                                        html.P('之股票', style=self_style.text_normal),
                                        
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
                                        html.P('董監質押', style=self_style.text_bold), # normal text
                                        html.P('比例', style=self_style.text_normal), 
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('10%', style=self_style.text_color_bold),
                                        html.P('之股票', style=self_style.text_normal),
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
                                        html.P('每股淨值', style=self_style.text_bold), # normal text
                                        html.P('大於', style=self_style.text_bold), # bold text
                                        html.P('10元', style=self_style.text_color_bold),
                                        html.P('之股票', style=self_style.text_normal),
                                        
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
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年內平均', style=self_style.text_normal),
                                        html.P('ROE大於', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('ROE', style=self_style.text_bold), # normal text
                                        html.P('連續', style=self_style.text_normal), 
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
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
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年內平均', style=self_style.text_normal),
                                        html.P('ROA大於', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('ROA', style=self_style.text_bold), # normal text
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
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
                                        html.P('2', style=self_style.text_color_bold), # bold text
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('EPS', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10元', style=self_style.text_color_bold),
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
                                        html.P('EPS', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('季成長', style=self_style.text_bold),
                                        html.P('5%', style=self_style.text_color_bold),
                                        html.P('以上', style=self_style.text_normal),
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
                                        html.P('上季', style=self_style.text_normal),
                                        html.P('EPS', style=self_style.text_bold),
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
                                        'index': button_id + '-add-0113'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('上', style=self_style.text_normal),
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('存貨週轉率大於', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('存貨週轉率', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('應收帳款週轉率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('應收帳款週轉率', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('流動比率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10%', style=self_style.text_color_bold),
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
                                        html.P('流動比率', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
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
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('速動比率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
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
                                        html.P('速動比率', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
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
                                        html.P('2', style=self_style.text_color_bold),
                                        html.P('季平均', style=self_style.text_normal),
                                        html.P('負債比率', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
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
                                        html.P('負債比率', style=self_style.text_bold),
                                        html.P('成長', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('%', style=self_style.text_color_bold),
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
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年內', style=self_style.text_normal),
                                        html.P('現金股利', style=self_style.text_bold),
                                        html.P('皆', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('10', style=self_style.text_color_bold),
                                        html.P('元', style=self_style.text_color_bold),
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
                                html.Div([
                                    html.Span([
                                        html.P('現金股利', style=self_style.text_bold),
                                        html.P('連續', style=self_style.text_normal),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年成長', style=self_style.text_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0125'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('年內', style=self_style.text_normal),
                                        html.P('殖利率', style=self_style.text_bold),
                                        html.P('皆', style=self_style.text_bold),
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
                                        'index': button_id + '-add-0126'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('本益比', style=self_style.text_bold),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('15', style=self_style.text_color_bold),
                                        html.P('倍', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0127'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('集保庫存', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('週內', style=self_style.text_normal),
                                        html.P('1-999股', style=self_style.text_color_bold),
                                        html.P('區間者增加', style=self_style.text_normal),
                                        html.P('100', style=self_style.text_color_bold),
                                        html.P('人', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0128'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('集保庫存', style=self_style.text_bold),
                                        html.P('3', style=self_style.text_color_bold),
                                        html.P('週內', style=self_style.text_normal),
                                        html.P('1-999股', style=self_style.text_color_bold),
                                        html.P('區間者均', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('100', style=self_style.text_color_bold),
                                        html.P('人', style=self_style.text_color_bold),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0129'
                                    })
                                ]),
                                html.Div([
                                    html.Span([
                                        html.P('每股自由現金流', style=self_style.text_bold),
                                        html.P('近一年', style=self_style.text_color_bold),
                                        html.P('數據', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_color_bold),
                                        html.P('0', style=self_style.text_color_bold),
                                        html.P('元', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button(
                                        html.Img(src=add_img_path, className='add-img-style'), 
                                        n_clicks=0, 
                                        className='btn-style', 
                                    id={
                                        'type': 'filter-btn',
                                        'index': button_id + '-add-0130'
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
                                                dcc.Input(required = True,
                                                    id={'type':'ip',
                                                        'index': '0102'},
                                                    type='number',
                                                    min=0,
                                                    max=999999999999,
                                                    value=5000000,
                                                    placeholder='5000000',
                                                    style=self_style.large_input_style),
                                            ], style=self_style.large_ipt_div_style),
                                            html.P('仟元', style=self_style.text_normal),
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
                                                dcc.Input(required = True,
                                                    id={'type':'ip',
                                                        'index': '0103'},
                                                    type='number',
                                                    min=0,
                                                    max=999999999999,
                                                    value=5000000,
                                                    placeholder='5000000',
                                                    style=self_style.large_input_style),
                                            ], style=self_style.large_ipt_div_style),
                                            html.P('仟元', style=self_style.text_normal),
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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
                                                dcc.Input(required = True,
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


def create_0125(output_count):
    '''0125 (現金股利/股票股利)連續(3)年(成長/衰退)'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0125'},
                                                options=[
                                                    {'label': '現金股利', 'value': '1'},
                                                    {'label': '股票股利', 'value': '2'},
                                                ],
                                                value='1',
                                                placeholder='現金股利',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('連續', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip',
                                                    'index': '0125'},
                                                type='number',
                                                min=0,
                                                max=10,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0125'},
                                                options=[
                                                    {'label': '成長', 'value': '1'},
                                                    {'label': '衰退', 'value': '-1'},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0126(output_count):
    '''0126 (3)年內殖利率(皆/平均)(大於)(5)%'''
    new_children = html.Div([
                                        html.Span([
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0126'},
                                                type='number',
                                                min=0,
                                                max=10,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('年內殖利率', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0126'},
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
                                                id={'type':'dd2',
                                                    'index': '0126'},
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
                                                    'index': '0126'},
                                                type='number',
                                                min=0,
                                                max=100,
                                                value=5,
                                                placeholder='5',
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


def create_0127(output_count):
    '''0127 本益比(大於)(15)倍'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('本益比', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd',
                                                    'index': '0127'},
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
                                                id={'type':'ip',
                                                    'index': '0127'},
                                                type='number',
                                                min=0,
                                                max=10000,
                                                value=15,
                                                placeholder='15',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('倍', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children

def create_0128(output_count):
    '''0128 集保庫存(3)(週/月)內，(1-999股)區間者增加(100)(人/%)'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('集保庫存', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0128'},
                                                type='number',
                                                min=2,
                                                max=30,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.short_input_style),
                                            ], style=self_style.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0128'},
                                                options=[
                                                    {'label': '週', 'value': 'w'},
                                                    {'label': '月', 'value': 'm'},
                                                ],
                                                value='w',
                                                placeholder='週',
                                                clearable=False,
                                                style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('內', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0128'},
                                                options=[
                                                    {'label': '1-999股', 'value': '1-999'},
                                                    {'label': '1-5張', 'value': '1,000-5,000'},
                                                    {'label': '5-10張', 'value': '5,001-10,000'},
                                                    {'label': '10-15張', 'value': '10,001-15,000'},
                                                    {'label': '15-20張', 'value': '15,001-20,000'},
                                                    {'label': '20-30張', 'value': '20,001-30,000'},
                                                    {'label': '30-40張', 'value': '30,001-40,000'},
                                                    {'label': '40-50張', 'value': '40,001-50,000'},
                                                    {'label': '50-100張', 'value': '50,001-100,000'},
                                                    {'label': '100-200張', 'value': '100,001-200,000'},
                                                    {'label': '200-400張', 'value': '200,001-400,000'},
                                                    {'label': '400-600張', 'value': '400,001-600,000'},
                                                    {'label': '600-800張', 'value': '600,001-800,000'},
                                                    {'label': '800-1,000張', 'value': '800,001-1,000,000'},
                                                    {'label': '1,000張以上', 'value': 'more than 1,000,001'},
                                                    {'label': '全部', 'value': 'total'},
                                                ],
                                                value='1,000-5,000',
                                                placeholder='1-5張',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('者增加', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip2',
                                                    'index': '0128'},
                                                type='number',
                                                min=0,
                                                max=99999999,
                                                value=100,
                                                placeholder='100',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0128'},
                                                options=[
                                                    {'label': '人', 'value': '1'},
                                                    {'label': '%', 'value': '2'},
                                                ],
                                                value='1',
                                                placeholder='人',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children


def create_0129(output_count):
    '''0129 集保庫存(3)(週/月)內，(1-999股)區間者均(大於/小於)(100)人'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('集保庫存', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Input(
                                                id={'type':'ip1',
                                                    'index': '0129'},
                                                type='number',
                                                min=2,
                                                max=30,
                                                value=3,
                                                placeholder='3',
                                                style=self_style.short_input_style),
                                            ], style=self_style.short_ipt_div_style),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0129'},
                                                options=[
                                                    {'label': '週', 'value': 'w'},
                                                    {'label': '月', 'value': 'm'},
                                                ],
                                                value='w',
                                                placeholder='週',
                                                clearable=False,
                                                style=self_style.short_dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('內', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0129'},
                                                options=[
                                                    {'label': '1-999股', 'value': '1-999'},
                                                    {'label': '1-5張', 'value': '1,000-5,000'},
                                                    {'label': '5-10張', 'value': '5,001-10,000'},
                                                    {'label': '10-15張', 'value': '10,001-15,000'},
                                                    {'label': '15-20張', 'value': '15,001-20,000'},
                                                    {'label': '20-30張', 'value': '20,001-30,000'},
                                                    {'label': '30-40張', 'value': '30,001-40,000'},
                                                    {'label': '40-50張', 'value': '40,001-50,000'},
                                                    {'label': '50-100張', 'value': '50,001-100,000'},
                                                    {'label': '100-200張', 'value': '100,001-200,000'},
                                                    {'label': '200-400張', 'value': '200,001-400,000'},
                                                    {'label': '400-600張', 'value': '400,001-600,000'},
                                                    {'label': '600-800張', 'value': '600,001-800,000'},
                                                    {'label': '800-1,000張', 'value': '800,001-1,000,000'},
                                                    {'label': '1,000張以上', 'value': 'more than 1,000,001'},
                                                    {'label': '全部', 'value': 'total'},
                                                ],
                                                value='1,000-5,000',
                                                placeholder='1-5張',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('者均', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd3',
                                                    'index': '0129'},
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
                                                    'index': '0129'},
                                                type='number',
                                                min=0,
                                                max=99999999,
                                                value=100,
                                                placeholder='100',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            html.P('人', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button(
                                            html.Img(src=delete_img_path, className='delete-img-style'), 
                                            n_clicks=0, 
                                            className='btn-style', 
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children


def create_0130(output_count):
    '''0130 每股自由現金流 “近一年” 數據 “大於“ ”0元”'''
    new_children = html.Div([
                                        html.Span([
                                            html.P('每股自由現金流，', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd1',
                                                    'index': '0130'},
                                                options=[
                                                    {'label': '近一年', 'value': '1'},
                                                    {'label': '近二年', 'value': '2'},
                                                    {'label': '近三年', 'value': '3'},
                                                ],
                                                value='1',
                                                placeholder='近一年',
                                                clearable=False,
                                                style=self_style.dropdown_style),
                                            ],style=self_style.dp_div_style),
                                            html.P('數據', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd2',
                                                    'index': '0130'},
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
                                                id={'type':'ip',
                                                    'index': '0130'},
                                                type='number',
                                                min=-999999999,
                                                max=999999999,
                                                value=0,
                                                placeholder='0',
                                                required=True,
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