ages = [12, 23, 30, 17, 16, 22, 19]

# 对每个元素执行指定行为
m = map(lambda ele: ele + 2, ages)
print(list(m))
