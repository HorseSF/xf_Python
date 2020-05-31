# 1.函数的声明，使用关键字def来声明一个函数
# 2.函数的格式 def 函数名(形参1，形参2...)
# 3.函数的调用 函数名(实参1，实参2...)
# 4.函数的返回值 使用return语句返回函数的执行结果
# 5.函数返回多个结果，就是将多个数据打包成一个整体返回

def get_sum(a, b):
    """
    获取两个数字的和
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 和
    """
    return a + b


x = get_sum(1, 3)
print(x)


def print_sum(a, b):
    print(a + b)


print_sum(4, 5)


def calc(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


m, n = calc(15, 4)
print(m, n)
