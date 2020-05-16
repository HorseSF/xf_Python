a = '31'
b = int(a)
print(a)
print(b)

x = 'hello'
# y = int(x)  # ValueError: invalid literal for int() with base 10: 'hello'

x = '1a2c'
y = int(x, 16)  # 表字符串转成16进制
print(y)

m = '12'
n = int(m, 8)
print(n)
