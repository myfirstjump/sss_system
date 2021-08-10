import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib



def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('股價', style={'display': 'inline-block'}),
                html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('120', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('元', style={'display': 'inline-block'}),
                html.Button('>', n_clicks=0, style=button_style, id='price-0201-button')
            ], style=item_style),
        ],
        className="page",
    )

def create_output(item_style, button_style, dropdown_style, input_style):
    return html.Div([
                html.P('股價', style={'display': 'inline-block'}),
                dcc.Dropdown(
                    id='price-0201-dd',
                    options=[
                        {'label': '大於', 'value': 1},
                        {'label': '小於', 'value': -1},
                    ],
                    value='1',
                    placeholder='大於',
                    style=dropdown_style),
                dcc.Input(
                    id='price-0201-ip',
                    type='number',
                    min=0,
                    max=99999,
                    value=120,
                    placeholder='120',
                    style=input_style),
                html.P('元', style={'display': 'inline-block'}),
                html.Button('x', n_clicks=0, style=button_style, id='price-0201-x')
            ], style=item_style)