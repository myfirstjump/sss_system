import pymssql





# 各項條件的string
def create_query(arg1, arg2):

    return 'select {} from {}'.format(arg1, arg2)



# 最後查詢
def final_query(arg):
    conn = pymssql.connect(host='localhost', user = 'myfirstjump', password='myfirstjump', database='STOCK_SKILL_DB')
    cursor = conn.cursor(as_dict=True)

