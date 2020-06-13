class Singlenton(object):
    __instance = None  # 类属性
    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，把一个对象的类型设置为cls
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False


# 1. 调用 __new__ 方法申请内存
# 如果不重写 __new__ 方法，会调用 object 的 __new__ 方法
# object 的 __new__ 方法会申请内存
# 如果重写了 __new__ 方法，需要自己手动的申请内存
s1 = Singlenton('hehe', 'heihei')
s2 = Singlenton('haha', 'xixi')

print(s1 is s2)  # True
print(s1.a, s1.b)
print(s2.a, s2.b)
