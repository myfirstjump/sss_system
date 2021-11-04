import pymssql
import datetime
from datetime import timedelta
from string import ascii_lowercase

            # now = datetime.datetime.now()
            # today = now.date()
            # yesterday = today - timedelta(days=1)
            # this_week_start = today - timedelta(days=now.weekday())
            # this_month_start = datetime.datetime(today.year, today.month, 1).date()
            # quarter_start_month = (today.month - 1) - (today.month - 1) % 3 + 1
            # this_quarter_start = datetime.datetime(today.year, quarter_start_month, 1).date()
            # this_year_start = datetime.datetime(today.year, 1, 1).date()

skill_info = 'STOCK_SKILL_DB.dbo.TW_STOCK_INFO'
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
counter_legal_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LEGALPERSON_Daily'
counter_margin_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_MARGINTRADE_SHORTSELL_Daily'
counter_loanshare_d = 'STOCK_COUNTER_DB.dbo.TW_STOCK_LOANSHARE_Daily'


# Query Combination
def query_combine(query_dict):
    query_number = len(query_dict)
    combined_query = "SELECT {}.stock_id, {}.stock_name, {}.industry_category, {}.type FROM ".format(ascii_lowercase[query_number], ascii_lowercase[query_number], ascii_lowercase[query_number], ascii_lowercase[query_number])
    for num, query in query_dict.items():
        align_code = ascii_lowercase[num]
        if align_code == 'a':
            combined_query = combined_query + " {} {} inner join ".format(query, align_code)
        else:
            combined_query = combined_query + query + " {} on {}.stock_id = {}.stock_id inner join ".format(align_code, ascii_lowercase[num-1], align_code)
    combined_query = combined_query + "{} {} on {}.stock_id = {}.stock_id".format(skill_info, ascii_lowercase[query_number], ascii_lowercase[query_number-1], ascii_lowercase[query_number])    
        
    if query_number == 0: # 例外處理
        combined_query = "SELECT * FROM {} WHERE type = 'no'".format(skill_info)

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
def create_query_0101(cate_str):
    # if type(cate_str) == str:
    #     cate_str = "('" + cate_str + "')"
    # else:
    #     cate_str = tuple(cate_str)
    
    # query = '''(SELECT stock_id FROM {} WITH(NOLOCK) WHERE industry_category IN {})'''.format(skill_info, cate_str)
    if len(cate_str) == 1:
        cate_str = str(cate_str)
        cate_str = cate_str.replace('[', '(')
        cate_str = cate_str.replace(']', ')')
    else:
        cate_str = tuple(cate_str)
    query = '''(SELECT stock_id FROM {} WITH(NOLOCK) WHERE industry_category IN {})'''.format(skill_info, cate_str)
    return query 

def create_query_0102(larger, price):
    '''公司股本(大於/小於)(100)億元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        
    price = price * 100000

    query = '''(SELECT stock_id FROM STOCK_SKILL_DB.dbo.TW_STOCK_CAPITAL WHERE Capital {} {})'''.format(sign, price)
    
    return query

def create_query_0103(larger, price):
    '''公司股本(大於/小於)(100)億元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        
    price = price * 100000

    query = '''(SELECT stock_id FROM STOCK_SKILL_DB.dbo.TW_STOCK_CAPITAL WHERE Capital {} {})'''.format(sign, price)
    
    return query

def create_query_0104(larger, ratio):
    '''董監持股比例(大於)(50)%之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id FROM (SELECT stock_id, AVG(share_ratio) new_share_ratio FROM {} 
            GROUP BY stock_id, name) t1
            GROUP BY stock_id HAVING SUM(new_share_ratio) {} {})'''.format(basic_info_supervisor, sign, ratio)

    return query

