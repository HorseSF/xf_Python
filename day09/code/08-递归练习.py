# 使用递归求n！
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(6))


# 使用递归求斐波那也数列的第n个数字
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(8))
