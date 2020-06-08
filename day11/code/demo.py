__all__ = ["m", "test"]
m = "yes"
n = 100


def test():
    print("我是demo模块里的test方法")


def foo():
    print("我是demo模块里的foo方法")


def division(a, b):
    return a / b


# __name__当直接运行时，值是__main__
# 当作为模块导入时，值是文件名
if __name__ == "__main__":
    print("demo里的__name__是：", __name__)
    print("测试division：", division(4, 2))
