class Student(object):
    __slots__ = ("name", "age", "city")  # 这个属性直接定义在类里，用来规定对象可以存在的属性

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print("大家好，我是", self.name)


# 1. 调用__new__方法，用来申请内存空间
# 2. 调用__init__方法，并让self指向申请好的内存空间
# 3. 让变量s1指向创建好的内存空间
s1 = Student("张三", 18)
print("s1的名字", s1.name)
s1.say_hello()

s2 = Student("jack", 21)
s2.say_hello()

s = Student("李四", 18)
s.say_hello()
# print(s.height)  # AttributeError

# 动态属性
# 直接使用=号给属性赋值，如果属性不存在会添加新属性，如果属性存在会修改属性值
s.city = "上海"
print(s.city)
