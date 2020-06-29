class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    # def sleep(self):
    #     print(self.name + '正在睡觉')

    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    # def sleep(self):
    #     print(self.name + '正在睡觉')

    def study(self):
        print(self.name + '正在学习')


# Dog() 调用__new__方法，再调用__init__方法
# Dog里没有__new__方法，会查看父类是否重写了__new__方法
# 父类也没有重写__new__方法，查找父类的父类，找到object

# 调用__init__方法,Dog类没有实现，会自动找父类的__init__方法
d1 = Dog('大黄', 3)
print(d1)  # 父类的属性可以直接使用
d1.sleep()  # 父类的方法可以直接调用
d1.bark()  # 自己的方法可以直接调用

s1 = Student('小明', 18)
s1.sleep()
s1.study()
