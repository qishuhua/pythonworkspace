
import pymysql

db = pymysql.connect(host="127.0.0.1", user='root', password='admin', db='world', port=3306)
cursor = db.cursor()

# 增加
sql = 'select * from city'
cursor.execute(sql)
result=cursor.fetchall()
for i in result:
    for j in i:
        print(j)

db.close()