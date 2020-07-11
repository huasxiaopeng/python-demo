# 类属性的修改
class Car():
    def __init__(self, make, model):
        """初始化汽车属性"""
        self.make = make,
        self.model = model,

    def get_describe_car_name(self):
        """返回汽车的整体描述信息"""
        long_name = self.make + self.model
        return long_name


my_new_car = Car("audi", "a4")
print(my_new_car.get_describe_car_name())
