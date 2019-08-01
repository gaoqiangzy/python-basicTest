#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#请求头
print("Content-Type: text/html")
#print ("Location: https://www.baidu.com")
#print("Refresh: 3;url=https://www.baidu.com")
#空行
print("")
#正文
print("<div id='btn'>3S后跳转到百度</div>")
html = """
    <script>
        var timer=3;
        window.setInterval(function(){
            --timer;
            var html = timer + 'S后跳转到百度';
            document.getElementById('btn').innerHTML=html;
            if(timer == 0){
                window.location.href = 'https://www.baidu.com';
            }
        },1000)
    </script>
"""
print(html)