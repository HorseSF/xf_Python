def calc(a, b, fn):
    return fn(a, b)


# def add(x, y):
#     return x + y


# def minus(x, y):
#     return x - y


# 回调函数
# x1 = calc(1, 2, add)
# x2 = calc(10, 5, minus)
# print(x1)
# print(x2)

x3 = calc(1, 2, lambda x, y: x + y)
x4 = calc(19, 3, lambda x, y: x - y)
x5 = calc(2, 7, lambda x, y: x / y)

print(x3, x4, x5)
