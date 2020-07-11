# python 异常类
# 处理文件找不到异常
fileName = 'lktbz.txt'
syd=''
try:
    with open(fileName) as d:
        syd = d.read()
except FileNotFoundError:
    print("文件找不到，请重新，读取")

print(syd)


# 忽略某些错误消息：

filename='list2.txt'
shd=''
try:
    with open(fileName) as filwobnd:
        shd=filwobnd.read()
except FileNotFoundError:
    pass
print("我继续执行"+shd)