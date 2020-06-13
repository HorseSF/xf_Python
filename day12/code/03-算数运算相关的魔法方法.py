class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return 'hello'

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other

    def __mul__(self, other):
        return self.name * other


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('zhangsan', 20)
print(p1 is p2)  # False

# ==运算符本质是调用对象的__eq__方法，获取__eq__方法的返回结果
print(p1 == p2)  # True

# !=运算符本质是调用__ne__方法 或者__eq__方法取反
print(p1 != p2)  # False

# >运算符本质是调用__gt__方法
print(p1 > p3)

# >=运算符本质是调用__ge__方法
print(p1 >= p2)

# <运算符本质是调用__lt__方法
print(p1 < p3)

# <=运算符本质是调用__le__方法
print(p1 <= p2)

# +运算符本质是调用__add__方法
print(p1 + p1)

# -运算符本质是调用__sub__方法
print(p1 - 10)

# *运算符本质是调用__mul__方法
print(p1 * 2)

# str()将对象转换成为字符串，会自动调用__str__方法
# 1.str()时调用 2.打印对象时调用
print(str(p1))  # 默认 <__main__.Person object at 0x7fe0dcf9ad90>