def create_query_0105(larger, ratio):
    '''董監質押比例(大於)(10)%之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id FROM (SELECT stock_id, AVG(pledge_ratio) new_pledge_ratio FROM {} 
            GROUP BY stock_id, name) t1
            GROUP BY stock_id HAVING SUM(new_pledge_ratio) {} {})'''.format(basic_info_supervisor, sign, ratio)

    return query

def create_query_0106(larger, price):
    '''0106 每股淨值(大於)(10)元之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND PER_STOCK_PRICE {} {})
    '''.format(basic_info_finDetail_q, sign, price)
    return query

def create_query_0107(numbers, larger, amount):
    '''0107 (3)年內平均ROE(大於)(10)%'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(after_return) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query

def create_query_0108(numbers, larger, percent):
    '''0108 ROE連續(3)年(成長/衰退)(5)%以上'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        percent = -percent
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {} AND after_return_last_year_ratio {} {}
    GROUP BY stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)
    return query

def create_query_0109(numbers, larger, amount):
    '''0109 (3)年內平均ROA(大於)(10)%'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(total_return) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query 

def create_query_0110(numbers, larger, percent):
    '''0110 ROA連續(3)年(成長/衰退)(5)%以上'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        percent = -percent
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {} AND total_return_last_year_ratio {} {}
    GROUP BY stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)
    return query

def create_query_0111(numbers, period, larger, amount):
    '''0111 上(2)(季/年)平均EPS(大於)(10)'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    if period == 'y':
        ref_table = basic_info_finState_y
    else:
        ref_table = basic_info_finState_q

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM (SELECT * FROM {} WITH(NOLOCK) where [type]='EPS') t1) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(value) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query 

def create_query_0112(numbers, period, direct, percent):

    """0112 EPS連續(3)(季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finState_y
    else:
        ref_table = basic_info_finState_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.last_period_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, numbers, sign, percent)

    return query


def create_query_0113(period, direct, percent):

    """0113 上(季/年)EPS較去年同期(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finState_y
    else:
        ref_table = basic_info_finState_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, sign, percent)

    return query

def create_query_0114(number, period, direct, percent):

    """0114 上(2)(季/年)平均存貨週轉率(大於)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Inventory_Turnover) {} {})
    '''.format(ref_table, number, sign, percent)

    return query



    
def create_query_0115(period, direct, percent):

    """0115 (季/年)存貨週轉率(成長/衰退)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        ref_column = 'Inventory_Turnover_last_year_ratio'
    else:
        ref_table = basic_info_finDetail_q
        ref_column = 'Inventory_Turnover_last_quarter_ratio'

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_table, ref_column, sign, percent)

    return query

def create_query_0116(number, period, direct, percent):

    """0116 上(2)(季/年)平均應收帳款週轉率(大於)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Accounts_Receivable_Turnover_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query

def create_query_0117(period, direct, percent):

    """0117 (季/年)應收帳款週轉率(成長/衰退)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        ref_column = 'Accounts_Receivable_Turnover_Rate_last_year_ratio'
    else:
        ref_table = basic_info_finDetail_q
        ref_column = 'Accounts_Receivable_Turnover_Rate_last_quarter_ratio'

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_table, ref_column, sign, percent)

    return query

def create_query_0118(number, period, direct, percent):

    """0118 上(2)(季/年)平均流動比率(大於)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Current_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query

def create_query_0119(period, direct, percent):

    """0119 (季/年)流動比率(成長/衰退)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        ref_column = 'Current_Rate_last_year_ratio'
    else:
        ref_table = basic_info_finDetail_q
        ref_column = 'Current_Rate_last_quarter_ratio'

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_table, ref_column, sign, percent)

    return query

def create_query_0120(number, period, direct, percent):

    """0120 上(2)(季/年)平均速動比率(大於)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Quick_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query

def create_query_0121(period, direct, percent):

    """0121 (季/年)速動比率(成長/衰退)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        ref_column = 'Quick_Rate_last_year_ratio'
    else:
        ref_table = basic_info_finDetail_q
        ref_column = 'Quick_Rate_last_quarter_ratio'

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_table, ref_column, sign, percent)

    return query

def create_query_0122(number, period, direct, percent):

    """0122 上(2)(季/年)平均負債比率(大於)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Debt_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query

