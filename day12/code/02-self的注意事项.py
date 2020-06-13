class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 20)

p1.eat()