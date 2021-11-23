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

# Query Combination
def query_combine(query_dict, col_name_dict):
    query_number = len(query_dict)

    specific_columns_string = " ,".join(['{}.{}'.format(alias, colname[1]) for colname,alias in zip(col_name_dict.items(), ascii_lowercase)]) + ","
    remark_string = "+".join(['{}.remark'.format(i) for i in ascii_lowercase][:query_number])
    combined_query = "SELECT {}.stock_id, {}.stock_name, {}.price , {}.spread_ratio , {}.industry_category, {}.type, {} {} Remark FROM ".format(ascii_lowercase[query_number], ascii_lowercase[query_number], 
    ascii_lowercase[query_number], ascii_lowercase[query_number], ascii_lowercase[query_number], ascii_lowercase[query_number], specific_columns_string, remark_string)

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
    
    if len(cate_str) == 1:
        cate_str = str(cate_str)
        cate_str = cate_str.replace('[', '(')
        cate_str = cate_str.replace(']', ')')
    else:
        cate_str = tuple(cate_str)
    query = '''(SELECT stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM {} WITH(NOLOCK) WHERE industry_category IN {})'''.format(skill_info, cate_str)
    return query, 'stock_id' #產業別在TW_STOCK_INFO已經有了，故以stock_id代替回傳值。

def create_query_0102(larger, price):
    '''公司股本(大於/小於)(100)仟元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, Capital [股本(仟元)], CAST(NULL AS NVARCHAR(100)) as remark FROM {} WHERE Capital {} {})'''.format(skill_capital, sign, price)
    
    return query, '[股本(仟元)]'

def create_query_0103(larger, price):
    '''公司股本(大於/小於)(100)仟元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, Capital [股本(仟元)], CAST(NULL AS NVARCHAR(100)) as remark FROM {} WITH(NOLOCK) WHERE Capital {} {})'''.format(skill_capital, sign, price)
    
    return query, '[股本(仟元)]'

def create_query_0104(larger, ratio):
    '''董監持股比例(大於)(50)%之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, SUM(new_share_ratio) [董監持股比例], CAST(NULL AS NVARCHAR(100)) as remark FROM (SELECT stock_id, AVG(share_ratio) new_share_ratio FROM {} WITH(NOLOCK)
            GROUP BY stock_id, name) t1
            GROUP BY stock_id HAVING SUM(new_share_ratio) {} {})'''.format(basic_info_supervisor, sign, ratio)

    return query, '[董監持股比例]'

def create_query_0105(larger, ratio):
    '''董監質押比例(大於)(10)%之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, SUM(new_pledge_ratio) [董監質押比例], CAST(NULL AS NVARCHAR(100)) as remark FROM (SELECT stock_id, AVG(pledge_ratio) new_pledge_ratio FROM {}
            GROUP BY stock_id, name) t1
            GROUP BY stock_id HAVING SUM(new_pledge_ratio) {} {})'''.format(basic_info_supervisor, sign, ratio)

    return query, '[董監質押比例]'

def create_query_0106(larger, price):
    '''0106 每股淨值(大於)(10)元之股票'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, PER_STOCK_PRICE [每股淨值], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND PER_STOCK_PRICE {} {})
    '''.format(basic_info_finDetail_q, sign, price)
    return query, '[每股淨值]'

def create_query_0107(numbers, larger, amount):
    '''0107 (3)年內平均ROE(大於)(10)%'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id, AVG(after_return) [平均ROE], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(after_return) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query, '平均ROE'

def create_query_0108(numbers, larger, percent):
    '''0108 ROE連續(3)年(成長/衰退)(5)%以上'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        percent = -percent
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id, AVG(after_return_last_year_ratio) [平均ROE成長%],
    case
    when sum(each_remark) > 0 then CAST('含ROE負轉正；' AS NVARCHAR(100))
    end remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    case
    when t1.After_Return > 0 and t2.After_Return < 0 then 1
    else 0
    end each_remark
    FROM {} t1 WITH(NOLOCK)
    left join {} t2 WITH(NOLOCK) on t1.stock_id = t2.stock_id and t1.date = dateadd(y, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= {} AND after_return_last_year_ratio {} {}
    GROUP BY stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, ref_table, numbers, sign, percent, numbers)
    return query, '[平均ROE成長%]'

