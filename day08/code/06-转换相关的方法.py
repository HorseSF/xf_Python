# 内置类 list tuple set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)  # 转换成为元组
print(x)

y = set(x)  # 转换成为集合
print(y)

# 使用内置方法eval,执行字符串里的代码
a = 'input("请输入您的用户名：")'
eval(a)

import json

# Python            JSON
# 字符串               字符串
# 字典                对象
# 列表，元组           数组

# JSON的使用，把列表，元组，字典转换为JSON字符串
person = {"name": "zhangsan", "age": 18, "gender": "female"}
# 字典传给前端页面或把字典写到一个文件里
m = json.dumps(person)  # 将字典，列表，元组，集合转成字符串
print(m)
print(type(m))

n = '{"name": "lisi", "age": 20, "gender": "male"}'
s = json.loads(n)  # 将字符串转成字典
print(s)
print(type(s))
