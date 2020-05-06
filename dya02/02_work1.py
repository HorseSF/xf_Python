# 判断3位水仙花数
num = int(input("输入一个三位数："))

# 百位
x = int(num/100%10)

# 十位
y = int(num/10%10)

# 个位
z = int(num%10)


if num == x**3+y**3+z**3:
    print("水仙花数")
else:
    print("非水仙花数")






