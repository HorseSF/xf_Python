import random

# 用来生成[2,9]的整数
print(random.randint(2, 9))

# 用来生成[0,1)的浮点数
print(random.random())

# 用来生成[a，b)的整数
print(random.randrange(2, 9))

# 可迭代对象里抽出数据
print(random.choice(["zhangsan", "lisi", "jack"]))

# 用来在可迭代对象里随机抽出n个数据
print(random.sample(["zhangsan", "lisi", "jack"], 2))
