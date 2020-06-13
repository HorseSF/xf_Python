class Person(object):
    '''
    这是一个人类
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 'name':'zhangsan','age':18,'eat':<function>
p = Person('zhangsan', 18)
print(dir(p))

print(p.__class__)  # <class '__main__.Person'>
print(p.__dict__)  # 把对象的属性和值转换为字典
print(p.__dir__())  # 等价于dir(p)
print(p.__doc__)  # 显示备注
print(range.__doc__)
print(p.__module__)  # __main__