def create_query_0109(numbers, larger, amount):
    '''0109 (3)年內平均ROA(大於)(10)%'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id, AVG(total_return) [平均ROA], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM {}) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(total_return) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query, '[平均ROA]'

def create_query_0110(numbers, larger, percent):
    '''0110 ROA連續(3)年(成長/衰退)(5)%以上'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
        percent = -percent
    
    ref_table = basic_info_finDetail_y

    query = '''(SELECT stock_id, AVG(total_return_last_year_ratio) [平均ROA成長%],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含ROA負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.total_return > 0 AND t2.total_return < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK) ON t1.stock_id = t2.stock_id AND t1.date = dateadd(y, 1, t2.date)) part_tbl
    WHERE part_tbl.row_num <= {} AND total_return_last_year_ratio {} {}
    GROUP BY stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, ref_table, numbers, sign, percent, numbers)
    return query, '[平均ROA成長%]'

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

    query = '''(SELECT stock_id, AVG(value) [平均EPS], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM (SELECT * FROM {} WITH(NOLOCK) where [type]='EPS') t1) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(value) {} {})
    '''.format(ref_table, numbers, sign, amount)
    return query, '[平均EPS]'

def create_query_0112(numbers, period, direct, percent):

    """0112 EPS連續(3)(季/年)(成長/衰退)(5)%以上"""
    """BUG: 負轉正好像有問題"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finState_y
        period_unit = 'year'
    else:
        ref_table = basic_info_finState_q
        period_unit = 'quarter'

    query = '''
    (SELECT stock_id, AVG(last_period_ratio) [平均EPS成長%],
    CASE 
    WHEN SUM(each_remark) > 0 THEN CAST('含EPS負轉正；' AS NVARCHAR(100))
    END remark 
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.value > 0 AND t2.value < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK) ON t1.stock_id = t2.stock_id AND t1.date = dateadd({}, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.[type] = 'EPS' AND part_tbl.last_period_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, ref_table, period_unit, numbers, sign, percent)

    return query, '[平均EPS成長%]'


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
    (SELECT stock_id, part_tbl.last_year_ratio [EPS成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含EPS負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.value > 0 AND t2.value < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK) ON t1.stock_id = t2.stock_id AND t1.date = dateadd(y, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[type] = 'EPS' AND part_tbl.last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, ref_table, sign, percent)

    return query, '[EPS成長率]'

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
    (SELECT stock_id, AVG(Inventory_Turnover) [平均存貨週轉率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Inventory_Turnover) {} {})
    '''.format(ref_table, number, sign, percent)

    return query, '[平均存貨週轉率]'



    
def create_query_0115(period, direct, percent):

    """0115 (季/年)存貨週轉率(成長/衰退)(10)%"""
    """BUG: 此寫法只抓最後一筆，會抓到下市的公司以前資料"""


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
    (SELECT stock_id, AVG({}) [存貨週轉率成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_column, ref_table, ref_column, sign, percent)

    return query, '[存貨週轉率成長率]'

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
    (SELECT stock_id, AVG(Accounts_Receivable_Turnover_Rate) [平均應收帳款週轉率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Accounts_Receivable_Turnover_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query, '[平均應收帳款週轉率]'

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
    (SELECT stock_id, AVG({}) [應收帳款週轉率成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_column, ref_table, ref_column, sign, percent)

    return query, '[應收帳款週轉率成長率]'

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
    (SELECT stock_id, AVG(Current_Rate) [平均流動比率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Current_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query, '[平均流動比率]'

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
    (SELECT stock_id, AVG({}) [流動比率成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_column, ref_table, ref_column, sign, percent)

    return query, '[流動比率成長率]'

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
    (SELECT stock_id, AVG(Quick_Rate) [平均速動比率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Quick_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query, '[平均速動比率]'

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
    (SELECT stock_id, AVG({}) [速動比率成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_column, ref_table, ref_column, sign, percent)

    return query, '[速動比率成長率]'

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
    (SELECT stock_id, AVG(Debt_Rate) [平均負債比率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY stock_id HAVING AVG(Debt_Rate) {} {})
    '''.format(ref_table, number, sign, percent)

    return query, '[平均負債比率]'

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
    (SELECT stock_id, AVG({}) [負債比率成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND {} {} {}
    GROUP BY stock_id)
    '''.format(ref_column, ref_table, ref_column, sign, percent)

    return query, '[負債比率成長率]'

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
        (SELECT stock_id, AVG({}) [平均股利], CAST(NULL AS NVARCHAR(100)) as remark FROM
        (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY yearly DESC) row_num
        FROM {} WITH(NOLOCK)) part_tbl
        WHERE part_tbl.row_num <= {} AND {} {} {}
        GROUP BY stock_id HAVING COUNT(row_num) = {})
        '''.format(ref_column, ref_table, number, ref_column, sign, price, number)
    else:
        query = '''
        (SELECT stock_id, AVG({}) [平均股利], CAST(NULL AS NVARCHAR(100)) as remark FROM
        (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY yearly DESC) row_num
        FROM {} WITH(NOLOCK)) part_tbl
        WHERE part_tbl.row_num <= {}
        GROUP BY stock_id HAVING AVG({}) {} {})
        '''.format(ref_table, number, ref_column, sign, price)

    return query, '[平均股利]'

def create_query_0125(distribution_type, number, growth):

    """0125 (現金股利/股票股利)連續(3)年(成長/衰退)"""

    ref_table = basic_info_dividend

    if distribution_type == '2':
        ref_column = 'stock_ratio'
    else:
        ref_column = 'cash_ratio'

    if growth == '1':
        sign = '>'
    else:
        sign = '<'

    query = '''
    (SELECT stock_id, AVG({}) [平均股利成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY yearly DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND {} {} 0
    GROUP BY stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_column, ref_table, number, ref_column, sign, number)

    return query, '[平均股利成長率]'

def create_query_0126(number, all_avg, larger, percent):

    """0126 (3)年內殖利率(皆/平均)(大於)(5)%"""

    if larger == '1':
        sign = '>='
    else:
        sign = '<='

    ref_table = skill_per

    if all_avg == '1':
        query = '''
        (select stock_id, AVG(dividend_yield) [平均殖利率], CAST(NULL AS NVARCHAR(100)) as remark FROM {} WITH(NOLOCK) where [date] > (GETDATE()-({}*365)) 
        GROUP BY stock_id HAVING MIN(dividend_yield) {} {})
        '''.format(ref_table, number, sign, percent)
    else:
        query = '''
        (select stock_id, AVG(dividend_yield) [平均殖利率], CAST(NULL AS NVARCHAR(100)) as remark FROM {} WITH(NOLOCK) where [date] > (GETDATE()-({}*365)) group by stock_id
        HAVING AVG(dividend_yield) {} {})
        '''.format(ref_table, number, sign, percent)

    return query, '[平均殖利率]'

def create_query_0127(larger, times):

    """0127 本益比(大於)(15)倍"""

    if larger == '1':
        sign = '>='
    else:
        sign = '<='

    ref_table = skill_per

    query = '''
    (SELECT stock_id, PER [本益比], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY [date] DESC) row_num
    FROM (SELECT * FROM {} WITH(NOLOCK) where [date] > (GETDATE()-(10)))t1 ) part_tbl
    WHERE row_num <= 1 AND PER {} {})
    '''.format(ref_table, sign, times)

    return query, '[本益比]'


def create_query_0128(number, period, interval, amount, unit):

    '''0128 集保庫存(3)(週/月)內，(1-999股)區間者增加(100)(人/%)'''

    if period == 'm':
        ref_table = counter_holdrange_m
        period_base = 31
    else:
        ref_table = counter_holdrange_w
        period_base = 7

    if unit == '1':
        # (C-B) + (B-A) = C-A 即人數差計算
        query = '''
        (select stock_id, SUM([people] - [last_period_people]) [集保區間增加], CAST(NULL AS NVARCHAR(100)) as remark from {} WITH(NOLOCK)
        where [date] > (GETDATE()-({}*({}-1)+1)) AND HoldingSharesLevel = '{}' 
        GROUP BY stock_id HAVING SUM([people] - [last_period_people]) >= {})
        '''.format(ref_table, period_base, number, interval, amount)
    else:
        query = '''
        (select stock_id, SUM([percent] - [last_period_percent]) [集保區間增加], CAST(NULL AS NVARCHAR(100)) as remark from {} WITH(NOLOCK)
        where [date] > (GETDATE()-({}*({}-1)+1)) AND HoldingSharesLevel = '{}' 
        GROUP BY stock_id HAVING SUM([percent] - [last_period_percent]) >= {})
        '''.format(ref_table, period_base, number, interval, amount)

    return query, '[集保區間增加]'



def create_query_0129(number, period, interval, larger, amount):

    '''0129 集保庫存(3)(週/月)內，(1-999股)區間者均(大於/小於)(100)人'''
    if larger == '1':
        sign = 'MIN'
    else:
        sign = 'MAX'
        
    if period == 'm':
        ref_table = counter_holdrange_m
        period_base = 31
    else:
        ref_table = counter_holdrange_w
        period_base = 7


    query = '''
        (SELECT stock_id, people [區間人數], CAST(NULL AS NVARCHAR(100)) as remark FROM {} WITH(NOLOCK)
        WHERE [date] > (GETDATE()-({}*({}-1)+1)) AND HoldingSharesLevel = '{}'
        GROUP BY stock_id HAVING {}([people]) > {})
        '''.format(ref_table, period_base, number, interval, sign, amount)

    return query, '[區間人數]'

def create_query_0201(larger, price):
    '''0201 公司股價[大於][120]元'''
    if larger == '1':
        sign = '>='
    else:
        sign = '<'

    query = '''(SELECT stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-(10))) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[close] {} {})'''.format(skill_price_d, sign, str(price))

    return query, 'stock_id'

def create_query_0202(larger, price):
    if larger == '1':
        sign = '>='
    else:
        sign = '<'
    
    query = '''(SELECT stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-(10))) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.[close] {} {})'''.format(skill_price_d, sign, str(price))

    return query, 'stock_id'

def create_query_0203(direct, days):
    '0203 公司股價連續[漲/跌停][3]日以上'
    if direct == '1':
        sign = '>='
    else:
        sign = '<='  
        days = -days
    
    query = '''(SELECT t1.stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM {} t1 
    inner join (SELECT stock_id, MAX(date) as each_max_date FROM {} WHERE date > (GETDATE()-(10)) GROUP BY stock_id) t2
    on t2.stock_id = t1.stock_id AND limitup_limitdown_CNT {} {} 
    inner join {} t3 on t3.stock_id = t2.stock_id AND t2.each_max_date = t3.date)'''.format(skill_info, skill_price_d, sign, str(days), skill_price_d)

    return query, 'stock_id'

def create_query_0204(days, period, direct, percent):

    """0204 於[3][日]內[漲/跌幅]均超過[10]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread_ratio {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query, 'stock_id'

def create_query_0205(days, period, direct, percent):

    """於[3][日]內[上漲/下跌][超過][20]元之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.spread {} {}
    GROUP BY stock_id HAVING count(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query, 'stock_id'


def create_query_0301(days, period, direct, percent):

    """於[3][日]內，成交量平均[大於][50000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, AVG(Trading_Volume) [平均成交量], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(skill_price_d, days, days, sign, percent)

    return query, '[平均成交量]'

def create_query_0302(days, period, direct, percent):

    """於[3][日]內，成交量平均[小於][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, AVG(Trading_Volume) [平均成交量], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING AVG(Trading_Volume) {} {})
    '''.format(skill_price_d, days, days, sign, percent)

    return query, '[平均成交量]'

