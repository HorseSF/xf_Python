import time


def cal_time(fn):
    print("我是外部函数")
    print("fn={}", format(fn))

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时:", end - start)

    return inner


@cal_time  # 调用cal_time；把被装饰的函数传给fn；
def foo():
    x = 0
    for i in range(1, 100000):
        x += i
    print(x)


print("装饰后的foo={}".format(foo))
foo()  # 再次调用foo函数时，此时的foo函数已经不再是foo函数

