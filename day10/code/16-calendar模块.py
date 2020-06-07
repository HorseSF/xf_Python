import calendar

calendar.setfirstweekday(calendar.SUNDAY)  # 设置每周起始⽇日期码。周⼀一到周⽇日分别对应 0 ~ 6
calendar.firstweekday()  # 返回当前每周起始⽇日期的设置。默认情况下，⾸首次载⼊入calendar模块时返回0 ，即星期⼀一。

c = calendar.calendar(2019)  # ⽣生成2019年年的⽇日历，并且以周⽇日为其实⽇日期码
print(c)  # 打印2019年年⽇日历

print(calendar.isleap(2000))  # True.闰年年返回True,否则返回False
count = calendar.leapdays(1996, 2010)  # 获取1996年年到2010年年⼀一共有多少个闰年年
print(calendar.month(2019, 3))  # 打印2019年年3⽉月的⽇日历
