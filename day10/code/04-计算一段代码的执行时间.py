import time

# 代码运行之前获取时间
start = time.time()
# 时间戳是从1970-1-1 00：00：00 UTC 到现在的秒数
# 中国 UTC+8
x = 0
for i in range(1, 100000000):
    x += i

print(x)
# 　代码运行以后再获取时间
end = time.time()

print("代码运行{}秒".format(end - start))
