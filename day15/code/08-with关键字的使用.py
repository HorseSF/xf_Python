# try:
#     file = open('01-练习.py', 'r')
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     try:
#         file.read()
#     finally:
#         file.close()

# with关键字会关闭文件
try:
    with open('01-练习.py', 'r') as file:
        file.read()
except FileNotFoundError:
    print('文件不存在')

# with是上下文管理器
# 文件连接，socket连接，数据库连接都能使用with关键字自动关闭连接
# with关键字后的对象需要实现 __enter__ 和 __exit__ 魔法方法
