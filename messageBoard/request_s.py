#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import io
import sys
import cgi,cgitb
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gbk")
print("Content-Type:text/html")
print("")
def index(request):
    print("index")
def edit(request):
    print(request.getvalue('id'))
    print("edit")

request = cgi.FieldStorage()
act = request.getvalue('act',"index")
eval(act)(request)