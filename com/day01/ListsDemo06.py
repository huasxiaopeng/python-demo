# 列表深入学习
# for v in range(1,6):
#     print(v)

# 生成的数据转换成列表
# numbers=list(range(1,6))

# print(numbers)


# squarus=[]
# for value in range(1,11):
#     # squa=value*2
#     # squarus.append(squa)
#     squarus.append(value**2)
#
#     print(squarus)


dits=[1,2,3,4,5,6,7,8,9,10]


sq=[value**2 for value in range(1,11)]
print(sq)

for c in range(1,11):
    print(c)

# 列表解析demo
# 列出1-10所有数字的平方
L=[]
for i in range(1,11):
    L.append(i**2)

print(L)


# 列表解析
L=[  i**2 for i in range(1,15)]

print(L)

# 要求：列出1~10中大于等于4的数字的平方

L=[]
for i in range(1,11):
    if i>=4:
        L.append(i**2)

print(L)

# 列表解析
G=[]
G=[i**2 for i in range(1,11) if i>=4]
print(G)

# 要求：列出1~10所有数字的平方除以2的值
GG=[]
for i in range(1,10):
    GG.append(i**2/2)

print(GG)


# 列表解析
YYY=[]
YYY=[i**2/2 for i in range(1,11)]
print(YYY)

# 要求：列出"/var/log"中所有已'.log'结尾的文件
import os
file=[]
for file in os.listdir('/var/log'):
     if(file.endswith('.log')):
         file.append(file)

print(file)

# 列表解析
import  os
file=[]
file=[ file for file in os.listdir('/var/log') if file.endswith('.log')]
print(file)


