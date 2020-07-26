import sys
import file_manager
import student_manager
import model


# 注册功能
def register():
    data = file_manager.read_json('data.json', {})

    while True:
        teacher_name = input('请输入账号(3-6位)：')
        if not 3 <= len(teacher_name) <= 6:
            print('账号不符合要求，请重新输入！')
        else:
            break

    if teacher_name in data:
        print('注册失败！该账户已经被注册了！')
        return

    while True:
        password = input('请输入账号(6-12位)：')
        if not 6 <= len(password) <= 12:
            print('账号不符合要求，请重新输入！')
        else:
            break

    # 创建一个teacher对象,保存数据。
    t = model.Teacher(teacher_name, password)
    data[t.name] = t.password
    file_manager.write_json('data.json', data)


# 登录功能
def login():
    data = file_manager.read_json('data.json', {})
    teacher_name = input('请输入老师账号：')
    if teacher_name not in data:
        print('登录失败！该账户没有注册！')
        return
    password = input('请输入密码：')
    import tools
    if data[teacher_name] == tools.encrypt_password(password):
        student_manager.name = teacher_name
        student_manager.show_manager()
    else:
        print('密码错误！登录失败！')


# 主函数
def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n请选择(1-3)：')

        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            # break
            # exit(0)
            sys.exit(0)
        else:
            print('输入有误')


if __name__ == '__main__':
    start()
