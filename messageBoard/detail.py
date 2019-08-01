#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gbk")
print("Content-Type:text/html")
print("")
import pymysql
import cgi
db = pymysql.connect(host='localhost',user='root',password='root',database='messageboard',charset='gbk')
cur = db.cursor()
file = cgi.FieldStorage()
uid = file.getvalue("uid")
sql = "select * from board where uid = %s"
cur.execute(sql,uid)
data = cur.fetchall()
for d in data:
    print(f"<h3>{d[1]}</h3>")
cur.close()
db.close()