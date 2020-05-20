for i in range(2, 101):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, "是素数")
    else:
        print(i, "能被", count, "个数整除")
