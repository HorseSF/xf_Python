# 定义一个点类 Pointer
# 属性是横坐标 x 与纵坐标 y
# 定义一个圆类 Circle
# 属性是圆心点 cp 与半径 radius
# 方法有：
# 1.求圆的面积
# 2.求圆的周长
# 3.求指定点与圆的关系
# 提示：关系有三种：圆内，圆外，圆上

import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp, radius):
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_length(self):
        return self.radius * 2 * math.pi

    def relationship(self, point):
        """
        求一个点和圆的关系。三种关系：圆内，圆上，圆外
        :param point: 需要判断的点
        """
        distance = (point.x - self.cp.x) ** 2 + (point.y - self.cp.y) ** 2
        if distance > self.radius ** 2:
            print("在圆外")
        elif distance < self.radius ** 2:
            print("在圆内")
        else:
            print("在圆上")


p = Pointer(3, 4)
c = Circle(p, 5)
print(c.get_area())
print(c.get_length())

p1 = Pointer(10, 10)
p2 = Pointer(2, 2)
p3 = Pointer(0, 0)
c.relationship(p1)
c.relationship(p2)
c.relationship(p3)
