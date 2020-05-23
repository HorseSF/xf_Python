# 删除数据 pop remove clear
masters = ["王昭君", "甄姬", "貂蝉", "妲己", "小乔", "大乔"]

# 输出指定位子的元素，默认删除最后一个
x = masters.pop(3)
print(x)
print(masters)

# 删除指定元素 数据在列表中不存在会报错
masters.remove("小乔")
print(masters)

# 使用del删除元素
del masters[3]
print(masters)

# 清空列表
masters.clear()
print(masters)

# 查找数据
tanks = ["亚瑟", "程咬金", "盾山", "张飞", "廉颇", "程咬金"]

# 返回index，不存在报错
print(tanks.index("盾山"))

# 返回元素个数
print(tanks.count("程咬金"))

# in运算符
print("张飞" in tanks)

# 修改元素
# 使用下标直接修改
tanks[5] = "凯"
print(tanks)