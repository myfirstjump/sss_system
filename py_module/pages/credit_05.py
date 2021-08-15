import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style


def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('融資張數', style={'display': 'inline-block'}),
                html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('50000', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('張', style={'display': 'inline-block'}),
                
            ], style=item_style),
            html.Button('>', n_clicks=0, style=self_style.button_style, id='0501-button')
        ],
        className="page",
    )

def create_output(item_style, button_style, dropdown_style, input_style):
    return html.Div([
                html.P('融資張數', style={'display': 'inline-block'}),
                dcc.Dropdown(
                    id='0501-dd',
                    options=[
                        {'label': '大於', 'value': 1},
                        {'label': '小於', 'value': -1},
                    ],
                    value='1',
                    placeholder='大於',
                    style=self_style.dropdown_style),
                dcc.Input(
                    id='0501-ip',
                    type='number',
                    min=0,
                    max=99999999,
                    value=50000,
                    placeholder='50000',
                    style=self_style.input_style),
                html.P('張', style={'display': 'inline-block'}),
                # html.Button('x', n_clicks=0, style=self_style.button_style, id='0501-x')
            ], style=self_style.output_item_style)