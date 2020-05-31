from functools import reduce

# reduce以前是一个内置函数
# 内置类和内置函数都在builtins.py文件里

scores = [100, 89, 76, 87]
print(reduce(lambda ele1, ele2: ele1 + ele2, scores))

students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 21, "score": 97, "height": 185},
    {"name": "jack", "age": 22, "score": 100, "height": 175},
    {"name": "tony", "age": 23, "score": 90, "height": 176},
    {"name": "henry", "age": 20, "score": 95, "height": 172}
]

# def bar(x, y):
#     return x + y["age"]
#
#
# print(reduce(bar, students, 0))

print(reduce(lambda x, y: x + y["age"], students, 0))
