def say_hello(name, age, city="襄阳"):
    print("大家好，我是{},我今年{}岁了,我来自{}".format(name, age, city))


say_hello("jack", 19)
say_hello(name="tony", age=20, city="北京")

# 缺省参数：有®些函数的参数是，如果传递了参数，就使用传递的参数，如果没有传递参数，就使用默认的值
