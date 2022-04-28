import pymssql
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time
import logging
import requests
import json
import lib.DB_SP as dbsp
import lib.line_push as push


def Crawl_STOCK_LOANSHARE(grab_time = datetime.now()+ timedelta(days=-1)):
    url = "http://www.twse.com.tw/exchangeReport/TWT72U"
    headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
    'referer': "http://www.twse.com.tw/zh/page/trading/exchange/TWT72U.html",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-TW,zh-CN;q=0.8,zh;q=0.6,en-US;q=0.4,en;q=0.2",
    'cookie': "JSESSIONID=8688F6ED6AD677B886011F56B3E86D0E; _ga=GA1.3.1953932169.1504347589; _gid=GA1.3.981495820.1505442422",
    'cache-control': "no-cache",
    'postman-token': "6790b24b-e9c5-61ac-5eea-f8ee81d4204e"
    }

    querystring = { "response": "json", "date": "{}".format(grab_time.strftime('%Y%m%d')), "selectType": "SLBNLB", "_": "1505545708340" }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        obj = json.loads(response.text)
    except:
        logging.ERROR('STOCK_LOANSHARE date error : _{}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('CRAWL STOCK_LOANSHARE fail',token)
    if len(obj) > 1:
        data = pd.DataFrame(obj['data'], columns=['stock_id','date','LoanBalance_yesterday','LOANSHARE','RepaySHARE','LoanBalance','STOCK_PRICE','LoanBalanceValue','market'])
        data['date'] = grab_time.strftime('%Y-%m-%d')
        data = data.drop(index=[len(data)-1, len(data)-2, len(data)-3])
        data['LoanBalance_yesterday'] = data['LoanBalance_yesterday'].str.replace(',','')
        data['LOANSHARE'] = data['LOANSHARE'].str.replace(',','')
        data['RepaySHARE'] = data['RepaySHARE'].str.replace(',','')
        data['LoanBalance'] = data['LoanBalance'].str.replace(',','')
        data['LoanBalanceValue'] = data['LoanBalanceValue'].str.replace(',','')
        data['STOCK_PRICE'] = data['STOCK_PRICE'].str.replace(',','')
        data['STOCK_PRICE'] = data['STOCK_PRICE'].astype(float)
        print('=========================================')
        print('workday')
        print(grab_time)
        try:
            logging.info('STOCK_LOANSHARE workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
            data_tuple = [tuple(row) for row in data.values]
            ##insert data to DB
            cursor.executemany(
            """INSERT INTO [STOCK_COUNTER_DB].[dbo].[TW_STOCK_LOANSHARE_Daily]
            (
                [stock_id]
                ,[date]
                ,[LoanBalance_yesterday]
                ,[LOANSHARE]
                ,[RepaySHARE]
                ,[LoanBalance]
                ,[STOCK_PRICE]
                ,[LoanBalanceValue]
                ,[market]
            ) 
            VALUES(%s,%s,%d,%d,%d,%d,%d,%d,%s)"""
            , data_tuple
            )
            conn.commit()
        except:
            logging.ERROR('INSERT STOCK_LOANSHARE FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
            push.lineNotifyMessage('INSERT STOCK_LOANSHARE fail',token)
    else:
        print('=========================================')
        print('holiday')
        print(grab_time)
        logging.info('STOCK_LOANSHARE holiday : {}'.format(grab_time.strftime('%Y-%m-%d')))

def Crawl_PCHOME(grab_time = datetime.now()):
    url_findme = "https://api.finmindtrade.com/api/v4/data"
    parameter = {
        "dataset": "TaiwanStockInfo",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wOC0wNSAxNDoyMDo1MiIsInVzZXJfaWQiOiJoZ2RmbWpnMjcxNSIsImlwIjoiMTIyLjE0Ny4xMzEuMiJ9.HZoGerzvLgYwmKH8l3E5NXMw0qE-IKimJI8YGzXsByc", # 參考登入，獲取金鑰
    }
    resp = requests.get(url_findme, params=parameter)
    data_findme = resp.json()
    data_findme = pd.DataFrame(data_findme["data"])

    mask1 = data_findme['industry_category'].isin(['水泥工業', '其他',
        '食品工業', '電器電纜', '農業科技業', '觀光事業', '塑膠工業', '建材營造', '汽車工業', '電子零組件類',
        '紡織纖維', '貿易百貨', '電子工業', '電子零組件業', '電機機械', '生技醫療類', '電腦及週邊類',
        '化學生技醫療', '生技醫療業', '化學工業', '其他電子類', '玻璃陶瓷', '造紙工業', '鋼鐵工業', '橡膠工業',
        '航運業', '電腦及週邊設備業', '半導體業', '其他電子業', '通信網路業', '光電業', '電子通路業',
        '資訊服務業', '油電燃氣業', '金融保險', '文化創意業', '光電業類', '半導體類', '通信網路類',
        '電子商務業', '資訊服務類', '電子通路類', '金融業', '油電燃氣類'])
    stock_id = data_findme[mask1]['stock_id'].unique()
    stock_id_all = data_findme['stock_id'].unique()

    # 股本
    insert_data = []
    try:
        for i in stock_id:
            url = "https://pchome.megatime.com.tw/stock/sto3/sid{}.html".format(i)
            data = {
                'is_check':'1'
            }
            response = requests.post(url = url,data=data)
            if '查無此股票代號!' in response.text:
                continue
            temp = pd.read_html(response.text)
            data = temp[1]
            data.index = data[0]
            insert_data.append([i,data.loc['資本額(仟元)',1]])

        capital_data = pd.DataFrame(insert_data, columns=['stock_id', 'Capital'])
        data_tuple = [tuple(row) for row in capital_data.values]
        cursor.execute("truncate table [STOCK_SKILL_DB].[dbo].[TW_STOCK_CAPITAL]")
        logging.info('TW_STOCK_CAPITAL workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        cursor.executemany(
        """INSERT INTO [STOCK_SKILL_DB].[dbo].[TW_STOCK_CAPITAL] 
        (
            [stock_id]
            ,[Capital]
        ) 
        VALUES(%s,%d)"""
        , data_tuple
        )
    except:
        logging.ERROR('TW_STOCK_CAPITAL FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('CRAWL TW_STOCK_CAPITAL fail',token)
    time.sleep(60)

    # 董監持股
    try:
        Director_Supervisor_data = pd.DataFrame(columns=['Identity', 'Name', 'Past_share', 'Now_share', 'share_ratio', 'Pledge_number', 'Pledge_ratio', 'stock_id'])
        for i in stock_id:
            url = "https://pchome.megatime.com.tw/stock/sto1/ock3/sid{}.html".format(i)
            data = {
                'is_check':'1'
            }
            response = requests.post(url = url,data=data)
            if '查無此股票代號!' in response.text:
                continue
            temp = pd.read_html(response.text)
            data = temp[1]
            data.drop([7],axis=1, inplace = True)
            data.columns = ['Identity', 'Name', 'Past_share', 'Now_share', 'share_ratio', 'Pledge_number', 'Pledge_ratio']
            data.drop([0,1], inplace = True)
            if len(data) < 2:
                continue
            data['stock_id'] = i
            Director_Supervisor_data = Director_Supervisor_data.append(data,ignore_index=True)
                

        Director_Supervisor_data = Director_Supervisor_data.drop_duplicates()
        Director_Supervisor_data['Pledge_ratio'] = Director_Supervisor_data['Pledge_ratio'].str.replace('－','0')
        data_tuple = [tuple(row) for row in Director_Supervisor_data.values]
        cursor.execute("truncate table [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_Director_Supervisor]")
        logging.info('TW_STOCK_Director_Supervisor workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        cursor.executemany(
        """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_Director_Supervisor] 
        (
            [ID]
            ,[Name]
            ,[Past_share]
            ,[Now_share]
            ,[share_ratio]
            ,[Pledge_number]
            ,[Pledge_ratio]
            ,[stock_id]
        ) 
        VALUES(%s,%s,%d,%d,%d,%d,%d,%s)"""
        , data_tuple
        )
    except:
        logging.info('TW_STOCK_Director_Supervisor FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('CRAWL TW_STOCK_Director_Supervisor fail',token)

    time.sleep(60)

    # 股票資訊
    if datetime.now().strftime('%m%d') not in ('0331','0401', '0402', '0515','0516','0517','0814','0815','0816','1114','1115','1116'):
        return 0
    if int((grab_time.month-1)/3+1) == 1:
        crawl_year = grab_time.year - 1
        crawl_month = 4
    else:
        crawl_year = grab_time.year
        crawl_month = int((grab_time.month-1)/3+1) - 1
    Info_data = pd.DataFrame(columns=['date','Gross_Profit_Margin','Operating_Profit_Margin','PreTax_Income_Margin','AfterTax_Income_Margin'
               ,'PER_STOCK_PRICE','PER_STOCK_Margin','PER_STOCK_Profit','PER_STOCK_Debt','PER_STOCK_CashFlow'
               ,'PER_STOCK_PreTax','PER_STOCK_AfterTax','PreTax_Return', 'After_Return','Total_Return','Income_growth'
               ,'Profit_Growth','PreTax_Growth','FixAsset_Growth','Current_Rate','Quick_Rate','Debt_Rate'
               ,'Accounts_Receivable_Turnover_Rate','Inventory_Turnover','FixAsset_Turnover','Per_Person_Income'
               ,'Per_Person_Profit','LongTerm_Fund_FixAsset_Rate','Cash_Current_Rate','Allowable_Cash_Flow_Rate'
               ,'Cash_Reinvestment_Rate','Interest_Coverage_Rate','stock_id']) 
    try:
        for i in stock_id:
            url = "https://pchome.megatime.com.tw/stock/sto2/ock2/{}{}/sid{}.html".format(crawl_year,crawl_month,i)
            data = {
                'is_check':'1'
            }
            response = requests.post(url = url,data=data)
            if '查無此股票代號!' in response.text:
                continue
            temp = pd.read_html(response.text)
            data = temp[1]
            if len(data) < 15:
                continue
            data.drop([0,1,2], inplace=True)
            data.drop([0,1],axis=1,inplace = True)
            data = data.T
            data[3] = data[3].str.replace('年第1季','-01-01')
            data[3] = data[3].str.replace('年第2季','-04-01')
            data[3] = data[3].str.replace('年第3季','-07-01')
            data[3] = data[3].str.replace('年第4季','-10-01')
            data.columns = ['date','Gross_Profit_Margin','Operating_Profit_Margin','PreTax_Income_Margin','AfterTax_Income_Margin'
                    ,'PER_STOCK_PRICE','PER_STOCK_Margin','PER_STOCK_Profit','PER_STOCK_Debt','PER_STOCK_CashFlow'
                    ,'PER_STOCK_PreTax','PER_STOCK_AfterTax','PreTax_Return', 'After_Return','Total_Return','Income_growth'
                    ,'Profit_Growth','PreTax_Growth','FixAsset_Growth','Current_Rate','Quick_Rate','Debt_Rate'
                    ,'Accounts_Receivable_Turnover_Rate','Inventory_Turnover','FixAsset_Turnover','Per_Person_Income'
                    ,'Per_Person_Profit','LongTerm_Fund_FixAsset_Rate','Cash_Current_Rate','Allowable_Cash_Flow_Rate'
                    ,'Cash_Reinvestment_Rate','Interest_Coverage_Rate']

            data['stock_id'] = i
            Info_data = Info_data.append(data.iloc[0,:],ignore_index=True)
    except:
        logging.ERROR('TW_STOCK_FinancialStatements_Detail FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('CRAWL TW_STOCK_FinancialStatements_Detail fail',token)
        return 0 
    
    try:
        Info_data = Info_data.replace('-','0')    
        data_tuple = [tuple(row) for row in Info_data.values]
        logging.info('TW_STOCK_FinancialStatements_Detail workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        cursor.executemany(
        """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_FinancialStatements_Detail] 
        (
            [date]
            ,[Gross_Profit_Margin]
            ,[Operating_Profit_Margin]
            ,[PreTax_Income_Margin]
            ,[AfterTax_Income_Margin]
            ,[PER_STOCK_PRICE]
            ,[PER_STOCK_Margin]
            ,[PER_STOCK_Profit]
            ,[PER_STOCK_Debt]
            ,[PER_STOCK_CashFlow]
            ,[PER_STOCK_PreTax]
            ,[PER_STOCK_AfterTax]
            ,[PreTax_Return]
            ,[After_Return]
            ,[Total_Return]
            ,[Income_growth]
            ,[Profit_Growth]
            ,[PreTax_Growth]
            ,[FixAsset_Growth]
            ,[Current_Rate]
            ,[Quick_Rate]
            ,[Debt_Rate]
            ,[Accounts_Receivable_Turnover_Rate]
            ,[Inventory_Turnover]
            ,[FixAsset_Turnover]
            ,[Per_Person_Income]
            ,[Per_Person_Profit]
            ,[LongTerm_Fund_FixAsset_Rate]
            ,[Cash_Current_Rate]
            ,[Allowable_Cash_Flow_Rate]
            ,[Cash_Reinvestment_Rate]
            ,[Interest_Coverage_Rate]
            ,[stock_id]
        ) 
        VALUES(%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%s)"""
        , data_tuple
        )
        conn.commit()
    except:
        logging.info('Insert TW_STOCK_FinancialStatements_Detail FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('INSERT TW_STOCK_FinancialStatements_Detail fail',token)
        return 0 

    # 股票資訊_year
    if datetime.now().strftime('%m%d') not in ('0410','0411','0412'):
        return 0
    Info_data_year = pd.DataFrame(columns=['date','Gross_Profit_Margin','Operating_Profit_Margin','PreTax_Income_Margin','AfterTax_Income_Margin'
               ,'PER_STOCK_PRICE','PER_STOCK_Margin','PER_STOCK_Profit','PER_STOCK_Debt','PER_STOCK_CashFlow'
               ,'PER_STOCK_PreTax','PER_STOCK_AfterTax','PreTax_Return', 'After_Return','Total_Return','Income_growth'
               ,'Profit_Growth','PreTax_Growth','FixAsset_Growth','Current_Rate','Quick_Rate','Debt_Rate'
               ,'Accounts_Receivable_Turnover_Rate','Inventory_Turnover','FixAsset_Turnover','Per_Person_Income'
               ,'Per_Person_Profit','LongTerm_Fund_FixAsset_Rate','Cash_Current_Rate','Allowable_Cash_Flow_Rate'
               ,'Cash_Reinvestment_Rate','Interest_Coverage_Rate','stock_id']) 
    try:
        for i in stock_id:
            url = "https://pchome.megatime.com.tw/stock/sto2/ock6/sid{}.html".format(i)
            data = {
                'is_check':'1'
            }
            response = requests.post(url = url,data=data)
            if '查無此股票代號!' in response.text:
                continue
            temp = pd.read_html(response.text)
            data = temp[1]
            if len(data) < 15:
                continue
            data.drop([0,1,2], inplace=True)
            data.drop([0,1],axis=1,inplace = True)
            data = data.T
            data[3] = data[3].str.replace('年','-01-01')
            data.columns = ['date','Gross_Profit_Margin','Operating_Profit_Margin','PreTax_Income_Margin','AfterTax_Income_Margin'
                    ,'PER_STOCK_PRICE','PER_STOCK_Margin','PER_STOCK_Profit','PER_STOCK_Debt','PER_STOCK_CashFlow'
                    ,'PER_STOCK_PreTax','PER_STOCK_AfterTax','PreTax_Return', 'After_Return','Total_Return','Income_growth'
                    ,'Profit_Growth','PreTax_Growth','FixAsset_Growth','Current_Rate','Quick_Rate','Debt_Rate'
                    ,'Accounts_Receivable_Turnover_Rate','Inventory_Turnover','FixAsset_Turnover','Per_Person_Income'
                    ,'Per_Person_Profit','LongTerm_Fund_FixAsset_Rate','Cash_Current_Rate','Allowable_Cash_Flow_Rate'
                    ,'Cash_Reinvestment_Rate','Interest_Coverage_Rate']

            data['stock_id'] = i
            if '{}'.format(grab_time.year-1) not in data.iloc[0,0]:
                continue
            Info_data_year = Info_data_year.append(data.iloc[0,:],ignore_index=True)
    except:
        logging.ERROR('TW_STOCK_FinancialStatements_Detail_Yearly FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('CRAWL TW_STOCK_FinancialStatements_Detail_Yearly fail',token)
        return 0 
    
    try:
        Info_data_year = Info_data_year.replace('-','0')    
        data_tuple = [tuple(row) for row in Info_data_year.values]
        logging.info('TW_STOCK_FinancialStatements_Detail_Yearly workday : {}'.format(grab_time.strftime('%Y-%m-%d')))
        cursor.executemany(
        """INSERT INTO [STOCK_BASICINTO_DB].[dbo].[TW_STOCK_FinancialStatements_Detail_Yearly] 
        (
            [date]
            ,[Gross_Profit_Margin]
            ,[Operating_Profit_Margin]
            ,[PreTax_Income_Margin]
            ,[AfterTax_Income_Margin]
            ,[PER_STOCK_PRICE]
            ,[PER_STOCK_Margin]
            ,[PER_STOCK_Profit]
            ,[PER_STOCK_Debt]
            ,[PER_STOCK_CashFlow]
            ,[PER_STOCK_PreTax]
            ,[PER_STOCK_AfterTax]
            ,[PreTax_Return]
            ,[After_Return]
            ,[Total_Return]
            ,[Income_growth]
            ,[Profit_Growth]
            ,[PreTax_Growth]
            ,[FixAsset_Growth]
            ,[Current_Rate]
            ,[Quick_Rate]
            ,[Debt_Rate]
            ,[Accounts_Receivable_Turnover_Rate]
            ,[Inventory_Turnover]
            ,[FixAsset_Turnover]
            ,[Per_Person_Income]
            ,[Per_Person_Profit]
            ,[LongTerm_Fund_FixAsset_Rate]
            ,[Cash_Current_Rate]
            ,[Allowable_Cash_Flow_Rate]
            ,[Cash_Reinvestment_Rate]
            ,[Interest_Coverage_Rate]
            ,[stock_id]
        ) 
        VALUES(%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%s)"""
        , data_tuple
        )
        conn.commit()
    except:
        logging.info('Insert TW_STOCK_FinancialStatements_Detail_Yearly FAIL : {}'.format(grab_time.strftime('%Y-%m-%d')))
        push.lineNotifyMessage('Insert TW_STOCK_FinancialStatements_Detail_Yearly fail',token)
        return 0 



if __name__ == '__main__':
    logging.basicConfig(
    level = logging.DEBUG,
    filename = '.\\log\\{}.log'.format(datetime.now().strftime('%Y%m%d')),
    filemode = 'a',
    format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    token = 'YGP4rPfKWCRVXe9hw4SISPbp1IITfbgCaWt5yirxT8C'
    logging.debug("Crawl Begin!")
    dt = datetime.now()+ timedelta(days=0)
    conn = pymssql.connect(host='localhost', user = 'crawler', password='!QAZ@WSX', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)
    try:  
        Crawl_STOCK_LOANSHARE()
    except:
        logging.error('Crawl_STOCK_LOANSHARE')
        push.lineNotifyMessage('Crawl_STOCK_LOANSHARE fail',token)
    try:  
        Crawl_PCHOME()
    except:
        logging.error('Crawl_PCHOME')
        push.lineNotifyMessage('Crawl_PCHOME fail',token)

    dbsp.DB_SP_CRAWL(conn)
    logging.debug("Crawl Finish!")

