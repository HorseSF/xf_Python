# 数学功能

# 绝对值
a1 = -10
print("绝对值", abs(a1))

# 比较两个数的大小
a3 = 100
a4 = 10
print((a3>a4)-(a3<a4))

# 返回给定参数的最大值
print(max(a3,a4))

# 给出给定参数的最小值
print(min(a3,a4))

# 求x的r次方
print(pow(2, 5))
print(2**5)

# 四舍五入 round(浮点型变量， 保留位数)
print(round(3.456))
print(round(3.546))
print(round(3.456,2))
print(round(3.546,1))

# 导入数学库
import math

# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

# 向下取整数
print(math.floor(18.1))
print(math.floor(18.9))

# 返回小数部分和整数部分的浮点型
print(math.modf(22.3))

# 开方
print(math.sqrt(16))
print(16**0.5)

# 随机数方法库
import random

# 随机数
# 从序列的元素里随机挑选
print(random.choice([1,3,5,7,9]))

# range(5) == [0,1,2,3,4]
print(random.choice(range(5)))

# "LUCK" = ["L","U","C","K"]
print(random.choice("LUCK"))

# 1-10之间的随机数
r1 = random.choice(range(10)) + 1
print(r1)

# 1到100之间的奇数
# random.randrange([start,]stop[,step])
# start 指定范围的开始值，包含范围内，默认0
# stop 指定范围的结束值，不包含范围内
# step 指定递增基数，默认1
print(random.randrange(1,100,2))

# 生成【0，1）之间的浮点数
print(random.random())

# 将列表顺序随机排列
list = [1,2,3,4,5]
random.shuffle(list)
print(list)

# 随机生成一个实数,范围[3,9]
print(random.uniform(3,9))

# 三角函数...