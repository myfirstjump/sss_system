import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State, ALL
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import json
import ast

from py_module.pages import (
    basic_01,
    price_02,
    volume_03,
    legal_04,
    credit_05,
    revenue_06,
    self_style
)

class DashBuilder(object):

    def __init__(self, data):
        
        # self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

        self.external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__, suppress_callback_exceptions=True)#, external_stylesheets=self.external_stylesheets)
        self.app.config.suppress_callback_exceptions = True
        # self.app = dash.Dash(__name__)
        self.app.title = 'Stock Target Selection'
        self.colors = {
            'background': '#ffffff',
            'text': '#111111'
        }

        self.top_div_style = self_style.top_div_style
        self.style = self_style.style
        self.category_btn_style = self_style.category_btn_style
        self.menu_style = self_style.menu_style
        self.item_style = self_style.item_style
        self.output_container_style = self_style.output_container_style
        self.filter_content_style = self_style.filter_content_style
        self.add_text_style = self_style.add_text_style
        self.filter_style = self_style.filter_style
        self.display_style = self_style.display_style
        self.button_style = self_style.button_style
        self.selection_style = self_style.selection_style
        self.frame_style = self_style.frame_style
        self.link_div_style = self_style.link_div_style
        self.dropdown_style = self_style.dropdown_style
        self.input_style = self_style.input_style

        self.app.layout = html.Div([ # TOP DIV
                dcc.Store('memory'),
                # HEADER
                html.Div([
                        html.H1('台股選股系統', style={'margin':self.style['margin'], 'padding':self.style['padding']})
                ]),# HEADER

                html.Div([ # FILTER & DISPLAY

                    # FILTER
                    html.Div([
                        # html.Div('FILTER'),
                        html.Div([ # MENU
                            html.Div(
                                html.Button(
                                    "基本資訊",
                                    id='01-btn',
                                    n_clicks=0,
                                    title='展開基本資訊選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "股價條件",
                                    id='02-btn',
                                    title='展開股價條件選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "成交量值",
                                    id='03-btn',
                                    title='展開成交量值選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "法人籌碼", 
                                    id='04-btn',
                                    title='展開法人籌碼選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "信用交易",
                                    id='05-btn',
                                    title='展開信用交易選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                            html.Div(
                                html.Button(
                                    "公司營收",
                                    id='06-btn',
                                    title='展開公司營收選項',
                                    style=self.category_btn_style
                                ),
                            style=self.link_div_style),
                        ], style=self.menu_style), # MENU
                        html.Div([html.Div('請由左方加入篩選類別', style=self.add_text_style)], id="filter-content", 
                            style=self.filter_content_style),
                    ], style=self.filter_style),# FILTER

                    # DISPLAY
                    html.Div([
                        # "DISPLAY",
                        html.Div('您的選股條件', style=self.add_text_style),
                        html.Div([
                        ],
                        id='dynamic-output-container',
                        style={
                                    'width': '95%', 
                                    'height': '85%', 
                                    'margin':'left', 
                                    'padding':'1%',
                                    'display':'inline-block',
                                    'verticalAlign':'middle'
                        }),
                    ], style=self.display_style),  # DISPLAY

                ], style=self.frame_style), # FILTER & DISPLAY

                # SELECTION RESULT
                html.Div([
                    html.Div([
                        html.Div(['查詢結果'], style=self.add_text_style),
                        html.Div([],id='dynamic-selection-result')
                    ], 
                    style=self.selection_style)
                ], style=self.frame_style),  # SELECTION RESULT                            
        ], style=self.top_div_style)#TOP DIV

        ### callbacks
        # 1. Links -> filter-content
        @self.app.callback(
            Output('filter-content', 'children'),
            Input('01-btn', 'n_clicks'),
            Input('02-btn', 'n_clicks'),
            Input('03-btn', 'n_clicks'),
            Input('04-btn', 'n_clicks'),
            Input('05-btn', 'n_clicks'),
            Input('06-btn', 'n_clicks'),
        )
        def filter_update(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, ):
            ctx = dash.callback_context
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == '01-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('股本', style={'display': 'inline-block'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('5', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('億元', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style, 
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])   
            elif button_id == '02-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('股價', style={'display': 'inline-block'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('120', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('元', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style,
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])
            elif button_id == '03-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('成交張數', style={'display': 'inline-block'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('500000', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('張', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style, 
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])
            elif button_id == '04-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('法人', style={'display': 'inline-block'}),
                                    html.P('買超', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('5000', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('張', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style, 
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])        
            elif button_id == '05-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('融資張數', style={'display': 'inline-block'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('50000', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('張', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style, 
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])
            elif button_id == '06-btn':
                content = html.Div(
                            [
                                html.Div([
                                    html.P('營收', style={'display': 'inline-block'}),
                                    html.P('大於', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('5', style={'display': 'inline-block', 'color':'red', 'padding':'0px 5px 0px 5px'}),
                                    html.P('億元', style={'display': 'inline-block'}),
                                    
                                ], style=self_style.item_style),
                                html.Button('>', n_clicks=0, style=self_style.button_style, 
                                id={
                                    'type': 'filter-btn',
                                    'index': button_id + '-add'
                                })
                            ])          
            else:
                content = html.Div("請由左方加入篩選類別", style=self.add_text_style)
            return content

        # 2. filter-content -> dynamic-output-container
        self.output_count = 0
        self.output_record = []
        self.all_btn = (
            '{"index":"01-btn-add","type":"filter-btn"}.n_clicks',
            '{"index":"02-btn-add","type":"filter-btn"}.n_clicks',
            '{"index":"03-btn-add","type":"filter-btn"}.n_clicks',
            '{"index":"04-btn-add","type":"filter-btn"}.n_clicks',
            '{"index":"05-btn-add","type":"filter-btn"}.n_clicks',
            '{"index":"06-btn-add","type":"filter-btn"}.n_clicks',
        )
        @self.app.callback(
            Output('dynamic-output-container', 'children'),
            Input({'type':'filter-btn', 'index': ALL}, 'n_clicks'),
            Input({'type':'output-btn', 'index': ALL}, 'n_clicks'),
            State('dynamic-output-container', 'children'),
        )
        def output_update(f_btn, x_btn, children):
            if (len(f_btn) == 0):
                raise PreventUpdate

            triggered = [t["prop_id"] for t in dash.callback_context.triggered]
            print(triggered)
            # adding = len([1 for i in triggered if i in ('{"index":"01-btn-add","type":"filter-btn"}.n_clicks')])
            adding = len([1 for i in triggered if i in self.all_btn])
            clearing = len([1 for i in triggered[0].split('"')[7] if i in ('output-btn')])

            if adding:
                ctx = dash.callback_context
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('filter clicked! And button id is:', button_id)
                f_btn = f_btn[0]

                if (button_id == '{"index":"01-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 01 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.P('股本', style={'display': 'inline-block'}),
                                            dcc.Dropdown(
                                                # id='0101-dd',
                                                options=[
                                                    {'label': '大於', 'value': 1},
                                                    {'label': '小於', 'value': -1},
                                                ],
                                                value='1',
                                                placeholder='大於',
                                                style=self_style.dropdown_style),
                                            dcc.Input(
                                                # id='0101-ip',
                                                type='number',
                                                min=0,
                                                max=99999,
                                                value=5,
                                                placeholder='5',
                                                style=self_style.input_style),
                                            html.P('億元', style={'display': 'inline-block'}),
                                            html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"02-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 02 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.P('股價', style={'display': 'inline-block'}),
                                        dcc.Dropdown(
                                            # id='0201-dd',
                                            options=[
                                                {'label': '大於', 'value': 1},
                                                {'label': '小於', 'value': -1},
                                            ],
                                            value='1',
                                            placeholder='大於',
                                            style=self_style.dropdown_style),
                                        dcc.Input(
                                            # id='0201-ip',
                                            type='number',
                                            min=0,
                                            max=99999,
                                            value=120,
                                            placeholder='120',
                                            style=self_style.input_style),
                                        html.P('元', style={'display': 'inline-block'}),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"03-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 03 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.P('成交張數', style={'display': 'inline-block'}),
                                        dcc.Dropdown(
                                            id='0301-dd',
                                            options=[
                                                {'label': '大於', 'value': 1},
                                                {'label': '小於', 'value': -1},
                                            ],
                                            value='1',
                                            placeholder='大於',
                                            style=self_style.dropdown_style),
                                        dcc.Input(
                                            id='0301-ip',
                                            type='number',
                                            min=0,
                                            max=9999999999,
                                            value=500000,
                                            placeholder='500000',
                                            style=self_style.input_style),
                                        html.P('張', style={'display': 'inline-block'}),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"04-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 04 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.P('法人', style={'display': 'inline-block'}),
                                        dcc.Dropdown(
                                            id='0401-dd',
                                            options=[
                                                {'label': '買超', 'value': 1},
                                                {'label': '賣超', 'value': -1},
                                            ],
                                            value='1',
                                            placeholder='買超',
                                            style=self_style.dropdown_style),
                                        dcc.Dropdown(
                                            id='0401-dd2',
                                            options=[
                                                {'label': '大於', 'value': 1},
                                                {'label': '小於', 'value': -1},
                                            ],
                                            value='1',
                                            placeholder='大於',
                                            style=self_style.dropdown_style),
                                        dcc.Input(
                                            id='0401-ip',
                                            type='number',
                                            min=0,
                                            max=999999,
                                            value=5000,
                                            placeholder='5000',
                                            style=self_style.input_style),
                                        html.P('億元', style={'display': 'inline-block'}),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"05-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 05 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
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
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                elif (button_id == '{"index":"06-btn-add","type":"filter-btn"}') and (f_btn > 0):
                    print('filter 06 clicked!')
                    # record
                    self.output_count += 1
                    self.output_record.append(self.output_count)
                    print('Record:', self.output_record)
                    # button_id = button_id.split('"')[3] 
                    new_children = html.Div([
                                        html.P('營收', style={'display': 'inline-block'}),
                                        dcc.Dropdown(
                                            id='0601-dd',
                                            options=[
                                                {'label': '大於', 'value': 1},
                                                {'label': '小於', 'value': -1},
                                            ],
                                            value='1',
                                            placeholder='大於',
                                            style=self_style.dropdown_style),
                                        dcc.Input(
                                            id='0601-ip',
                                            type='number',
                                            min=0,
                                            max=99999,
                                            value=5,
                                            placeholder='5',
                                            style=self_style.input_style),
                                        html.P('億元', style={'display': 'inline-block'}),
                                        html.Button('x', n_clicks=0, style=self_style.button_style,
                                                id={'type':'output-btn',
                                                    'index': str(self.output_count)})
                                    ], style=self_style.output_item_style)
                    children.append(new_children)
                    return children
                else:
                    return children
            elif clearing:
                ctx = dash.callback_context 
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
                print('output clicked! And button id is:', button_id)

                remove_number = int(button_id.split('"')[3])
                remove_idx = self.output_record.index(remove_number)
                print('remove_number:', remove_number, 'remove_idx:', remove_idx)
                self.output_record.remove(remove_number)
                del children[remove_idx]
                print('Record:', self.output_record)
                
                    # new_spec = new_children if not clearing
            # elif (button_id == '01-btn-add-output') and (x_btn == [1]):
                
            #     new_children = ''
            # else:

            else:
                print('Dont know which filter clicked!')

            return children







        # @app.callback(
        #     [
        #         Output('dynamic-output-container', "children"),
        #         Output("new-item", "value")
        #     ],
        #     [
        #         Input("add", "n_clicks"),
        #         Input("new-item", "n_submit"),
        #         Input("clear-done", "n_clicks")
        #     ],
        #     [
        #         State("new-item", "value"),
        #         State({"index": ALL}, "children"),
        #         State({"index": ALL, "type": "done"}, "value")
        #     ]
        # )
        # def edit_list(add, add2, clear, new_item, items, items_done):
        #     triggered = [t["prop_id"] for t in dash.callback_context.triggered]
        #     adding = len([1 for i in triggered if i in ("add.n_clicks", "new-item.n_submit")])
        #     clearing = len([1 for i in triggered if i == "clear-done.n_clicks"])
        #     new_spec = [
        #         (text, done) for text, done in zip(items, items_done)
        #         if not (clearing and done)
        #     ]
        #     if adding:
        #         new_spec.append((new_item, []))
        #     new_list = [
        #         html.Div([
        #             dcc.Checklist(
        #                 id={"index": i, "type": "done"},
        #                 options=[{"label": "", "value": "done"}],
        #                 value=done,
        #                 style={"display": "inline"},
        #                 labelStyle={"display": "inline"}
        #             ),
        #             html.Div(text, id={"index": i}, style=style_done if done else style_todo)
        #         ], style={"clear": "both"})
        #         for i, (text, done) in enumerate(new_spec)
        #     ]
        #     return [new_list, "" if adding else new_item]


        # @app.callback(
        #     Output({"index": MATCH}, "style"),
        #     Input({"index": MATCH, "type": "done"}, "value")
        # )
        # def mark_done(done):
        #     return style_done if done else style_todo


        # @app.callback(
        #     Output("totals", "children"),
        #     Input({"index": ALL, "type": "done"}, "value")
        # )
        # def show_totals(done):
        #     count_all = len(done)
        #     count_done = len([d for d in done if d])
        #     result = "{} of {} items completed".format(count_done, count_all)
        #     if count_all:
        #         result += " - {}%".format(int(100 * count_done / count_all))
        #     return result


        self.app.run_server(debug=True, dev_tools_hot_reload=True)#, dev_tools_ui=False, dev_tools_props_check=False)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

