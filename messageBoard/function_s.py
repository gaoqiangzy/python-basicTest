def redirect(url,msg='',times=3):
    '''
    :param url: 跳转链接
    :param msg: 提示信息
    :param times: 间隔时间
    :return:
    '''
    if times > 0:
        html = f'<div id="msg">{msg}</div>'
        html += f'<div id="times">{times}S后跳转</div>'
        html +="<script>"
        html +=f"var times = {times};"
        html +="""
            window.setInterval(function(){
                --times;
                var html = times + "秒后跳转";
                document.getElementById("times").innerHTML = html;
                if(times == 0 ){
                """
        html +=f"window.location.href='{url}';"
        html +="""
                  }
            },1000)
            </script>
            """
    else:
        html =f"<script>window.location.href='{url}'</script>"
    print(html)




