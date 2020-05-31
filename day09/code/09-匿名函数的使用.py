def add(a, b):
    return a + b


print("0x%X" % id(add))

x = add(4, 5)  # 函数名(实参)作用是调用函数，获取到函数的执行结果，并赋值给变量
print(x)

fn = add
print(fn)

print(fn(4, 5))

# 除了使用def关键字定义一个函数以为，还能使用lambda表达式定义一个函数
lambda a, b: a * b  # 匿名函数，用来表达一个简单的函数。

# 调用匿名函数两种方式
# 1.定义名字
mul = lambda a, b: a * b
print(mul(4, 5))

# 2.把函数当参数传给另一个函数