def create_query_0303(days, period, direct, lot):

    """於[3][日]內，成交量均[增加][1000]張之股票"""
    """BUG: 均增加1000，是否要用相減算?"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    # lot = lot * 1000

    query = '''
    (SELECT stock_id, AVG(Trading_spread) [成交量平均增減量], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, lot, days)


    return query, '[成交量平均增減量]'

def create_query_0304(days, period, direct, lot):

    """0304 於[3][日]內，成交量均[減少][1000]張之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
    
    # lot = lot * 1000

    query = '''
    (SELECT stock_id, AVG(Trading_spread) [成交量平均增減量], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, lot, days)

    return query, '[成交量平均增減量]'
    


def create_query_0305(days, period, direct, percent):

    """0305 於[3][日]內，成交量均[增加][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, AVG(Trading_spread_ratio) [成交量平均增減%], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query, '[成交量平均增減%]'


def create_query_0306(days, period, direct, percent):

    """0305 於[3][日]內，成交量均[減少][20]%之股票"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    query = '''
    (SELECT stock_id, AVG(Trading_spread_ratio) [成交量平均增減%], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Trading_spread_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(skill_price_d, days, days, sign, percent, days)

    return query, '[成交量平均增減%]'


def create_query_0401(days, period, buy_sell, direct, lot):

    """0401 外資[3][日]內[買超/賣超][大於][5000]張"""
    if buy_sell == '1' and direct == '1':
        sign = '>='
        sign_0 = '>=' 
        lot = lot * 1000 #以每股為單位
    elif buy_sell == '1' and direct == '-1':
        sign = '<='
        sign_0 = '>='
        lot = lot * 1000 #以每股為單位
    elif buy_sell == '-1' and direct == '1':
        sign = '<='
        sign_0 = '<='
        lot = lot * -1000 #以每股為單位
    else:
        sign = '>='
        sign_0 = '<='
        lot = lot * -1000 #以每股為單位

    query = '''
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [外資平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Foreign_Investor') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[外資平均買賣超]'

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
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [外資平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Foreign_Investor') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[外資平均買賣超]'

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
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [投信平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Investment_Trust') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[投信平均買賣超]'

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
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [投信平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Investment_Trust') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[投信平均買賣超]'

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
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [自營商平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Dealer_Hedging') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[自營商平均買賣超]'

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
    (SELECT stock_id, AVG(part_tbl.buy - part_tbl.sell) [自營商平均買賣超], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10)) AND name = 'Dealer_Hedging') part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.buy) - SUM(part_tbl.sell) {} {} AND SUM(part_tbl.buy) - SUM(part_tbl.sell) {} 0)
    '''.format(counter_legal_d, days, days, sign, lot, sign_0)

    return query, '[自營商平均買賣超]'



def create_query_0501(days, period, direct, lot):

    """0501 融資於[3][日]內，共[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    if period == 'w':
        ref_table = counter_margin_w 
    elif period == 'm':
        ref_table = counter_margin_m
    elif period == 'q':
        ref_table = counter_margin_q
    elif period == 'y':
        ref_table = counter_margin_y
    else:
        ref_table = counter_margin_d

    query = '''
    (SELECT stock_id, SUM(MARGIN_SPREAD) [融資增加數], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.MARGIN_SPREAD) {} {} )
    '''.format(ref_table, days, days, sign, lot)

    return query, '[融資增加數(張)]'

def create_query_0502(days, period, direct, lot):

    """0502 融資於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    if period == 'w':
        ref_table = counter_margin_w 
    elif period == 'm':
        ref_table = counter_margin_m
    elif period == 'q':
        ref_table = counter_margin_q
    elif period == 'y':
        ref_table = counter_margin_y
    else:
        ref_table = counter_margin_d

    query = '''
    (SELECT stock_id, AVG(MARGIN_ratio) [融資平均增加%], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.MARGIN_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING  count(row_num) = {})
    '''.format(ref_table, days, days, sign, lot, days)

    return query, '[融資平均增加%]'

def create_query_0503(days, period, direct, lot):

    """0503 融券於[3][日]內，共[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    if period == 'w':
        ref_table = counter_margin_w 
    elif period == 'm':
        ref_table = counter_margin_m
    elif period == 'q':
        ref_table = counter_margin_q
    elif period == 'y':
        ref_table = counter_margin_y
    else:
        ref_table = counter_margin_d

    query = '''
    (SELECT stock_id, SUM(SHORTSELL_SPREAD) [融券增加數], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.SHORTSELL_SPREAD) {} {} )
    '''.format(ref_table, days, days, sign, lot)

    return query, '[融券增加數(張)]'

def create_query_0504(days, period, direct, lot):

    """0504 融券於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    if period == 'w':
        ref_table = counter_margin_w 
    elif period == 'm':
        ref_table = counter_margin_m
    elif period == 'q':
        ref_table = counter_margin_q
    elif period == 'y':
        ref_table = counter_margin_y
    else:
        ref_table = counter_margin_d

    query = '''
    (SELECT stock_id, AVG(SHORTSELL_ratio) [融券平均增加%], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.SHORTSELL_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING  COUNT(row_num) = {})
    '''.format(ref_table, days, days, sign, lot, days)

    return query, '[融券平均增加%]'

def create_query_0505(days, period, direct, lot):

    """0505 借券於[3][日]內，共[增加/減少][100]張以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    lot = lot * 1000 #每股為單位
    
    if period == 'w':
        ref_table = counter_loanshare_w
    elif period == 'm':
        ref_table = counter_loanshare_m
    elif period == 'q':
        ref_table = counter_loanshare_q
    elif period == 'y':
        ref_table = counter_loanshare_y
    else:
        ref_table = counter_loanshare_d

    query = '''
    (SELECT stock_id, SUM(load_spread) [借券增加數(股)], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(part_tbl.load_spread) {} {} )
    '''.format(ref_table, days, days, sign, lot)

    return query, '[借券增加數(股)]'

def create_query_0506(days, period, direct, lot):

    """0506 借券於[3][日]內均[增加/減少][20]%以上"""
    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        lot = -lot
    
    if period == 'w':
        ref_table = counter_loanshare_w
    elif period == 'm':
        ref_table = counter_loanshare_m
    elif period == 'q':
        ref_table = counter_loanshare_q
    elif period == 'y':
        ref_table = counter_loanshare_y
    else:
        ref_table = counter_loanshare_d

    query = '''
    (SELECT stock_id, AVG(load_ratio) [借券平均增加%], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)
    WHERE date > (GETDATE()-({}+10))) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.load_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, days, days, sign, lot, days)

    return query, '[借券平均增加%]'


def create_query_0601(numbers, period, direct, amount):

    """0601 近(2)(月/季/年)營收合計(大於)(500000000)元"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='

    if period == 'q':
        ref_table = basic_info_revenue_q
    elif period == 'y':
        ref_table = basic_info_revenue_y
    else:
        ref_table = basic_info_revenue_m

    query = '''
    (SELECT stock_id, SUM(revenue) [合計營收], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {}
    GROUP BY part_tbl.stock_id HAVING SUM(revenue) {} {})
    '''.format(ref_table, numbers, sign, amount)

    return query, '[合計營收]'

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
    (SELECT stock_id, AVG(last_month_ratio) [平均營收成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.last_month_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query, '[平均營收成長率]'

    

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
    (SELECT stock_id, lastyear_month_revenue [營收成長率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.lastyear_month_revenue {} {}
    GROUP BY stock_id)
    '''.format(ref_table, sign, percent)

    return query, '[營收成長率]'


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
    (SELECT stock_id, AVG(Gross_Profit_Margin) [平均營業毛利率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Gross_Profit_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query, '[平均營業毛利率]'

def create_query_0605(numbers, period, direct, percent):

    """0605 營業毛利率連續(3)(季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        period_unit = 'year'
    else:
        ref_table = basic_info_finDetail_q
        period_unit = 'quarter'

    query = '''
    (SELECT stock_id, AVG(Gross_Profit_Margin_last_quarter_ratio) [平均營業毛利率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含營業毛利率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.Gross_Profit_Margin > 0 AND t2.Gross_Profit_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd({}, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Gross_Profit_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, ref_table, period_unit, numbers, sign, percent, numbers)

    return query, '[平均營業毛利率成長率]'

    

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
    (SELECT stock_id, AVG(Gross_Profit_Margin_last_year_ratio) [營業毛利率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含營業毛利率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.Gross_Profit_Margin > 0 AND t2.Gross_Profit_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd(y, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.Gross_Profit_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, ref_table, sign, percent)

    return query, '[營業毛利率成長率]'

def create_query_0607(numbers, period, direct, percent):

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
    (SELECT stock_id, AVG(Operating_Profit_Margin) [平均營業利益率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Operating_Profit_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query, '[平均營業利益率]'

def create_query_0608(numbers, period, direct, percent):

    """0608 營業利益率連續(3)(月/季/年)(成長/衰退)(5)%以上"""

    if direct == '1':
        sign = '>='
    else:
        sign = '<='
        percent = -percent

    if period == 'y':
        ref_table = basic_info_finDetail_y
        period_unit = 'year'
    else:
        ref_table = basic_info_finDetail_q
        period_unit = 'quarter'

    query = '''
    (SELECT stock_id, AVG(Operating_Profit_Margin_last_quarter_ratio) [平均營業利益率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含營業利益率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.Operating_Profit_Margin > 0 AND t2.Operating_Profit_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd({}, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.Operating_Profit_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, ref_table, period_unit, numbers, sign, percent, numbers)

    return query, '[平均營業利益率成長率]'

    

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
    (SELECT stock_id, AVG(Operating_Profit_Margin_last_year_ratio) [營業利益率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含營業利益率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.Operating_Profit_Margin > 0 AND t2.Operating_Profit_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd(y, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.Operating_Profit_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, ref_table, sign, percent)

    return query, '[營業利益率成長率]'

def create_query_0610(numbers, period, direct, percent):

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
    (SELECT stock_id, AVG(AfterTax_Income_Margin) [平均稅後淨利率], CAST(NULL AS NVARCHAR(100)) as remark FROM
    (SELECT *,  ROW_NUMBER() OVER(PARTITION BY stock_id ORDER BY date DESC) row_num
    FROM {} WITH(NOLOCK)) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.AfterTax_Income_Margin {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, numbers, sign, percent, numbers)

    return query, '[平均稅後淨利率]'

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
        period_unit = 'year'
    else:
        ref_table = basic_info_finDetail_q
        period_unit = 'quarter'

    query = '''
    (SELECT stock_id, AVG(AfterTax_Income_Margin_last_quarter_ratio) [平均稅後淨利率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含稅後淨利率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.AfterTax_Income_Margin > 0 AND t2.AfterTax_Income_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd({}, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= {} AND part_tbl.AfterTax_Income_Margin_last_quarter_ratio {} {}
    GROUP BY part_tbl.stock_id HAVING COUNT(row_num) = {})
    '''.format(ref_table, ref_table, period_unit, numbers, sign, percent, numbers)

    return query, '[平均稅後淨利率成長率]'

    

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
    (SELECT stock_id, AVG(AfterTax_Income_Margin_last_year_ratio) [稅後淨利率成長率],
    CASE
    WHEN SUM(each_remark) > 0 THEN CAST('含稅後淨利率負轉正；' AS NVARCHAR(100))
    END remark
    FROM
    (SELECT t1.*,  ROW_NUMBER() OVER(PARTITION BY t1.stock_id ORDER BY t1.[date] DESC) row_num,
    CASE
    WHEN t1.AfterTax_Income_Margin > 0 AND t2.AfterTax_Income_Margin < 0 THEN 1
    ELSE 0
    END each_remark
    FROM {} t1 WITH(NOLOCK)
    LEFT JOIN {} t2 WITH(NOLOCK)
    ON t1.stock_id = t2.stock_id AND t1.date = dateadd(y, 1, t2.date)
    ) part_tbl
    WHERE part_tbl.row_num <= 1 AND part_tbl.AfterTax_Income_Margin_last_year_ratio {} {}
    GROUP BY part_tbl.stock_id)
    '''.format(ref_table, ref_table, sign, percent)

    return query, '[稅後淨利率成長率]'