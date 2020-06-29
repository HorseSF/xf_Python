# open 参数
# file：用来指定打开的文件（不是文件名，而是文件的路径）
# mode：打开文件时的模式，默认是 r 表示只读
# encoding：打开文件时的编码方式

# 路径分为两种
# 1. 绝对路径：从电脑盘符开始
file = open('/Users/maxiaofei/work/Python/xf_Python/day13/code/xxx.txt')
print(file.read())
file.close()

# 2. 相对路径：当前文件所在的文件夹开始的路径
file = open('xxx.txt')
print(file.read())
file.close()