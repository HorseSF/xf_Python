# 手动指定Person的父类是object
class Person(object):
    pass


# 没有指定Student的父类，Python3里默认继承object
class Student:
    pass

# 新式类和经典类的概念
# 1.新式类：继承自object的类我们称为新式类
# 2.经典类：不继承自object的类

# 在Python2里，如果不手动的指定一个类的父类是object，这个类就是一个经典类
# Python3里不存在经典类，都是新式类
