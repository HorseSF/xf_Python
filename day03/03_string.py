# 什么是字符串
# 字符串是以单引号或双引号括起来的文本

# 创建字符串
str1 = "hello world"

# 字符串运算
# 字符串连接
str6 = "hello"
str7 = "world"
str8 = str6 + str7
print(str8)

# 输出重复字符串
str9 = "hello"
str10 = str9 * 3
print(str10)

# 通过索引下标查找字符串，索引从0开始
str11 = "hello world"
print(str11[1])
# str11[1] = "a" #字符串不可变

# 截取字符串的一部分
str12 = "hello world"
str13 = str12[0:5]
print(str13)

# 判断
str14 = "hello world"
print("hello" in str14)
print("hello" not in str14)

# 格式化输出
num = 10
str15 = "hello world"
f = 3.1415
print("num =", num)
# 占位符
print("num = %d, str15 = %s, f = %.2f" %(num, str15, f))

# 转义字符
# \n 换行
# \\ 显示\
# \t 制表符

# 用r 内部字符串默认不转义 打印路径时常用
print(r"\\\t\\")

# eval(str) 将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1,type(num1))
print(eval("12+3"))

# len(str) 字符串长度
print(len("hello world"))

# str.lower() 转换为小写
# str.upper() 转换为大写
str16 = "HELLO world"
print(str16.lower())
print(str16.upper())

# swapcase() 大->小 小->大
str17 = "Hello World"
print(str17.swapcase())

# capitalize() 首字母大写，其他小写
str18 = "Hello World"
print(str18.capitalize())

# title() 每个单词的首字母大写
str19 = "Hello World"
print(str19.title())

# center(width [, fillchar]) 指定宽度居中的字符串
str20 = "Hello World"
print(str20.center(40, "*"))

# ljust(width [, fillchar]) 指定宽度左对齐的字符串
str21 = "Hello World"
print(str21.ljust(40, "*"))

# rjust(width [, fillchar]) 指定宽度右对齐的字符串
str22 = "Hello World"
print(str22.rjust(40, "*"))

# zfill(width) 左补零
str23 = "Hello World"
print(str23.zfill(40))

# count(str[, start][, end]) 找个数
str24 = "Hello World"
print(str24.count("Hel"))

# find(str [, start][, end]) 第一次出现str的索引下标 左->右 没有时返回-1
# rfind(str [, start][, end]) 第一次出现str的索引下标 右->左 没有时返回-1
str25 = "Hello World"
print(str25.find("or"))

# index(str, start=0, end=len(str)) 和find()功能一样，但是没有时报错
# rindex(str, start=0, end=len(str)) 和find()功能一样，但是没有时报错
str26 = "Hello World"
print(str26.index("or"))

# lstrip() 删除字符串左侧的指定字符，默认空格
# rstrip() 删除字符串右侧的指定字符，默认空格
str27 = "  *  Hello World  *  "
print(str27.lstrip())

# strip() 删除字符串左右的指定字符，默认空格
str28 = "    ***Hello World***    "
print(str28.strip())
