def add(a: int, b: int):
    """
    这个函数用来将两个数字相加
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字相加结果
    """
    return a + b


print(add(1, 2))
help(add)

y = add("hello", "world")
print(y)
