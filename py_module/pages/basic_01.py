import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pathlib
from py_module.pages import self_style



# create_item = 
#     [
#         html.Div([
#             html.P('股本', style=self_style.text_normal), # normal text
#             html.P('大於', style=self_style.text_bold), # bold text
#             html.P('5', style=self_style.text_bold),
#             html.P('億元', style=self_style.text_normal),
            
#         ], style=self_style.item_style),
#         html.Button('>', n_clicks=0, style=self_style.button_style, 
#         id={
#             'type': 'filter-btn',
#             'index': button_id + '-add'
#         })
#     ]