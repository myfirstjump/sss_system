
from py_module.config import Configuration
from py_module.data_reader import DataReader
from py_module.dash_builder import DashBuilder
from py_module.data_processing import DataProcessing

import pymssql
import datetime
from datetime import timedelta
from string import ascii_lowercase
import random

import pandas as pd
import os
import matplotlib.pyplot as plt

            # now = datetime.datetime.now()
            # today = now.date()
            # yesterday = today - timedelta(days=1)
            # this_week_start = today - timedelta(days=now.weekday())
            # this_month_start = datetime.datetime(today.year, today.month, 1).date()
            # quarter_start_month = (today.month - 1) - (today.month - 1) % 3 + 1
            # this_quarter_start = datetime.datetime(today.year, quarter_start_month, 1).date()
            # this_year_start = datetime.datetime(today.year, 1, 1).date()

skill_info = 'STOCK_SKILL_DB.dbo.TW_STOCK_INFO'
skill_capital = 'STOCK_SKILL_DB.dbo.TW_STOCK_CAPITAL'
basic_info_supervisor = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_Director_Supervisor'
basic_info_revenue_m = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_MonthRevenue'
basic_info_revenue_q = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_MonthRevenue_Quarterly'
basic_info_revenue_y = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_MonthRevenue_Yearly'
basic_info_finDetail_q = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_FinancialStatements_Detail'
basic_info_finDetail_y = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_FinancialStatements_Detail_Yearly'
basic_info_finState_q = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_FinancialStatements'
basic_info_finState_y = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_FinancialStatements_Yearly'
basic_info_dividend = 'STOCK_BASICINTO_DB.dbo.TW_STOCK_DIVIDEND_YEARLY'
skill_price_d = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Daily'
skill_price_w = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Weekly'
skill_price_m = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_monthly'
skill_price_q = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_quarterly'
skill_price_y = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_yearly'
skill_per = 'STOCK_SKILL_DB.dbo.TW_STOCK_PER'
counter_legal_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Daily'
counter_legal_w = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Weekly'
counter_legal_m = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Monthly'
counter_legal_q = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Quarterly'
counter_legal_y = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Yearly'
counter_margin_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Daily' #融資 #融券
counter_margin_w = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Weekly'
counter_margin_m = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Monthly'
counter_margin_q = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Quarterly'
counter_margin_y = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Yearly'
counter_loanshare_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Daily' #借券
counter_loanshare_w = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Weekly'
counter_loanshare_m = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Monthly'
counter_loanshare_q = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Quarterly'
counter_loanshare_y = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Yearly'
counter_holdrange_w = 'STOCK_Counter_DB.dbo.TW_STOCK_HOLDRANGE'
counter_holdrange_m = 'STOCK_Counter_DB.dbo.TW_STOCK_HOLDRANGE_monthly'


folder_path = "D:\\myfirstjump_datasets\\tw_stock\\filter_report"
output_folder = "D:\\myfirstjump_datasets\\tw_stock\\industry_prediction_project"


config_obj = Configuration()
reader_obj = DataReader()
process_obj = DataProcessing()



def sql_execute(query):

    conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query)
    # data = [row for row in cursor]
    data = []
    for row in cursor:
        data.append(row)
    cursor.close()
    conn.close()
    return data

def create_query_index_data(period_str):

    query = '''
            SELECT * FROM STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_{} WHERE date < '2022-01-01' AND stock_id IN  ('Automobile',
        'BiotechnologyMedicalCare',
        'BuildingMaterialConstruction',
        'Cement',
        'Chemical',
        'ChemicalBiotechnologyMedicalCare',
        'CommunicationsInternet',
        'ComputerPeripheralEquipment',
        'ElectricalCable',
        'ElectricMachinery',
        'Electronic',
        'ElectronicPartsComponents',
        'ElectronicProductsDistribution',
        'FinancialInsurance',
        'Food',
        'GlassCeramic',
        'InformationService',
        'IronSteel',
        'OilGasElectricity',
        'Optoelectronic',
        'Other',
        'OtherElectronic',
        'PaperPulp',
        'Plastics',
        'Rubber',
        'Semiconductor',
        'ShippingTransportation',
        'Textiles',
        'Tourism',
        'TradingConsumersGoods',
        'TAIEX',
        'TPEx'
        )
    '''.format(period_str)

    return query

