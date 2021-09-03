import pandas as pd
import numpy as np

class DataProcessing(object):

    def __init__(self):
        pass

    def sss_demo_data_processing(self, data):

        
        new_col_0 = np.random.exponential(70, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '股價', new_col_0)

        new_col_1 = np.random.exponential(5, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '每股淨值', new_col_1)

        new_col_2 = np.random.exponential(10000000, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_2)

        # new_col_3 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_3)

        # new_col_4 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_4)

        # new_col_5 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_5)

        # new_col_6 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_6)
        
        return new_data

    def add_column_to_pd_dataframe(self, data, new_column_name, new_column_array):

        data[new_column_name] = new_column_array

        return data
    