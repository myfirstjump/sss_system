import os
import time

class Configuration(object):

    def __init__(self):
        
        ###

        self.data_folder = ".\\data"
        self.taiwan_stock_info = "TaiwanStockInfo.csv"

        self.dash_port = '8050'
