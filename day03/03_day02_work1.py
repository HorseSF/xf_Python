# 水仙花数

num = int(input("输入一个三位数"))

a = num % 10
b = num // 10 % 10
c = num //100

if num == a**3 + b**3 + c**3:
    print("yes")
else:
    print("no")