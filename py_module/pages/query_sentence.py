import pymssql
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
skill_info = 'STOCK_SKILL_DB.dbo.TW_STOCK_INFO'
skill_price_d = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Daily'
skill_price_w = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_Weekly'
skill_price_m = 'STOCK_SKILL_DB.dbo.TW_STOCK_PRICE_monthly'

# Query Combination
def query_combine(query_dict):
    query_number = len(query_dict)
    combined_query = "SELECT DISTINCT {}.stock_id, {}.stock_name FROM ".format(ascii_lowercase[query_number], ascii_lowercase[query_number])
    for num, query in query_dict.items():
        align_code = ascii_lowercase[num]
        if align_code == 'a':
            combined_query = combined_query + " {} {} inner join ".format(query, align_code)
        else:
            combined_query = combined_query + query + " {} on {}.stock_id = {}.stock_id inner join ".format(align_code, ascii_lowercase[num-1], align_code)
    combined_query = combined_query + "{} {} on {}.stock_id = {}.stock_id".format(skill_info, ascii_lowercase[query_number], ascii_lowercase[query_number-1], ascii_lowercase[query_number])    
        
    return combined_query

# 最後查詢
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

# 各項條件的string
def create_query_0201(larger, price):
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-(20))) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[close] {} {})'''.format(sign, str(price))

    return query

def create_query_0202(larger, price):
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-(20))) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[close] {} {})'''.format(sign, str(price))

    return query

def create_query_0203(direct, days):
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    if days < 0:
        days = -days
    
    query = '''(SELECT t1.stock_id, [close], t1.stock_name FROM {} t1 
    inner join (SELECT stock_id, MAX(date) as each_max_date FROM {} GROUP BY stock_id) t2
    on t2.stock_id = t1.stock_id AND limitup_limitdown_CNT {} {} 
    inner join {} t3 on t3.stock_id = t2.stock_id AND t2.each_max_date = t3.date)'''.format(skill_info, skill_price_d, sign, str(days), skill_price_d)

    return query

def create_query_0204(days, period, direct, percent):

    """0204 於[3][日]內[漲/跌幅]均超過[10]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread_ratio {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(days, days, sign, percent, days)

    return query

def create_query_0205(days, period, direct, percent):

    """0204 於[3][日]內[漲/跌幅]均超過[10]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(days, days, sign, percent, days)

    return query


def create_query_0301(days, period, direct, percent):

    """於[3][日]內，成交量平均[大於][50000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(days, days, sign, percent)

    return query

def create_query_0302(days, period, direct, percent):

    """於[3][日]內，成交量平均[小於][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(days, days, sign, percent)

    return query

def create_query_0303(days, period, direct, percent):

    """於[3][日]內，成交量[增加][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING SUM(part_tbl.Trading_Volume) {} {})
    '''.format(days, days, sign, percent, days)

    return query

def create_query_0304(days, period, direct, percent):

    """於[3][日]內，成交量[增加][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING SUM(part_tbl.Trading_Volume) {} {})
    '''.format(days, days, sign, percent, days)

    return query
    

    

def create_query_0305(days, period, direct, percent):

    """0305 於[3][日]內，成交量[增加][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING SUM(part_tbl.Trading_spread_ratio) {} {})
    '''.format(days, days, sign, percent, days)

    return query


def create_query_0306(days, period, direct, percent):

    """0305 於[3][日]內，成交量[減少][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+20))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING SUM(part_tbl.Trading_spread_ratio) {} {})
    '''.format(days, days, sign, percent, days)

    return query
