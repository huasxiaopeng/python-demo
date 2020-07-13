import urllib.request
import urllib.parse
# 优化写法
url='http://httpbin.org/post'
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

}
user={'name':'lktbz'}
data=bytes(urllib.parse.urlencode(user).encode("utf-8"))
# 上面的步骤都是将数据转换成二进制
# 构件request
req=urllib.request.Request(url,data=data,headers=header)
res=urllib.request.urlopen(req)
print(res.read().decode())

