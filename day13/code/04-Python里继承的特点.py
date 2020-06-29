class A(object):
    def demo_a(self):
        print('我是A类里的方法demo_a')

    def foo(self):
        print('我是A类里的foo方法')


class B(object):
    def demo_b(self):
        print('我是B类的方法demo_b')

    def foo(self):
        print('我是B类里的foo方法')


# Python里可以多继承
class C(A, B):  # 如果不写父类，Python3以后默认object
    pass


c = C()
c.demo_a()
c.demo_b()

# 如果两个不同类有同名方法，有一个类属性可以查看方法的调用顺序
c.foo()
print(C.__mro__)