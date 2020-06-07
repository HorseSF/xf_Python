# 模块：在Python里一个py文件就可以理解为一个模块
# 不是所有py文件都能作为一个模块来导入
# 如果想要让一个py文件能够被导入，模块名字必须要遵守命名规则
# python为了方便开发，提供了很多内置模块


import time  # import 模块名
from random import randint  # from 模块名 import 函数名 -> 导入方法
from math import *  # from 模块名 import * -> 导入模块的"所有"方法和变量
import datetime as dt  # import 模块名 as 别名
from copy import deepcopy as dp  # from 模块名 import 函数名 as 别名

# 导入模块后，可以使用模块的方法和变量
print(time.time())
# time.sleep(3)

# 只能使用导入的方法，不能使用模块
randint(0, 2)

# 调用时不需要加模块名
print(pi)

print(dt.MAXYEAR)

dp(["hello", "good"])

