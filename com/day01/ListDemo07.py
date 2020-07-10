# 列表的切片
dits=[1,2,3,4,5,6,7,8,9,10]

# 切片：读部分数据
#读数据，只三个
print(dits[0:3])
#读2-4个元素
print(dits[1:4])
#不指定索引，看如何切
print(dits[:3])
# 指定索引，不指定范围
print(dits[3:])

#使用 -直接输出末尾
print(dits[-2:])


print("开始使用遍历切片。。")
# 遍历
for i in dits[:3]:
    print(i)


#列表的复制
fs=dits[:]
print(fs)




