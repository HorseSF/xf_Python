# 定义一个类属性，记录创建了多少个对象


class Person(object):
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return object.__new__(cls)

    def __init__(self, name, age):
        # Person.count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count


# 每次创建对象，都会调用 __new__ 和 __init__ 方法
p1 = Person('张三', 18)
p2 = Person('李四', 19)
p3 = Person('王五', 20)

print(Person.get_count())
