import dash_html_components as html
import pandas as pd
import pathlib



def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('法人籌碼篩選條件一', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='legal-01')
            ], style=item_style),
            html.Div([
                html.P('法人成交量篩選條件二', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='legal-02')
            ], style=item_style),
        ],
        className="page",
    )