person = {"name": "zhangsan", "age": 18}
print(person["name"])

person["name"] = "lsii"
person["gender"] = "female"

# 如果key存在，修改key值对应的value
# 如果key值不存在会报错
print(person)

# 删除指定连接
# 删除元素
person.pop("name")
print(person)

# 删除键值对
result = person.popitem()
print(person, result)

# 清空字典
print(person.clear())