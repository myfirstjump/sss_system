# import pymssql
import datetime
from datetime import timedelta

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



# 各項條件的string
def create_query_0201(today_date, larger, price):
    if larger == 1:
        sign = '>='
    else:
        sign = '<'
    
    query = "SELECT stock_id FROM TW_STOCK_PRICE_Daily WHERE date=" + "'" + str(today_date) + "'" + "AND close" + sign + str(price)
    return query


# # 最後查詢
# def final_query(arg):
#     conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
#     cursor = conn.cursor(as_dict=True)


# conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
# cursor = conn.cursor(as_dict=True)
# cursor.execute('SELECT * FROM TW_STOCK_PRICE_Daily WHERE stock_id = "2330"')

# for row in cursor:
#     #print(row)