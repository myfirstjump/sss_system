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
    
    def iq_info_adjust(self, data):

        if data.iloc[0,0] > 0: # 漲跌
            data.iloc[0,0] = '▲' + str(data.iloc[0,0])
        elif data.iloc[0,0] < 0:
            data.iloc[0,0] = '▼' + str(np.abs(data.iloc[0,0]))
        else:
            data.iloc[0,0] = str(data.iloc[0,0])
        
        if data.iloc[0,1] > 0: # 漲幅
            data.iloc[0,1] = '+' + str(np.round(data.iloc[0,1], 2)) + '%' 
        elif data.iloc[0,1] < 0:
            data.iloc[0,1] = str(np.round(data.iloc[0,1], 2)) + '%' 
        else:
            data.iloc[0,1] = str(np.round(data.iloc[0,1], 2)) + '%' 

        data.iloc[0,2] = "{:,}".format(data.iloc[0,2]) + '張' #成交量
        

        return data

    def iq_table_01_01_adjust(self, dataframe):
        
        if len(dataframe) == 0:
            return pd.DataFrame()
        else:
            dataframe['date'] = dataframe['date'].dt.to_period('Q')
            # dataframe['date'] = dataframe['date'].apply(lambda x: x.strftime('%Y-%m-%d')) # 為了後面轉為column name，所以先轉成字串
            dataframe.set_index('date', inplace=True)
            dataframe.index = dataframe.index.to_series().astype(str) # 為了後面轉為column name，所以先轉成字串
            data_transposed = dataframe.T
            data_transposed.reset_index(inplace=True) # dash datatable不會顯示index在網頁上，所以將index轉成一個column
            data_transposed.rename(columns={"index":""}, inplace=True)
            # print(data_transposed.index)
            # print(data_transposed.columns)
        return data_transposed
    
    def iq_table_round_adjust(self, data):

        data = np.round(data, 2)

        return data

    def iq_legal_table_concat(self, df1, df2, df3, df4):

        df1['日期'] = df1['日期'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df2['日期'] = df2['日期'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df3['日期'] = df3['日期'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df4['日期'] = df4['日期'].apply(lambda x: x.strftime('%Y-%m-%d'))
        print(df1)

        df1.set_index('日期', inplace=True)
        print(df1)
        df2.set_index('日期', inplace=True)
        df3.set_index('日期', inplace=True)
        df4.set_index('日期', inplace=True)

        df = pd.concat([df1, df2, df3, df4], axis=1)
        df.reset_index(inplace=True)

        return df

    
