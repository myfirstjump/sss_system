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
                                        html.P('營收', style=self_style.text_normal),
                                        html.P('大於', style=self_style.text_bold),
                                        html.P('5', style=self_style.text_bold),
                                        html.P('億元', style=self_style.text_normal),
                                    ], style=self_style.item_style),
                                    html.Button('+', n_clicks=0, style=self_style.button_style,
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
                                            html.P('營收', style=self_style.text_normal),
                                            html.Div([
                                                dcc.Dropdown(
                                                id={'type':'dd',
                                                    'index': '0601'},
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
                                                id={'type':'ip',
                                                    'index': '0601'},
                                                type='number',
                                                min=0,
                                                max=99999,
                                                value=5,
                                                placeholder='5',
                                                style=self_style.input_style),
                                            ], style=self_style.ipt_div_style),
                                            
                                            html.P('億元', style=self_style.text_normal),
                                        ], style=self_style.output_item_style),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(output_count)})
                                    ])

    return new_children