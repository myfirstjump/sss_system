import pymssql





# 各項條件的string
def create_query_0201(today_date, sign_value, price):

    if sign_value == 1:
        sign = '>='
    elif sign_value == -1:
        sign = '<'
    else:
        return None
    query = "SELECT stock_id FROM TW_STOCK_PRICE_Daily WHERE date=[today_date] AND close >= [120]".format(today_date, sign, price)
    return 



# 最後查詢
def final_query(arg):
    conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)


conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
cursor = conn.cursor(as_dict=True)
result = cursor.execute('SELECT * FROM STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Daily WHERE stock_id = "2330"')
print(result)