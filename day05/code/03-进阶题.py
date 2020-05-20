# 使用循环计算0-100的和
# num = 0
# for i in range(1, 101):
#     num += i
# print(num)

# 统计100以内，个位数是2并能被3整除的数的个数
# result = 0
# for i in range(1, 101):
#     if (i % 10 == 2) and (i % 3 == 0):
#         result += 1
# print(result)

# 输入一个正整数，求他是几位数
# num = int(input("请输入一个整数："))
# count = 0
# while True:
#     num = num // 10
#     count += 1
#     if num == 0:
#         break
# print(count)

# 打印水仙花数
# for i in range(100, 1000):
#     x = i % 10
#     y = i // 10 % 10
#     z = i // 100
#     if x**3 + y**3 + z**3 == i:
#         print(i)

# 不停输入数字，如果为0则停止程序
while True:
    num = int(input("输入一个数字："))
    if num == 0:
        print("程序结束")
        break
