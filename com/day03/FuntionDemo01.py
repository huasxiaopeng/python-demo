# 返回值函数
def tilte_name(first_name,last_name):
    """整洁 的name"""
    full_name=first_name+" "+last_name
    return  full_name.title()

mus=tilte_name('jim','block')
# 首字母大写
print(mus)


# 传递参数的可选型
# last_name 设置默认值，不传参数也不会引起函数出错
def title_name(first_name,middle_name,last_name='default'):
    if last_name:
        full_name=first_name+" "+middle_name+""+last_name
    else:
        full_name = first_name + " " + middle_name
    return full_name.title()



jsn=title_name("lk",'jmd','co')
print(jsn)

jsn=title_name("lk",'jmd')
print(jsn)

# 字典的返回

def build_person(first_name,last_name):
    person={"first":first_name,'last':last_name}

    return person

prs=build_person("lktbz",'xiao')
print(prs)

# 增加字段

def build_person(first_name,last_name,age=''):
    person={"first":first_name,'last':last_name}
    if age:
        person['age']=age
    return person

p2=build_person("lktbz",'xiao','20')
print(p2)


# 列表

def greet_users(names):
    for name in names:
        msg="hello,"+name.title()+"!"
        print(msg)

username=['ls','zs','ww']
greet_users(username)


# 函数中修改列表
# 需求：一家3D打印机需要打印的存放在一个列表，打印好的存档在一个列表
# 函数一：
# 模拟打印列表中个没个元素，打印好了，加载进新的列表中
# 函数二：
# 遍历新列表，为打印好的

# 打印添加函数
def change_list(inLists,outLists):
    while inLists:
        redys=inLists.pop();
        print("正在打印"+redys)
        outLists.append(redys)


def print_list(outLists):
    for out in outLists:
        print("已经打印的"+out)

inLists=['huawei','apple','xiaomi']
outLists=[]

change_list(inLists,outLists)
print_list(outLists)

# 多参数，没限制
def make_pizaa(*topping):
    """打印制作披萨的材料"""
    print(topping)

make_pizaa("red")
make_pizaa("red","yellow")
make_pizaa("red","black","yellow")