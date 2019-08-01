#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
import io
import sys
#系统默认输出流 = 文本io流打包（系统默认输出流缓存，utf-8）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
'''
常见编码设置方式有两种（网页内容编码）
    a.设置响应头
    print("Content-Type:text/html;charset=utf-8")
    b.通过html上的meta标签设置
    <meta charset="utf-8>
统一编码为utf-8
    print()方法在标准输出流的时候采用的是系统默认的编码（Windows gbk）
    处理方案 将默认的输出流编码更改为utf-8
    使用io,sys
'''
print("Content-Type:text/json;charset=utf-8")
print("")

print("hello world")
print("你好 世界") # 乱码
