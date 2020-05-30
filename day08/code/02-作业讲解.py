# 用三个元组表示三门学科选课学生（一个学生可以选多门课）

sing = ("李白", "白居易", "李清照", "杜甫", "王昌龄", "王维", "孟浩然", "王安石")
dance = ("李商隐", "杜甫", "李白", "白居易", "曾参", "王昌龄")
rap = ("李清照", "刘禹锡", "曾参", "王昌龄", "苏轼", "王维", "李白")

# 求选课学生人数 # 使用集合去重
total = set(sing + dance + rap)
print("选课人数%d" % len(total))

# 求只选了第一门课的学生姓名
sing_only = []
for person in sing:
    if person not in dance and person not in rap:
        sing_only.append(person)
print("只选择sing的有{}人，分别是{}".format(len(sing_only), sing_only))

# 求只选了一门课的学生数量和姓名
# 求只选了两门课的学生数量和姓名
# 求选了三门课的学生数量和姓名
total = sing + dance + rap
student_dict = {}
for p in total:
    if p not in student_dict:
        student_dict[p] = total.count(p)

for k, v in student_dict.items():
    if v == 1:
        print("报了1门课的有：", k)
    elif v == 2:
        print("报了2门课的有：", k)
    else:
        print("报了3门课的有：", k)
