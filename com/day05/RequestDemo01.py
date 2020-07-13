import  urllib.request
# 快速抓取一个页面：
# 建立请求
repspon=urllib.request.urlopen("http://www.baidu.com")

# 解析页面
html=repspon.read().decode('utf-8')
# 打印
print(html)

