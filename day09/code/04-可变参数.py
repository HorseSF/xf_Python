def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(1, 3))
print(add(1, 3, 9, 5, 4, 2, 0))


# 形参，可变参数，缺省参数, 可变关键字参数
# def add(a, b, *args, mul=1, **kwargs):
def test(a, b, *args, mul=1, **kwargs):
    c = a + b
    print("kwargs = {}".format(kwargs))
    for arg in args:
        c += arg
    return c * mul


print(test(1, 3, 5, 7, mul=2, x=0, y=0))
