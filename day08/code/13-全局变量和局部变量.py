a = 100  # 这个变量是全局变量，在整个pv文件里都可以访问
word = "hi"

def test():
    x = "hello"  # 这个变量是在函数内部定义的变量，只能在函数内部使用
    print("x = {}".format(x))

    a = 10  # 在函数内部定义一个局部变量
    print("函数内部a={}".format(a))

    # 在函数内部修改外部全局变量
    global word
    word = "ok"
    print(locals())

test()
print("函数外部a={}".format(a))
print("函数外部word={}".format(word))

#  内置函数
#  globals() 查看全局变量
#  locals() 查看局部变量

print(globals())

# 在python里，只有函数能够分隔作用域
if 3 > 2:
    m = "hello"
print(globals(m))
