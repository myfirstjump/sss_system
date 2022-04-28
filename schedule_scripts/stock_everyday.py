import pymssql
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time
import logging
import lib.DB_SP as dbsp


def StockDividend(grab_time = datetime.now()):
    ##delete period data
    cursor.execute("delete from [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_Dividend] where date >= '{}'".format(grab_time.strftime('%Y-%m-%d')))
        
    for i in range(90):
        parameter = {
            "dataset": "TaiwanStockDividend",
            "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
        }
        try:
            resp = requests.get(url, params=parameter)
            data = resp.json()
        except:
            time.sleep(10)
            logging.ERROR('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
            print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
            resp = requests.get(url, params=parameter)
            data = resp.json()
        data = pd.DataFrame(data["data"])
        if len(data) != 0:
            print('=========================================')
            print('workday')
            logging.info('StockDividend workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
            data_tuple = [tuple(row) for row in data.values]
            
            ##insert data to DB
            cursor.executemany(
            """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_Dividend]
            (
                [date]
                ,[stock_id]
                ,[belong_year]
                ,[StockEarningsDistribution]
                ,[StockStatutorySurplus]
                ,[StockExDividendTradingDate]
                ,[TotalEmployeeStockDividend]
                ,[TotalEmployeeStockDividendAmount]
                ,[RatioOfEmployeeStockDividendOfTotal]
                ,[RatioOfEmployeeStockDividend]
                ,[CashEarningsDistribution]
                ,[CashStatutorySurplus]
                ,[CashExDividendTradingDate]
                ,[CashDividendPaymentDate]
                ,[TotalEmployeeCashDividend]
                ,[TotalNumberOfCashCapitalIncrease]
                ,[CashIncreaseSubscriptionRate]
                ,[CashIncreaseSubscriptionpRrice]
                ,[RemunerationOfDirectorsAndSupervisors]
                ,[ParticipateDistributionOfTotalShares]
                ,[AnnouncementDate]
                ,[AnnouncementTime]
            ) 
            VALUES(%s,%s,%s,%d,%d,%s,%d,%d,%d,%d,%d,%d,%s,%s,%d,%d,%d,%d,%d,%d,%s,%s)"""
            , data_tuple
            )
            logging.info('StockDividend workday success : {}'.format(grab_time.strftime('%Y-%m-%d')))
            conn.commit()
        else:
            print('=========================================')
            print('holiday')
            logging.info('Ndata : {}'.format(grab_time.strftime('%Y-%m-%d')))
        grab_time = grab_time + timedelta(days=1)


def HOLDRANGE(grab_time = datetime.now() + timedelta(days=-2)):
    parameter = {
        "dataset": "TaiwanStockHoldingSharesPer",
        "start_date": "{}".format(grab_time.strftime('%Y-%m-%d')),
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNy0zMSAxMjo0ODoxOCIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.rIEjxbGHjaMYjhP4CZBwQu1wyvkNiGnUryeFACyqq9o", # 參考登入，獲取金鑰
    }
    try:
        resp = requests.get(url, params=parameter)
        data = resp.json()
    except:
        time.sleep(10)
        logging.ERROR('date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        print('ERROR {}'.format(grab_time.strftime('%Y-%m-%d')))
        resp = requests.get(url, params=parameter)
        data = resp.json()
    data = pd.DataFrame(data["data"])
    if len(data) != 0:
        print('=========================================')
        print('workday')
        logging.info('TW_STOCK_HOLDRANGE workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        data_tuple = [tuple(row) for row in data.values]
        ##insert data to DB
        cursor.executemany(
        """INSERT INTO [STOCK_COUNTER_DB].[dbo].[TW_STOCK_HOLDRANGE] 
        (
               [date]
              ,[stock_id]
              ,[HoldingSharesLevel]
              ,[people]
              ,[percent]
              ,[unit]
        ) 
        VALUES(%s,%s,%s,%d,%d,%d)"""
        , data_tuple
        )
        conn.commit()
    else:
        print('=========================================')
        print('holiday')
        logging.info('HOLDRANGE Ndata : {}'.format(grab_time.strftime('%Y-%m-%d')))



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

    logging.debug("EveryDay Begin!")
    dt = datetime.now()
    try:
        StockDividend(dt)
    except:
        logging.error('StockDividend')
        push.lineNotifyMessage('StockDividend fail',token)
    try:
        HOLDRANGE(dt+ timedelta(days=-2))
    except:
        logging.error('HOLDRANGE')
        push.lineNotifyMessage('HOLDRANGE fail',token)
    dbsp.DB_SP_EVERYDAY(conn)
    logging.debug("EveryDay Finish!")