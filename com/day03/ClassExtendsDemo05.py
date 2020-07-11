# 子类特有属性的初始化
# 父类
class Car1:
    def __init__(self, make, model, year=''):
        self.make = make
        self.model = model
        self.year = year
        self.odmter_read = 0

    def get_sescribe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_obd(self):
        print("获取属性为" + self.odmter_read)

    def update_obd(self, mils):
        if mils >= self.odmter_read:
            self.odmter_read = mils
        else:
            print("你不能修改")

    def increment_autoodd(self, mils):
        self.odmter_read += mils

    def addoil(self):
        print("加油功能")


# 定义子类， python 只要父类在其上面，下面的就是子类

class ElastricCar(Car1):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 电动车的特殊属性
        self.battery_size = 70

    # 定义特有的功能
    def descirbe_battery(self):
        print("特斯拉的标准电压为" + str(self.battery_size))

    # 电动车没有油箱，屏蔽加油功能
    def addoil(self):
        print("电动车没有油箱，不支持加油的操作")


# 调用
my_tesla1 = ElastricCar('tesla', 'models', '2020')
print(my_tesla1.get_sescribe_name())
my_tesla1.descirbe_battery()
