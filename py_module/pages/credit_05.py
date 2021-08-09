import dash_html_components as html
import pandas as pd
import pathlib



def create_layout(item_style, button_style):
    return html.Div(
        [
            html.Div([
                html.P('信用交易篩選條件一', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='credit-01')
            ], style=item_style),
            html.Div([
                html.P('信用交易篩選條件二', style={'display': 'inline-block'}),
                html.Button('>', style=button_style, id='credit-02')
            ], style=item_style),
        ],
        className="page",
    )