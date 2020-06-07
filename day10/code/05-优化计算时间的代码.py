import time


def cal_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print("代码运行的时间：{}".format(end - start))


def demo():
    print("hello")
    time.sleep(3)
    print("world")


cal_time(demo)
