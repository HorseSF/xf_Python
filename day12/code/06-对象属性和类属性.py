class Person(object):
    type = '人类'  # 这个属性定义在类里，称为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象 p 是通过 Person 类创建出来的实例对象
# name 和 age 是对象属性，在 __init__ 方法里，以参数的形式定义
p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

# 类属性可以通过类对象和实例对象获取
print(Person.type)
print(p1.type)

# 类属性只能通过类对象来修改，实例对象无法修改
Person.type = 'human'
print(Person.type)
