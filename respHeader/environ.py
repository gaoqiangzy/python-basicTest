#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type:text/json;charset=gbk")
print("")
import os
for key in os.environ.keys():
    print("{}:{}".format(key,os.environ.get(key)))