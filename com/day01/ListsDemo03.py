# 列表是顺序的

#定义lists
mylist=[]
# 添加元素
mylist.append(1)
mylist.append(2)
mylist.append(3)
# 测试列表是否可重复 可以重复
mylist.append(2)
print(mylist[3])
#打印
print(mylist[0])
print(mylist[1])
print(mylist[2])
#添加不同改的类型进去
mylist.append("lktbz")
# 测试成功
print(mylist[4])

# 修改删除

mylist[3]="lktbz"
# 指定位置删除
# del  mylist[3] 彻底删除
# 假删除

list=['honda','toyota',"suziki"]
print(list)
prs=list.pop();
print(list)
print(prs)

# 指定位置删除

dsj=list.pop(1)
print(dsj)
print(list)
# for循环
for x in mylist:
    print(x)
#访问一个也不存在的角标元素
# print(mylist[5]) IndexError: list index out of range
# 排序

nums=[1,2,6,4,10,7,5]
cars=['bmw','audi','toyota','byd','furte','das auto']
# sord 属于永久性的排序
nums.sort()
print(nums)
cars.sort()
print(cars)
# 反转
# nums.sort(reverse=True)
# print(nums)

# 进行临时排序
carss=['bmw','audi','toyota','byd']
sorted(carss)
print(carss)