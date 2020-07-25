# 系统内置的异常
# ZeroDivisionError：除0异常 1/0
# FileNotFoundError：文件不存在异常 open('xxx.txt')
# FileExistsError：文件存在异常 os.mkdir('test')
# ValueError：int('hello')
# KeyError：key不存在 person = {'name':'zhangsan'} person['age']
# SyntaxError：语法错误
# IndexError：脚标错误

# 要求输入用户名和密码，如果用户名和密码的长度在6-12位正确，否则不正确


class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}和{}之间'.format(self.x, self.y)


password = input('请输入密码:')
m = 6
n = 12

if m <= len(password) <= n:
    print('密码正确')
else:
    # print('密码不正确')
    # 使用raise关键字抛出异常
    raise LengthError(m, n)

# 把密码保存到数据库
print('将密码保存到数据库')
