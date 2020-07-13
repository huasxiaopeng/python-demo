import urllib.request
import urllib.parse
import urllib.response

# 出去get请求
# 1准备url
# https://www.baidu.com/s?wd=%E6%96%B0%E6%B5%AA
# 自己出入查询，语句如上，其中新浪被替换成%E6%96%B0%E6%B5%AA
url = 'http://www.baidu.com/s?'
data = {
    'wd': '新浪'
}
ucdata = urllib.parse.urlencode(data)
# 1.2拼接
url += ucdata
# 1.3添加代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
# 2构造request
req = urllib.request.Request(url, headers=headers)

# 3发送请求
rep = urllib.request.urlopen(req)
# 4打印结果
print(rep.read().decode())
