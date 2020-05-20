# 可迭代对象 str, list, tuple, dict, set, range
# str, list, tuple可以通过下标来获取或操作

word = "zhangsan"
print(word[4])

# word[4] = "x"
# 字符串是不可变数据类型

m = "abcdefghijklmopqrstuvwxyz"
print(m[2:9])  # 包含开头，不包含结尾
print(m[2:])  # 如果只用开头，则截取到最后
print(m[:9])  # 如果只有结尾，则从头截取
print(m[3:15:2])  # step步长，每隔step-1取一个
print(m[3:15:1])  # step默认1，不能为0
print(m[3:15:-1])  # 从右往左走,没数据
print(m[15:3:-1])  # 从右往左走，有数据
print(m[::])  # 从头到尾复制
print(m[::-1])  # 倒过来复制
print(m[-9:-5])  # 从右边开始数


