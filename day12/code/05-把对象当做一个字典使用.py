class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        p.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('张三', 18)
print(p.__dict__)  # 将对象转换为字典
p['name'] = 'jack'  # 赋值调用__setitem__方法
print(p.name)

print(p['name'])  # 取值调用__getitem__方法

