# break和continue只能用于循环语句

# break:结束循环
# continue:结束本轮循环
i = 0
while i < 5:
    if i == 3:
        i += 1
        # continue
        break
    print(i)
    i += 1

while True:
    username = input("用户名：")
    password = input("密码：")
    if username == "zhangsan" and password == "123":
        break
