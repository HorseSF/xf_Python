# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write 只能写入字符串 或者 二进制
# 字典，列表，数字等都不能直接写入到文件里

# 将输入转换为字符串：repr/str 使用json模块
# json 本质就是字符串，区别在于json里要使用双引号表示字符串

# 将数据转换成二进制
# 将数据转换成为二进制：使用pickle模块

import json

names = ['zhangsan', 'lisi', 'jack', 'tony']
# x = json.dumps(names)  # ["zhangsan", "lisi", "jack", "tony"]
#
file = open('name.txt', 'w')
# file.write(x)

# json里将数据持久有两个方法：
# dumps:将数据转换成json字符串，不会将数据保存到文件里。
# dump：将数据转换成字符串同时写入到指定文件。

# json 反序列化也有两个方法：
# loads：将 json 字符串加载成为 Python 里的数据
# load：读取文件，把读取的内容加载成为 Python 里的数据
json.dump(names, file)
file.close()

x = '{"name":"zhangsan","age":18}'
p = json.loads(x)
print(p, type(p))
print(p['name'])

# load 读取一个文件，并把文件里的 json 字符串加载成为一个对象
file1 = open('name.txt', 'r')
y = json.load(file1)
print(y)
print(y[0])
file1.close()


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('henry', 20)
print(json.dump(p))
