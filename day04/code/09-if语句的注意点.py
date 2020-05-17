# 1. 区间判断
score = float(input("请输入您的成绩"))

# Python可以使用连续的区间判断
if 60 > score >= 0:
    print("不及格")

# 2. 隐式类型转换
# if后不是布尔值时，会自动转换为布尔值
if 4:
    print("hello world")

# 3. 三元表达式
num1 = int(input("请输入一个数字"))
num2 = int(input("请再输入一个数字"))

# if num1 > num2:
#     maxNum = num1
# else:
#     maxNum = num2
maxNum = num1 if num1 > num2 else num2
print(maxNum)

