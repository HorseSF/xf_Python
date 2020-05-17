# range内置类，用来生成指定区间的整数序列
# 注意：in的后面必须是一个可迭代对象
# 字符串， 字典，元组，集合，range
for i in range(0, 10):
    print(i)

for y in 'hello':
    print(y)

z = 0
for i in range(1, 101):
    z += i
print(z)
