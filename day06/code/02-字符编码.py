# ASCII ==》 Latin1 ==》 Unicode
# 字符和编码存在对于关系

# 根据字符获得编码
print(ord('a'))

# 根据编码获得字符
print(chr(65))

# GBK utf-8 BIG5
# encode方法：字符串转换指定编码集

# GBK 一个汉字占两个字节
print("你".encode("gbk"))

# utf-8 一个汉字占三个字节
print("你".encode("utf-8"))

# decode方法：编码转字符串
x = b"\xe4\xbd\xa0"
print(x.decode("utf-8"))

y = "你".encode("gbk")
print(y)
print(y.decode("big5"))

