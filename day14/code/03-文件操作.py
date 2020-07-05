# Python里使用 open 内置函数来打开有一个文件
# file：文件的路径。相对路径和绝对路径
# mode：打开文件的模式，r：只读， w：写入， b：二进制， t：文本形式打开
# mode默认使用的 rt
# decoding：用来指定文件的编码方式，windows里默认gbk

# file = open('xxx.txt', 'w')
# file.write('你好')
# file.close()

file = open('xxx.txt')
# print(file.read())  # 将所有的数据读取出来
# print(file.readline())  # 只读取一行数据

# while True:
#     content = file.readline()
#     print(content)
#     if content == '':
#         break

# x = file.readlines()  # 读取所有行数据保存到列表里
# print(x)

x = file.read(5)  # 读取长度
print(x)

file.close()
