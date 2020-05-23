# 遍历
killers = ["李白", "兰陵王", "韩信", "张云", "阿珂", "孙悟空"]

# for...in循环的本质就是不断调用迭代器next方法查找下一个数据
for killer in killers:
    print(killer)

i = 0
while i < len(killers):
    print(killers[i])
    i += 1
