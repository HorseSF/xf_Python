a = 13
b = 20

# 方法1 使用第三变量

# 方法2 使用运算符，只能是数字
a = a + b
b = a - b
a = a - b

# 方法3 使用异或运算符
a = a ^ b
b = a ^ b
a = a ^ b

# 方法4 使用python特有
a, b = b, a

print(a)
print(b)
