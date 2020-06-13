class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b


Calculator.add(1, 5)


class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法：会用到实例对象的属性，self指向调用这个方法的实例对象
    # 两种调用方式：
    # 1.实例对象.方法名 ==> 不需要手动给self传参，会自动将实例对象传递给self
    # 2.类对象.方法名 ==> 需要手动给self传参
    def eat(self, food):
        print(self.name + '正在吃' + food)

    # 如果一个方法里没用用到任何实例对象属性，可以将这个方法定义成static
    # 静态方法：如果一个方法即用不到实例对象，也用不到类对象，可以把这个方法定义为一个静态方法
    @staticmethod
    def demo():  # 默认的方法都是对象方法
        pass

    # 如果一个函数只用到了类属性，我们可以把定义成为一个类方法
    # 类方法：会有一个参数cls，cls指的是类对象
    # 如果一个方法只使用到类属性，可以将这个方法定义为类方法
    @classmethod
    def test(cls):  # cls指类对象，不需要手动传参
        print('yes')


p1 = Person('zhangsan', 18)

# 直接使用实例
# 实例对象在调用方法时，不需要给形参self传参，会自动把实例对象传递个self
p1.eat('红烧牛肉')

p2 = Person('lisi', 20)

print(p1.eat is p2.eat)

# 使用 类对象来调用类名。方法名()
# 这种方式，需要手动指定self
Person.eat(p2, '蛋炒西红柿')

# 类方法：可以使用实例对象和类对象调用
p1.test()
Person.test()
