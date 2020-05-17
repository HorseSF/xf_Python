import random

player = int(input("请输入(0)剪刀 (1)石头 (2)布："))
print("用户输入的是", player)

computer = random.randint(0, 2)
print("电脑出的是", computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("恭喜你赢了")
elif player == computer:
    print("平局")
else:
    print("你输了")
