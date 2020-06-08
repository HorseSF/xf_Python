# 一个模块本质上就是一个py文件

# 导入模块后可以使用模块里的变量和方法
import my_module

# 使用 from module_name import * 导入这个模块里的"所有"的变量和函数
# 本质是读取模块里的__all__属性，看这个属性里定义了哪些变量和函数
# 如果模块里没有定义__all__才会导入所有不以_开头的变量和函数
from demo import *
from hello import *

print(my_module.a)
my_module.test()
print(my_module.add(1, 2))

# 使用from demo import * 写法，不需要再写模块名
# 定义__all__属性后不能使用n
# print(n)
test()

print(x)
print(y)

import hello

# print(hello._age)
# hello._bar()
