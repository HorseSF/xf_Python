def test1():
    print("test1开始了")
    print("test1结束了")


def test2():
    print("test2开始了")
    test1()
    print("test2结束了")


test2()


# 求n到m之间所有整数之和
def add_int(n, m):
    count = 0
    for i in range(n, m):
        count += i
    return count


print(add_int(0, 101))


# 求一个n的阶乘
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(factorial(5))


# 计算m阶乘的和
def fac_sum(m):
    x = 0
    for i in range(1, m + 1):
        x += factorial(i)
    return x


print(fac_sum(5))
