def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数只会执行一个return语句
    # 特殊情况下(finally语句)，一个函数会执行多个return语句
    # return表示一个函数的结束
    # return [x, y]
    # return {"x": x, "y": y}
    return x, y


shang, yushu = test(8, 3)
print("商是{},余数是{}".format(shang, yushu))
