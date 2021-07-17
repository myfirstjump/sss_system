import os

from py_module.config import Configuration
from py_module.data_reader import DataReader
from py_module.dash_builder import DashBuilder
from py_module.data_processing import DataProcessing

class CLASSPLACEHOLDER(object):

    def __init__(self):
        self.config_obj = Configuration()
        self.reader_obj = DataReader()
        self.processing_obj = DataProcessing()
    
    def data_loading(self):
        file_path = os.path.join(self.config_obj.data_folder, self.config_obj.taiwan_stock_info)
        data = self.reader_obj.read_csv_data(file_path)
        return data

    def data_processing(self, data):
        new_data = self.processing_obj.sss_demo_data_processing(data)
        return new_data

    def dash_server(self, data):
        self.dash_app = DashBuilder(data)

def PLACEHOLDER_main():
    main_obj = CLASSPLACEHOLDER()
    data = main_obj.data_loading()
    data = main_obj.data_processing(data)
    # print(data.head())
    main_obj.dash_server(data) # Run dash server

if __name__ == "__main__":
    PLACEHOLDER_main()

    # comment myfirstjump