def test(a, b):
    x = a + b
    return x
    return 'hello'


def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        print('除数不能为0')
    else:
        return x
    finally:
        return '结束'  # finally会覆盖前面的返回值


print(demo(1, 1))
