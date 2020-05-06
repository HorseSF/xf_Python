# 输入三个数，输出较大值

num1 = int(input("输入第一个数"))
num2 = int(input("输入第二个数"))
num3 = int(input("输入第三个数"))

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
elif num3>num1 and num3>num2:
    print(num3)
else:
    print("一样大")
