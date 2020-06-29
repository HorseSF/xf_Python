class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


p1 = Person('张三', 18)
p2 = Person('张三', 18)

s = Student('jack', 20)

# is身份运算符，比较两个对象的内存地址
print(p1 is p2)

# type()获取的就是类对象
if type(p1) == Person:
    print('p1是Person类创建的实例对象')

# type()无法获取父类对象
print(type(s) == Person)

# isinstance()用来判断一个对象是否是由指定的类(或者父类)实例化出来的
print(isinstance(s, Student))
print(isinstance(s, Person))

# issubclass()用来判断一个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))