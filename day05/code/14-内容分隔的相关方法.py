# split, splitlines, partition, rpartition

x = "zhangsan-lisi-wangwu-zhaoliu"
# 使用split将字符串切割成列表
y = x.split("-")
print(y)

z = x.split("-", 2)
print(z)

a = x.rsplit("-", 2)
print(a)

# partition 指定字符串作为分隔符，分为三部分，前，分隔符 ，后
print("abcdefXmpqXzxcv".partition("X"))  # ('abcdef', 'X', 'mpqXzxcv')
print("abcdefXmpqXzxcv".rpartition("X"))  # ('abcdefXmpq', 'X', 'zxcv')


