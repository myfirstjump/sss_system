import requests
import pandas as pd
import time


my_token = 'your_token'
output_folder = "C:\\Datasets\\tw_stock\\info"

# today_date = time.strftime("%Y-%m-%d", time.gmtime()) # 過12點，用倫敦時間。
today_date = time.strftime("%Y-%m-%d") # 沒過12點，用本地時間。

print('\n1. 台股資訊')
'''
台股資訊包含：產業別、股票id、股票名稱、類型(上市Taiwan Stock Exchange(twse)、上櫃Taipei Exchange(tpex))
'''
url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockInfo",
    "token": my_token, # 參考登入，獲取金鑰
}
resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])

data.to_csv(output_folder + '\\111-02-05_TaiwanStockInfo.csv', index=False)