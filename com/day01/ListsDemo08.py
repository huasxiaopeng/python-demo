# 元祖 就是不可变的集合

zoo=(1,2)
print(zoo[0])
print(zoo[1])

# 遍历

for i in zoo:
    print(i)

# 值不可以修改，但可以给修改变量的引用
zoo=(3,4)
for i in zoo:
    print(i)