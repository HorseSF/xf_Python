# 声明一个字典保存学校信息，学生信息中包括：姓名，年龄，成绩，电话，性别
# student = {"name": "zhangsan", "age": 18, "socre": 98, "tel": "13888889988", "gender": "female"}

# 声明一个列表，在列表中保存6个学生信息
students = [
    {"name": "zhangsan", "age": 18, "score": 98, "tel": "13888889988", "gender": "female"},
    {"name": "lisi", "age": 28, "score": 95, "tel": "138666666666", "gender": "male"},
    {"name": "wangwu", "age": 21, "score": 98, "tel": "13855555555", "gender": "unknown"},
    {"name": "chris", "age": 17, "score": 58, "tel": "13777778888", "gender": "male"},
    {"name": "jack", "age": 18, "score": 52, "tel": "13666666666", "gender": "female"},
    {"name": "tony", "age": 15, "score": 89, "tel": "13888889999", "gender": "unknown"}
]

# 统计不及格的人数
count = 0
for student in students:
    if student["score"] < 60:
        count += 1
print("不及格的学生%d人" % count)

# 打印不及格的学生名字及成绩
for student in students:
    if student["score"] < 60:
        print("不及格的学生姓名%s,成绩%d" % (student["name"], student["score"]))

# 统计未成年学生的个数
count = 0
for student in students:
    if student["age"] < 18:
        count += 1
print("未成年学生人数%d" % count)

# 打印手机尾号是八的学生姓名
for student in students:
    if student["tel"].endswith("8"):
        print("%s的手机号以8结尾" % student["name"])

# 打印最高分和学生的姓名
max_score = 0
max_index = []
for i, student in enumerate(students):
    if max_score <= student["score"]:
        max_score = student["score"]
        max_index.append(i)
        print(max_index)
else:
    for z in range(len(max_index)):
        print("%s最高分是%d" % (students[max_index[z]]["name"], max_score))

# 删除性别不明的学生
# 将不删除的数据抽出放入新列表
new_student = [x for x in students if x["gender"] != "unknown"]
print(new_student)

# 倒写循环删除数据
i = 0
for i in range(len(students) -1,-1,-1):
    if students[i]["gender"] == "unknown":
        students.remove(students[i])
print(students)

# 按学生成绩从大到小排序
for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1):
        if students[i]["score"] < students[i + 1]["score"]:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
