import dash_html_components as html
import pandas as pd
import pathlib



def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('公司基本資訊篩選條件一', id='basic-01P', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='basic-01')
            ], style=item_style),
            html.Div([
                html.P('公司基本資訊篩選條件二', id='basic-02P', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='basic-02')
            ], style=item_style),
        ],
        className="page",
    )
