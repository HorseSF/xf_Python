#  根据输入百分制打印及格不及格

# score = float(input("请输入您的成绩："))

# if 100 >= score >= 60:
#     print("及格")
# elif (score < 60) and (score >= 0):
#     print("不及格")
# else:
#     print("输入有错")

# 根据年龄打印成年未成年，年龄不在范围内打印不是人
# age = int(input("请输入年龄："))

# # if 0 <= age < 18:
# #     print("未成年")
# # elif 18 <= age <= 150:
# #     print("成年")
# # else:
# #     print("不是人")
#
# if 150 >= age >= 0:
#     if age < 18:
#         print("未成年")
#     else:
#         print("成年")
# else:
#     print("这不是人")

# 输入两个整数，相减输出结果为奇数则输出结果，否则输出结果不是奇数
# num1 = int(input("请输入第一个数"))
# num2 = int(input("请输入第二个数"))
#
# num = num1 - num2
# if num % 2 != 0:
#     print("结果是：", num)
# else:
#     print("结果不是奇数")

# 用for循环输入0-100的奇数
# i = 0
# for i in range(0, 101):
#     if i % 2 != 0:
#         print(i)
#
#     if i % 2 ==0:
#         continue
#     print(i)

# 用while语句打印0-100的所有偶数
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
