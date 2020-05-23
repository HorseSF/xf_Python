# 可变类型和不可变类型

# 不可变数据类型：字符串，数字，元组 如果修改值内存地址发生变化
# 可变类型：列表，字典，集合 如果修改值内存地址不发生变化
# 使用内置函数id可以获得变量的内存地址

# a = 12
# b = a
# print("修改前, a={}, b={}".format(id(a), id(b)))
# a = 10
# print(b)
# print("修改后, a={}, b={}".format(id(a), id(b)))
#
# nums1 = [100, 200, 300]
# nums2 = nums1
# print("修改前, nums1={}, nums2={}".format(id(nums1), id(nums2)))
# nums1[0] = 1
# print(nums2)
# print("修改后, nums1={}, nums2={}".format(id(nums1), id(nums2)))

x = [100, 200, 300]
y = x  # x和y指向了同一个内存空间
z = x.copy()
print("%x,%x,%x" % (id(x), id(y), id(z)))

x[0] = 1
print(x, y, z)

# 除了使用列表的copy()方法以外，可以使用copy模块的copy方法

import copy

a = copy.copy(x)  # 效果等价于x.copy()，都是浅拷贝

# 切片就是浅拷贝
names1 = ["张三", "李四", "王五"]
names2 = names1[::]
names1[0] = "jerry"
print(names2)
