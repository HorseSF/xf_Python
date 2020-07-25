# 可迭代对象：list/tuple/dict/set/str/range/filter/map
# for ... in 可迭代对象
from collections.abc import Iterable


# class Foo(object):
#     def __next__(self):
#         return 1


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):  # 重写了 __iter__ 方法后就是一个可迭代对象
        # return Foo()
        return self

    def __next__(self):
        #  每一个for...in都会调用一次__next__方法，获取返回值
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止


d = Demo(10)
print(isinstance(d, Iterable))  # isinstance：用来判断一个实例对象是否是由指定的类创建出来的

for x in d:  # for...in 循环的本质就是调用对象的 __iter__ 方法获取返回值，返回值是一个迭代器对象，然后再调用对象的 __next__ 方法
    print(x)

# names = list(('zhangsan', 'lisi'))
# print(isinstance(names, Iterable))


# for i in range(10):
#     print(i)
