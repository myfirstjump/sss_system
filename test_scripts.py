import pymssql
import datetime
from datetime import timedelta
from string import ascii_lowercase
import pandas as pd
import os

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

def create_query_index_monthly_data():

    query = '''
            SELECT * FROM STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Monthly WHERE date < '2022-01-01' AND stock_id IN  ('Automobile',
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
    '''

    return query


# ===== Query from DB後寫出檔案 =====
# data_query = create_query_index_monthly_data()
# data = sql_execute(data_query)

# data = pd.DataFrame.from_records(data)
# data.to_excel(folder_path + '\\TaiwanStockInfo_index_info.xlsx', index=False)
# print(data.head(50))
# ==================================


# ===== 統計資料 =====
data = pd.read_excel(folder_path + '\\TaiwanStockInfo_index_info.xlsx')

tmp = data["date"].astype(str).str.split("-", n = 2, expand = True)
data['date_month'] = tmp[1]

data = data.groupby(['stock_name', 'date_month'])['spread_ratio'].agg(['mean', 'std'])


print(data.tail(100))

data.to_excel(folder_path + '\\台股產業_各月份均值&標準差_2010-2021.xlsx')
# ==================================