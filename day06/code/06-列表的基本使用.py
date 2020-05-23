# 保存多个数据
name1 = "张三"
name2 = "李四"
name3 = "王五"
name4 = "jack"

# 使用[]来表示一个列表，每个数据称为元素，元素之间使用逗号隔离
names = ["张三", "李四", "王五", "张飞", "关羽"]

# 使用list(可迭代对象)将可迭代对象转换成一个列表
listNames = list(("兰陵王", "东皇太一", "王昭君", "程咬金"))

# 通过下标修改
print(names[3])
names[3] = "花木兰"
print(names)

# 通过下标切片
print(names[1:4])