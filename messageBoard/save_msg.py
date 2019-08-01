#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import io
import sys
import function_s
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gbk")
print("Content-Type:text/html")
print("")
#引入cgi模块接受数据
import  cgi,cgitb
cgitb.enable()
import pymysql
#创建form便于接受数据
form=cgi.FieldStorage() #存储数据
#接受数据
username = form.getvalue('username')
content = form.getvalue('content')
if  username and content:
    db = pymysql.connect(host='localhost',user='root',password='root',database='messageboard',charset='gbk')
    cur = db.cursor()
    sql = "insert into board(username,content) values (%s,%s)"
    #输出到页面
    # print(f"<p>接受到的数据：用户名：{username},留言：{content}</p>")
    try:
        rs = cur.execute(sql, (username, content))
    except Exception as e:
        print(e)
        print("<p >留言失败</p>")
        db.rollback()
    else:
        if rs >0:
            #添加成功
            function_s.redirect('./showMsg.py','添加成功')
            # print("<p>留言成功,<a href='./showMsg.py'>点击查看留言</a></p>")
            db.commit()
            cur.close()
            db.close()
        else:
            #添加失败
            function_s.redirect('../../messageBoard','添加失败，请从新添加')
else:
    #没有数据
    function_s.redirect('../../messageBoard','添加失败，请输入数据')



