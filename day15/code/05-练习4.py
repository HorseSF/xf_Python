# 学生类 Student
# 属性：学号，姓名，年龄，性别，成绩

# 班级类 Grade
# 属性：班级名称，班级中的学生
# 方法：
# 1.查看该班级中的所有学生的信息
# 2.查看指定学号的学生信息
# 3.查看班级中成绩不及格的学生信息
# 4.将班级中的学生按照成绩降序排序


class Student(object):
    def __init__(self, number, name, age, gender, score):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return '学号：{}，姓名：{}，年龄：{}，性别：{}，成绩：{}'.format(self.number, self.name, self.age, self.gender, self.score)


class Grade(object):
    def __init__(self, grade_name, student_list=None):
        self.grade_name = grade_name
        if student_list is None:
            student_list = []
        self.student_list = student_list

    def show_students(self):
        if len(self.student_list) == 0:
            print('没有学生')
            print('----------')
            return

        print('{}共有{}名学生。'.format(self.grade_name, len(self.student_list)))
        for student in self.student_list:
            print(student)
        print('----------')

    def search_student(self, search_number):
        if len(self.student_list) == 0:
            print('没有学生')
            print('----------')
            return
        for student in self.student_list:
            if student.number == search_number:
                print(student)
                print('----------')
                return
        else:
            print('没有指定学生')
            print('----------')

    def show_failed_student(self):
        if len(self.student_list) == 0:
            print('没有学生')
            print('----------')
            return
        for student in self.student_list:
            if student.score < 60:
                print(student)
        print('----------')

    def order_student(self):
        # self.student_list.sort(key=lambda s: s.score, reverse=True)
        return sorted(self.student_list, key=lambda s: s.score, reverse=True)


s1 = Student(13233, '张三', 21, 'male', 87)
s2 = Student(12495, '李四', 19, 'male', 25)
s3 = Student(42501, '王五', 51, 'male', 60)
s4 = Student(36721, '赵六', 18, 'male', 59)
s5 = Student(25912, '孙七', 22, 'male', 61)

g = Grade('一班', [s1, s2, s3, s4, s5])
g.show_students()
g.search_student(13233)
g.show_failed_student()

for student in g.order_student():
    print(student)
