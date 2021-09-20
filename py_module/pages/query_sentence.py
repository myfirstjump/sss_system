# import pymssql
import datetime
from datetime import timedelta
from string import ascii_lowercase

# now = datetime.datetime.now()
# today = now.date()
# #print('今天 is :{}'.format(today))

# yesterday = today - timedelta(days=1)
# #print('yesterday is {}'.format(yesterday))

# #print('Now weekday: {}'.format(now.weekday()))
# #print('yesterday weekday: {}'.format(yesterday.weekday()))

# this_week_start = today - timedelta(days=now.weekday())
# #print('本周第一天: {}'.format(this_week_start))
# #print('this week start weekday: {}'.format(this_week_start.weekday()))

# #print('this month: {}'.format(now.month))
# this_month_start = datetime.datetime(today.year, today.month, 1).date()
# #print('本月第一天: {}'.format(this_month_start))

# quarter_start_month = (today.month - 1) - (today.month - 1) % 3 + 1
# #print('this quarter start month: {}'.format(quarter_start_month))
# this_quarter_start = datetime.datetime(today.year, quarter_start_month, 1).date()
# #print('本季第一天: {}'.format(this_quarter_start))

# this_year_start = datetime.datetime(today.year, 1, 1).date()
# #print('本年第一天: {}'.format(this_year_start))

# Query Combination
def query_combine(query_dict):
    query_number = len(query_dict)
    combined_query = "SELECT {}.stock_id, {}.stock_name FROM ".format(ascii_lowercase[query_number], ascii_lowercase[query_number])
    for num, query in query_dict.items():
        align_code = ascii_lowercase[num]
        if align_code == 'a':
            combined_query = combined_query + " {} {} inner join ".format(query, align_code)
        else:
            combined_query = combined_query + query + " {} on {}.stock_id = {}.stock_id inner join ".format(align_code, ascii_lowercase[num-1], align_code)
    combined_query = combined_query + "STOCK_SKILL_DB.dbo.TW_STOCK_INFO {} on {}.stock_id = {}.stock_id".format(ascii_lowercase[query_number], ascii_lowercase[query_number-1], ascii_lowercase[query_number])    
        
    return combined_query

# 最後查詢
def sql_execute(query):

    conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query))
    conn.commit()

    data = conn.fectchall()
    conn.close()
    return data

# 各項條件的string
def create_query_0201(today_date, larger, price):
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    query = "(SELECT stock_id FROM TW_STOCK_PRICE_Daily WHERE date= '{}' AND [close] {} {})".format(str(today_date), sign, str(price))
    return query

def create_query_0202(today_date, larger, price):
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    query = "(SELECT stock_id FROM TW_STOCK_PRICE_Daily WHERE date= '{}' AND [close] {} {})".format(str(today_date), sign, str(price))
    return query

def create_query_0203(today_date, direct, days):
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    query = "(SELECT stock_id FROM TW_STOCK_INFO WHERE date= '{}' AND limitup_limitdown_CNT {} {})".format(str(today_date), sign, str(days))
    return query

