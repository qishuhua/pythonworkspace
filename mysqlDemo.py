import MySQLdb
conn=MySQLdb.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='admin',
    db='mysql'
)
cur=conn.cursor()
sql=r'insert into t_demo (name) values ("pwd")'
cur.execute(sql)
conn.commit()
cur.close()
conn.close()