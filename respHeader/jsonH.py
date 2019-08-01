#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type:text/json;charset=gbk")
print("")
from datetime import datetime
import json
import time
import cgi,cgitb
import pymysql
cgitb.enable() #程序报错时，在页面显示错误信息
db = pymysql.connect(host='localhost',user='root',password='root',database='store',charset='gbk')
cur = db.cursor()
sql ="select * from product where pid =1"
cur.execute(sql)
data = cur.fetchone()
data = list(data)
data[5] = data[5].strftime('%Y-%m-%d %H:%M %S')
print(json.dumps(data))

