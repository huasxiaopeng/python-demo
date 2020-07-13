import urllib.request
response=urllib.request.urlopen("http://www.sina.com.cn")
# 打印响应的数据类型
print(type(response))
# 打印属性或者方法
print(dir(response))
# 常用方法：
# 状态码：
print(response.getcode())
# 获取相应url
print(response.geturl())
# 获取相应元信息
print(response.info())
print(type(response.info)) #<class 'method'>
# 获取响应头信息
# print(response.getheaders()) 列表