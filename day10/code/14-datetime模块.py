import datetime as dt

# 以一个下划线开始 _x
# 以两个下划线开始 __x
# 以两个下划线开始，两个下划线结束 __x__


print(dt.date(2020, 1, 1))  # 创建⼀一个⽇日期
print(dt.time(18, 23, 45))  # 创建⼀一个时间
print(dt.datetime.now())  # 获取当前的⽇日期时间
print(dt.datetime.now() + dt.timedelta(3))  # 计算三天以后的⽇日期时间