def create_query_0123(period, direct, percent):

    """0123 (季/年)負債比率(成長/衰退)(10)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        ref_column = 'Debt_Rate_last_year_ratio'
    else:
        ref_table = basic_info_finDetail_q
        ref_column = 'Debt_Rate_last_quarter_ratio'

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_table, ref_column, sign, percent)

    return query

def create_query_0124(number, distribution_type, all_avg, direct, price):

    """0124 (3)年內(現金股利/股票股利)(皆/平均)(大於)(10)元"""

    if distribution_type == '2':
        ref_column = 'StockEarningsDistribution'
    else:
        ref_column = 'CashEarningsDistribution'

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    ref_table = basic_info_dividend

    if all_avg == '1':
        query = '''
        (SELECT stock_id FROM
        (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
        FROM {} WITH(NOLOCK)) part_tbl
        WHERE part_tbl.row_num <= {} AND {} {} {}
        GROUP BY stock_id HAVING COUNT(row_num) = {})
        '''.format(ref_table, number, ref_column, sign, price, number)
    else:
        query = '''
        (SELECT stock_id FROM
        (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
        FROM {} WITH(NOLOCK)) part_tbl
        WHERE part_tbl.row_num <= {}
        GROUP BY stock_id HAVING AVG({}) {} {})
        '''.format(ref_table, number, ref_column, sign, price)

    return query


def create_query_0201(larger, price):
    '''0201 公司股價[大於][120]元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM TW_STOCK_PRICE_Daily WITH(NOLOCK)
    WHERE date > (GETDATE()-(10))) part_tbl
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
    WHERE date > (GETDATE()-(10))) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[close] {} {})'''.format(sign, str(price))

    return query

def create_query_0203(direct, days):
    if direct == '1':
        sign = '>='
    else:
        sign = '<='  
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
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread_ratio {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query

def create_query_0205(days, period, direct, percent):

    """於[3][日]內[上漲/下跌][超過][20]元之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

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
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(skill_price_d, days, days, sign, percent)

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
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(skill_price_d, days, days, sign, percent)

    return query

