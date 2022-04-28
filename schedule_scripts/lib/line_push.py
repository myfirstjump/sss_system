import requests
import pymssql

def lineNotifyMessage(msg,token='UHWuGFeLSCBH844IJcqjiiQM9KOI9XNEQhJFmggJuZ5'):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    print(r.status_code)
    return r.status_code


if __name__ == "__main__":
    message = ''
    conn = pymssql.connect(host='localhost', user = 'stock_search', password='1qazZAQ!', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)  
    cursor.execute("""select * from [STOCK_SKILL_DB].[dbo].[LINE_PUSH] order by phase""")
    lineNotifyMessage('\n 1.三大皆買,量>10000,漲停\n2.三大皆買,量>5000,漲停\n3.外&投皆買,量>10000,漲停\n4.外&投皆買,量>5000,漲停\n5.三大合買,量>10000,漲停\n6.三大合買,量>5000,漲停')
    for row in cursor:
        message = message+'\n{} {} ({},{},{})'.format(row['stock_id'], row['stock_name'], row['phase'], row['type'], row['industry_category'])
    
    lineNotifyMessage(message)