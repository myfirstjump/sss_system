import os
import time

class Configuration(object):

    def __init__(self):
        
        ###

        self.data_folder = ".\\data"
        self.taiwan_stock_info = "112-10-29_TaiwanStockInfo.csv"
        self.log_folder = ".\\data\\log\\log.csv"

        self.dash_port = '8050'
