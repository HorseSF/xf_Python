a = b = c = d = 'hello'
print(a, b, c, d)

# 拆包
m, n = 3, 5
print(m, n)

x = 'hello', 'good', 'yes'
print(x)  # ('hello', 'good', 'yes')

# 拆包可变长度
o, *p, q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # 1 [2, 3, 4, 5] 6

