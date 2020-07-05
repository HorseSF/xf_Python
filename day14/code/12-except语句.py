# try...except 语句用来处理程序运行过程中的异常

try:
    1 / 0
    file = open('ddd.txt')
    print(file.read())
    file.close()
# except Exception as e:  # 给异常起一个变量名e
#     print(e)

except (FileNotFoundError, ZeroDivisionError) as e:  # 处理指定类型的异常
    print(e)
