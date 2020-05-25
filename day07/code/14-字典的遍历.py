person = {"name": "zhangsan", "age": 18, "height": 180}

# 遍历方式
# for...in遍历
for x in person:  # for...in循环获取key
    print(x, "=", person[x])

# 获取所有key，之后遍历key
print(person.keys())  # dict_keys(['name', 'age', 'height'])
for k in person.keys():
    print(k, "=", person[k])

# 获取所有value 只能拿到值不能拿到key
for v in person.values():
    print(v)

# 遍历键值对
print(person.items())  # dict_items([('name', 'zhangsan'), ('age', 18), ('height', 180)])
for item in person.items():
    print(item[0], "=", item[1])

for k, v in person.items():
    print(k, "=", v)
