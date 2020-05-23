nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 调用sort()方法排序, 直接对原有的列表进行排序
# nums.sort(reverse=True)
# print(nums)

# 调用sorted方法排序，不会改变原有列表数据
sorted(nums)
print(nums)
print(sorted(nums))

# 列表元素反转
names = ["zhangsan", "lisi", "wangwu"]
names.reverse()
print(names)
print(names[::-1])
