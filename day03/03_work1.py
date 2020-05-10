# 判断闰年
# 能被4整除但不能被100整除 或能被400整除

year = int(input("输入年"))

if ((year % 4 == 0) and (year % 100 != 0) or year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")