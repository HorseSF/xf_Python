# 输入三个数，输出较大值

num1 = int(input("输入第一个数"))
num2 = int(input("输入第二个数"))
num3 = int(input("输入第三个数"))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print("max=",max)