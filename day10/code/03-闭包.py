def outer():
    x = 10

    def inner():
        nonlocal x  # 此时修改外部的x变量
        y = x + 1
        # x = 20  # 不是修改外部的x变量，而是在inner函数内部又创建了一个新的变量x
        # 在内部函数修改外部函数的局部变量
        x = 20
        print("inner里的y:", y)
    return inner


outer()()
