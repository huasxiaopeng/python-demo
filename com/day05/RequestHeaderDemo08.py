import urllib.request
import urllib.response
import urllib.parse

# 添加请求头，伪装浏览器发送的请求
# 两种方式
# 一：

url = "http://www.baidu.com"
# # 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

}
# 构架request
request = urllib.request.Request(url, headers=headers)
# 方式二：
request.add_header("name", "lktbz")
# 获取请求头
name = request.get_header("name")
print(name)
# 发送请求
response = urllib.request.urlopen(request)
# 获取相应数据
print(response.read().decode())
