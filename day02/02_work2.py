# 判断5位回文数
num = int(input("输入一个五位数："))

# 万位
a = int(num/10000%10)

# 千位
b = int(num/1000%10)

# 百位
c = int(num/100%10)

# 十位
d = int(num/10%10)

# 个位
e = int(num%10)

if a==e and b==d:
    print("是回文数")
else:
    print("不是回文数")