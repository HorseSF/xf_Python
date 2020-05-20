# 一张纸的厚度大约是0.08mm，对折多少次后能达到珠峰高度（8848.13米）
height = 8848.13 * 1000
a = 0.08
i = 0
while True:
    i += 1
    a = a * 2
    if a >= height:
        print(i)
        break
