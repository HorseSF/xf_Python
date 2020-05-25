# 和列表很像，保存多个数据
# 元组和列表的区别，列表是可变的，元组是不可变数据类型

words = ["hello", "yes", "good", "hi"]
nums = (9, 4, 3, 1, 7, 6, 9, 3, 9)

# 和列表一样，也是一个有序的存储数据容器
# 可以通过下标来获取元素
print(nums[3])

# 查找下标
print(nums.index(7))

# 出现次数
print(nums.count(9))

# 特殊情况：如何表示只有一个元素的元组
# 如果元组中只有一个元素，后面要加，
ages = (18,)
print(type(ages))

# tuple(可迭代对象)
print(tuple("hello"))

# 列表 <==> 元组转换
print(tuple(words))
print(list(nums))

heights = ("189", "174", "170")
print("*".join(heights))
print("".join(('h', 'e', 'l', 'l', 'o')))

# 元组遍历
for i in nums:
    print(i)

j = 0
while j < len(nums):
    print(nums[j])
    j += 1
