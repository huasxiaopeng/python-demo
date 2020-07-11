# 文件
with open('pijec.txt')as fileob:
    text = fileob.read()
    print(text)
    print(text.rstrip())  # 去除空格

# 一行行的去读取
fileName = 'demo.txt'
with open(fileName)as line:
    for ls in line:
        print(ls.rstrip())

# 创建一个包含文件内容的列表
fileName = 'demo.txt'
with open(fileName)as djk:
    lines = djk.readlines()

for li in lines:
    print(li.rstrip())

# 使用文件的内容
fileName = 'demo.txt'
with open(fileName)as djk:
    lines = djk.readlines()

p_string = ''
for lin in lines:
    p_string += lin.rstrip()

print(p_string)
print(len(p_string))

# 左空格
fileName = 'demo.txt'
with open(fileName)as djk:
    lines = djk.readlines()

p_sstring = ''
for ins in lines:
    p_sstring += ins.strip()

print(p_sstring)


