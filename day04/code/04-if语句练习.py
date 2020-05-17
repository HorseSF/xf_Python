# 判断一个数是否能同时被3和7整除
# num1 = int(input("输入一个数"))
#
# if (num1 % 3 == 0) and (num1 % 7 == 0):
#     print("能被3和7整除")
# else:
#     print("不能被3和7整除")

# 判断一个数是否能被3或7整除
# num2 = int(input("输入一个数"))
#
# if (num2 % 3 == 0) and (num2 % 7 != 0):
#     print("能被3整除")
# elif (num2 % 3 != 0) and (num2 % 7 == 0):
#     print("能被3整除")
# else:
#     print("不能被3或7整除")

# 输入年判断是否是闰年
# year = int(input("输入年份："))
#
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print("是闰年")
# else:
#     print("不是闰年")

# 输入秒，计算到少小时，多少分，多少秒
# time = int(input("输入秒："))
#
# hour = time // 3600
# minute = time % 3600 // 60
# second = time % 60
# print(hour, minute, second)

# 判断身材是否正常
# 体重/身高的平方在18.5-24.9之间属于正常
weight = float(input("输入体重（kg）:"))
height = float(input("输入身高（m）："))

BMI = weight / height ** 2
if 18.5 < BMI < 24.9:
    print("正常")
print(BMI)
