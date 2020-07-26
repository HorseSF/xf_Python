import file_manager
import model

name = ''


def add_student():
    students_json = file_manager.read_json(name + '.json', {})
    if not students_json:
        students = []
        num = 0
    else:
        students = students_json['all_student']
        num = int(students_json['num'])

    while True:
        s_name = input('请输入学生姓名：')
        s_age = input('请输入年龄：')
        s_gender = input('请输入性别：')
        s_tel = input('请输入电话：')
        num += 1
        s_id = 'stu_' + str(num).zfill(4)

        # 创建Student对象
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)
        students.append(s.__dict__)

        # 拼接字典
        data = {'all_student': students, 'num': len(students)}

        # 把数据写入文件
        file_manager.write_json(name + '.json', data)
        choice = input('添加成功！\n1.继续\n2.返回\n请选择(1-2)')
        if choice == '2':
            break
        elif choice != '2' and choice != '1':
            print('输入有误！')


def show_student():
    x = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他：返回\n请选择：')

    student_json = file_manager.read_json(name + '.json', {})
    # if not student_json:
    #     students = []
    # else:
    #     students = student_json['all_student']
    students = student_json.get('all_student', [])

    # if x == '1':
    #     for student in students:
    #         print('学号：{id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))
    # elif x == '2':
    #     count = 0
    #     s_name = input('请输入学生姓名：')
    #     for student in students:
    #         if student['name'] == s_name:
    #             print('学号：{id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))
    #             count += 1
    #     if count == 0:
    #         print('没有找到指定学生！')
    # elif x == '3':
    #     count = 0
    #     s_id = input('请输入学号：')
    #     for student in students:
    #         if student['id'] == s_id:
    #             print('学号：{id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))
    #             count += 1
    #             break
    #     if count == 0:
    #         print('没有找到指定学生！')
    # else:
    #     return

    if x == '1':
        pass
    elif x == '2':
        s_name = input('请输入学生姓名：')
        students = filter(lambda s: s['name'] == s_name, students)
    elif x == '3':
        s_id = input('请输入学生ID：')
        students = filter(lambda s: s['s_id'] == s_id, students)
    else:
        return

    if not students:
        print('未找到学生')
        return

    for student in students:
        print('学号：{id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))


def modify_student():
    pass


def delete_student():
    student_json = file_manager.read_json(name + '.json', {})
    all_students = student_json.get('all_student', [])
    key = value = ''

    x = input('1.按姓名删除\n2.按学号删除\n其他：返回\n请选择：')
    if x == '1':
        key = 'name'
        value = input('请输入学生姓名：')
    elif x == '2':
        key = 'id'
        value = input('请输入学生ID：')
    else:
        return

    students = list(filter(lambda s: s.get(key, '') == value, all_students))

    if not students:
        print('未找到学生')
        return

    for i, student in enumerate(students):
        print('{x} 学号：{id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(x=i, **student))

    del_index = input('请输入需要删除的学生的标号(0-{}),q-返回：'.format(i))

    if not del_index.isdigit() or not 0 <= int(del_index) <= i:
        print('输入错误！')
        return

    # 删除学生
    all_students.remove(students[int(del_index)])
    student_json['all_student'] = all_students
    file_manager.write_json(name + '.json', student_json)


def show_manager():
    content = file_manager.read_file('students_page.txt') % name
    while True:
        print(content)
        operator = input('请选择(1-5)：')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delete_student()
        elif operator == '5':
            break
        else:
            print('输入错误！')
