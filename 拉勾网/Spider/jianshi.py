import DBfun
import time
last1 = 0
last2 = 0
while 1:
    sql = 'Select count(*) from url_list'
    db = DBfun.connectRDB()
    c=db.cursor()
    c.execute(sql)
    print('url_list:', c._rows[0][0])
    print("100s item_info内插入了", c._rows[0][0] - last1)
    last1 = c._rows[0][0]
    sql = "Select count(*) from item_info"
    c.execute(sql)
    print('item_info:', c._rows[0][0])
    print("100s item_info内插入了", c._rows[0][0] - last2)
    last2 = c._rows[0][0]
    c.close()
    db.close()
    time.sleep(100)