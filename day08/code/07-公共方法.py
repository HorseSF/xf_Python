# +：可以用来拼接，用于字符串，元组，列表
print("hello" + "world")
print(("good", "yes") + ("hi", "ok"))
print([1, 2, 3] + [4, 5, 6])

# -：只能用集合，求差集
print({1, 2, 3} - {3})

# *：可以用于字符串,元组,列表，表示重复多次
print("hello" * 3)
print([1, 2, 3] * 3)
print((1, 2, 3) * 3)

# in：成员运算符
print("a" in "abc")
print(1 in [1, 2, 3])
print(4 in (4, 5, 6))
# 用于字典判断key是否存在
print("zhangsan" in {"name": "zhangsan", "age": 18})
print(3 in {3, 4, 5})

# for...in：遍历
# 带下标的遍历
nums = [19, 82, 39, 12, 34, 58]
for x in enumerate(nums):
    pass

x = enumerate(nums)
for i, e in x:
    print("第%d个数据是%d" % (i, e))


