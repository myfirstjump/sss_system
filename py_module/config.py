import os
import time

class Configuration(object):

    def __init__(self):
        
        ###

        self.data_folder = ".\\data"
        self.taiwan_stock_info = "111-06-20_TaiwanStockInfo.csv"
        self.log_folder = ".\\data\\log\\log.csv"

        self.dash_port = '8050'
