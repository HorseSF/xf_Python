# filter 对可迭代对象过滤，得到filter对象。Python2里是内置函数，python3里修改成内置类

ages = [12, 23, 30, 17, 16, 22, 19]
# filter可以给定两个参数，第一参数是函数，第二个参数是可迭代对象
x = filter(lambda ele: ele > 18, ages)
# 得到filter可迭代对象
print(x)  # <filter object at 0x10b53dfa0>

# for a in x:
#     print(a)
adult = list(x)
print(adult)
