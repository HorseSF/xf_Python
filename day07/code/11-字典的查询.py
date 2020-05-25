person = {"name": "zhangsan", "age": 18, "x": "y"}

# 查找数据 字典是无序的，不能通过下标来获取
print(person["name"])  # 使用key获取value

x = "age"
print(person[x])
print(person["x"])

# print(person["height"])  # key值不存在会报错
# 如果key不存在，使用默认值
print(person.get("height"))  # key值不存在会返回None
print(person.get("gender", "female"))  # key值不存在会返回默认值

print(person)
