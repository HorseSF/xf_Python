class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这个方法要打印对象的姓名
    def demo(self):
        print('姓名是', self.name)

    # 这个方法需要访问到类属性 type
    @classmethod
    def bar(cls):
        print(cls.type)

    # 这个方法只需要打印hello world
    @staticmethod
    def foo():
        print('hello world')


p = Person('zhangsan', 19)
p.demo()
p.bar()
p.foo()
