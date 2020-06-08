# 没有设置__all__会读取除了以_开始的所有变量和函数
x = "hello"
y = 1000

# 以一个下划线开始的变量，建议只在本模块里使用。
_age = 19

_age += 1


def _bar():
    print("我是hello里的bar函数，我只能hello文件内部使用")


del (_age, _bar)
