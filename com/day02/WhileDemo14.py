# while 循环用来处理列表和字典
# 元素移动

list1=['one','two','three']
list2=[]
# while list1:
#   sjj=  list1.pop()
#   print("弹出的值为"+sjj)
#   list2.append(sjj)
#
# for ins in list2:
#     print("遍历移动的新列表的数据"+ins)


# 删除特定的值

pets=['dog','cat','dog','rabbit']

while 'cat' in pets:
    pets.remove('cat')

print(pets)