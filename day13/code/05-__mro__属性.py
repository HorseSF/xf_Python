class A(object):
    pass


class B(object):
    def foo(self):
        print('我是B类里的foo方法')


class C(A):
    def foo(self):
        print('我是C类里的foo方法')


class D(B):
    pass


class X(D, C):
    pass


x = X()
# 继承：深度优先
x.foo()
print(X.mro())
