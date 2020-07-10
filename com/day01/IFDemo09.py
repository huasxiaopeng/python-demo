#if
# 简单demo
cars=['audi','bmw','subs','toyota']
for car in cars:
    if car=='bmw':
         print(car.upper())
    else:
        print(car.title())


#判断是否大小
for car in cars:
    if car.upper()=="audi":print(car)

st1='zs'
st2='li'
if(st1==st2):
    print("相等")
else:print("不等")



# 多个条件的检查
age1=22
age2=18
if(age1>=21 and age2<18):
    print("x")

# age1>=21 and age2<19 条件语句

# if

age3=19
if age3>18:
    print("能进行投票")


# if else

age4=17
if age4 >=18:
    print("可以进行投票的操作")
else:
    print("年龄不够，不能进行投票")


# if elseif else
#
# 4岁免费，4到12 收半价
# 12以上收全家票

age5 =2
if age5<4:
    print("free")
elif age5<12 and age5>=4:
    print("only half price")
else:
    print("all price")


#if elseif elseif else
# 4岁免费，
# 4到12 收半价
# 12以上收全家票
#65岁的免费
age5 =6
if age5<4:
    print("free")
elif age5<12 and age5>=4:
    print("only half price")
elif age5>=65 :
    print("free")
else:
    print("all price")



# 省略 else
age5 =3
if age5<4:
    print("free")
elif age5<12 and age5>=4:
    print("only half price")
elif age5>=65 :
    print("free")
elif age5>=12 and age5< 65:
    print("all price")

# 上面代码出错，或者匹配到都将不会执行
# 现在进行优化，不适用if elseif
lsy=['zs','ls','ww']
if 'zs'in lsy:
    print("张三存在")
if 'ls' in lsy:
    print("李四存在")
if 'ww'in lsy:
    print("王五存在")


#使用if 处理列表，检查特殊元素
#需求：在披萨店制作披萨时，没添加一种配料就打印一条信息。
#然而披萨店的青椒用完了，改如何处理呢？在披萨中提前进行配料个数检查，
# 如果不存在，就提示给顾客不能点青椒的原因

pizza= ['one','two','three']
for s in pizza:
    if s =='two':
        print("原料two 不存在，不能进行添加")
    else:
        print(s+"被加入到披萨中")


# 列表的判断空处理

pz=[1,2]
if pz :
    for i in pz:
        print(i)
else:
   print("列表是空的，是否创建")

pz=[]
if pz :
    for i in pz:
        print(i)
else:
   print("列表是空的，是否创建")
