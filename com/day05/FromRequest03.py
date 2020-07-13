import urllib.request
import urllib.parse

# 数据构件
data = {'name': 'lktbz'}
# 进行URL转码
data = urllib.parse.urlencode(data)
# 抓换成字节对象
data = bytes(data.encode())
# 指定headers 构建用户代理
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
# 构造request
request = urllib.request.Request('http://httpbin.org/post', data=data, headers=headers)
# 发送请求
repose = urllib.request.urlopen(request)
# 打印相应信息
print(repose.read().decode())
