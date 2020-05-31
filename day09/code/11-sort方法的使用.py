# 列表的内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]

# nums.sort()
# print(nums)

# 不会改变原有数据，会生成新的有序列表
x = sorted(nums)
print(nums, x)

students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 21, "score": 97, "height": 185},
    {"name": "jack", "age": 22, "score": 100, "height": 175},
    {"name": "tony", "age": 23, "score": 90, "height": 176},
    {"name": "henry", "age": 20, "score": 95, "height": 172}
]

# def foo(ele):
#     # print(ele)
#     return ele["height"]


# 字典和字典之间不能使用比较运算
# students.sort()
# key需要一个函数
# students.sort(key=foo)

students.sort(key=lambda ele: ele["score"])
print(students)
