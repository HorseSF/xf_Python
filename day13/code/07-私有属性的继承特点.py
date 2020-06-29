class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('我是Animal类里的test方法')


class Person(Animal):
    pass


p = Person('张三', 18)
print(p.name)
p.eat()

# 私有方法不能被继承
# p.__test()
