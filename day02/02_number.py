# 整数：Python可以处理任意大小的整数（包括负整数）
# 在程序中表示和数学写法一样

num1 = 10
num2 = num1
# 连续定义多个变量
num3 = num4 = num5 = 1
print(num3,num4,num5)

# 交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7)

# 浮点数：浮点型由整数部分与小数部分组成
# 浮点运算可能会有四舍五入的误差

f1 = 1.1
f2 = 2.2
print(f1 + f2)

# 复数：实数部分和虚数步部分组成

# 数字类型转换
# float->int
print(int(1.1))
print(int(1.9))

# int->float
print(float(1))

# str->int
print(int("123"))
print(int("+123"))
print(int("-123"))