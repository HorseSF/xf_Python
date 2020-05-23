# 修改大小写

# 首字母大写
print("hello world.good morning".capitalize())

# 全大写
print("hello".upper())

# 全小写
print("HELLO".lower())

# 每个单词的首字母大写
print("hello world".title())

# 自定长度显示，长度不够右（左）边空格补齐
print("hello".ljust(10, "+"))
print("hello".rjust(10))

# 居中
print("apple".center(20, "*"))

# 去除空格
print("   apple   ".lstrip())
print("    apple    ".rstrip())
print("  apple   ".strip())

# 以某种固定格式显示的字符串切割成列表
x = 'zhangsan+lisi+wangwu+zhaoliu'
names = x.split("+")
print(names)

# 将列表转换成指定字符串
fruits = ['apple', 'pear', "peach"]
print("-".join(fruits))
print("*".join("hello"))
