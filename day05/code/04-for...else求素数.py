# 统计101到200之间的素数个数
count = 0
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
print(count)
