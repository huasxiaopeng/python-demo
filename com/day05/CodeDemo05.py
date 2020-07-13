# url编解码
#
import urllib.parse

data = {
    "a": '太阳无限好',
    "b": "不是很美好"
}
# (常用)
result = urllib.parse.urlencode(data)
print(result)
# URl解码，把url编码后的字符串，转换成普通字符成员
#常用
data=urllib.parse.unquote(result)
print(data)

# 进行编码,对字符串(用的少)=号，都进行了编码
unda=urllib.parse.quote(data)
print(unda)
