x = "abcdefghijklmn"

#  获取字符串长度
print(len(x))

#  查找内容相关的方法 find/index/rfind/rindex
print(x.find("l"))
print(x.index("l"))

print(x.find("p"))  # 不存在返回-1
# print(x.index("p"))  # 不存在报错

print(x.find("l", 4, 9))

# startswith, endswith, isalpha, isdigit, isalnum, isspace
# 返回布尔值
print("hello".startswith("h"))
print("he45llo".isalpha())
print("123".isdigit())
print("ab12num".isalnum())  # 判断是否由数字字母组成

# replace方法
word = "hello"
m = word.replace("l", "x")
print(word)
print(m)

