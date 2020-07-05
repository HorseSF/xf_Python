# 建立一个汽车类auto
# 包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
# 至少要求 汽车能够加速 减速 停车

# 再定义一个小汽车类CarAuto 继承Auto，并添加空调，CD属性
# 并且重新实现方法覆盖加速，减速的方法


class Auto(object):
    def __init__(self, color, weight, speed=0, wheel_count=4):
        self.wheel_count = wheel_count
        self.color = color
        self.weight = weight
        self.speed = speed

    def change_speed(self, x):
        """
        修改车速
        :param x: 表示要修改的车速值。
        """
        if x == 0:
            self.speed = 0
            return
        self.speed += x


class CarAuto(Auto):
    def __init__(self, color, weight, ac, navigator, speed=0, wheel_count=4):
        super(CarAuto, self).__init__(color, weight, speed, wheel_count)
        self.navigator = navigator
        self.ac = ac


car = Auto('白色', 1.6)

car.change_speed(-10)
print(car.speed)

car.change_speed(30)
print(car.speed)

car.change_speed(-10)
print(car.speed)

car.change_speed(0)
print(car.speed)

car1 = ('黑色', 1.6, '美的', 'Android', 10, 5)
