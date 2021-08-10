import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib



def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('法人', style={'display': 'inline-block'}),
                html.P('買超', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('5000', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                html.P('張', style={'display': 'inline-block'}),
                html.Button('>', n_clicks=0, style=button_style, id='legal-0501-button')
            ], style=item_style),
        ],
        className="page",
    )

def create_output(item_style, button_style, dropdown_style, input_style):
    return html.Div([
                html.P('法人', style={'display': 'inline-block'}),
                dcc.Dropdown(
                    id='legal-0501-dd',
                    options=[
                        {'label': '買超', 'value': 1},
                        {'label': '賣超', 'value': -1},
                    ],
                    value='1',
                    placeholder='買超',
                    style=dropdown_style),
                dcc.Dropdown(
                    id='legal-0501-dd2',
                    options=[
                        {'label': '大於', 'value': 1},
                        {'label': '小於', 'value': -1},
                    ],
                    value='1',
                    placeholder='大於',
                    style=dropdown_style),
                dcc.Input(
                    id='legal-0501-ip',
                    type='number',
                    min=0,
                    max=999999,
                    value=5000,
                    placeholder='5000',
                    style=input_style),
                html.P('億元', style={'display': 'inline-block'}),
                html.Button('x', n_clicks=0, style=button_style, id='legal-0501-x')
            ], style=item_style)