import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10

    def get_money(self):
        print('{}查询了余额。'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, qian):
        if type(qian) != int:
            print('设置的余额不合法')
            return
        print('{}修改了余额。'.format(datetime.datetime.now()))
        self.__money = qian

    def __test(self):
        print('我是test私有函数，外部不能调用')


p = Person('zhangasan', 18)
print(p.name, p.age)
# print(p.__money)  # 私有变量不能直接获取

# 获取私有变量的方式
# 1.使用 对象.类名__私有变量名获取
print(p._Person__money)

# 2.定义get和set方法来获取
print(p.get_money())
p.set_money(2000)

# 3. 定义property来获取
