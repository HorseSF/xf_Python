# 小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
# 小美今年17岁，身高1.65，小美不跑步，喜欢吃东西

# 定义类:
# 使用class来定义一个类，一般遵守大驼峰命名法。
# 1. class <类名>：
# 2. class <类名>(object):


class Student(object):
    def __init__(self, name, age, height):  # 在__init__方法里，以参数的形式定义属性
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print("正在跑步")

    def eat(self):
        print("正在吃东西")


# 使用Student类创建了两个实例对象
s1 = Student("小明", 18, 1.75)
s2 = Student("小美", 17, 1.65)

# 根据业务逻辑让不同对象执行不同行为
s1.run()
s1.eat()

s2.eat()
