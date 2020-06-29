# 面向对象编程的三大特性：封装，继承和多态

# 封装：打包，函数是对语句的封装，类是对函数和变量的封装


def test():
    a = 23
    a += 3
    print('hello')


class Person(object):
    type = '人类'

    def __init__(self):
        pass

    def eat(self):
        pass

# 继承：类和类之间可以手动的建立父子关系，父类的属性和方法，子类可以有条件的使用


# 多态：是一种技巧，提高代码的灵活度
