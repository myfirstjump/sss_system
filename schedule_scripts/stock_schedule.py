import pymssql
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time
import logging
import lib.DB_SP as dbsp
import lib.line_push as push
import os

def STOCK_PRICE(grab_time = datetime.now()):
    parameter = {
        "dataset": "TaiwanStockPrice",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        logging.info('STOCK_PRICE workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data['spread_ratio'] = data['spread']/(data['close'] - data['spread'])*100
        data['spread_ratio'] = data['spread_ratio'].fillna(0)
        data['Trading_Volume']=data['Trading_Volume']/1000
        data_tuple = [tuple(row) for row in data.values]
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_SKILL_DB].[dbo].[TW_STOCK_PRICE_Daily] 
        (
               [date]
              ,[stock_id]
              ,[Trading_Volume]
              ,[Trading_money]
              ,[open]
              ,[max]
              ,[min]
              ,[close]
              ,[spread]
              ,[Trading_turnover]
              ,[spread_ratio]
        ) 
        VALUES(%s,%s,%d,%d,%d,%d,%d,%d,%d,%d,%d)"""
        , data_tuple
        )
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))

def PBRandPER(grab_time = datetime.now()):
    parameter = {
        "dataset": "TaiwanStockPER",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }

    resp = requests.get(url, params=parameter)
    data = resp.json()
        
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('PBRandPER workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_SKILL_DB].[dbo].[TW_STOCK_PER] 
        (
               [date]
              ,[stock_id]
              ,[dividend_yield]
              ,[PER]
              ,[PBR]
        ) 
        VALUES(%s,%s,%d,%d,%d)"""
        , data_tuple
        )
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('PBRandPER holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))

def LEGALPERSON(grab_time = datetime.now()):
    parameter = {
        "dataset": "TaiwanStockInstitutionalInvestorsBuySell",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.warning('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('TW_STOCK_LEGALPERSON_Daily fail',token)
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('LEGALPERSON workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_COUNTER_DB].[dbo].[TW_STOCK_LEGALPERSON_Daily] 
        (
               [date]
              ,[stock_id]
              ,[buy]
              ,[name]
              ,[sell]
        ) 
        VALUES(%s,%s,%d,%s,%d)"""
        , data_tuple
        )
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))


def STOCK_INFO(grab_time = datetime.now()):
    parameter = {
    "dataset": "TaiwanStockInfo",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.warning('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('STOCK_INFO fail',token)
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    data['insert_time'] = datetime.now()

    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('STOCK_INFO workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##先刪除資料
        # cursor.execute("truncate table [STOCK_SKILL_DB].[dbo].[TW_STOCK_INFO]")
        ##insert data to DB
        # print(data_tuple[0])
        cursor.executemany(
        """INSERT INTO [STOCK_SKILL_DB].[dbo].[TW_STOCK_INFO] 
        (
            [industry_category]
            ,[stock_id]
            ,[stock_name]
            ,[type]
            ,[date]
            ,[Insert_time]
        ) 
        VALUES(%s,%s,%d,%s,%s,%s)"""
        , data_tuple
        )
        conn.commit()
        print('success!')
    else:
        print('=========================================')
        print('holiday')
        logging.info('holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))

def StockMarginPurchaseShortSale(grab_time = datetime.now()):
    parameter = {
        "dataset": "TaiwanStockMarginPurchaseShortSale",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.ERROR('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('TW_STOCK_MARGINTRADE_SHORTSELL_Daily fail',token)
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('StockMarginPurchaseShortSale workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_COUNTER_DB].[dbo].[TW_STOCK_MARGINTRADE_SHORTSELL_Daily]
        (
               [date]
              ,[stock_id]
              ,[MarginPurchaseBuy]
              ,[MarginPurchaseCashRepayment]
              ,[MarginPurchaseLimit]
              ,[MarginPurchaseSell]
              ,[MarginPurchaseTodayBalance]
              ,[MarginPurchaseYesterdayBalance]
              ,[Note]
              ,[OffsetLoanAndShort]
              ,[ShortSaleBuy]
              ,[ShortSaleCashRepayment]
              ,[ShortSaleLimit]
              ,[ShortSaleSell]
              ,[ShortSaleTodayBalance]
              ,[ShortSaleYesterdayBalance]
        ) 
        VALUES(%s,%s,%d,%d,%d,%d,%d,%d,%s,%d,%d,%d,%d,%d,%d,%d)"""
        , data_tuple
        )
        logging.info('StockMarginPurchaseShortSale workday success : {}'.format(grab_time.strftime('%Y-%m-%d')))
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('TaiwanStockMarginPurchaseShortSale holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))

def MONTH_REVENUE(grab_time=datetime(datetime.now().year, datetime.now().month, 1)):
    parameter = {
        "dataset": "TaiwanStockMonthRevenue",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.ERROR('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('TW_STOCK_MonthRevenue fail',token)
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('MONTH_REVENUE workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        try:
            ##insert data to DB
            cursor.executemany(
            """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_MonthRevenue]
            (
                [date]
                ,[stock_id]
                ,[country]
                ,[revenue]
                ,[revenue_month]
                ,[revenue_year]
            ) 
            VALUES(%s,%s,%s,%d,%d,%d)"""
            , data_tuple
            )
            conn.commit()
        except:
            push.lineNotifyMessage('{}_MONTH_REVENUE_ERROR'.format(datetime.now()), token)
    else:
        print('=========================================')
        print('holiday')
        logging.info('holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))


def FinancialStatement(grab_time = datetime.now()):
    if grab_time.month >= 1 and grab_time.month <=3:
        grab_time = datetime(grab_time.year-1, 12,31)
    elif grab_time > datetime(grab_time.year, 4,1) and grab_time < datetime(grab_time.year, 5,16):
        grab_time = datetime(grab_time.year, 3,31)
    elif grab_time > datetime(grab_time.year, 7,1) and grab_time < datetime(grab_time.year, 8,16):
        grab_time = datetime(grab_time.year, 6,30)
    elif grab_time > datetime(grab_time.year, 10,1) and grab_time < datetime(grab_time.year, 11,16):
        grab_time = datetime(grab_time.year, 9,30)
    parameter = {
        "dataset": "TaiwanStockFinancialStatements",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.ERROR('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('TW_STOCK_FinancialStatements fail',token)
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('FinancialStatement workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##delete period data
        cursor.execute("delete from [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_FinancialStatements] where date = '{}'".format(grab_time.strftime('%Y-%m-%d')))
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_FinancialStatements]
        (
               [date]
              ,[stock_id]
              ,[type]
              ,[value]
              ,[origin_name]
        ) 
        VALUES(%s,%s,%s,%d,%s)"""
        , data_tuple
        )
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('FinancialStatements holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))



if __name__ == '__main__':
    logging.basicConfig(
    level = logging.DEBUG,
    filename = 'C:\\stock_schedule\\log\\{}.log'.format(datetime.now().strftime('%Y%m%d')),
    filemode = 'a',
    format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    conn = pymssql.connect(host='localhost', user = 'stock_search', password='1qazZAQ!', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)  

    url = "https://api.finmindtrade.com/api/v4/data"
    token = 'YGP4rPfKWCRVXe9hw4SISPbp1IITfbgCaWt5yirxT8C'

    dt = datetime.now()+ timedelta(days=0)
    STOCK_INFO(dt)
    STOCK_PRICE(dt)
    PBRandPER(dt)
    LEGALPERSON(dt)
    StockMarginPurchaseShortSale(dt)
    if datetime.now().day >= 11:
        MONTH_REVENUE()
    FinancialStatement(dt)
    dbsp.DB_SP_SCHDULE(conn,dt.strftime('%Y-%m-%d'))

    # push_stock
    message = '{}'.format(datetime.now().strftime('%Y%m%d'))
    cursor.execute("""select * from [STOCK_SKILL_DB].[dbo].[LINE_PUSH] order by LV""")
    push.lineNotifyMessage('\n1.三大皆買,量>10000,漲停\n2.外&投皆買,量>10000,漲停\n3.三大合買,量>10000,漲停\n4.量>10000,漲停\n5.量>10000,漲幅>5%')
    for row in cursor:
        message = message+'\n{} {} ({},{},{})'.format(row['stock_id'], row['stock_name'], row['LV'], row['stock_type'], row['industry_category'])
    
    push.lineNotifyMessage(message)
    
    logging.debug("weekdays Finish!")

