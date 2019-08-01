#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import os
print("Content-Type:text/html;charset=gbk")
print("")

if os.environ.get("HTTP_USER_AGENT").find("IE")!=-1:
    print("请使用高版本浏览器")
else:
    print ("浏览器OK")
# print(os.environ) 系统环境
#for key in os.environ.keys():
 #   print("<p>{}:{}</p>".format(key,os.environ[key]))
