# 魔法方法：是类里的特殊的方法
# 特点：
# 1. 不需要手动调用，会在合适的时间自动调用
# 2. 这些方法都是使用__开始__结束
# 3. 方法名都是系统规定好的


class Person(object):
    # 在创建对象时会自动调用这个方法
    def __init__(self, name, age):
        print("__init__方法被调用了")
        self.name = name
        self.age = age

    # 当对象被销毁时，会自动调用这个方法
    def __del__(self):
        print("__del__方法被调用")

    def __repr__(self):
        return "hello"

    def __str__(self):
        return "姓名：{}年龄：{}".format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print("__call__方法被调用了")
        fn = kwargs["fn"]
        return fn(args[0], args[1])


p = Person("zhangsan", 16)

# 如果不做任何修改直接打印对象，会打印对象模块名.类型和内存地址
# 当打印一个对象时，会调用对象的__str__或__repr__方法
# 如果两个方法都被重写了会只执行__str__
print(p)  # <__main__.Person object at 0x10622ed90>

# 手动调用魔法方法
print(p.__repr__())

# 重写__call__方法
n = p(1, 2, fn=lambda x, y: x + y)
print(n)
