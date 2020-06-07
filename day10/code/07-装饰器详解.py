import time


def cal_time(fn):
    def inner(x, *args, **kwargs):
        start = time.time()
        s = fn(x)
        end = time.time()
        print("代码耗时:", end - start)
        return s

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


@cal_time
def foo():
    print("hello")
    time.sleep(3)
    print("world")


# foo()
m = demo(1000000, "good", y="hello")
print(m)
