persons = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 20},
    {"name": "wangwu", "age": 19},
    {"name": "jerry", "age": 21}
]

# 输入姓名，如果姓名存在，提示用户，如果姓名不存在，输入年龄

name = input("输入姓名")

for person in persons:
    if name == person["name"]:
        print("用户已经存在")
        break
else:
    age = input("输入年龄")
    new_person = {name: age}
    persons.append(new_person)
print(persons)
