#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gbk")
print("Content-Type:text/html")
print("")
import pymysql
db = pymysql.connect(host='localhost',user='root',password='root',database='messageboard',charset='gbk')
cur = db.cursor()
try:
    cur.execute("select * from board")
except Exception as e:
    print(e)
    print("出错了噢")
else:
    msgs = cur.fetchall()
    print("<ul>")
    for msg in msgs:
        print("<table>")
        print("<tr>")
        print(f"<td>{msg[0]}</td>")
        print(f"<td><a href='detail.py?uid={msg[2]}'>{msg[1]}</a></td>")
        print(f"<td><a href='detail.py?uid={msg[2]}'>修改</a></td>")
        print("</tr>")
        print("</table>")
        # print(f"<li><a href='#'>{msg[1]}</a></li>")
    print("</ul>")
    cur.close()
    db.close()