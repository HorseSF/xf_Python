class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)


p1 = Person('张三', 18)
p2 = Person('李四', 20)

persons = [p1, p2]

# 直接打印列表会调用列表里的元素的 __repr__ 方法
print(persons)  # [<__main__.Person object at 0x7fe64119adc0>, <__main__.Person object at 0x7fe6411698e0>]
