# 类
# 创建
# 小狗类蹲下和打滚
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def site(self):
        print(self.name.title()+"正在蹲下")

    def roll_over(self):
        print(self.name.title()+"正在打滚")



# 实例类
my_dog=Dog('wis','2')
print(my_dog.name.title()+"是我的狗,它今年"+my_dog.age+"岁了")

# 方法调用
my_dog.site()
my_dog.roll_over()

# 多个实例类
my_dog1=Dog('zb',3)
my_dog2=Dog('mnfdnjk',6)

print(str(my_dog1.age))
print(str(my_dog2.age))




