import urllib.request
import urllib.parse
import urllib.response

# 以有道翻译为例
# POST请求
# 1准备url
# https://www.baidu.com/s?wd=%E6%96%B0%E6%B5%AA
#
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# 此url 反爬虫措施严重,只需要换个url 就能行
# 准别post请求数据
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {
    'i':' english',
    'from':' AUTO',
    'to': 'AUTO',
    'smartresult':' dict',
    'client':' fanyideskweb',
    'bv':' 3fc88d9bb22d67787533c6b0170d26d8',
    'doctype':' json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_REALTlME'
}
ucdata = urllib.parse.urlencode(data)
# 转换成byte对象
data=bytes(ucdata,"utf-8")
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
# 2构造request
req = urllib.request.Request(url,data=data, headers=headers)

# 3发送请求
rep = urllib.request.urlopen(req)
# 4打印结果
print(rep.read().decode())
# {"errorCode":50}