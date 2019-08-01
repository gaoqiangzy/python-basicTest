#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
print("Content-Type:text/html")
print("")
import pymysql
db = pymysql.connect(host="localhost",user="root",password="root",database="test",charset="utf8")
cur = db.cursor()
sql = "select * from user"
try:
    cur.execute(sql)
except Exception as e:
    print(e)
else:
    users = cur.fetchall()
    for user in users:
        print(f"<p>{user[0]}</p>")
        print(f"<p>{user[1]}</p>")
        print(f"<p>{user[2]}</p>")
        print(f"<p>{user[3]}</p>")




