import pandas as pd
import numpy as np

class DataProcessing(object):

    def __init__(self):
        pass

    def sss_demo_data_processing(self, data):

        
        new_col_0 = np.random.exponential(70, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '股價', new_col_0)

        new_col_1 = np.random.exponential(5, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '每股淨值成長百分比比率%', new_col_1)

        new_col_2 = np.random.exponential(10000000, data.shape[0])
        new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_2)

        new_data = self.add_column_to_pd_dataframe(data, 'Remark', '含ROE負轉正；含ROE負轉正；含ROE負轉正；')

        # new_col_3 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_3)

        # new_col_4 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_4)

        # new_col_5 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_5)

        # new_col_6 = np.random.exponential(10000000, data.shape[0])
        # new_data = self.add_column_to_pd_dataframe(data, '營業額', new_col_6)
        
        return new_data
    
    def sss_data_preprocessing(self, data):
        data = data[['date','industry_category','stock_id','stock_name','type']]
        return data
    
    def get_stock_id_and_stock_name_list(self, data):
        series = data['stock_id'] + " " + data['stock_name']
        options = []
        for string, stock_id  in zip(series, data['stock_id']):
            options.append({'label': string, 'value': stock_id})

        return options
        

    def add_column_to_pd_dataframe(self, data, new_column_name, new_column_array):

        data[new_column_name] = new_column_array

        return data
    
    def iq_table_adjust(self, dataframe):
        
        dataframe['date'] = dataframe['date'].dt.to_period('Q')
        # dataframe['date'] = dataframe['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        dataframe.set_index('date', inplace=True)
        dataframe.index = dataframe.index.to_series().astype(str)
        print(dataframe)
        data_transposed = dataframe.T
        data_transposed.reset_index(inplace=True) # dash datatable不會顯示index，所以將index轉成column
        data_transposed.rename(columns={"index":""}, inplace=True)
        print(data_transposed.index)
        print(data_transposed.columns)
        return data_transposed
    
