# 在程序运行的过程中，程序无法正常运行时报错
def div(a, b):
    return a / b


try:
    x = div(5, 0)
except Exception as e:
    print('程序出错')
else:
    print(x)
