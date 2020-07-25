# with 语句后面的结果对象，需要重写 __enter__和 __exit__ 方法
# 当进入到with代码块时，会自动调用 __enter__ 方法
# 当with代码块执行完成后，会自动调用 __exit__ 方法


class Demo(object):
    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被执行了')


def create_obj():
    x = Demo()
    return x


# d = create_obj()

with create_obj() as d:  # as 变量名
    print(d)  # 变量 d 不是create_obj的返回结果，是创建的对象x调用 __enter__ 之后返回的结果
