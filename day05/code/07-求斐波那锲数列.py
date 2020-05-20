# 求斐波那锲数列的第n个数
num = int(input("输入n："))

i = 1
j = 1
# if num == 1 or num == 2:
#     j = 1
# else:
for _ in range(1, num-1):
    z = i
    i = j
    j = j + z
print(j)