def create_query_data():

    query = '''
            SELECT [date]
      ,t1.[stock_id]
	  ,t2.Category
      ,[Trading_Volume]
      ,[close]
      ,[spread]
      ,[spread_ratio]
  FROM [STOCK_SKILL_DB].[dbo].[TW_STOCK_PRICE_Monthly] t1
  LEFT JOIN [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_Company_BASICINFO] t2 ON t1.stock_id = t2.stock_id
  WHERE [date] >= '2016-01-01'

    '''

    return query


def date_interval_non_overlap_selection(self, date_series, interval_length, sample_amount):

    samples = []
    

    return samples

# ===== Query from DB後寫出檔案 =====
data_query = create_query_data()
# data_query = create_query_index_data(period_str='daily')
data = sql_execute(data_query)

data = pd.DataFrame.from_records(data)
# # data.to_excel(folder_path + '\\TaiwanStockInfo_index_info.xlsx', index=False)
data.to_excel(folder_path + '\\2023-06-20_個股月資料.xlsx', index=False)
print(data.head(50))
# ==================================


# ===== 統計資料 ===== 觀察產業月份規律
# data = pd.read_excel(folder_path + '\\TaiwanStockInfo_index_info.xlsx')

# tmp = data["date"].astype(str).str.split("-", n = 2, expand = True)
# data['date_month'] = tmp[1]

# data = data.groupby(['stock_name', 'date_month'])['spread_ratio'].agg(['mean', 'std'])


# print(data.tail(100))

# data.to_excel(folder_path + '\\台股產業_各月份均值&標準差_2010-2021.xlsx')
# ==================================


# ===== 統計資料 ===== 參數趨勢線
# data = pd.read_excel(folder_path + '\\TaiwanStockInfo_index_info.xlsx')
# industry_names = data['stock_name'].unique()

# # print(data.head(100))
# # print(data.dtypes)
# # print(industry_names)

# tpex_index = data[data['stock_id']=='TAIEX']
# tpex_index = tpex_index.sort_values(by='date', ascending=True)

# semi_index = data[data['stock_id']=='Semiconductor']
# semi_index = semi_index.sort_values(by='date', ascending=True)
# print(tpex_index.head(100))
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.plot(tpex_index['date'], tpex_index['spread_ratio'])
# ax.plot(semi_index['date'], semi_index['spread_ratio'])
# plt.show()
# ===== 統計資料 ===== 


# ===== 統計資料 ===== 觀察產業大起大落趨勢，來當作y值

# data = pd.read_excel(folder_path + '\\TaiwanStockInfo_index_daily_data.xlsx')
# fig, ax = plt.subplots(figsize=(8, 6))
# semi_index = data[data['stock_id']=='Semiconductor']
# semi_index = semi_index.sort_values(by='date', ascending=True)

# # ax.plot(semi_index['date'], semi_index['spread_ratio'])
# semi_index['spread_ratio'].plot.hist(bins=100)
# plt.show()
# print(semi_index['spread_ratio'].describe())
# ===== 統計資料 ===== 



# data = pd.read_excel(folder_path + '\\2023-06-20_加權指數櫃買指數數據.xlsx')
# date_series = data.date
# data_close = data.pivot(index='date', columns='stock_id', values='close') #把stock_id欄位值變成新的欄位，並提出close當作欄位值，index為date
# data_y = process_obj.use_shift_to_get_new_columns(data_close, data_close.columns, 30, 'ratio')

# data_x = data.pivot(index='date', columns='stock_id', values=['Trading_Volume', 'spread_ratio']) #把stock_id欄位值變成新的欄位，並提出['Trading_Volume', 'spread_ratio']當作欄位值，index為date

# print(data_y.shape)
# print(data_x.shape)














# data = data_x.merge(data_y, on='date')
# data.to_excel(output_folder + '\\test.xlsx')
