# 类的继承
# 父类的创建

class Car:
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


# 定义子类， python 只要父类在其上面，下面的就是子类

class ElastricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElastricCar('tesla', 'models', '2016')
print(my_tesla.get_sescribe_name())
