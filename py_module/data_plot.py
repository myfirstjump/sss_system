import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

class DataPlot(object):

    def __init__(self):
        pass

    def read_csv_data(self, path):

        data = pd.read_csv(path, header=0, encoding='utf-8', sep=',')
        print("[SSS_INFO] READ CSV DATA")
        print("[SSS_INFO] The data path is from {}".format(path))
        print("[SSS_INFO] The data has {} rows and {} columns".format(data.shape[0], data.shape[1]))

        return data
    
    def plot_01_02(self, data):
        data = data.sort_values(by=['所屬年度'], ascending=True)
        fig = go.Figure(data=[go.Scatter(x=data['所屬年度'], y=data['現金股利(元)'])])

        return fig

    def plot_01_03(self, data):

        if len(data) == 0:
            fig = go.Figure()
        else:
            data = data.sort_values(by=['date'], ascending=True)
            fig = go.Figure(data=[go.Scatter(x=data['date'], y=data['value'])]) # date需要轉換成Q

        return fig

    def plot_01_04(self, data):

        if len(data) == 0:
            fig = go.Figure()
        else:
            data = data.sort_values(by=['年度/月'], ascending=True)
            fig = go.Figure(data=[go.Scatter(x=data['年度/月'], y=data['殖利率(%)'])])
        return fig

    def plot_01_05(self, data):

        if len(data) == 0:
            fig = go.Figure()
        else:
            data = data.sort_values(by=['年度/月'], ascending=True)
            fig = go.Figure(data=[go.Scatter(x=data['年度/月'], y=data['本益比'])]) # 民國需要轉西元
        return fig