def create_query_0303(days, period, direct, lot):

    """於[3][日]內，成交量均[增加][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    # lot = lot * 1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_Volume {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, lot, days)


    return query

def create_query_0304(days, period, direct, lot):

    """0304 於[3][日]內，成交量均[減少][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    # lot = lot * 1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_Volume {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, lot, days)

    return query
    


def create_query_0305(days, period, direct, percent):

    """0305 於[3][日]內，成交量均[增加][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query


def create_query_0306(days, period, direct, percent):

    """0305 於[3][日]內，成交量均[減少][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query


def create_query_0401(days, period, buy_sell, direct, lot):

    """0401 外資[3][日]內[買超/賣超][大於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Foreign_Investor') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query

def create_query_0402(days, period, buy_sell, direct, lot):

    """0402 外資[3][日]內[買超/賣超][小於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Foreign_Investor') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query

def create_query_0403(days, period, buy_sell, direct, lot):

    """0403 投信[3][日]內[買超/賣超][大於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Investment_Trust') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query

def create_query_0404(days, period, buy_sell, direct, lot):

    """0404 投信[3][日]內[買超/賣超][小於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Investment_Trust') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query

def create_query_0405(days, period, buy_sell, direct, lot):

    """0405 自營商[3][日]內[買超/賣超][大於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Dealer_Hedging') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query

def create_query_0406(days, period, buy_sell, direct, lot):

    """0406 自營商[3][日]內[買超/賣超][小於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Dealer_Hedging') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query



def create_query_0501(days, period, direct, lot):

    """0501 融資於[3][日]內均[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.MARGIN_SPREAD {} {}
    GROUP BY part_tbl.stock_id HAVING  count(row_num) = {})
    '''.format(counter_margin_d, days, days, sign, lot, days)

    return query

def create_query_0502(days, period, direct, lot):

    """0502 融資於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.MARGIN_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING  count(row_num) = {})
    '''.format(counter_margin_d, days, days, sign, lot, days)

    return query

def create_query_0503(days, period, direct, lot):

    """0503 融券於[3][日]內均[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.SHORTSELL_SPREAD {} {}
    GROUP BY part_tbl.stock_id HAVING  count(row_num) = {})
    '''.format(counter_margin_d, days, days, sign, lot, days)

    return query

def create_query_0504(days, period, direct, lot):

    """0504 融券於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.SHORTSELL_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING  COUNT(row_num) = {})
    '''.format(counter_margin_d, days, days, sign, lot, days)

    return query

def create_query_0505(days, period, direct, lot):

    """0505 借券於[3][日]內均[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.load_spread) {} {} )
    '''.format(counter_loanshare_d, days, days, sign, lot)

    return query

def create_query_0506(days, period, direct, lot):

    """0506 借券於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.load_ratio) {} {} )
    '''.format(counter_loanshare_d, days, days, sign, lot)

    return query


def create_query_0601(numbers, period, direct, amount):

    """0601 近(2)(月/季/年)營收(大於)(5)百萬元"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    amount = amount * 1000000 # 以百萬元為單位

    if period == 'q':
        ref_table = basic_info_revenue_q
    elif period == 'y':
        ref_table = basic_info_revenue_y
    else:
        ref_table = basic_info_revenue_m

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.revenue {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, amount, numbers)

    return query

def create_query_0602(numbers, period, direct, percent):

    """0602 營收連續(3)(月/季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'q':
        ref_table = basic_info_revenue_q
    elif period == 'y':
        ref_table = basic_info_revenue_y
    else:
        ref_table = basic_info_revenue_m

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.last_month_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

    

def create_query_0603(period, direct, percent):

    """0603 上(月/季/年)營收較去年同期(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'q':
        ref_table = basic_info_revenue_q
    elif period == 'y':
        ref_table = basic_info_revenue_y
    else:
        ref_table = basic_info_revenue_m

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.lastyear_month_revenue {} {}
    GROUP BY stock_id)
    '''.format(ref_table, sign, percent)

    return query


def create_query_0604(numbers, period, direct, percent):

    """0604 近(2)(月/季/年)營業毛利率(大於)(5)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Gross_Profit_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

def create_query_0605(numbers, period, direct, percent):

    """0605 營業毛利率連續(3)(季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Gross_Profit_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

    

def create_query_0606(period, direct, percent):

    """0606 上(季/年)營業毛利率較去年同期(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.Gross_Profit_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, sign, percent)

    return query

def create_query_0607(numbers, period, direct, amount):

    """0607 近(2)(月/季/年)營業利益率(大於)(5)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Operating_Profit_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

def create_query_0608(numbers, period, direct, percent):

    """0608 營業利益率連續(3)(月/季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Operating_Profit_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

    

def create_query_0609(period, direct, percent):

    """0609 上(月/季/年)營業利益率較去年同期(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.Operating_Profit_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, sign, percent)

    return query

def create_query_0610(numbers, period, direct, amount):

    """0610 近(2)(月/季/年)稅後淨利率(大於)(5)%"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.AfterTax_Income_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

    return query

def create_query_0611(numbers, period, direct, percent):

    """0611 稅後淨利率連續(3)(月/季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.AfterTax_Income_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query

    

def create_query_0612(period, direct, percent):

    """0612 上(月/季/年)稅後淨利率較去年同期(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
    else:
        ref_table = basic_info_finDetail_q

    query = '''
    (SELECT stock_id FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.AfterTax_Income_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, sign, percent)

    return query