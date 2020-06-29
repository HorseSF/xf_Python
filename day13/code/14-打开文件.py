# Python 里使用 open 内置函数打开并操作一个文件

# open 参数
# file：用来指定打开的文件（不是文件名，而是文件的路径）
# mode：打开文件时的模式，默认是 r 表示只读
# encoding：打开文件时的编码方式

# open 函数会有一个返回值
file = open('xxx.txt')
print(type(file))
print(file.read())

file.close()
