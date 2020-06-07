# os：OperationSystem 操作系统
# os模块里提供的方法就是用来调用操作系统里的方法
import os

# 获取操作系统的名称 Windows系列 -> nt，非Windows系统 -> posix
print(os.name)

# 路径分隔符号 Windows系列 -> \，非Windows系统 -> /
print(os.sep)

# 获取文件的绝对路径
print(os.path.abspath("01-高阶函数.py"))

# 判断是否是文件夹
print(os.path.isdir("02-函数的嵌套.py"))

# 判断是否是文件
print(os.path.isfile("02-函数的嵌套.py"))

# 判断文件是否存在
print(os.path.exists("05-优化计算时间的代码.py"))

# 获取文件名和后缀
file_name = "2020.2.21.demo.py"
print(os.path.splitext(file_name))

# os里其他方法
os.getcwd()  # 获取当前的⼯工作⽬目录，即当前python脚本⼯工作的⽬目录
os.chdir('test')  # 改变当前脚本⼯工作⽬目录，相当于shell下的cd命令
os.rename('毕业论⽂文.txt', '毕业论⽂文-最终版.txt')  # ⽂文件重命名
os.remove('毕业论⽂文.txt')  # 删除⽂文件
os.rmdir('demo')  # 删除空⽂文件夹
os.removedirs('demo')  # 删除空⽂文件夹
os.mkdir('demo')  # 创建⼀一个⽂文件夹
os.chdir('C:\\')  # 切换⼯工作⽬目录
os.listdir('C:\\')  # 列列出指定⽬目录⾥里里的所有⽂文件和⽂文件夹
os.name  # nt->windows posix->Linux/Unix或者MacOS
os.environ  # 获取到环境配置
os.environ.get('PATH')  # 获取指定的环境配置
