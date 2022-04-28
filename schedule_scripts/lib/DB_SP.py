import logging
from datetime import datetime
import lib.line_push as push


logging.basicConfig(
level = logging.DEBUG,
filename = 'C:\\stock_schedule\\log\\{}.log'.format(datetime.now().strftime('%Y%m%d')),
filemode = 'a',
format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
token = 'YGP4rPfKWCRVXe9hw4SISPbp1IITfbgCaWt5yirxT8C'

def DB_SP_SCHDULE(conn,dt=''):
    cursor = conn.cursor(as_dict=True)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.UPDATE_TRADING_VOLUMN '{}'".format(dt))
        conn.commit()
        logging.debug("update_trading_volumn success!!")
    except:
        logging.error('update trading volumn fail')
        push.lineNotifyMessage('update trading volumn fail',token)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.UPDATE_UPPERLOWER_LIMIT")
        conn.commit()
        logging.debug("UPDATE_UPPERLOWER_LIMIT success!!")
    except:
        logging.error('UPDATE_UPPERLOWER_LIMIT fail')
        push.lineNotifyMessage('UPDATE_UPPERLOWER_LIMIT fail',token)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.INSERT_WEEK_DATA '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_WEEK_DATA success!!")
    except:
        logging.error('INSERT_WEEK_DATA fail')
        push.lineNotifyMessage('INSERT_WEEK_DATA fail',token)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.INSERT_MONTH_DATA '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_MONTH_DATA success!!")
    except:
        logging.error('INSERT_MONTH_DATA fail')
        push.lineNotifyMessage('INSERT_MONTH_DATA fail',token)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.INSERT_QUARTER_DATA '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_QUARTER_DATA success!!")
    except:
        logging.error('INSERT_QUARTER_DATA fail')
        push.lineNotifyMessage('INSERT_QUARTER_DATA fail',token)
    try:
        cursor.execute("exec STOCK_SKILL_DB.dbo.INSERT_YEAR_DATA '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_YEAR_DATA success!!")
    except:
        logging.error('INSERT_YEAR_DATA fail')
        push.lineNotifyMessage('INSERT_YEAR_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[INSERT_LEGAL_PERSON_WEEK_MONTH] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_LEGAL_PERSON_WEEK_MONTH success!!")
    except:
        logging.error('INSERT_LEGAL_PERSON_WEEK_MONTH fail')
        push.lineNotifyMessage('INSERT_LEGAL_PERSON_WEEK_MONTH fail',token)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[UPDATE_LEGAL_PERSON_RATIO] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_LEGAL_PERSON_RATIO success!!")
    except:
        logging.error('UPDATE_LEGAL_PERSON_RATIO fail')
        push.lineNotifyMessage('UPDATE_LEGAL_PERSON_RATIO fail',token)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[INSERT_MARGINTRADE_SHORTSELL_PERIOD_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_MARGINTRADE_SHORTSELL_PERIOD_DATA!!")
    except:
        logging.error('INSERT_MARGINTRADE_SHORTSELL_PERIOD_DATA')
        push.lineNotifyMessage('INSERT_MARGINTRADE_SHORTSELL_PERIOD_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[UPDATE_MARGINTRADE_SHORTSELL_RATIO] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_MARGINTRADE_SHORTSELL_RATIO!!")
    except:
        logging.error('UPDATE_MARGINTRADE_SHORTSELL_RATIO')
        push.lineNotifyMessage('UPDATE_MARGINTRADE_SHORTSELL_RATIO fail',token)
    try:
        cursor.execute("exec [STOCK_BASICINTO_DB].[dbo].[INSERT_REVENUE_PERIOD_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_REVENUE_PERIOD_DATA!!")
    except:
        logging.error('INSERT_REVENUE_PERIOD_DATA')
        push.lineNotifyMessage('INSERT_REVENUE_PERIOD_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_BASICINTO_DB].[dbo].[UPDATE_LAST_YM_REVENUE_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_LAST_YM_REVENUE_DATA!!")
    except:
        logging.error('UPDATE_LAST_YM_REVENUE_DATA')
        push.lineNotifyMessage('UPDATE_LAST_YM_REVENUE_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_BASICINTO_DB].[dbo].[INSERT_FinancialStatements_PERIOD_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_FinancialStatements_PERIOD_DATA!!")
    except:
        logging.error('INSERT_FinancialStatements_PERIOD_DATA')
        push.lineNotifyMessage('INSERT_FinancialStatements_PERIOD_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_BASICINTO_DB].[dbo].[UPDATE_FinancialStatements_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_FinancialStatements_DATA!!")
    except:
        logging.error('UPDATE_FinancialStatements_DATA')
        push.lineNotifyMessage('UPDATE_FinancialStatements_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_SKILL_DB].[dbo].[SP_line_push] '{}'".format(dt))
        conn.commit()
        logging.debug("SP_line_push!!")
    except:
        logging.error('SP_Line_Push')
        push.lineNotifyMessage('SP_line_push fail',token)



def DB_SP_CRAWL(conn,dt=''):
    cursor = conn.cursor(as_dict=True)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[INSERT_LOADSHARE_PERIOD_DATA] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_LOADSHARE_PERIOD_DATA!!")
    except:
        logging.error('INSERT_LOADSHARE_PERIOD_DATA')
        push.lineNotifyMessage('INSERT_LOADSHARE_PERIOD_DATA fail',token)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[UPDATE_LOANSHARE_RATIO] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_LOANSHARE_RATIO!!")
    except:
        logging.error('UPDATE_LOANSHARE_RATIO')
        push.lineNotifyMessage('UPDATE_LOANSHARE_RATIO fail',token)
    try:
        cursor.execute("exec [STOCK_BASICINTO_DB].[dbo].[UPDATE_FinancialStatements_Detail] '{}'".format(dt))
        conn.commit()
        logging.debug("UPDATE_FinancialStatements_Detail!!")
    except:
        logging.error('UPDATE_FinancialStatements_Detail')
        push.lineNotifyMessage('UPDATE_FinancialStatements_Detail fail',token)



def DB_SP_EVERYDAY(conn,dt=''):
    cursor = conn.cursor(as_dict=True)
    try:
        cursor.execute("exec [STOCK_COUNTER_DB].[dbo].[INSERT_HOLDRANGE_PERIOD] '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_HOLDRANGE_PERIOD!!")
    except:
        logging.error('INSERT_HOLDRANGE_PERIOD')
        push.lineNotifyMessage('INSERT_HOLDRANGE_PERIOD fail',token)
    try:
        cursor.execute("exec STOCK_BASICINTO_DB.dbo.INSERT_UPDATE_DIVIDEND '{}'".format(dt))
        conn.commit()
        logging.debug("INSERT_UPDATE_DIVIDEND!!")
    except:
        logging.error('INSERT_UPDATE_DIVIDEND')
        push.lineNotifyMessage('INSERT_UPDATE_DIVIDEND fail',token)    
    # try:
    #     cursor.execute("exec STOCK_COUNTER_DB.dbo.INSERT_HOLDRANGE_PERIOD '{}'".format(dt))
    #     conn.commit()
    #     logging.debug("INSERT_HOLDRANGE_PERIOD!!")
    # except:
    #     logging.error('INSERT_HOLDRANGE_PERIOD')
    #     push.lineNotifyMessage('INSERT_HOLDRANGE_PERIOD fail',token)

